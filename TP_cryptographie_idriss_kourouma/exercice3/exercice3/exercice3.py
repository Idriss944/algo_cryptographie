texte = input("Veuillez saisir le texte\n")

if (len(texte)%2)==1: #si la chaine de caractere est impair on ne peut pas chiffrer
    print("La chaine comporte un nombre impair de caractere")

else:

    type = int(input("\nSi vous voulez chiffrer tapez 1,\nSi vous voulez dechiffrer tapez 2 \n"))  #On demande à l'utilisateur s'il veut chiffrer ou dechiffrer
    a, b = int(input("\nRentrez a1 tel que la matrice cle soit [a1, a2][b1, b2]\n")), int(input("Rentrez a2 tel que la matrice cle soit [a1, a2][b1, b2]\n"))
    c, d = int(input("Rentrez b1 tel que la matrice cle soit [a1, a2][b1, b2]\n")), int(input("Rentrez b2 tel que la matrice cle soit [a1, a2][b1, b2]\n"))
    message=''
    cle = [[a, b], [c, d]]  #On initialise la cle
    print("La cle est", cle)
    length = len(texte)     #On a besoin de la longueur du texte pour pouvoir se deplacer dans ce dernier
    m=len(cle[0])           #Nombre de colonnes de la matrice cle
    p=len(cle)              #Nombre de lignes de la matrice cle


    for i in range(0, length, 2):                   #On balaye le texte par pas de 2
        M_chiff=[[0, 0]]                            #M_chiffr nous servira soit de matrice chiffre, s'il ont veut chiffrer, soit de matrice clair, si l'on veut dechiffrer
        M = [[ord(texte[i]), ord(texte[i+1])]]      #M nous sert soit de matrice clair soit de matrice chiffre. Elle prend les valeurs des deux lettres la ou nous sommes rendu dans le texte
        if (type==1):                               #Si l'utilisateur veut chiffrer
            for j in range(m):                          #On parcours les colones de la matrice cle
                for k in range(p):                      #On parcours les lignes de la matrice cle
                    M_chiff[0][j] += M[0][k]*cle[k][j]  #On calcule la valeur de la matrice chiffre 
            
            M_chiff[0][0] = M_chiff[0][0] % 128   #On reduit les valeurs a mod(128) pour rester dans la table ASCII
            M_chiff[0][1] = M_chiff[0][1] % 128
        elif (type==2):                               #Si l'utilisateur veut dechiffrer 
            determinant_cle=(cle[0][0]*cle[1][1] - cle[0][1]*cle[1][0]) %128
            for i in range(128):                      #On se place entre 0 et 127 car l'inverse est compris dans Z128
                if ((determinant_cle*i)%128==1):      #On indique la condition qui permet de dire que i est l'inverse de a
                    inv_a=i                           #On associe la valeur de i a inv(a)
                    inversible=True                   #On indique via un booleen que a est inversible
                    break                             #On s'arrete ici car on a trouve l'inverse
                else:                                 #Dans le cas ou la condition n'est pas rempli alors 
                    inversible=False                  #On indique via le booleen que a n'est pas inversible
                    inv_a=0                           #On associe 0 a inv(a)
            if (inversible==True):                    #Si le det est inversible alors on calcule l'inverse de la cle
                inv_cle=[[0, 0], [0, 0]]
                inv_cle[0][0]=(inv_a*(cle[1][1]) %128)      #ici on calcule la matrice inverse grace à l'inverse du determinant
                inv_cle[0][1]=(inv_a*(-cle[0][1]) %128)
                inv_cle[1][0]=(inv_a*(-cle[1][0]) %128)
                inv_cle[1][1]=(inv_a*(cle[0][0]) %128)
            
                for j in range(m):                              #On parcours les colones de la matrice cle. La taille de la matrice inverse est identique a celle de la matrice de base
                    for k in range(p):                          #On parcours les lignes de la matrice cle
                        M_chiff[0][j] += M[0][k]*inv_cle[k][j]  #On calcule la valeur de la matrice clair 
            
                M_chiff[0][0] = M_chiff[0][0] % 128       #On reduit les valeurs a mod(128) pour rester dans la table ASCII
                M_chiff[0][1] = M_chiff[0][1] % 128 
            else:
                break
           
        message+=chr(M_chiff[0][0])+chr(M_chiff[0][1])  #Le message est compose des lettres trouvees a partir des matrices chiffres de chaque etape.

    if type==1:                                         #Si l'objectif etait de chiffrer alors on affiche cela
        print ("\nle message est", message)     
    elif type==2 and inversible==True:                  #Si l'objectif etait de dechiffrer et la matrice est inversible alors on affiche cela
        print("\nJ'ai trouve le message ! Le voici : \n", message)  
    else :                                              #Sinon, donc dans le cas ou on veut dechiffrer et que la matrice n'est pas inversible on affiche le message d'erreur suivant
        print(determinant_cle,"n'a pas d'inverse dans Z128. Par consequent le dechiffrement n'est pas possible")
    
    
    
     
#Question 2
#Lorsque l'on dechiffre le texte fourni on obtient 
# a▬e8     #XK6;>@m♠u4{j=IK&↕&[Ssz⌂bh\♂▲<4G5←)nPq<fRw>q<←)m♠0GC6<4q~M)←)r|a@;M1Ey:yH{j`IK-2|☺ <4S9m♠`IK-←)fRXKlTm♠g;n♦DP{jAAdd     #XK6;>@E7sFxpDP{jfR^?u4g↕fRXKlT4xd].KXDg↕DP=I{jo@>+;M§◄DPi093L9kOXh|:=%%▬g;n♦j5nPa@.KGQ[L$,a@t=←)fRXKlTm♠DWDP<4G593D-[L?)y]00[ScJ►¶♠"g↕K-=-OVDP=I{ji7e[Xh\
#M♣2|d►{ja@;M^T=I;Mn♦fRa@e[♥!E7_6j5B?'-t=0GH393/IGQGC←)e[B6q<HO[L*.RWM)n♦i0|h⌂bj5{YIMQ6_KGQL+♠"M0gP{jfRa@GQGC<4G5↕&mDiZ00[ScJ▬▬
#soit une chaine de caractere composee egalement de caractere non interpretable,
#ce qui empeche de dechiffrer correctement par la suite.




#Question 3
#avec la matrice [6, 3]
#                [3, 1]
#On arrive a chiffrer le texte exemple
#Neanmoins, il est impossible de dechiffrer car la matrice n'est pas inversible
#Lorsque l'on tente de dechiffrer le programme nous renvoie que le dechiffrement n'est pas possible.

    
    
    
    
    
    
    
    