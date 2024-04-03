# Demander à l'utilisateur la taille des tableaux
taille = int(input("Entrez la taille des tableaux d'accessoires : "))

# Initialiser les tableaux des noms d'accessoires et des prix HT
accessoires = []
prixHT = []

# Demander à l'utilisateur de saisir les noms et prix HT des accessoires
for i in range(taille):
    nom = input(f"Entrez le nom de l'accessoire {i + 1} : ")
    prix = float(input(f"Entrez le prix HT de l'accessoire {i + 1} : "))
    accessoires.append(nom)
    prixHT.append(prix)

# Afficher les noms et prixHT des accessoires à l'aide des tableaux
print("Liste des accessoires dans le panier :")
for i in range(taille):
    print(f"{accessoires[i]} : {prixHT[i]} €")

# Calculer la somme totale des achats
total_achats = sum(prixHT)
print(f"Somme totale des achats : {total_achats} €")