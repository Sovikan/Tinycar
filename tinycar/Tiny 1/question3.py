
prixHT = int(input("Veuillez entrer le prix hors taxe de la quantité à l'unité que vous avez prise: ")) # Demande à l'utilisateur de saisir le prix HT de l'unité
tauxTVA = 0.2  # Taux de TVA en pourcentage
prixTTC = prixHT * (1 + tauxTVA)  #Calcul du prix TTC

print("Le prix TTC à payé est de :",prixTTC) #Affichage du résultat




