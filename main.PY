import requests
import json
import time
from datetime import datetime

# --- PARAMÈTRES (Vous pouvez les modifier) ---
URL = "https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000"
Te = 10                # Période d'échantillonnage en secondes (temps de pause)
DUREE_MINUTES = 1      # Durée totale de l'enregistrement en minutes
FICHIER_SORTIE = "historique_parkings.json"

# --- INITIALISATION ---
# Cette liste contiendra toute l'historique pour l'analyse
historique_global = [] 

start_time = time.time()
duree_secondes = DUREE_MINUTES * 60

print(f"--- Démarrage de la collecte pour {DUREE_MINUTES} minutes ---")
print(f"Une mesure toutes les {Te} secondes...")

# --- BOUCLE AUTOMATIQUE ---
while (time.time() - start_time) < duree_secondes:
    try:
        # 1. Requête
        response = requests.get(URL)
        
        if response.status_code == 200:
            data_brute = response.json()
            
            # Timestamp actuel (pour savoir quand la mesure a été prise)
            temps_actuel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Liste temporaire pour cet instant T
            snapshot_parkings = []

            # 2. Extraction et Calcul des données
            for parking in data_brute:
                try:
                    nom = parking.get('name', {'value': 'Inconnu'})['value']
                    total = parking['totalSpotNumber']['value']
                    libres = parking['availableSpotNumber']['value']
                    
                    # Calcul des places occupées
                    occupes = total - libres
                    
                    # On crée un dictionnaire propre pour ce parking
                    info_parking = {
                        "nom": nom,
                        "total": total,
                        "libres": libres,
                        "occupes": occupes,
                        "pourcentage_libre": round((libres / total) * 100, 2) if total > 0 else 0
                    }
                    snapshot_parkings.append(info_parking)
                    
                except KeyError:
                    continue # On saute les parkings mal formés

            # 3. Ajout à la liste globale (Analyse temporelle)
            mesure = {
                "temps": temps_actuel,
                "timestamp_unix": time.time(),
                "donnees": snapshot_parkings
            }
            historique_global.append(mesure)
            
            print(f"[{temps_actuel}] Données récupérées avec succès ({len(snapshot_parkings)} parkings).")
            
        else:
            print(f"Erreur serveur : {response.status_code}")

    except Exception as e:
        print(f"Erreur de connexion : {e}")

    # 4. Pause (Gestion du temps)
    time.sleep(Te)

# --- SAUVEGARDE FINALE POUR ANALYSE ---
with open(FICHIER_SORTIE, 'w', encoding='utf-8') as f:
    json.dump(historique_global, f, indent=4, ensure_ascii=False)

print(f"\n--- Terminé ! ---")
print(f"Les données sont prêtes pour analyse dans le fichier : {FICHIER_SORTIE}")
