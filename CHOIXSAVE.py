from os import path,listdir,popen,execl,system
from math import *
from random import *
from upemtk import *

hauteurFenetre = 1030
largeurFenetre = 1920

def choixsave(lst):
#CEST LE TEXTE D'INFORMATION
    rectangle(0,0,1920,1030,'white','honeydew3')
    texte((largeurFenetre/2),60,"Choisissez votre fichier prédéfinis de variantes : ",taille=60,ancrage='center')

    #FLECHE GAUCHE
    rectangle(860,200,1060,300)
    texte(960,240,"↑",ancrage='center',taille=60)
    
    #FLECHE DROITE
    rectangle(860,650,1060,750)
    texte(960,690,"↓",ancrage='center',taille=60)
    
#============ MES AUTRES VARIABLES ================================================================
    maxliste = len(lst)
    nomfichiersa = None
    a = 1
#============ MON WHILE ================================================================
    # dans la doc c'est while true mais je fais arreter mon programme après selection de la couleur d'équipe dans nomfichierob (couleurTeam1)
    while nomfichiersa is None :

        #Truc pr faire des événement de la doc
        evenement = donne_evenement()
        type_ev = type_evenement(evenement) #type = touche ou clic

        #RAJOUT DALTONIEN
        efface('lol')
        #texte(960,380,lst[a-1],ancrage="center",tag='lol',taille=30)
        texte(960,475,lst[a],ancrage="center",tag='lol',taille=60)
        #texte(960,570,lst[a+1],ancrage="center",tag='lol',taille=30)

        #BOUTON DE SELECTION
        rectangle(760,800,1160,900,'black','DeepSkyBlue3')
        texte(960,850,"ENTER",ancrage='center',taille=50)


#============ LES TOUCHES ================================================================
        if type_ev == 'Touche': #Dire le type de evenement (touche ou clic)
            nom_touche = touche(evenement)
            if nom_touche == 'Up':
                a -= 1 
        # a c'est pour rappel l'indice dans la position de la liste donc si a change, la couleur aussi
            if nom_touche == 'Down':
                a += 1
            if nom_touche == 'Return': 
                #RETURN CEST ENTRER
                nomfichiersa = lst[a] #DONC SI ON CLIQUE ON CHOISIT LA COULEUR PR LA TEAM
                efface_tout()
                return nomfichiersa
            if a == maxliste or a == -(maxliste) :
                a = 0
        #ce if c'est pour éviter le out of range

        if type_ev == "ClicGauche": #Dire le type de evenement (touche ou clic)
                x = int(clic_x(evenement)) #On note les co de x
                y = int(clic_y(evenement)) #On note les co de y
                #print((clic_x(evenement)),(clic_y(evenement)))
                if 860<x<1060 and 200<y<300 :
                    a -=1
                if 860<x<1060 and 650<y<750 :
                    a +=1
                if a == maxliste or a == -(maxliste) :
                    a = 0
                if 760<x<1160 and 800<y<900: #Dimension du bouton et if si le clic est dedans
                    nomfichiersa = lst[a] #DONC SI ON CLIQUE ON CHOISIT LA COULEUR PR LA TEAM
                    efface_tout()
                    return nomfichiersa
                    
        mise_a_jour()



def enregistrement():
    valider = False
    nom =''
    #================QUITTER ==================================================
    rectangle(1840,20,1900,80,'black','DeepSkyBlue3',4)
    texte(1870,50,"X",'black','center',taille=45)
    #================LOGO =====================================================
    image(990,150,path.join('.','icones','LOGOMAKER.png'),ancrage='center')
    #================INFORMATIONS =============================================
    texte(990,350,"ATTENTION : Si vous appelez votre fichier par le nom d'un fichier déjà existant, le fichier précédent sera écrasé",'black','center')
    texte(990,410,'Seules les touches minuscules et "_" sont comptabilisées','black','center')
    #================INPUT ====================================================
    rectangle(490,500,1490,600,'black','white',4)
    #================VALIDER ==================================================
    rectangle(790,700,1190,800,'black','coral2',4)
    texte(990,750,'VALIDER','black','center',taille=24)

    while valider != True :
        texte(990,550,nom,ancrage='center',tag='nom')

        #Truc pr faire des événement de la doc
        evenement = donne_evenement()
        type_ev = type_evenement(evenement) #type = touche ou clic

        if type_ev == "ClicGauche": #Dire le type de evenement (touche ou clic)
                        x = int(clic_x(evenement)) #On note les co de x
                        y = int(clic_y(evenement)) #On note les co de y
                        if 1840<x<1900 and 20<y<80 :
                            ferme_fenetre()
                        if 790<x<1190 and 700<y<800:
                            return nom
                        else : 
                            continue

        if type_ev == 'Touche': 
            nom_touche = touche(evenement)
            if nom_touche == 'underscore' :
                nom += "_"
            if nom_touche == 'Return':
                valider = True
                return nom
            if nom_touche == 'Delete':
                nom = nom[:-1]
            if nom_touche == 'BackSpace':
                nom = nom[:-1]
            else :
                nom += nom_touche
            efface('nom')
        mise_a_jour()