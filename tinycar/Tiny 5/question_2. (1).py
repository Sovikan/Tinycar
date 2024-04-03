def calculer_prix_TTC(prixHT):
    tva = 0.20  # Taux de TVA de 20%
    prixTTC = prixHT * (1 + tva)
    return prixTTC

accessoires = ["Chaussures", "Lunettes", "Bague", "Gants", "Collier"]
prixHT = [60.50, 25, 90.99, 5.99, 70]


prixTTC = []

for prix in prixHT:
    prix_ttc = calculer_prix_TTC(prix)
    prixTTC.append(prix_ttc)

  
for i in range(len(accessoires)):
    nom = accessoires[i]
    prix_ht = prixHT[i]
    prix_ttc = prixTTC[i]
    print(f"Nom de l'accessoire : {nom}")
    print(f"Prix HT : {prix_ht} €")
    print(f"Prix TTC : {prix_ttc} €")
    print()  