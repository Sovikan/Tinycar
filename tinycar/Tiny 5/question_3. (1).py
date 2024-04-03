def afficher_elements_tableaux(accessoires, prixHT, prixTTC):
  for i in range(len(accessoires)):
      nom = accessoires[i]
      prix_ht = prixHT[i]
      prix_ttc = prixTTC[i]
      print(f"Nom de l'accessoire : {nom}")
      print(f"Prix HT : {prix_ht} €")
      print(f"Prix TTC : {prix_ttc} €")
      print()  


accessoires = ["Chaussures", "Lunettes", "Bague", "Gants", "Collier"]
prixHT = [60.50, 25, 90.99, 5.99, 70]


prixTTC = [prix * 1.20 for prix in prixHT]


afficher_elements_tableaux(accessoires, prixHT, prixTTC)