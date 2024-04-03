def afficher_description_accessoire(nom, prixHT):
  print(f"Nom de l'accessoire : {nom}")
  print(f"Prix HT de l'accessoire : {prixHT} €")
  print()  

accessoires = ["Chaussures", "Lunettes", "Bague", "Gants", "Collier"]
prixHT = [60.50, 25, 90.99, 5.99, 70]


for i in range(len(accessoires)):
  nom = accessoires[i]
  prix = prixHT[i]
  afficher_description_accessoire(nom, prix)