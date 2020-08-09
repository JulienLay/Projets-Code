# Programme testant si une ann�e, saisie par l'utilisateur, est bissextile ou non

annee = input("Saisissez une ann�e : ") # On attend que l'utilisateur saisisse l'ann�e qu'il d�sire tester
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'ann�e saisie est bissextile.")
else:
    print("L'ann�e saisie n'est pas bissextile.")

