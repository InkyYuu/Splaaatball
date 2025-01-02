from os import path
from math import *
from random import *
from upemtk import *
from CHOIXSAVE import *

def debut():
    hauteurFenetre = 1080
    largeurFenetre = 1920
    menu = True

    # COULEURS
    couleurboutonsGauche = 'SkyBlue2'
    couleurboutonsVar = 'snow'
    policevar = 'Franklin Gothic Medium Cond'
    lstcolo=['red','blue','green','cyan','pink','purple','yellow','orange']
    maxcolo = len(lstcolo)

    variants = {
        "sablier": {
            "x": 765,
            "y": 350,
            "actif": False,
            "description": "Attention, posez vite votre boule !\nLe temps vous est compté avant que\nvotre tour soit passé !"
        },
        "score": {
            "x": 1150,
            "y": 350,
            "actif": False,
            "description": "Vous pouvez appuyer sur votre touche \"s\"\ndu clavier pour faire apparaître vos scores\npendant 2 secondes"
        },
        "choix-taille-boule": {
            "x": 1535,
            "y": 350,
            "actif": False,
            "description": "Vous décidez de la taille de votre boule pour\nle tour. Vous commencez avec un certain\nbudget fixé, pour chaque boule posée, votre\nbudget diminue."
        },
        "dynamique": {
            "x": 765,
            "y": 675,
            "actif": False,
            "description": "La taille évolue automatiquement au fur et\nà mesure que la partie avance"
        },
        "terminaison": {
            "x": 1150,
            "y": 675,
            "actif": False,
            "description": "Une fois dans la partie vous pouvez\ndécider de la faire se finir dans 5 tours"
        },
        "obstacles": {
            "x": 1535,
            "y": 675,
            "actif": False,
            "description": "Le tableau commence avec certains obstacles\nque vos boules ne peuvent pas toucher."
        }
    }

    a = 0 #EasterEgg
    min_tour, max_tour = 5, 50
    tour = min_tour

    #====================================GROS BOUTONS========================================================================================================================

    cree_fenetre(largeurFenetre,hauteurFenetre)

    #FOND DECRAN
    rectangle(0,0,1920,1080,remplissage='honeydew3')

    #LE LOGO
    chemin = path.join('.','icones',"LOGO.png")
    image(largeurFenetre/2,100,chemin,'center')
    cercle((largeurFenetre/2)-200,80,30,'cyan','cyan')

    #JOUER
    rectangle(65,250,635,366,remplissage='DeepSkyBlue3')
    texte(350,308,"JOUER",ancrage='center',police='Franklin Gothic Medium Cond')

    #REGLE
    rectangle(65,396,635,804,remplissage='white')
    texte(350,600,"Règles du jeu :\n\nLe but du jeu est d'avoir le plus gros territoire possible !\nPlus le territoire est repeint par votre couleur plus vous \ngagnez de points.\n\nVous avez pour cela plusieurs possibilités :\n- Poser votre boule sans quelle dépasse sur les bords\n- Cliquer dans la boule d'un autre joueur pour lui \nséparer sa boule en deux\n\n - - - - - - - - - - - - - - - - ! ATTENTION ! - - - - - - - - - - - - - - - - \n\nVous ne pouvez pas intersecter la boule d'un adversaire !\nIl est uniquement autorisé d'intersecter sa boule.\nPlusieurs variantes sont à votre disposition pour PIMENTER\nle jeu !",ancrage='center', police='Franklin Gothic Medium Cond', taille=13)

    #QUITTER
    rectangle(65,834,635,950,remplissage='DeepSkyBlue3')
    texte(350,892,"QUITTER",ancrage='center',police='Franklin Gothic Medium Cond')

    #LIGNE
    ligne(700,250,700,950,epaisseur=5)

    #VARIANTS
    rectangle(765,250,1855,300,remplissage='orangered')
    texte(1310,275,'MENU DES VARIANTES',ancrage='center',police='Franklin Gothic Medium Cond')   

    for key, item in variants.items():
        bord = 'lime green' if item["actif"] else 'black'
        x, y = item['x'], item['y']    
        rectangle(x,y,x+320,y+275,'black',remplissage=couleurboutonsVar,epaisseur=10)
        texte(x+160,y+25,key,ancrage='center',police=policevar,taille=20)
        image(x+160,y+125, path.join('.','icones',f"icone-{key}-couleur-reduit.png"),'center')
        texte(x+160,y+235,item['description'],taille=10,ancrage='center',police=policevar)

    #====================================IFS===========================================================================================================================
    while menu == True :
            cercle((largeurFenetre/2)-125,57,50,lstcolo[a],lstcolo[a])

            #====================================VARIANTS===========================================================================================================================

            #Longueur dediée aux variants : 1220 de largeur 
            # On va dire 65 px entre chaques variants  tailleX des variants : 320px
            # Ligne de séparation faire 550 de haut donc 50 px entre chaque et tailleY des variants : 200px
            # longeur largeur 320  -  275 px 

            for key, item in variants.items():
                bord = 'lime green' if item["actif"] else 'black'
                x, y = item['x'], item['y']    
                rectangle(x,y,x+320,y+275,bord,epaisseur=10)

            #=======================================================LES CONDITIONNELLES=======================================================================
            rectangle(65,50,565,120, 'black', 'SandyBrown', epaisseur=2)
            texte(315,85,'Sauvegarder variantes choisies', 'black', 'center',taille=18, police=policevar)
            rectangle(65,130,565,200, 'black', 'Khaki', epaisseur=2)
            texte(315,165,'Choisir variantes sauvegardées', 'black', 'center',taille=18, police=policevar)

            rectangle(1505, 50, 1855, 200, 'black', epaisseur=2, tag= 'nombre_tour')
            texte(1680, 75, 'Nombre de tours (entre '+str(min_tour)+' et '+str(max_tour)+') :', 'black', 'center', policevar, 15, 'info-tour' )
            texte(1680, 100, '(Choix avec flèches haut/bas)', 'black', 'center', policevar, 10, 'info')
            efface('tour')
            texte(1680, 150, str(tour), 'red', 'center', policevar, 40, 'tour')
            
            evenement = donne_evenement()
            type_ev = type_evenement(evenement) #type = touche ou clic
            
            if type_ev == 'Touche': #Dire le type de evenement (touche ou clic)
                nom_touche = touche(evenement)
                if nom_touche == 'Up':
                    tour += 1
                
                if nom_touche == 'Down':
                    tour -= 1

                if tour > max_tour :
                    tour = min_tour

                if tour < min_tour :
                    tour = max_tour

            if type_ev == "ClicGauche": #Dire le type de evenement (touche ou clic)
                    x = int(clic_x(evenement)) #On note les co de x
                    y = int(clic_y(evenement)) #On note les co de y

                    #=================================================EASTER EGG===================================================
                    if ((largeurFenetre/2)-205)<x<((largeurFenetre/2)-25) and 37<y<97: 
                        a = a + 1
                    if a == 7 :
                        texte(largeurFenetre/2,200,"Bravo ceci est un Easter EGG !","lawn green",'center')
                    if a == maxcolo or a == -(maxcolo) :
                        a = 0
                    
                    #=================================================VARIANTS===========================================================
                    for key, item in variants.items():
                        Ox, Oy = item['x'], item['y']  
                        if Ox < x < (Ox + 320) and Oy < y < (Oy + 275):
                            # Alterner l'état de "actif"
                            item["actif"] = not item["actif"]

                    #=================================================BOUTONS PRINCIPAUX==============================================
                    #COORDONNEE DU BOUTON JOUER
                    if 65<x<635 and 250<y<366:
                        efface_tout()
                        lstvar = [data["actif"] for data in variants.values()]
                        return lstvar, tour

                    #COORDONNEE DU BOUTON QUITTER 
                    if 65<x<635 and 834<y<950: 
                        menu = False
                        quit()

                    #Boutons supplémentaires
                    if 65 < x < 565 and 50 < y < 120:
                        efface_tout()
                        nom = str(enregistrement())
                        lien = path.join(".","saves_variantes",nom+'.txt')
                        lstvar = [data["actif"] for data in variants.values()]
                        with open(lien,'x') as fichier :
                            fichier.write(str(lstvar)+'\n')
                            fichier.write(str(tour)+'\n')
                        return variants, tour


                    if 65 <x <565 and 130 <y< 200:
                        listes_fichiers = []
                        dossier = path.join('.','saves_variantes')
                        for i in (listdir(dossier)):
                            listes_fichiers.append(i)
                        fichiersa = str(choixsave(listes_fichiers))
                        lien = path.join('.','saves_variantes',fichiersa)
                        lstvar = [data["actif"] for data in variants.values()]
                        with open(lien, 'r') as liste :
                            lstvar = eval(liste.readline()[:-1])
                            tour = int(liste.readline()[:-1])
                        return lstvar, tour

            mise_a_jour()
    