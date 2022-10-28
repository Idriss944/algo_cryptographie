#Exercice 3
#Dans cet exercice on cherche a chiffrer / dechiffrer avec le chiffrement affine. 
#Ce dernier consiste a utiliser une fonction affine afin de chiffrer un message. 
#Le a utilise doit etre inversible dans Zn sinon le message ne sera pas dechiffrable.



#Question 1
#Dans la question 1 la fonction affine est la suivante : e1(x) = 119x + 82 mod128.
#Pour trouver l’inverse de 119 on doit calculer phi(128). Or 128 = 2^7 d’ou phi(128) = (2-1) * 2^6 Donc phi(128) = 64.
#D'apres le théoreme d'Euler : Alors a * a^[phi(n)-1]  congru 1 mod n => a^[phi(n)-1] est l’inverse de a dans Zn.
#Calculons (119^63) mod 128 = 71.  inv (119) dans Z128 = 71.
#Neanmoins ceci peut etre effectue directement dans le code, comme c'est le cas ci-apres:


texte = input("Veuillez renseigner le texte \n") #On demande à l'utilisateur de rentrer le texte 
type = int(input("\nSi vous voulez chiffrer tapez 1,\nSi vous voulez dechiffrer tapez 2 \n"))  #On demande à l'utilisateur s'il veut chiffrer ou dechiffrer
msg=''              #On initialise le msg chiffre a vide
a = int(input("\nEntrez la valeur de a de la fonction affine\n"))  #On demande a l'utilisateur de rentrer la valeur de a de la fonction affine
b = int(input("\nEntrez la valeur de b de la fonction affine\n"))   #On demande a l'utilisateur de rentrer la valeur de b de la fonctiona affine
print("\nLa fonction affine utilisee est :",a,"x +",b)

if (type==1):   #Si l'utilisateur veut chiffrer
    for i in texte:                # on boucle sur les lettres du texte
        val_lettre=((a*ord(i)+b) % 128)      #la valeur de la lettre chiffre est (119x + 82) mod 128
        lettre=chr(val_lettre)                  #on trouve le caractere qui correspond a la valeur 
        msg+=lettre                     #on ajoute la lettre dans le message
    print("\nLe message chiffre est : \n")
elif (type==2):                 #si l'utilisateur veut dechiffrer 
    
    for i in range(128):   #on se place entre 0 et 127 car l'inverse est compris dans Z128
        if ((a*i)%128==1):      #On indique la condition qui permet de dire que i est l'inverse de a
            inv_a=i             #On associe la valeur de i a inv(a)
            inversible=True     #On indique via un booleen que a est inversible
            break               #On s'arrete ici car on a trouve l'inverse
        else:                   #Dans le cas ou la condition n'est pas rempli alors 
            inversible=False    #On indique via le booleen que a n'est pas inversible
            inv_a=0             #On associe 0 a inv(a)
    if (inv_a==0):
        print ("\n",a," n'est pas inversible dans Z128 : le dechiffrement n'est pas possible \n")   #On affiche un message comme quoi le dechiffrement n'est pas possible


    if (inversible==True): #Si a est inversible alors on dechiffre
        for j in texte:            
            val_lettre=((inv_a*(ord(j)-b)) % 128)       #la valeur de la lettre dechiffre est (inv(119)x - 82) mod 128
            lettre=chr(val_lettre)                    #on retrouve la lettre qui correspond à la valeur
            msg+=lettre                         #on ajoute la lettre dans le message
        print("\nJ'ai trouve le message ! Le voici : \n")

print (msg)             #On affiche le message



#Question 2 
#On obtient le message chiffre suivant : C*Et2Wk}}itNG2iPE2PEiN2<Pk}2i2>>_F2>*E2!t>EPbPE>EP2!G2Gi!N2>k2`E2!t2!t>EPiW>!,E2}kNE42At2>*!G2}kNE2!>2bPk}b>G2<kP2>*E2tE_>2Wk}}itN2#!>*2>*E2bP!}iP_2bPk}b>F25G5i___2>*PEE23PEi>EP=>*it2G!3tG2j$$$a?2<kP2Wkt>!t5i>!kt2_!tEG2!>2bPk}b>G2#!>*2>*E2GEWktNiP_2bPk}b>F2`_2NE<i5_>2>*PEE2Nk>G2j444a42^*E2!t>EPbPE>EP2bP!t>G2i2#E_Wk}E2}EGGi3E2G>i>!t32!>G2,EPG!kt2t5}`EP2itN2i2Wkb_P!3*>2tk>!WE2`E<kPE2bP!t>!t32>*E2<!PG>2bPk}b>4
#Lorsque l'on dechiffre on obtient : When commands are read from a tty, the interpreter is said to be in interactive mode. In this mode it prompts for the next command with the primary prompt, usually three greater-than signs (>>>); for continuation lines it prompts with the secondary prompt, by default three dots (...). The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt.



#Question 3
# Grâce au programme on peut chiffrer la chaîne "RATEAU" et la chaîne chiffree donne : 'Uoaog'
# Néanmoins, il est impossible de dechiffrer car 6 n'est pas inversible dans Z128 or il est necessaire que a soit inversible dans Zn pour le dechiffrement d'une fonction affine
#Le chiffrement 6x - 23 ne peut donc pas etre utilise en pratique car il n'est pas possible de dechiffrer le message.

