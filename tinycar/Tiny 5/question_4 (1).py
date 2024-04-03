prixHT = [60.50, 25, 90.99, 5.99, 70]
#Calcul de la moyenne du prix HT
def calculer_moyenne_prixHT(prixHT):
   moyenne = sum(prixHT) / len(prixHT)
   return moyenne
# Calcul du prix HT minimal
def trouver_prixHT_minimal(prixHT):
      prix_min = min(prixHT)
      return prix_min
# Calcul du prix HT maximal
def trouver_prixHT_maximal(prixHT):
        prix_max = max(prixHT)
        return prix_max
# Calcul et affichage des statistiques
moyenne_prixHT = calculer_moyenne_prixHT(prixHT)
prixHT_minimal = trouver_prixHT_minimal(prixHT)
prixHT_maximal = trouver_prixHT_maximal(prixHT)


print(f"Moyenne des prix HT : {moyenne_prixHT} €")
print(f"Prix HT minimal : {prixHT_minimal} €")
print(f"Prix HT maximal : {prixHT_maximal} €")






