from math import sqrt

L1 = [3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4]
L2 = [108,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96]


def moy(*W):
    return [sum(lst) / len(lst) for lst in W]

def var(*W):
    res = []
    for lst in W:
        moy = sum(lst) / len(lst)
        ecarts_carres = [(x - moy)**2 for x in lst]
        res.append(sum(ecarts_carres) / len(lst))
    return res

def ecartype(*W):
    return [sqrt(v) for v in var(*W)]


def covar(X, Y):
    moy_x = sum(X) / len(X)
    moy_y = sum(Y) / len(Y)
    produit_ecarts = [(X[i] - moy_x) * (Y[i] - moy_y) for i in range(len(X))]
    return sum(produit_ecarts) / len(X)


def correl(X, Y):
    cov = covar(X, Y)
    sigma_x = sqrt(var(X)[0])
    sigma_y = sqrt(var(Y)[0])
    return cov / (sigma_x * sigma_y)

def mat_correl(*W):
    matrice = []
    for L_ligne in W:
        ligne = [correl(L_ligne, L_colonne) for L_colonne in W]
        matrice.append(ligne)
    return matrice

moys = moy(L1, L2)
vars = var(L1, L2)
sigs = ecartype(L1, L2)

print("Moyennes arrondies    :", [round(m, 2) for m in moys])
print(f"Variances (L1, L2)    :", [round(v, 2) for v in vars])
print(f"Écarts-types (L1, L2) :", [round(s, 2) for s in sigs])

cov = covar(L1, L2)
corr = correl(L1, L2)

print("Covariance :", round(cov,2))
print("Corrélation :", round(corr, 2))

matrice = mat_correl(L1, L2)
for ligne in matrice:
    print([round(val, 2) for val in ligne])


"""Pour creer des courbes et des (heatmap) il y a des library, si jai bien compris,
pour ca sur l'internet mais M Druon m'a expliquer clairement que c'etait moins interressant 
ou moins rigoureux d'utiliser des library et l'interet de creer ses propres outils, et suite a un 
essaie pathetic de creer mon outils jai arreter pour l'instant d'essayer"""