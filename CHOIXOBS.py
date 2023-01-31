from os import path,listdir,popen,execl,system
from SPLAAATOMAKER import SPLAATOMAKER
from math import *
from random import *
from upemtk import *


hauteurFenetre = 1030
largeurFenetre = 1920


    

def choixobs(lst):
#CEST LE TEXTE D'INFORMATION
    rectangle(0,0,1920,1030,'white','honeydew3')
    texte((largeurFenetre/2),60,"Choisissez votre fichier prédéfinis d\'obstacles : ",taille=60,ancrage='center')

    #FLECHE GAUCHE
    rectangle(860,200,1060,300)
    texte(960,240,"↑",ancrage='center',taille=60)
    
    #FLECHE DROITE
    rectangle(860,650,1060,750)
    texte(960,690,"↓",ancrage='center',taille=60)
    
#============ MES AUTRES VARIABLES ================================================================
    maxliste = len(lst)
    nomfichierob = None
    a = 1
#============ MON WHILE ================================================================
    # dans la doc c'est while true mais je fais arreter mon programme après selection de la couleur d'équipe dans nomfichierob (couleurTeam1)
    while nomfichierob is None :

        #Truc pr faire des événement de la doc
        evenement = donne_evenement()
        type_ev = type_evenement(evenement) #type = touche ou clic

        #Le ROND AU MILIEU

        #RAJOUT DALTONIEN
        efface('lol')
        #texte(960,380,lst[a-1],ancrage="center",tag='lol',taille=30)
        texte(960,475,lst[a],ancrage="center",tag='lol',taille=60)
        #texte(960,570,lst[a+1],ancrage="center",tag='lol',taille=30)

        #BOUTON DE SELECTION
        rectangle(760,800,1160,900,'black','DeepSkyBlue3')
        texte(960,850,"ENTER",ancrage='center',taille=50)

        rectangle(1210,800,1610,900,'black','coral2')
        texte(1410,850,"ALEATOIRE",ancrage='center',taille=50)

        rectangle(310,800,710,900,'black','chartreuse')
        texte(510,850,"CREATION",ancrage='center',taille=50)

#============ LES TOUCHES ================================================================
        if type_ev == 'Touche': #Dire le type de evenement (touche ou clic)
            nom_touche = touche(evenement)
            if nom_touche == 'Up':
                a -= 1 
        # a c'est pour rappel l'indice dans la position de la liste donc si a change, la couleur aussi
                #print(a)
            if nom_touche == 'Down':
                a += 1
                #print(a)
            if nom_touche == 'Return': 
                #RETURN CEST ENTRER
                nomfichierob = lst[a] #DONC SI ON CLIQUE ON CHOISIT LA COULEUR PR LA TEAM
                affichagecoloT1 = lst[a]
                efface_tout()
                return nomfichierob
                print("couleur séléctionnée de l'équipe 1 :",affichagecoloT1)
            if a == maxliste or a == -(maxliste) :
                a = 0
        #ce if c'est pour éviter le out of range

        if type_ev == "ClicGauche": #Dire le type de evenement (touche ou clic)
                x = int(clic_x(evenement)) #On note les co de x
                y = int(clic_y(evenement)) #On note les co de y
                #print((clic_x(evenement)),(clic_y(evenement)))
                # rectangle(860,650,1060,750)
                if 860<x<1060 and 200<y<300 :
                    a -=1
                if 860<x<1060 and 650<y<750 :
                    a +=1
                if a == maxliste or a == -(maxliste) :
                    a = 0  
                if 760<x<1160 and 800<y<900: #Dimension du bouton et if si le clic est dedans
                    nomfichierob = lst[a] #DONC SI ON CLIQUE ON CHOISIT LA COULEUR PR LA TEAM
                    efface_tout()
                    return nomfichierob
                if 1210<x<1610 and 800<y<900:
                    nomfichierob = 'ALEATOIRE'
                    efface_tout()
                    return nomfichierob
                if 310<x<710 and 800<y<900:
                    efface_tout()
                    nomfichierob = SPLAATOMAKER(False)
                    efface_tout()
                    return nomfichierob
                    
        mise_a_jour()
