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

# Afficher les noms et prixHT des accessoires à l'aide des tableaux (boucle for)
print("Liste des accessoires dans le panier :")
for i in range(taille):
    print(f"{accessoires[i]} : {prixHT[i]} €")

# Calculer la somme totale des achats
total_achats = sum(prixHT)
print(f"Somme totale des achats : {total_achats} €")

# Trouver le prix minimum et afficher l'accessoire correspondant
prix_min = min(prixHT)
index_prix_min = prixHT.index(prix_min)
accessoire_prix_min = accessoires[index_prix_min]
print(f"Accessoire avec le prix minimum : {accessoire_prix_min} (Prix : {prix_min} €)")

# Trouver le prix maximum et afficher l'accessoire correspondant
prix_max = max(prixHT)
index_prix_max = prixHT.index(prix_max)
accessoire_prix_max = accessoires[index_prix_max]
print(f"Accessoire avec le prix maximum : {accessoire_prix_max} (Prix : {prix_max} €)")

# Calculer le prix moyen
prix_moyen = total_achats / taille
print(f"Prix moyen : {prix_moyen} €")