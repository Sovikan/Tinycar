accessoires = ["Chaussures", "Lunettes", "Bague", "Gants", "colier"]  #Initialisation d'un tableau contenant des valeurs
prixHT = [60.50, 25, 90.99, 5.99, 70] #Initialisation d'un tableau contenant des valeurs de prixHT

for i in range(len(accessoires)):  # 
    nom = accessoires[i]
    prix = prixHT[i]
    print(f"{nom} : {prix} €")