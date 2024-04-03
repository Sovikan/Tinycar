marque_modele = int(input("Entrez la marque et le modele souhaites : "))
prixHT = int(input("Entrez le prix HT : "))
tauxTVA = 0.2
prixTTC = prixHT * (1 + tauxTVA)

if prixTTC > 2000:
    remise = 0.1 * prixTTC  
    prixTTC -= remise  

print("Le prix TTC a payer est de :", prixTTC)
