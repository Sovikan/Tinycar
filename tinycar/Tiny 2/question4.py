code_secret = input("Entrez le code secret : ")

if code_secret == "0000":
    
    print("Choisissez une option")
    print("1 - Sans carte de fidélité")
    print("2 - Avec carte Gold")
    print("3 - Avec carte Platinum")

    choix = input("Votre choix (1/2/3) : ")

    marque_modele = input("Entrez la marque et le modèle souhaités : ")
    prixHT = (input("Entrez le prix HT : "))

    est_electrique = input("Le produit est-il électrique ? oui ou non? : ").lower()

    if est_electrique == "oui":
        tauxTVA = 0.05
    elif est_electrique == "non":
        tauxTVA = 0.2
    else:
        print("Réponse invalide. Veuillez répondre 'Oui' ou 'Non'.")

    if est_electrique == "oui" or est_electrique == "non":
        prixTTC = prixHT * (1 + tauxTVA)

        
        if choix == "2": 
            prixTTC = 0.8  
        elif choix == "3": 
            prixTTC= 0.85  

        print("Le prix TTC à payer est de :", prixTTC)

else:
    print("Code secret incorrect.")
