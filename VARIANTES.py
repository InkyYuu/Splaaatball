# ==================================================================================== IMPORTS ========================================================================= #

from upemtk import *
from random import *
from math import *
from time import *
from os import path
from functools import lru_cache

from BOULE import Boule, distance, point_dans_boule
from CARRE import Carre

# ==================================================================================== VARIABLES ====================================================================== #
policevar = 'Franklin Gothic Medium Cond'
# ==================================================================================== FONCTIONS ====================================================================== #

def sauvegarder (couleurJ1, couleurJ2, lstJ1, lstJ2, tour, fin_partie, variantes, lstObs, banqueJ1, banqueJ2, PasseJ1) :

    rectangle(600,125,1320,250,'black','white',8,'info_terminaison')
    texte(950,170,'Voulez vous sauvegarder la partie en cours ?','black','center','Franklin Gothic Medium Cond', 14,'info_terminaison')
    texte(950,210,'Appuyer sur s pour sauvegarder ou cliquer pour quitter','black','center','Franklin Gothic Medium Cond', 14,'info_terminaison')

    while True :
            mise_a_jour()
            evenement = donne_evenement()
            type_ev = type_evenement(evenement) #type =  clic

            if type_ev == 'Touche': 
                nom_touche = touche(evenement)
                if nom_touche == 's':
                        lien = path.join(".","save","save.txt")

                        with open(lien,'w') as fichier :
                            fichier.write(str(couleurJ1)+'\n')
                            fichier.write(str(couleurJ2)+'\n')
                            fichier.write(str(lstJ1)+'\n')
                            fichier.write(str(lstJ2)+'\n')
                            fichier.write(str(tour)+'\n')
                            fichier.write(str(fin_partie)+'\n')
                            fichier.write(str(variantes)+'\n')
                            fichier.write(str(PasseJ1)+'\n')
                            if lstObs != [] :
                                fichier.write(str(lstObs)+'\n')
                            if banqueJ1 != None :
                                fichier.write(str(banqueJ1)+'\n')
                                fichier.write(str(banqueJ2)+'\n')
                        
                            ferme_fenetre()
                            quit()

            if type_ev == "ClicGauche":
                lien = path.join(".","save","save.txt")
                with open(lien,'w') as fichier :
                    fichier.truncate()
                ferme_fenetre()
                quit()

@lru_cache
def calcul_score(tuple_boule) -> int :
    """
    Paramètre :
    liste_boule : Type list - Contient les données des boules du joueur qui pose sa boule - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]

    Fonctionnement :
    La fonction vérifie si le pixel appartient aux ronds du joueurs et renvoie le score total cumulé
    """
    score = 0
    for boule in tuple_boule :
        for x in range (int(boule.x - boule.rayon),int(boule.x + boule.rayon)+1):
            for y in range (int(boule.y - boule.rayon),int(boule.y + boule.rayon)+1):
                if point_dans_boule(boule, x, y) :
                    score += 1
    return score

def creation_obstacles() -> list:
    """
    Fonctionnement:
    Renvoie une liste de sous listes contenant les données de boules sous forme : [X(int/float), Y(int/float), R(int/float), Tag(str)]
    Les boules ne dépassent pas de la zone de jeu
    """
    obstacles = []
    nbr = 0

    #Créer la liste sans avoir de boules qui dépassent de la zone de jeu
    while nbr != 15 :
        rond = Boule(randint(0,1220),randint(0,1029), choice([25,50,75,100,125,150]), 'black'+str(nbr))
        if rond.x - rond.rayon > 0 and rond.y + rond.rayon < 1029 and rond.x - rond.rayon > 0  and rond.y + rond.rayon < 1220 :
            obstacles.append(rond)
            cercle(rond.x,rond.y,rond.rayon,'black','black',tag=rond.tag)
            nbr += 1
        mise_a_jour()
    return obstacles

def affiche_cercles(lst, couleur) :
    for o in lst :
        cercle(o.x,o.y,o.rayon,remplissage=couleur,tag=o.tag)

def affiche_obstacles(lst) :
    for o in lst :
        if isinstance(o, Boule) :
            cercle(o.x,o.y,o.rayon,tag=o.tag,remplissage='black')
        if isinstance(o, Carre) :
            rectangle(o.x,o.y,o.x2,o.y2,tag=o.tag,remplissage='black')


def calcul_obstacles(Ox,Oy,rayon,liste_obstacle) -> bool:
    """
    Paramètres :
    Ox : type int or float - X de la boule que le joueur veut poser
    Oy : type int or float - Y de la boule que le joueur veut poser
    rayon : type int or float - Rayon de la boule que le joueur veut poser
    liste_obstacle : type list - liste de sous listes contenant les données de boules sous forme : [X(int/float), Y(int/float), R(int/float), Tag(str)]

    Fonctionnement :
    Regarde si la boule dépasse ou touche un obstacle

    Renvoie :
    False si la boule touche
    True si la boule ne touche pas
    """
    for h in range(len(liste_obstacle)):
            if isinstance(liste_obstacle[h], Boule)  :
                if point_dans_boule(liste_obstacle[h], Ox, Oy, rayon):
                    return False
            elif isinstance(liste_obstacle[h], Carre) :
                for x in range (int(Ox-rayon),int(Ox+rayon)+1):
                    for y in range(int(Oy-rayon),int(Oy+rayon)+1):
                        if sqrt((x-Ox)**2 + (y-Oy)**2) <= rayon :
                            if liste_obstacle[h].x < x < liste_obstacle[h].x2 and liste_obstacle[h].y < y < liste_obstacle[h].y2 :
                                return False
    return True

def affiche_fenetre_timer (joueur,variantes,lst_bouleJ1,lst_bouleJ2,couleurJ1,couleurJ2):
        """
        Paramètres :
        joueur : Type string - "Nom" du joueur
        liste_boule_J1: Type list - Contient les données des boules du joueur qui pose sa boule - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
        liste_boule_J2 : Type list - Contient les données des boules du joueur ennemi (qui ne pose pas sa boule) - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
        couleurJ1 : Type string - Couleur du joueur qui pose sa boule
        couleurJ2: Type string - Couleur du joueur ennemi (qui ne pose pas sa boule)
        variantes : Type list - Contient les informmations si les variables sont activées ou non (obstacles soit variante[5] contient une liste d'obstacle si le mode est activé)

        Fonctionnement :
        La fonction attend le clic de l'utilisateur puis va vérifier si la boule est posable en fonction des règles déterminées
        Les variantes viennent rajouter des appels de fonctions dans d'autres modules
        """

        rectangle(660,125,1260,250,'black',couleurJ1,5,'infotour')
        texte(960,170,'Au tour du '+str(joueur),'black','center','Franklin Gothic Medium Cond', 30,'titre')
        texte(960,220,'Cliquez pour passer','black','center','Franklin Gothic Medium Cond', 20,'soustitre')
        debuttimer = None
        while True :
            evenement = donne_evenement()
            type_ev = type_evenement(evenement)
            if debuttimer is not None :
                    while (time()-debuttimer) < 2 :
                        pass
                    efface("SJ1")
                    efface("SJ2")
            if type_ev == 'Touche': 
                nom_touche = touche(evenement)
                if variantes[1] == True :
                    if nom_touche == 's':
                        debuttimer = time()
                        ScoreFinJ1 = calcul_score(tuple(lst_bouleJ1))
                        ScoreFinJ2 = calcul_score(tuple(lst_bouleJ2))
                        texte(1320,535,"J1 :  "+str(ScoreFinJ1),taille=20,ancrage='center', couleur=couleurJ1,police=policevar,tag="SJ1")
                        texte(1480,535,"J2 :  "+str(ScoreFinJ2),taille=20,ancrage='center', couleur=couleurJ2,police=policevar,tag="SJ2")

            if type_ev == 'ClicGauche' :
                break
            mise_a_jour()
        efface('infotour')
        efface('titre')
        efface('soustitre')

def clicOxOy(variantes,lst_bouleJ1,lst_bouleJ2,couleurJ1,couleurJ2,tour,fin_partie,terme) -> int or float:
    """
    Paramètres :
    lst_bouleJ1: Type list - Contient les données des boules du joueur qui pose sa boule - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
    lst_bouleJ2 : Type list - Contient les données des boules du joueur ennemi (qui ne pose pas sa boule) - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
    couleurJ1 : Type string - Couleur du joueur qui pose sa boule
    couleurJ2: Type string - Couleur du joueur ennemi (qui ne pose pas sa boule)
    variantes : Type list - Contient les informmations si les variables sont activées ou non (obstacles soit variante[5] contient une liste d'obstacle si le mode est activé)

    Fonctionnement :
    Enregistre les coordonnées du joueur lorsqu'il clique et active la fonction score si besoin avec la variante score
    """
    Ox = None
    Oy = None
    debuttimer = None
    while Ox == None :
        evenement = donne_evenement()
        type_ev = type_evenement(evenement)
        if debuttimer is not None :
                while (time()-debuttimer) < 2 :
                    pass
                efface("SJ1")
                efface("SJ2")

        if type_ev == 'Touche': 
            nom_touche = touche(evenement)

            if variantes[1] == True :
                if nom_touche == 's':
                    debuttimer = time()
                    ScoreFinJ1 = calcul_score(tuple(lst_bouleJ1))
                    ScoreFinJ2 = calcul_score(tuple(lst_bouleJ2))
                    texte(1320,535,"J1 :  "+str(ScoreFinJ1),taille=20,ancrage='center', couleur=couleurJ1,police=policevar,tag="SJ1")
                    texte(1480,535,"J2 :  "+str(ScoreFinJ2),taille=20,ancrage='center', couleur=couleurJ2,police=policevar,tag="SJ2")
            if variantes[4] == True and terme == True:
                if nom_touche == 't':
                    fin_partie = tour + 6
                    terme = False
                    cercle(1740, 635, 75, 'red', 'white', 1, "fin_partie")
                    texte(1740,625,'Fin au tour :','red','center','Franklin Gothic Medium Cond', 17)
                    texte(1740,650,fin_partie,'red','center','Franklin Gothic Medium Cond', 25)


        if type_ev == 'ClicGauche' :
            Oy = clic_y(evenement)
            Ox = clic_x(evenement)
            return Ox,Oy,fin_partie,terme

        mise_a_jour()



def timer (fintps,variantes,lst_bouleJ1,lst_bouleJ2,couleurJ1,couleurJ2) -> int or float:
    """
    Paramètres :
    fintps : Type integer - Temps en seconde pour le chrono
    lst_bouleJ1: Type list - Contient les données des boules du joueur qui pose sa boule - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
    lst_bouleJ2 : Type list - Contient les données des boules du joueur ennemi (qui ne pose pas sa boule) - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
    couleurJ1 : Type string - Couleur du joueur qui pose sa boule
    couleurJ2: Type string - Couleur du joueur ennemi (qui ne pose pas sa boule)
    variantes : Type list - Contient les informmations si les variables sont activées ou non (obstacles soit variante[5] contient une liste d'obstacle si le mode est activé)

    Fonctionnement :
    Enregistre les coordonnées du joueur lorsqu'il clique en affichant le temps restant pour cliquer et active la fonction score si besoin avec la variante score
    """    
    
    debuttimer = time()
    debuttimerscore = None
    pose = False
    Ox = None
    Oy = None

    while int(time()-debuttimer) < fintps and pose != True :
        efface('timer2')
        rdt = round((fintps-(time()-debuttimer)),1)
        texte(1400, 400, str(rdt), 'red', 'center', 'Franklin Gothic Medium Cond', 50, 'timer1')

        if debuttimerscore is not None :
                while (time()-debuttimer) < 2 :
                    pass
                efface("SJ1")
                efface("SJ2")

        evenement = donne_evenement()
        type_ev = type_evenement(evenement) #type =  clic

        if type_ev == "ClicGauche": #Dire le type de evenement clic
            Ox = int(clic_x(evenement)) #On note les co de x
            Oy = int(clic_y(evenement)) #On note les co de y
            pose = True
            
        if type_ev == 'Touche': 
            nom_touche = touche(evenement)
            if variantes[1] == True :
                if nom_touche == 's':
                    debuttimerscore = time()
                    ScoreFinJ1 = calcul_score(tuple(lst_bouleJ1))
                    ScoreFinJ2 = calcul_score(tuple(lst_bouleJ2))
                    texte(1320,535,"J1 :  "+str(ScoreFinJ1),taille=20,ancrage='center', couleur=couleurJ1,police=policevar,tag="SJ1")
                    texte(1480,535,"J2 :  "+str(ScoreFinJ2),taille=20,ancrage='center', couleur=couleurJ2,police=policevar,tag="SJ2")
                
        if type_ev != 'ClicGauche':
            texte(1400, 400, str(rdt), 'red', 'center', 'Franklin Gothic Medium Cond', 50, 'timer2')
            efface('timer1')

        mise_a_jour()
        
    efface('timer1')
    efface('timer2')

    return Ox, Oy, fintps

def terminaison (tour, fin_partie,couleur) -> bool and int:
    """
    Paramètres :
    tour : Type integer - tour actuel
    fin_partie : Type integer - tour auquel le jeu se finit

    Fonctionnement:
    Demande au joueur s'il veut arrêter ou non le jeu dans 5 tours, modifie ensuite fin_partie si nécessaire (+5)
    Renvoie un booléen pour dire si terminaison doit être désactivé ou non et le tour auquel le jeu se finit
    """
    réponse = False
    rectangle(600,125,1320,250,couleur,'white',8,'info_terminaison')
    texte(950,170,'Tour suivant','black','center','Franklin Gothic Medium Cond', 14,'info_terminaison')
    texte(950,210,'Pour activer terminaison appuyez sur "t" ou cliquez pour passer','black','center','Franklin Gothic Medium Cond', 14,'info_terminaison')

    while réponse == False :
            evenement = donne_evenement()
            type_ev = type_evenement(evenement) #type =  clic

            if type_ev == 'Touche': 
                nom_touche = touche(evenement)
                if nom_touche == 't':
                    fin_partie = tour + 6
                    terme = False
                    cercle(1740, 635, 75, 'red', 'white', 1, "fin_partie")
                    texte(1740,625,'Fin au tour :','red','center','Franklin Gothic Medium Cond', 17)
                    texte(1740,650,fin_partie,'red','center','Franklin Gothic Medium Cond', 25)
                    réponse = True
            if type_ev == "ClicGauche":
                réponse = True
                terme = True
            mise_a_jour()

    efface('info_terminaison')
    return terme, fin_partie


def choix_taille_boules(banqueboules,couleurJ1,couleurJ2, lst_boule_J1, lst_boule_J2, tour, fin_partie, variantes, liste_obstacle, banqueboulesJ1, banqueboulesJ2,PasseJ1) -> int :
    """
    Paramètres : 
    banqueboules : Type integer - Banque du joueur

    Fonctionnement :
    Permet à l'utilisateur de rentrer un nombre puis l'enlever à sa banque et renvoie la banque actuel et le rayon voulu
    """


    rectangle(1240,20,1900,150,'black','white',10,tag='fen')
    rectangle(1600,375,1650,425)
    texte(1625,400,"0",ancrage='center')

    rectangle(1660,375,1710,425)
    texte(1685,400,"1",ancrage='center')

    rectangle(1720,375,1770,425)
    texte(1745,400,"2",ancrage='center')

    rectangle(1780,375,1830,425)
    texte(1805,400,"3",ancrage='center')

    rectangle(1840,375,1890,425)
    texte(1865,400,"4",ancrage='center')

    rectangle(1600,435,1650,485)
    texte(1625,460,"5",ancrage='center')

    rectangle(1660,435,1710,485)
    texte(1685,460,"6",ancrage='center')

    rectangle(1720,435,1770,485)
    texte(1745,460,"7",ancrage='center')

    rectangle(1780,435,1830,485)
    texte(1805,460,"8",ancrage='center')

    rectangle(1840,435,1890,485)
    texte(1865,460,"9",ancrage='center')

    rectangle(1600,495,1745,545)
    texte(1672,520,"Valider",ancrage='center')

    rectangle(1755,495,1890,545)
    texte(1822,520,"Effacer",ancrage='center')

    debuttimer = None
    debuttimerscore = None
    rayon = None
    chrrayon = ''
    while rayon is None :
            efface('choixTB')
            texte(1570,66,'Choix taille boules :',ancrage='center',tag='ctbr')

            texte(1380,110,"Banque :",ancrage='center',tag='choixTB')
            texte(1490,110,banqueboules,ancrage='center',tag='choixTB')

            texte(1650,110,"Taille :",ancrage='center',tag='choixTB')
            texte(1740,110,chrrayon,ancrage='center',tag='choixTB')

            #Truc pr faire des événement de la doc
            evenement = donne_evenement()
            type_ev = type_evenement(evenement) #type = touche ou clic

            if debuttimer is not None :
                while (time()-debuttimer) < 2 :
                    pass
                efface("SJ1")
                efface("SJ2")

            if type_ev == 'Touche': 
                nom_touche = touche(evenement)

                if variantes[1] == True :
                    if nom_touche == 's':
                        debuttimer = time()
                        ScoreFinJ1 = calcul_score(tuple(lst_boule_J1))
                        ScoreFinJ2 = calcul_score(tuple(lst_boule_J2))
                        texte(1320,535,"J1 :  "+str(ScoreFinJ1),taille=20,ancrage='center', couleur=couleurJ1,police=policevar,tag="SJ1")
                        texte(1480,535,"J2 :  "+str(ScoreFinJ2),taille=20,ancrage='center', couleur=couleurJ2,police=policevar,tag="SJ2")

            if type_ev == "ClicGauche": #Dire le type de evenement (touche ou clic)
                    x = int(clic_x(evenement)) #On note les co de x
                    y = int(clic_y(evenement)) #On note les co de y
                    #print((clic_x(evenement)),(clic_y(evenement)))
                    if 1600<x<1650 and 375<y<425:
                        chrrayon += '0'
                    if 1660<x<1710 and 375<y<425:
                        chrrayon += '1'
                    if 1720<x<1770 and 375<y<425:
                        chrrayon += '2'
                    if 1780<x<1830 and 375<y<425:
                        chrrayon += '3'
                    if 1840<x<1890 and 375<y<425:
                        chrrayon += '4'
                    if 1600<x<1650 and 435<y<485:
                        chrrayon += '5'
                    if 1660<x<1710 and 435<y<485:
                        chrrayon += '6'
                    if 1720<x<1770 and 435<y<485:
                        chrrayon += '7'
                    if 1780<x<1830 and 435<y<485:
                        chrrayon += '8'
                    if 1840<x<1890 and 435<y<485:
                        chrrayon += '9'
                    if 1755<x<1890 and 495<y<545:
                        chrrayon = ''
                    if 1360<x<1780 and 900<y<1000:
                        if variantes[5] == False :
                            liste_obstacle = []
                        sauvegarder(couleurJ1,couleurJ2, lst_boule_J1, lst_boule_J2, tour, fin_partie, variantes, liste_obstacle, banqueboulesJ1, banqueboulesJ2,PasseJ1)
                    if 1600<x<1745 and 495<y<545:
                        if 10<= int(chrrayon) <= 100 and int(chrrayon)<= banqueboules :
                            rayon = int(chrrayon)
                            banqueboules -= rayon
                            break
                        else : 
                            rectangle(1240,20,1900,150,'red',remplissage='white',epaisseur=10,tag='boitealerte')
                            texte(1570,80,'LA TAILLE DOIT ETRE CONTENUE ENTRE 10 ET 100',ancrage='center',couleur='red',tag='alerte',taille=18)
                            attente_clic()
                            efface('alerte')
                            efface('boitealerte')
            mise_a_jour()
    efface('fen')
    efface('ctbr')
    efface('choixTB')
    efface('alerte')
    return rayon,banqueboules

def detection_ennemi(liste_boule_ennemi,Ox,Oy,expension):
    proche = None
    for boule in liste_boule_ennemi :
        distance = sqrt((boule.x-Ox)**2 + (boule.y-Oy)**2)
        if distance < boule.rayon + expension :
            if proche == None :
                proche = (distance, boule)
            elif proche[0] > distance :
                proche = (distance,boule)
    return proche


def dynamique (lst_boule_J1,lst_boule_J2,couleurJ1,couleurJ2,expension,obstacles,liste_obstacle):
    """
    Paramètres :
    lst_boule : Type list - Contient les données des boules du joueur qui pose sa boule - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
    liste_boule_ennemi : Type list - Contient les données des boules du joueur ennemi (qui ne pose pas sa boule) - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
    couleur : Type string - Couleur du joueur qui pose sa boule
    couleur_ennemi : Type string - Couleur du joueur ennemi (qui ne pose pas sa boule)
    agrandissement : Type integer - Agrandissement pour la boule
    variante : Type bool - Si variante obstacle est activé ou non
    liste_obstacle : type list - liste de sous listes contenant les données de boules sous forme : [X(int/float), Y(int/float), R(int/float), Tag(str)]

    Fonctionnement :
    Fais grandir les boules de l'agrandissement en vérifiant que la boule de ne dépasse pas sur un obstacle ou l'ennemi

    /!\ ATTENTION MARGE D'ERREUR DÛ A L'UTILISATION D'INTERGER /!\
    """
    #============================================================================AVEC OBSTACLES==========================================================================================
    if obstacles == True :
        #==============CALCUL DISTANCE LST JOUEUR 1====================================================================================================================================
        for boule in lst_boule_J1 :
            if boule.y - boule.rayon < 5 or boule.y + boule.rayon > 1024 or boule.x - boule.rayon < 5  or boule.x + boule.rayon > 1215 :
                continue
            proche = detection_ennemi(lst_boule_J2,boule.x,boule.y,boule.rayon+expension) 
            #On calcule si il y a une boule proche 
            if proche != None :
                    if proche[0] <= 2.5 :
                        expension = proche[0]/2
                    else : 
                        expension = 5
                    if calcul_obstacles(proche[1].x, proche[1].y, proche[1].rayon+expension, liste_obstacle) == True and detection_ennemi(lst_boule_J1,proche[1].x, proche[1].y, proche[1].rayon+expension) == None:
                        Ox,Oy,rayon,tag = boule.x,boule.y,boule.rayon+expension,boule.tag
                        efface(boule.tag)
                        boule.changer_rayon(rayon)
                        cercle(Ox,Oy,rayon,remplissage=couleurJ1,tag=tag)
                        Ox,Oy,rayon,tag = proche[1].x, proche[1].y, proche[1].rayon+expension, proche[1].tag
                        efface(proche[1].tag)
                        boule.changer_rayon(rayon)
                        cercle(Ox,Oy,rayon,remplissage=couleurJ2,tag=tag)
            else  :
                if calcul_obstacles(boule.x, boule.y, boule.rayon+expension, liste_obstacle) == True:
                    Ox,Oy,rayon,tag = boule.x,boule.y,boule.rayon+expension,boule.tag
                    efface(boule.tag)
                    boule.changer_rayon(rayon)
                    cercle(Ox,Oy,rayon,remplissage=couleurJ1,tag=tag)
        #==============CALCUL DISTANCE LST JOUEUR 2====================================================================================================================================
        for boule in lst_boule_J2 :
            if boule.y - boule.rayon < 5 or boule.y + boule.rayon > 1024 or boule.x - boule.rayon < 5  or boule.x + boule.rayon > 1215 :
                continue
            proche = detection_ennemi(lst_boule_J1,boule.x,boule.y,boule.rayon+expension) 
            #On calcule si il y a une boule proche 
            if proche != None :
                    if proche[0] <= 2.5 :
                        expension = proche[0]/2
                    else : 
                        expension = 5
                    if calcul_obstacles(proche[1].x, proche[1].y, proche[1].rayon+expension, liste_obstacle) == True and detection_ennemi(lst_boule_J2,proche[1].x, proche[1].y, proche[1].rayon+expension) == None:
                        Ox,Oy,rayon,tag = boule.x,boule.y,boule.rayon+expension,boule.tag
                        efface(boule.tag)
                        boule.changer_rayon(rayon)
                        cercle(Ox,Oy,rayon,remplissage=couleurJ2,tag=tag)
                        Ox,Oy,rayon,tag = proche[1].x, proche[1].y, proche[1].rayon+expension, proche[1].tag
                        efface(proche[1].tag)
                        boule.changer_rayon(rayon)
                        cercle(Ox,Oy,rayon,remplissage=couleurJ1,tag=tag)
            else  :
                if calcul_obstacles(boule.x, boule.y, boule.rayon+expension, liste_obstacle) == True:
                    Ox,Oy,rayon,tag = boule.x,boule.y,boule.rayon+expension,boule.tag
                    efface(boule.tag)
                    boule.changer_rayon(rayon)
                    cercle(Ox,Oy,rayon,remplissage=couleurJ2,tag=tag)

    #============================================================================SANS OBSTACLES==========================================================================================
    #============================================================================SANS OBSTACLES==========================================================================================
    else :
        #==============CALCUL DISTANCE LST JOUEUR 1====================================================================================================================================
        for boule in lst_boule_J1 :
            if boule.y - boule.rayon < 5 or boule.y + boule.rayon > 1024 or boule.x - boule.rayon < 5  or boule.x + boule.rayon > 1215 :
                continue
            proche = detection_ennemi(lst_boule_J2,boule.x,boule.y,boule.rayon+expension) 
            #On calcule si il y a une boule proche 
            if proche != None :
                    if proche[0] <= 2.5 :
                        expension = proche[0]/2
                    else : 
                        expension = 5
                    if detection_ennemi(lst_boule_J1,proche[1].x, proche[1].y, proche[1].rayon+expension) == None:
                        Ox,Oy,rayon,tag = boule.x,boule.y,boule.rayon+expension,boule.tag
                        efface(boule.tag)
                        boule.changer_rayon(rayon)
                        cercle(Ox,Oy,rayon,remplissage=couleurJ1,tag=tag)
                        Ox,Oy,rayon,tag = proche[1].x, proche[1].y, proche[1].rayon+expension, proche[1].tag
                        efface(proche[1].tag)
                        boule.changer_rayon(rayon)
                        cercle(Ox,Oy,rayon,remplissage=couleurJ2,tag=tag)
            else  :
                Ox,Oy,rayon,tag = boule.x,boule.y,boule.rayon+expension,boule.tag
                efface(boule.tag)
                boule.changer_rayon(rayon)
                cercle(Ox,Oy,rayon,remplissage=couleurJ1,tag=tag)
        #==============CALCUL DISTANCE LST JOUEUR 2====================================================================================================================================
        for boule in lst_boule_J2 :
            if boule.y - boule.rayon < 5 or boule.y + boule.rayon > 1024 or boule.x - boule.rayon < 5  or boule.x + boule.rayon > 1215 :
                continue
            proche = detection_ennemi(lst_boule_J1,boule.x,boule.y,boule.rayon+expension) 
            #On calcule si il y a une boule proche 
            if proche != None :
                    if proche[0] <= 2.5 :
                        expension = proche[0]/2
                    else : 
                        expension = 5
                    if detection_ennemi(lst_boule_J2,proche[1].x, proche[1].y, proche[1].rayon+expension) == None:
                        Ox,Oy,rayon,tag = boule.x,boule.y,boule.rayon+expension,boule.tag
                        efface(boule.tag)
                        boule.changer_rayon(rayon)
                        cercle(Ox,Oy,rayon,remplissage=couleurJ2,tag=tag)
                        Ox,Oy,rayon,tag = proche[1].x, proche[1].y, proche[1].rayon+expension, proche[1].tag
                        efface(proche[1].tag)
                        boule.changer_rayon(rayon)
                        cercle(Ox,Oy,rayon,remplissage=couleurJ1,tag=tag)
            else  :
                Ox,Oy,rayon,tag = boule.x,boule.y,boule.rayon+expension,boule.tag
                efface(boule.tag)
                boule.changer_rayon(rayon)
                cercle(Ox,Oy,rayon,remplissage=couleurJ2,tag=tag)