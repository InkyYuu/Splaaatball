from os import path,listdir,popen,execl,system
from math import *
from random import *
from upemtk import *

hauteurFenetre = 1030
largeurFenetre = 1920

def customcolor(independance):
    policevar = "Arial"
    hexcode = "000000"
    valider = False
    #FOND DECRAN
    rectangle(0,0,largeurFenetre,hauteurFenetre,remplissage='honeydew3')
    #CEST LE TEXTE D'INFORMATION
    texte((largeurFenetre/2),60,"Entrez le hex code (6 caractères)",taille=60,ancrage='center',police=policevar)
    #Le ROND AU MILIEU
    cercle((largeurFenetre/2),((hauteurFenetre/2)-50),150,'black',"#"+hexcode,3)
    #BOUTON DE SELECTION
    rectangle(760,650,1160,750,'black','DeepSkyBlue3')
    texte(960,700,"ENTER",ancrage='center',taille=66,police=policevar)
    #RECTANGLE CLAVIER
    rectangle(760,175,1160,250,'black',epaisseur=5)

    while valider != True :
        texte(960,215,hexcode,'black','center',tag='hexcode')
        if len(hexcode) == 6 :
            cercle((largeurFenetre/2),((hauteurFenetre/2)-50),150,'black',"#"+hexcode,3)
        else : 
            cercle((largeurFenetre/2),((hauteurFenetre/2)-50),150,'black',"#"+"000000",3)


        #Truc pr faire des événement de la doc
        evenement = donne_evenement()
        type_ev = type_evenement(evenement) #type = touche ou clic

        if type_ev == "ClicGauche": #Dire le type de evenement (touche ou clic)
                        x = int(clic_x(evenement)) #On note les co de x
                        y = int(clic_y(evenement)) #On note les co de y
                        if 1840<x<1900 and 20<y<80 :
                            ferme_fenetre()
                        if 790<x<1160 and 650<y<750:
                            if len(hexcode) == 6 :
                                efface_tout()
                                nomcouleur = clavier()
                                saver(("#"+hexcode),nomcouleur)
                                return str("#"+hexcode)
                        else : 
                            continue

        listetouches = ['agrave','ampersand','eacute','quotedbl','apostrophe','parenleft','minus','egrave','underscore','ccedilla']
        if type_ev == 'Touche': 
            nom_touche = touche(evenement)
            if nom_touche == 'Return':
                if len(hexcode) == 6 :
                    efface_tout()
                    nomcouleur = clavier()
                    saver(("#"+hexcode),nomcouleur)
                    return str("#"+hexcode)
            if nom_touche == 'Delete':
                hexcode = hexcode[:-1]
            if nom_touche == 'BackSpace':
                hexcode = hexcode[:-1]
            if nom_touche in listetouches :
                hexcode += str(listetouches.index(nom_touche))
            if nom_touche in ['a','b','c','d','e','f'] :
                hexcode += nom_touche.upper()
            efface('hexcode')
        mise_a_jour()



def clavier():
    valider = False
    nom =''
    #================QUITTER ==================================================
    rectangle(1840,20,1900,80,'black','DeepSkyBlue3',4)
    texte(1870,50,"X",'black','center',taille=45)
    #================INFORMATIONS =============================================
    texte(990,350,"ATTENTION : Si vous appelez votre fichier par le nom d'un fichier déjà existant, le fichier précédent sera écrasé",'black','center')
    texte(990,410,'Seules les touches minuscules et "_" sont comptabilisées','black','center')
    #===================LOGO============================
    texte(990,200,'CUSTOM COLORS','black','center',taille=70)
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

def saver(couleur,nomcouleur):
    lien = path.join('.','save','couleurs.txt')

    with open (lien,'r') as fichier :
        lstcolo = fichier.readline()
        lstnomcolo = fichier.readline()
    lstcolo = lstcolo[:-1]
    lstnomcolo = lstnomcolo[:-1]

    with open (lien,'w') as fichier :
        fichier.write(lstcolo+","+"'"+couleur+"'"+"\n")
        fichier.write(lstnomcolo+","+"'"+nomcouleur+"'"+"\n")

if __name__ == "__main__" :
    cree_fenetre(largeurFenetre,hauteurFenetre)
    couleur = customcolor(True)
    ferme_fenetre()
    quit()