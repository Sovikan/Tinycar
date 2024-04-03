while True:
  marque_modele = int(input("Entrez la marque et le modèle souhaités : ")) #Demande à l'utilisateur de mettre la marque ainsi que le modèle souhaite
  prixHT = (input("Entrez le prix HT : "))#Demande à l'utilisateur de mettre le prix HT
  tauxTVA = 0.2
  prixTTC = prixHT * (1 + tauxTVA)

  if prixTTC > 20000:                   #Condition : Si le prixTTC est supérieur à 20000 
    remise = 0.1 * prixTTC              #La remise sera de 0.1 multiplié par le prixTTC
    prixTTC -= remise                   #Le prix TTC sera calculé en faisaint une soustraction entre le prixTTC et la remise

  print("Le prix TTC à payer est de :", prixTTC)  #Affichage du prixTTC

  choix = int(input("Voulez-vous calculer le prix TTC pour un autre produit ? (1 pour continuer, 0 pour quitter) : ")) #demande à l'utilisateur si ils souhaite calculer le prixTTC d'un autre produit 
  if choix == '0':    
    print("Merci et au revoir !")
    break
