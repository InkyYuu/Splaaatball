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
    lstbords=['black','lime green']
    maxcolo = len(lstcolo)

    #Variants par défauts
    variant_sablier = False
    variant_score = False
    variant_taille_boule = False
    variant_dynamique = False
    variant_terminaison = False
    variant_obstacles = False

    #Bords des Variants
    bord_sablier = 0
    bord_score = 0
    bord_taille_boule = 0
    bord_dynamique = 0
    bord_terminaison = 0
    bord_obstacle = 0
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

    #====================================IFS===========================================================================================================================
    while menu == True :
            cercle((largeurFenetre/2)-125,57,50,lstcolo[a],lstcolo[a])

            #====================================VARIANTS===========================================================================================================================

            #Longueur dediée aux variants : 1220 de largeur 
            # On va dire 65 px entre chaques variants  tailleX des variants : 320px
            # Ligne de séparation faire 550 de haut donc 50 px entre chaque et tailleY des variants : 200px

            #SABLIER
            rectangle(765,350,1085,625,lstbords[bord_sablier],remplissage=couleurboutonsVar,epaisseur=10)
            texte(925,375,"Sablier",ancrage='center',police=policevar,taille=20)
            image(925,475, path.join('.','icones',"icone-sablier-couleur-reduit.png"),'center')
            texte(925,585,"Attention, posez vite votre boule !\nLe temps vous est compté avant que\nvotre tour soit passé !",taille=10,ancrage='center',police=policevar)

            #SCORES
            rectangle(1150,350,1470,625,lstbords[bord_score],remplissage=couleurboutonsVar,epaisseur=10)
            texte(1310,375,"Affichage des scores",ancrage='center',police=policevar,taille=20)
            image(1310,475, path.join('.','icones',"icone-score-couleur-reduit.png"),'center')
            texte(1310,585,"Vous pouvez appuyer sur votre touche \"s\"\ndu clavier pour faire apparaître vos scores\npendant 2 secondes",taille=10,ancrage='center',police=policevar)

            #TAILLE
            rectangle(1535,350,1855,625,lstbords[bord_taille_boule],remplissage=couleurboutonsVar,epaisseur=10)
            texte(1695,375,"Choix taille des boules",ancrage='center',police=policevar,taille=20)
            image(1695,475, path.join('.','icones',"icone-choix-taille-boule-couleur-reduit.png"),'center')
            texte(1695,585,"Vous décidez de la taille de votre boule pour\n le tour. Vous commencez avec un certain\nbudget fixé, pour chaque boule posée, votre\nbudget diminue.",taille=10,ancrage='center',police=policevar)

            #DYNAMIQUE
            rectangle(765,675,1085,950,lstbords[bord_dynamique],remplissage=couleurboutonsVar,epaisseur=10)
            texte(925,700,"Dynamique",ancrage='center',police=policevar,taille=20)
            image(925,800, path.join('.','icones',"icone-dynamique-couleur-reduit.png"),'center')
            texte(925,910,"La taille évolue automatiquement au fur et\nà mesure que la partie avance",taille=10,ancrage='center',police=policevar)

            #TERMINAISON
            rectangle(1150,675,1470,950,lstbords[bord_terminaison],remplissage=couleurboutonsVar,epaisseur=10)
            texte(1310,700,"Terminaison",ancrage='center',police=policevar,taille=20)
            image(1310,800, path.join('.','icones',"icone-terminaison-couleur-reduit.png"),'center')
            texte(1310,910,"Une fois dans la partie vous pouvez\ndécider de la faire se finir dans 5 tours",taille=10,ancrage='center',police=policevar)

            #OBSTACLES
            rectangle(1535,675,1855,950,lstbords[bord_obstacle],remplissage=couleurboutonsVar,epaisseur=10)
            texte(1695,700,"Obstacles",ancrage='center',police=policevar,taille=20)
            image(1695,800, path.join('.','icones',"icone-obstacles-couleur-reduit.png"),'center')
            texte(1695,910,"Le tableau commence avec certains obstacles\nque vos boules ne peuvent pas toucher.",taille=10,ancrage='center',police=policevar)


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
                    #COORDONNEE VARIANT DYNAMIQUE rectangle 765,675,1085,950
                    if 765<x<1085 and 675<y<950:
                        if variant_dynamique == 0 :
                            variant_dynamique = True
                            bord_dynamique = 1
                        elif bord_dynamique == 1 :
                            variant_dynamique = False
                            bord_dynamique = 0

                    #COORDONNEE VARIANT SCORE rectangle 1150,350,1470,625
                    if 1150<x<1470 and 350<y<625:
                        if variant_score == 0 :
                            variant_score = True
                            bord_score = 1
                        elif bord_score == 1 :
                            variant_score = False
                            bord_score = 0

                    #COORDONNEE VARIANT CHOIX TAILLE rectangle 1535,350,1855,625
                    if 1535<x<1855 and 350<y<625:
                        if variant_taille_boule == 0 :
                            variant_taille_boule = True
                            bord_taille_boule = 1
                        elif bord_taille_boule == 1 :
                            variant_taille_boule = False
                            bord_taille_boule = 0
                
                    #COORDONNEE VARIANT OBSTACLE rectangle 765,350,1085,625
                    if 765<x<1085 and 350<y<625:
                        if variant_sablier == 0 :
                            variant_sablier= True
                            bord_sablier = 1
                        elif bord_sablier == 1 :
                            variant_sablier = False
                            bord_sablier = 0

                    #COORDONNEE VARIANT TERMINAISON rectangle 1150,675,1470,950
                    if 1150<x<1470 and 675<y<950:
                        if variant_terminaison == 0 :
                            variant_terminaison = True
                            bord_terminaison = 1
                        elif bord_terminaison == 1 :
                            variant_terminaison = False
                            bord_terminaison = 0

                    #COORDONNEE VARIANT OBSTACLE rectangle 1535,675,1855,950
                    if 1535<x<1855 and 675<y<950:
                        if variant_obstacles == 0 :
                            variant_obstacles = True
                            bord_obstacle = 1
                        elif bord_obstacle == 1 :
                            variant_obstacles = False
                            bord_obstacle = 0

                    #=================================================BOUTONS PRINCIPAUX==============================================
                    #COORDONNEE DU BOUTON JOUER
                    if 65<x<635 and 250<y<366:
                        lstvar = [variant_sablier,variant_score,variant_taille_boule,variant_dynamique,variant_terminaison,variant_obstacles]
                        efface_tout()
                        return lstvar, tour

                    #COORDONNEE DU BOUTON QUITTER 
                    if 65<x<635 and 834<y<950: 
                        menu = False
                        quit()

                    #Boutons supplémentaires
                    if 65 < x < 565 and 50 < y < 120:
                        lstvar = [variant_sablier,variant_score,variant_taille_boule,variant_dynamique,variant_terminaison,variant_obstacles]
                        efface_tout()
                        nom = str(enregistrement())
                        lien = path.join(".","saves_variantes",nom+'.txt')
                        with open(lien,'x') as fichier :
                            fichier.write(str(lstvar)+'\n')
                            fichier.write(str(tour)+'\n')
                        return lstvar, tour


                    if 65 <x <565 and 130 <y< 200:
                        listes_fichiers = []
                        dossier = path.join('.','saves_variantes')
                        for i in (listdir(dossier)):
                            listes_fichiers.append(i)
                        fichiersa = str(choixsave(listes_fichiers))
                        lien = path.join('.','saves_variantes',fichiersa)
                        with open(lien, 'r') as liste :
                            lstvar = eval(liste.readline()[:-1])
                            tour = int(liste.readline()[:-1])
                        return lstvar, tour

            mise_a_jour()
    