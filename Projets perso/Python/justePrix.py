# -*- coding:utf-8 -*-
from random import randint
def plusOuMoins():
	cont=1
	while cont == 1:
		compte=0
		print ("Bienvenue sur le jeu du plus ou moins")
		difficulte=int(input("Choisissez la difficulté entre 1, 2 et 3 \n"))
		if difficulte==1:
 			n=10
		elif difficulte==2:
			n=100
		elif difficulte==3:
			n=1000
		nbATrouver=randint(1,n)
		nbPropose=int(input("Choisissez un nombre \n"))
		if nbPropose > n:
			print("Erreur. Nombre trop grand, veuillez choisir un nombre entre O et"+str(n))
		elif nbPropose < n:
			print("Erreur. Nombre trop petit, veuillez choisir un nombre entre O et"+str(n))
		while ( nbATrouver != nbPropose ):
			compte+=1
			if ( nbATrouver < nbPropose ):
				print ("Trop grand")
			else:
				nbATrouver > nbPropose 
				print ("Trop petit")
			nbPropose=int(input("Choisissez un nombre \n"))
		print (" gagne ")
		print("Tu as trouvé en "+str(compte)+" coups")
		cont=int(input("Voulez vous rejouer. 1=oui,0=non"))
plusOuMoins()
