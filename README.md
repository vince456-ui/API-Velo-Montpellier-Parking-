# Analyse de la Mobilité Urbaine - Montpellier

## Description du Projet
Ce projet répond à une commande de la Mairie de Montpellier visant à optimiser la gestion du stationnement et l'intermodalité (Voiture + Vélo).
L'objectif est d'analyser les données réelles des parkings et des stations Vélomagg pour répondre à trois questions clés :
1. **Les parkings sont-ils bien dimensionnés ?**
2. **Existe-t-il une saturation critique à certaines heures ?**
3. **Y a-t-il une corrélation entre le trafic voiture et l'usage des vélos (Intermodalité) ?**

## Structure du Dépôt
* `analysis.ipynb` : Le rapport complet (Code Python + Graphiques + Analyses textuelles).
* `analyses.py` : Module Python personnalisé contenant les fonctions mathématiques (moyenne, corrélation).
* `VOITURE169.json` : Données brutes des parkings voitures.
* `VELO169.json` : Données brutes des stations vélos.
* `requirements.txt` : Liste des librairies nécessaires.

## Installation et Exécution
Pour reproduire cette analyse sur votre machine :

1. **Cloner le projet :**
   ```bash
   git clone [https://github.com/VOTRE-NOM/VOTRE-REPO.git](https://github.com/VOTRE-NOM/VOTRE-REPO.git)
   ```
2. **Installer les dépendances :**
  ```bash
  pip install -r requirements.txt
  ```
3. **Lancer le Notebook : Ouvrez analysis.ipynb dans VS Code ou Jupyter Notebook et cliquez sur "Run All".**

## Conclusions Principales
Saturation Voiture : Le parking Gaumont OUEST est saturé en permanence (~99%), suggérant un problème de "voitures ventouses". À l'inverse, les parkings périphériques (ex: Sabines) sont sous-utilisés.

Réseau Vélo : Aucune saturation critique détectée. Le réseau Vélomagg est capable d'absorber plus d'usagers.

Intermodalité : Les scores de corrélation (proches de 0) montrent que l'usage des vélos est indépendant du remplissage des parkings voitures. Les automobilistes ne semblent pas utiliser les vélos en "relais" immédiat.

## Technologies Utilisées
Python 3.13
Pandas (Traitement des données temporelles)
Matplotlib (Visualisation graphique)
JSON (Manipulation des données brutes)
--------------------------------------------------------------------------------------------------------------------------------------------------
Projet réalisé dans le cadre de la SAE "Traitement de Données".
