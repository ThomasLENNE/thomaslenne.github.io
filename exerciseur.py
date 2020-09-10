from random import *

nbits=8
n_10=randint(0,2**nbits)
N=1
pts=0

print("Quelle est l'écriture en base 2 de l'entier "+ str(n_10))

continuer = 1
while continuer:
    reponse=input('Ecrire votre réponse :')
    if reponse==bin(n_10)[2:]:
        pts=pts+1
        print ("Bonne réponse ! "+ "\U0001F600")
        print("Score : "+str(pts)+'/'+str(N))
        recommencer=input ("Recommencer ?(o/n)").upper()
        if recommencer !='O':
            continuer=0
            fin=input("Score final : "+str(pts)+'/'+str(N))
        else:
            n_10=randint(0,2**nbits)
            print("Quelle est l'écriture en base 2 de l'entier "+ str(n_10))
            pts=0
            N=N+1
           
    else:
        print("Mauvaise réponse... "+"\U0001F612")

