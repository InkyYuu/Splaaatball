# ==================================================================================== IMPORTS ========================================================================= #

import json
from upemtk import *
from math import *
from os import path

# =============================================================================== NOS MODULES A NOUS ================================================================== #

from BOULE import Boule, point_dans_boule
from CARRE import Carre

# ==================================================================================== FONCTIONS ====================================================================== #


# ============================================================================== VARIABLES ================================================================================== #

#Fenêtres
hauteurFenetre = 1030
largeurFenetre = 1920

policevar = 'Franklin Gothic Medium Cond'
TAI = 45

# ================================================================================== CODE PRINCIPAL ========================================================================== #

def SPLAATOMAKER(independance):

    #Zone de jeu
    rectangle(0,0,1220,1029,'black')

    #Zone des paramètres
    rectangle(1221,0,1919,1029,'black','honeydew3')

    #Paramètres
    rectangle(1240,20,1900,150,'red','white',10,'boitedialogue')

    rectangle(1360,750,1780,850,'black','coral2',tag='Sauvegarder')
    texte(1570,800,"SAUVEGARDER", "black", "center",police=policevar)

    rectangle(1360,875,1780,975,'black','DeepSkyBlue3',tag='Quitter')
    texte(1570,925,"QUITTER", "black", "center",police=policevar)

    rectangle(1240,20,1900,150,'black','white',10,tag='fen')

    rectangle(1458,180,1548,270,'black')
    rectangle(1478,200,1528,250,'black','black')
    #1503
    rectangle(1590,180,1680,270,'black')
    cercle(1637,225,30,'black','black')

    rectangle(1240,301,1364,425)
    texte(1302,363,"0",ancrage='center',taille=TAI)

    rectangle(1374,301,1498,425)
    texte(1436,363,"1",ancrage='center',taille=TAI)

    rectangle(1508,301,1632,425)
    texte(1570,363,"2",ancrage='center',taille=TAI)

    rectangle(1642,301,1766,425)
    texte(1704,363,"3",ancrage='center',taille=TAI)

    rectangle(1776,301,1900,425)
    texte(1838,363,"4",ancrage='center',taille=TAI)

    rectangle(1240,435,1364,559)
    texte(1302,497,"5",ancrage='center',taille=TAI)

    rectangle(1374,435,1498,559)
    texte(1436,497,"6",ancrage='center',taille=TAI)

    rectangle(1508,435,1632,559)
    texte(1570,497,"7",ancrage='center',taille=TAI)

    rectangle(1642,435,1766,559)
    texte(1704,497,"8",ancrage='center',taille=TAI)

    rectangle(1776,435,1900,559)
    texte(1838,497,"9",ancrage='center',taille=TAI)


    rectangle(1240,580,1565,640)
    texte(1402,610,"Valider",ancrage='center')

    rectangle(1575,580,1900,640)
    texte(1737,610,"Effacer",ancrage='center')

    # =========================================================================================================================================================================== #
    # ==                                                                                   JEU                                                                                 == #
    # =========================================================================================================================================================================== #



    def choix_rayon():
        rayon = None
        chrrayon = ''
        while rayon is None :
                efface('choixTB')
                texte(1570,66,'Choix taille boules :',ancrage='center',tag='ctbr')

                texte(1480,100,"Taille :",ancrage='center',tag='choixTB')
                texte(1600,100,chrrayon,ancrage='center',tag='choixTB')

                #Truc pr faire des événement de la doc
                evenement = donne_evenement()
                type_ev = type_evenement(evenement) #type = touche ou clic

                if type_ev == 'Touche': 
                    nom_touche = touche(evenement)
                    if nom_touche == 'Return':
                        if 10 <= int(chrrayon):
                                rayon = int(chrrayon)
                                return rayon
                        else :
                            rectangle(1240,20,1900,150,'red',remplissage='white',epaisseur=10,tag='boitealerte')
                            texte(1570,80,'LA TAILLE DOIT ETRE CONTENUE ENTRE 10 ET 100',ancrage='center',couleur='red',tag='alerte',taille=18)
                            attente_clic()
                            efface('alerte')
                            efface('boitealerte')

                if type_ev == "ClicDroit": #Dire le type de evenement (touche ou clic)
                        x = int(clic_x(evenement)) #On note les co de x
                        y = int(clic_y(evenement)) #On note les co de y
                        print(calcul_effacer(x,y,lstobs))
                
                if type_ev == "ClicGauche": #Dire le type de evenement (touche ou clic)
                        x = int(clic_x(evenement)) #On note les co de x
                        y = int(clic_y(evenement)) #On note les co de y
                        #print((clic_x(evenement)),(clic_y(evenement)))
                        if 1240<x<1364 and 301<y<425:
                            chrrayon += '0'
                        if 1374<x<1498 and 301<y<425:
                            chrrayon += '1'
                        if 1508<x<1632 and 301<y<425:
                            chrrayon += '2'
                        if 1642<x<1766 and 301<y<425:
                            chrrayon += '3'
                        if 1776<x<1900 and 301<y<425:
                            chrrayon += '4'
                        if 1240<x<1364 and 435<y<559:
                            chrrayon += '5'
                        if 1374<x<1498 and 435<y<559:
                            chrrayon += '6'
                        if 1508<x<1632 and 435<y<559:
                            chrrayon += '7'
                        if 1642<x<1766 and 435<y<559:
                            chrrayon += '8'
                        if 1776<x<1900 and 435<y<559:
                            chrrayon += '9'
                        if 1575<x<1900 and 580<y<640:
                            chrrayon = ''
                        if 1360<x<1780 and 875<y<975:
                            ferme_fenetre()
                            quit()
                        if 1360<x<1780 and 750<y<850:
                            fin = True
                            break
                        if 1240<x<1565 and 580<y<640:
                            if 10 <= int(chrrayon):
                                rayon = int(chrrayon)
                                return rayon
                            else :
                                rectangle(1240,20,1900,150,'red',remplissage='white',epaisseur=10,tag='boitealerte')
                                texte(1570,80,'LA TAILLE DOIT ETRE CONTENUE ENTRE 10 ET 100',ancrage='center',couleur='red',tag='alerte',taille=18)
                                attente_clic()
                                efface('alerte')
                                efface('boitealerte')
                mise_a_jour()

    def pose_ronds (Ox, Oy, rayon,tour) :
        if Ox + rayon > 1220 :
            fautecercle(Ox, Oy, rayon, "FAUTE : Zone de jeu")
            return
        else :
            cercle(Ox,Oy,rayon,'black','black',tag='black'+str(tour))
            lstobs.append(Boule(Ox,Oy,rayon,'black'+str(tour)))
        mise_a_jour()

    def pose_carre(Ox,Oy,rayon,tour):
        if Ox + rayon > 1220 :
            fautecarre(Ox, Oy, rayon, "FAUTE : Zone de jeu")
            return
        else :
            rectangle(Ox,Oy,Ox+rayon,Oy+rayon,'black','black',tag='black'+str(tour))
            lstobs.append(Carre(Ox,Oy,rayon,'black'+str(tour)))
        mise_a_jour()

    def calcul_effacer(x,y,lst):
        for i in range(len(lst)):
            if isinstance(lst[i], Boule) :
                if point_dans_boule(lst[i], x, y):
                    efface(lst[i].tag)
                    lst.remove(lst[i])
                    return
            elif isinstance(lst[i], Carre) :
                if lst[i].x <= x <= lst[i].x2 and lst[i].y <= y <= lst[i].y2 :
                    efface(lst[i].tag)
                    lst.remove(lst[i])
                    return
                
    def clicOxOy():
        Ox = None
        Oy = None
        pose = False
        debuttimer = None
        while Ox == None :
            evenement = donne_evenement()
            type_ev = type_evenement(evenement)
            if type_ev == 'ClicGauche' :
                Oy = clic_y(evenement)
                Ox = clic_x(evenement)
                return Ox,Oy
            mise_a_jour()

    def fautecercle (Ox,Oy,rayon, text):
        if Ox != None :
            cercle(Ox,Oy,rayon,'red',tag='Faute')
        efface('tour')
        rectangle(1240,20,1900,150,'red',remplissage='white',epaisseur=10,tag='Faute')
        texte(1570,60,text,'red','center','Franklin Gothic Medium Cond',30,'Faute')
        attente_clic()
        efface('Faute')
        return
    
    def fautecarre (Ox,Oy,rayon,text):
        if Ox != None :
            rectangle(Ox,Oy,Ox+rayon,Oy+rayon,'red',tag='Faute')
        efface('tour')
        rectangle(1240,20,1900,150,'red',remplissage='white',epaisseur=10,tag='Faute')
        texte(1570,60,text,'red','center','Franklin Gothic Medium Cond',30,'Faute')
        attente_clic()
        efface('Faute')
        return
    
    def choix_forme():
        forme = None
        while forme == None :
            evenement = donne_evenement()
            type_ev = type_evenement(evenement)
            if type_ev == 'ClicGauche' :
                y = clic_y(evenement)
                x = clic_x(evenement)
                if 1600<x<1680 and 180<y<270:
                    forme = 'rond'
                    return forme
                if 1458<x<1548 and 180<y<270:
                    forme = 'carre'
                    return forme
            mise_a_jour()

    def clavier():
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

    #=========================================================== VARIABLES ==========================================================
    fin = False
    lstobs = []
    tour = 0
    #=========================================================== CODE PRINCIPAL  ==========================================================

    while fin != True :
        num_tour = str(tour + 1)
        rayon = choix_rayon()
        texte(1570,125,'CHOISIR LA FORME',ancrage='center',couleur='black',tag='ATTENTE',taille=15)
        if rayon is None :
            fin = True
        else :
            forme = choix_forme()
            efface('ATTENTE')
            texte(1570,125,'VEUILLEZ PLACER VOTRE FORME',ancrage='center',couleur='black',tag='ATTENTE',taille=15)
            Ox, Oy = clicOxOy()
            efface('ATTENTE')
            if forme == 'rond' :
                pose_ronds(Ox, Oy,rayon,num_tour)
            elif forme == 'carre' :
                pose_carre(Ox,Oy,rayon,num_tour)
            tour +=1

    efface_tout()
    nom = clavier()
    nom = str(nom)+".json"
    lien = path.join(".","saves_obstacles",nom)
    obstacles_data = [obs.to_dict() for obs in lstobs]
    
    with open(lien, 'w') as fichier:
            json.dump({"obstacles": obstacles_data}, fichier, indent=4)

    if independance == False :
        return nom


if __name__ == "__main__" :
    cree_fenetre(largeurFenetre,hauteurFenetre)
    SPLAATOMAKER(True)
    ferme_fenetre()
    quit()