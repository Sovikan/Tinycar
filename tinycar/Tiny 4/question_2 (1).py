accessoires = ["Chaussures", "Lunettes", "Bague", "Gants", "colier"]  #Initialisation d'un tableau contenant des valeurs
prixHT = [59.99 , 25, 90, 93, 75] 

for accessoires in accessoires :
    prix=float(input(f"veuillez entrer le prixHT de { accessoires}:"))
for i in range(len(accessoires)):
                nom = accessoires [i] 
                prixHT = prixHT[i] 
                print(f"{nom} : {prix} €")