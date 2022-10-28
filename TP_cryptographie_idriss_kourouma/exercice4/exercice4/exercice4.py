#fonction question1

def chiffrement_substitution(texte, substitution):  #on defini la fonction de chiffrement qui a pour entree le texte et la substitution
    mapping={}                                      #On initialise le dictionnaire de substitution
    message=''                                      #On initialise le message
    for i in Alphabet:                              #On se deplace dans l'alphabet afin de remplir le dictionnaire
        mapping[i] = substitution[Alphabet.find(i)] #On rempli le dictionnaire de substitution tel que mapping[a] = la lettre en position 0 dans la chaine substitution, mapping [b] = la lettre en position 1 dans la chaine substitution, ...
    for i in texte:                                 #On se deplace dans le texte que l'on doit chiffrer
        if i in Alphabet:                           #Si le caractere est une minuscule non accentuee de l'alphabet alors on chiffre
            message+=mapping[i]                     #On chiffre en allant chercher la valeur correspondant a la lettre du texte dans notre dictionnaire. Par exemple si i=a, le mapping[a] va chercher la valeur associee a 'a' dans notre dictionnaire
        else:                                       #Si le caractere est different d'une minuscule alors on le reecrit tel quel
            message+=i
    print("Je suis le message chiffre",message)     #On affiche le message chiffre
    return 0


#fonction question2

def dechiffrement_substitution(texte_chiffre, substitution):  #on defini la fonction de dechiffrement qui a pour entree le texte chiffre et la substitution
    mapping={}                                      #On initialise le dictionnaire de substitution
    message=''                                      #On initialise le message
    for i in Alphabet:                              #On se deplace dans l'alphabet afin de remplir le dictionnaire
        mapping[substitution[Alphabet.find(i)]] = i #On rempli le dictionnaire de substitution tel que mapping[c]=a avec a la valeur en clair de c. Pour ce faire on cherche la place de la lettre dans l'alphabet ensuite on trouve quelle lettre est a cette place dans la chaine substitution et on associe les deux valeurs. 
                                                    #Par exemple pour 'a' on va trouver quelle lettre est en position 0 dans la chaine substitution (par exemple 'c') et on va associe c:a.
    for i in texte_chiffre:                         #On se deplace dans le texte que l'on doit dechiffrer
        if i in Alphabet:                           #Si le caractere est une minuscule non accentuee de l'alphabet alors on chiffre
            message+=mapping[i]                     #On dechiffre en allant chercher la valeur correspondant a la lettre du texte dans notre dictionnaire. Par exemple si i=a, le mapping[a] va chercher la valeur associee a 'a' dans notre dictionnaire
        else:                                       #Si le caractere est different d'une minuscule alors on le reecrit tel quel
            message+=i
    print("Je le message clair est",message)     #On affiche le message chiffre
    return 0
 
 

 #initialisation et appel des fonctions
 
texte=input("Entrez le texte\n")                    #On demande a l'utilisateur de rentrer le texte 
type = int(input("\nSi vous voulez chiffrer tapez 1,\nSi vous voulez dechiffrer tapez 2 \n"))  #On demande à l'utilisateur s'il veut chiffrer ou dechiffrer
Alphabet='abcdefghijklmnopqrstuvwxyz'               #On initialise l'alphabet
substitution=['u', 'n', 'v', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z'] #On initialise la chaine de substitution
if type==1:                                         #Si l'utilisateur souhaite chiffrer
    chiffrement_substitution(texte, substitution)   #On appelle la fonction de chiffrage avec le texte saisit par l'utilisateur et la substitution
elif type==2:                                       #Si l'utilisateur souhaite dechiffrer
    dechiffrement_substitution(texte, substitution) #On appelle la fonction de dechiffrage avec le texte saisit par l'utilisateur et la substitution
else:                                               #Sinon message d'erreur
    print("Veuillez rentrez un argument valide")
