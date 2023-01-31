from upemtk import *
from random import *
from math import *
from time import *
from os import path,listdir,popen,execl,system
from CUSTOMCOLOR import customcolor


def choixcouleur(largeurFenetre,hauteurFenetre,Joueur):
    """
    Paramètres:
        largeurFenetre : Type integer - Contient la largeur de la fenêtre du module qui va s'ouvrir
        hauteurFenetre : Type integer - Contient la hauteur de la fenêtre du module qui va s'ouvrir
        Joueur : Type string - Contient le nom du Joueur qui est entrain de choisir sa couleur

    Fonctionnement:
    La fonction choix couleur permet de choisir sa couleur afin de se différencier de son adversaire.
    Les couleurs utilisées sont celles du module upemtk qui sont égales à celles sur tkinter.(Donc libre à l'utilisateur de rajouter dans les listes de couleurs plus de couleurs du module).
    
    Renvoie : 
    Renvoie la couleur choisie en type string
    """
#=================== VARIABLES ET LISTES DE BASE ==================================================
    lien = path.join('.','save','couleurs.txt')

    with open (lien,'r') as fichier :
        lstcolo = eval(fichier.readline())
        lstcolofr = eval(fichier.readline())

    a = 0 #a c'est l'indice de la position dans la liste (voir en dessous)
    policevar = 'Franklin Gothic Medium Cond'

#============CREATION TRUC DE BASE DESSIN ========================================================

    #FOND DECRAN
    rectangle(0,0,largeurFenetre,hauteurFenetre,remplissage='honeydew3')

    #CEST LE TEXTE D'INFORMATION
    texte((largeurFenetre/2),60,"Choisissez votre couleur d\'équipe : "+str(Joueur),taille=60,ancrage='center',police=policevar)

    #FLECHE GAUCHE
    rectangle(460,365,660,565)
    texte(560,475,"<",ancrage='center',taille=110,police=policevar)
    
    #FLECHE DROITE
    rectangle(1260,365,1460,565)
    texte(1360,475,">",ancrage='center',taille=110,police=policevar)
    
    hexnb = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    codecustom = '#'
    for i in range(6):
        codecustom += choice(hexnb)

    rectangle(760,800,1160,900,'black',codecustom)
    texte(960,850,"CUSTOM",ancrage='center',taille=66,police=policevar)

#============ MES AUTRES VARIABLES ================================================================
    maxcolo = len(lstcolo)
    couleurT1 = None
    
#============ MON WHILE ================================================================
    # dans la doc c'est while true mais je fais arreter mon programme après selection de la couleur d'équipe dans couleurT1 (couleurTeam1)
    while couleurT1 is None :
        temps = time()

        #Truc pr faire des événement de la doc
        evenement = donne_evenement()
        type_ev = type_evenement(evenement) #type = touche ou clic

        #Le ROND AU MILIEU
        cercle((largeurFenetre/2),((hauteurFenetre/2)-50),150,'black',lstcolo[a],3)

        #RAJOUT DALTONIEN
        efface('lol')
        texte(960,250,(lstcolofr[a].upper()),lstcolo[a],"center",police=policevar,tag='lol',taille=60)

        #BOUTON DE SELECTION
        rectangle(760,650,1160,750,'black','DeepSkyBlue3')
        texte(960,700,"ENTER",ancrage='center',taille=66,police=policevar)

            

#============ LES TOUCHES ================================================================
        if type_ev == 'Touche': #Dire le type de evenement (touche ou clic)
            nom_touche = touche(evenement)
            if nom_touche == 'Left':
                a -= 1 
        # a c'est pour rappel l'indice dans la position de la liste donc si a change, la couleur aussi
                #print(a)
            if nom_touche == 'Right':
                a += 1
                #print(a)
            if nom_touche == 'Return': 
        #RETURN CEST ENTRER
                couleurT1 = lstcolo[a] #DONC SI ON CLIQUE ON CHOISIT LA COULEUR PR LA TEAM
                affichagecoloT1 = lstcolofr[a]
                efface_tout()
                return couleurT1

            if a == maxcolo or a == -(maxcolo) :
                a = 0
        #ce if c'est pour éviter le out of range

        if type_ev == "ClicGauche": #Dire le type de evenement (touche ou clic)
                x = int(clic_x(evenement)) #On note les co de x
                y = int(clic_y(evenement)) #On note les co de y
                #print((clic_x(evenement)),(clic_y(evenement)))
                if 460<x<660 and 365<y<565 :
                    a -=1
                if 1260<x<1460 and 365<y<565 :
                    a +=1
                if a == maxcolo or a == -(maxcolo) :
                    a = 0  
                if 760<x<1160 and 650<y<750: #Dimension du bouton et if si le clic est dedans
                    couleurT1 = lstcolo[a] #DONC SI ON CLIQUE ON CHOISIT LA COULEUR PR LA TEAM
                    #Confirmation
                    affichagecoloT1 = lstcolofr[a]
                    efface_tout()
                    return couleurT1
                if 760<x<1160 and 800<y<900:#rectangle(760,800,1160,900,'black',codecustom)
                    efface_tout()
                    couleurT = customcolor(False)
                    efface_tout()
                    return couleurT
        mise_a_jour()
    