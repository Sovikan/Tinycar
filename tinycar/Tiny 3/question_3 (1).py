tentatives_restantes = 3

while tentatives_restantes > 0:
    code_secret = input("Entrez le code secret : ")

    if code_secret == "HELLO":
        marque_modele = input("Entrez la marque et le modèle souhaités : ")
        prixHT = float(input("Entrez le prix HT : "))

        est_electrique = input("Le produit est-il électrique ? (Oui/Non) : ").lower()

        if est_electrique == "oui":
            tauxTVA = 0.05
        elif est_electrique == "non":
            tauxTVA = 0.2
        else:
            print("Réponse invalide. Veuillez répondre 'Oui' ou 'Non'.")
            continue 

        if est_electrique == "oui" or est_electrique == "non":
            prixTTC = prixHT * (1 + tauxTVA)

            if prixTTC > 20000:
                remise = 0.1 * prixTTC 
                prixTTC -= remise

            print("Le prix TTC à payer est de :", prixTTC)
            break  

    else:
        tentatives_restantes -= 1
        print(f"Code secret incorrect. Il vous reste {tentatives_restantes} tentatives.")

if tentatives_restantes == 0:
    print("Vous avez épuisé toutes vos tentatives. L'application est verrouillée.")