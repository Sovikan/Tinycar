marque_modele = int(input("Entrez la marque et le modele souhaites : "))
prixHT = int(input("Entrez le prix HT : "))
est_electrique=int(input("Est ce que le produit est electrique veuillez nous dire oui ou non"))

if est_electrique == 'oui':
    tauxTVA=0.05
elif est_electrique== 'non':
    tauxTVA=0.2

if prixTTC > 20000:
    remise = 0.1 * prixTTC  
    prixTTC -= remise  

print("Le prix TTC a payer est de :", prixTTC)
