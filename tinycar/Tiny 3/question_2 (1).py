n = int(input("Entrez le nombre de produits à traiter : "))

for i in range(n):
    marque_modele = input(f"Entrez la marque et le modèle du produit {i+1} : ")
    prixHT = int(input(f"Entrez le prix HT du produit {i+1} : "))
    tauxTVA = 0.2
    prixTTC = prixHT * (1 + tauxTVA)

    if prixTTC > 20000:
        remise = 0.1 * prixTTC  
        prixTTC -= remise  

    print(f"Le prix TTC à payer pour ce produit {i+1} est de : {prixTTC}")

print("Merci d'avoir utilisé le programme !")





