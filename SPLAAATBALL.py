# ==================================================================================== IMPORTS ========================================================================= #

from upemtk import *
from math import sqrt, acos, pi
from random import *
from time import *
from os import listdir

# =============================================================================== NOS MODULES A NOUS ================================================================== #

from BOULE import Boule, distance, point_dans_boule
from COLORS import *
from DEBUT import *
from VARIANTES import *
from CHOIXOBS import *
from CHOIXSAVE import *

# ==================================================================================== FONCTIONS ====================================================================== #

def faute (Ox,Oy,rayon,couleur_allie, text) -> None:
    """
    Paramètres :
    Ox : Type int - abscisse du point
    Oy : Type int - ordonnée du point
    rayon : Type integer ou float - Rayon de la boule qui va être posé
    couleur_allie : Type string - Couleur du joueur qui pose sa boule
    text : Type string - Texte à afficher

    Fonctionnement :
    La fonction affiche un message d'erreur personnalisé qui attends un clic pour être passé
    """
    if Ox != None :
        cercle(Ox,Oy,rayon,couleur_allie,tag='Faute')
    efface('tour')
    texte(1570,60,text,'red','center','Franklin Gothic Medium Cond',30,'Faute')
    attente_clic()
    efface('Faute')
    return
    
def reprendre () :

    rectangle(600,125,1320,250,'black','white',8,'info_terminaison')
    texte(950,170,'Voulez vous reprendre la partie en cours ?','black','center','Franklin Gothic Medium Cond', 14,'info_terminaison')
    texte(950,210,'Appuyer sur r pour sauvegarder ou cliquer pour quitter','black','center','Franklin Gothic Medium Cond', 14,'info_terminaison')

    while True :
            evenement = donne_evenement()
            type_ev = type_evenement(evenement) #type =  clic

            if type_ev == 'Touche': 
                nom_touche = touche(evenement)
                if nom_touche == 'r':
                        return True

            if type_ev == "ClicGauche":
                ferme_fenetre()
                lien = path.join(".","save","save.json")
                with open(lien,'w') as fichier :
                    fichier.truncate()
                return False
                
            mise_a_jour()

def pose_ronds (Ox, Oy, liste_boule_allie,liste_boule_ennemi, couleur_allie, couleur_ennemi, tour, rayon, variantes) :
    """
    Paramètres :
    Ox : Type int - abscisse du point
    Oy : Type int - ordonnée du point
    liste_boule_allie : Type list - Contient les données des boules du joueur qui pose sa boule - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
    liste_boule_ennemi : Type list - Contient les données des boules du joueur ennemi (qui ne pose pas sa boule) - Sous forme [X(int/float), Y(int/float), R(int/float), Tag(str)]
    couleur_allie : Type string - Couleur du joueur qui pose sa boule
    couleur_ennemi : Type string - Couleur du joueur ennemi (qui ne pose pas sa boule)
    tour : Type integer - Numéro du tour actuel
    rayon : Type integer ou float - Rayon de la boule qui va être posé
    variantes : Type list - Contient les informmations si les variables sont activées ou non (obstacles soit variante[5] contient une liste d'obstacle si le mode est activé)

    Fonctionnement :
    La fonction attend le clic de l'utilisateur puis va vérifier si la boule est posable en fonction des règles déterminées
    Les variantes viennent rajouter des appels de fonctions dans d'autres modules

    Les différents cas étudiés :
    La bordure est dépassée - La boule est intersecter par une autre (allié ou ennemie) - Clique dans une boule existante (allié ou ennemie) - La boule est la première posée - Variantes
    """

    #Différencation des cas
    Cas1 = False 
    Cas2 = False
    Cas3 = False

    # ============================================================= Premières vérifications ========================================================== #
    
    #Bordure de l'écran
    if Oy - rayon < 0 or Oy + rayon > 1029 or Ox - rayon < 0  or Ox + rayon > 1220 :
        faute(Ox, Oy, rayon, couleur_allie, "FAUTE : Zone de jeu")
        return

    #Obstacles
    if variantes[5] != False : 
        divise = False
        for i in range(len(liste_boule_ennemi)):
            divise = point_dans_boule(liste_boule_ennemi[i], Ox, Oy)
        if calcul_obstacles(Ox,Oy,rayon,liste_obstacle) == False and divise == False:
            faute(Ox,Oy,rayon,couleur_allie,'FAUTE : Obstacle')
            return

    #Premier rond : Ajout sans passée par le reste des cas
    if liste_boule_allie == [] and liste_boule_ennemi == []:
        cercle(Ox,Oy,rayon,'black',couleur_allie,tag='boule'+couleur_allie+str(tour))
        liste_boule_allie.append(Boule(Ox,Oy,rayon,'boule'+couleur_allie+str(tour)))

    # ============================================================= Autres vérifications ========================================================== #
    
    else :

        # ============================================ Conditions ennemis : Rien / Intersection / Clique dessus =========================================== #
        
        for i in range(len(liste_boule_ennemi)):

            # ============================= Vérification si joueur appuie dans la couleur ennemie : division boule en 2 =============================== #
            if point_dans_boule(liste_boule_ennemi[i], Ox, Oy) :
                Cas3 = True
                indice = i
                break

            # ================================== Vérification si joueur intersec la couleur ennemie : interdit ======================================== #
            elif point_dans_boule(liste_boule_ennemi[i], Ox, Oy, rayon):
                Cas2 = True

        # ================================================================= Rien de particulier ========================================================= #
        if Cas2 == False and Cas3 == False :
            Cas1 = True

        # ==================================================== Affichage / Calcul / Manipulations des cas =============================================== #

        #Cas 1
        if Cas1 == True :
            cercle(Ox,Oy,rayon,'black',couleur_allie,tag='boule'+couleur_allie+str(tour))
            liste_boule_allie.append(Boule(Ox,Oy,rayon,'boule'+couleur_allie+str(tour)))

        #Cas 2
        elif Cas2 == True and Cas3 == False:
            faute(Ox,Oy,rayon,couleur_allie,'FAUTE : Intersection')

        #Cas 3
        elif Cas3 == True :

            #Calcul du vecteur
            vecteurU = [(Ox-liste_boule_ennemi[indice].x),(Oy-liste_boule_ennemi[indice].y)]
            normeU = sqrt((vecteurU[0]**2)+vecteurU[1]**2)

            #Calcul du nouveau rayon
            rayon_bouleclic = liste_boule_ennemi[indice].rayon- normeU
            rayon_boulerestante = normeU

            #Calcul des coordonnées de la nouvelle boule non choisie
            if rayon_boulerestante == 0 :
                return
            NewOx = (liste_boule_ennemi[indice].x)-((rayon_bouleclic/rayon_boulerestante)*(Ox-liste_boule_ennemi[indice].x))
            NewOy = (liste_boule_ennemi[indice].y)-((rayon_bouleclic/rayon_boulerestante)*(Oy-liste_boule_ennemi[indice].y))

            #Nouvelles sous-boules
            cercle(Ox,Oy,rayon_bouleclic,'black',couleur_ennemi,tag='boule'+couleur_ennemi+str(tour)+'A')
            cercle(NewOx,NewOy,rayon_boulerestante,'black',couleur_ennemi,tag='boule'+couleur_ennemi+str(tour)+'B')
            
            #Ajout des informations à la liste
            liste_boule_ennemi.append(Boule(Ox,Oy,rayon_bouleclic,'boule'+couleur_ennemi+str(tour)+'A'))
            liste_boule_ennemi.append(Boule(NewOx,NewOy,rayon_boulerestante,'boule'+couleur_ennemi+str(tour)+'B'))

            #Suppression ancienne boule et ancien score (soustraction)
            efface(liste_boule_ennemi[indice].tag)
            liste_boule_ennemi.pop(indice)
            
    mise_a_jour()

# ============================================================================== VARIABLES ================================================================================== #

#Fenêtres
hauteurFenetre = 1030
largeurFenetre = 1920

#Jeu
victoire = False
tour = 0
lst_boule_J1 = []
lst_boule_J2 = []
scoreJ1 = 0
scoreJ2 = 0
sauvegarde = False
liste_obstacle = []
policevar = 'Franklin Gothic Medium Cond'

def main():

    #Fenêtres
    global hauteurFenetre, largeurFenetre
    hauteurFenetre = 1030
    largeurFenetre = 1920

    #Jeu
    global victoire, tour, lst_boule_J1, lst_boule_J2, scoreJ1, scoreJ2, sauvegarde, liste_obstacle
    victoire = False
    tour = 0
    lst_boule_J1 = []
    lst_boule_J2 = []
    scoreJ1 = 0
    scoreJ2 = 0
    sauvegarde = False
    liste_obstacle = []
    policevar = 'Franklin Gothic Medium Cond'

    lien = path.join('.', 'save', 'save.json')
    if path.exists(lien):
        with open(lien, 'r') as f:
            try:
                data = json.load(f)
                if data:
                    cree_fenetre(largeurFenetre, hauteurFenetre)
                    if reprendre() == True:
                        efface_tout()  # Efface tout pour redémarrer la partie

                        # Initialisation des variables à partir du fichier JSON
                        sauvegarde = True
                        couleurJ1 = data.get("couleurJ1", "")
                        couleurJ2 = data.get("couleurJ2", "")
                        lst_boule_J1 = [Boule(int(b['x']), int(b['y']), int(b['rayon']), b['tag']) for b in data.get("lstJ1", [])]
                        lst_boule_J2 = [Boule(int(b['x']), int(b['y']), int(b['rayon']), b['tag']) for b in data.get("lstJ2", [])]
                        tour = data.get("tour")
                        fin_partie = data.get("fin_partie")
                        variantes = data.get("variantes")
                        PasseJ1 = data.get("PasseJ1")
                        
                        affiche_cercles(lst_boule_J1, couleurJ1)
                        affiche_cercles(lst_boule_J2, couleurJ2)

                        for obs in data.get("lstObs"):
                            if obs["type"] == "boule":
                                liste_obstacle.append(Boule(obs["x"], obs["y"], obs["rayon"], obs["tag"]))
                            elif obs["type"] == "carre":
                                liste_obstacle.append(Carre(obs["x"], obs["y"], obs["cote"], obs["tag"]))
                        if liste_obstacle:
                            affiche_obstacles(liste_obstacle)

                        banqueboulesJ1 = data.get("banqueJ1", None)
                        banqueboulesJ2 = data.get("banqueJ2", None)
            except json.JSONDecodeError:
                pass
                    
    if sauvegarde == False :
    #Menu jeu + Choix variantes
        variantes, fin_partie = debut()

    #Couleurs joueurs
        couleurJ1 = choixcouleur(1920,1030,"Joueur1")
        couleurJ2 = choixcouleur(1920,1030,"Joueur2")
        while couleurJ2 == couleurJ1 :
            couleurJ2 = choixcouleur(1920,1030,"Joueur2")

    # ================================================================================== CODE PRINCIPAL ========================================================================== #


    # =================================== Création variables des variantes ============================ #

        if variantes[5] == True :
            listes_fichiers = []
            dossier = path.join('.','saves_obstacles')
            for i in (listdir(dossier)):
                listes_fichiers.append(i)

            fichierob = choixobs(listes_fichiers)
            if fichierob == 'ALEATOIRE' :
                liste_obstacle = creation_obstacles()
            else :
                lien = path.join('.','saves_obstacles',fichierob)
                with open(lien, 'r') as f:
                        data = json.load(f)
                liste_obstacle = []
                for obs in data["obstacles"]:
                    if obs["type"] == "boule":
                        liste_obstacle.append(Boule(obs["x"], obs["y"], obs["rayon"], obs["tag"]))
                    elif obs["type"] == "carre":
                        liste_obstacle.append(Carre(obs["x"], obs["y"], obs["cote"], obs["tag"]))
                affiche_obstacles(liste_obstacle)

        if variantes[2] == True :
            banqueboulesvar4 = 50* fin_partie
            banqueboulesJ1 = banqueboulesvar4
            banqueboulesJ2 = banqueboulesvar4

    terme = True
    if sauvegarde == False :
        PasseJ1 = False

    # =================================================== Délimitation du terrain de jeu ============================================ #

    #Zone de jeu
    rectangle(0,0,1220,1029,'black')

    #Zone des paramètres
    rectangle(1221,0,1919,1029,'black','honeydew3')

    #Paramètres
    rectangle(1240,20,1900,150,'red','white',10,'boitedialogue')
    rectangle(1360,900,1780,1000,'black','DeepSkyBlue3',tag='Quitter')
    texte(1570,950,"QUITTER", "black", "center",police=policevar)

    #Affichage paramètres
    Mode = []
    for i in range (len(variantes)):
        if variantes[i] == True :
            Mode.append('-couleur-reduit.png')
        else :
            Mode.append('-gris-reduit.png')

    image(1400, 250, path.join('.','icones','icone-sablier' + Mode[0]),'center')
    image(1740, 250, path.join('.','icones','icone-choix-taille-boule' + Mode[2]),'center')
    texte(1740, 350, 'BANQUE', "red", "center", policevar, 30)
    image(1400, 635, path.join('.','icones','icone-score' + Mode[1]),'center')
    image(1740, 635, path.join('.','icones','icone-terminaison' + Mode[4]),'center')
    image(1400, 800, path.join('.','icones','icone-dynamique' + Mode[3]),'center')
    image(1740, 800, path.join('.','icones','icone-obstacles' + Mode[5]),'center')

    # =========================================================================================================================================================================== #
    # ==                                                                                   JEU                                                                                 == #
    # =========================================================================================================================================================================== #

    rayon = 50

    while victoire != True :
        for joueur in range (2):

            efface('numérotour')
            num_tour = 'Tour : ' + str(tour + 1)
            texte(1570,110,num_tour,ancrage='center', tag='numérotour',police=policevar)

            if not(joueur%2) :
                plusthunes = False
                if PasseJ1 == False :
                    efface('tour')
                    rectangle(1240,20,1900,150,couleurJ1,epaisseur=10,tag='tour')
                    texte(1570,60, "Au tour du J1", couleurJ1,'center',policevar, tag='tour')

                    if variantes[2] == True :
                        if banqueboulesJ1 <= 9 :
                            faute(0,0,0,couleurJ1,'Tour passé pour J1')
                            plusthunes = True
                        else :
                            rayon,banqueboulesJ1 = choix_taille_boules(banqueboulesJ1,couleurJ1,couleurJ2, lst_boule_J1, lst_boule_J2, tour, fin_partie, variantes, liste_obstacle, banqueboulesJ1, banqueboulesJ2, PasseJ1=False)

                    if plusthunes == False :        
                        if variantes[0] == True :
                            affiche_fenetre_timer('Joueur 1',variantes,lst_boule_J1,lst_boule_J2,couleurJ1,couleurJ2)
                            Ox, Oy, fintps = timer(5,variantes,lst_boule_J1,lst_boule_J2,couleurJ1,couleurJ2)
                            if Ox == None :
                                faute(Ox, Oy, rayon, couleurJ1, 'FAUTE : Temps écoulé !')
                        else :
                            Ox, Oy, fin_partie, terme = clicOxOy(variantes,lst_boule_J1,lst_boule_J2,couleurJ1,couleurJ2,tour,fin_partie,terme)

                    if Ox != None :
                        #Quitter
                        if 1360 < Ox < 1780 and 900 < Oy < 1000 :
                            if variantes[5] == False :
                                liste_obstacle = []
                            if variantes[2] == False :
                                banqueboulesJ1 = None
                                banqueboulesJ2 = None
                            sauvegarder(couleurJ1,couleurJ2, lst_boule_J1, lst_boule_J2, tour, fin_partie, variantes, liste_obstacle, banqueboulesJ1, banqueboulesJ2, PasseJ1=False)

                        pose_ronds (Ox, Oy, lst_boule_J1,lst_boule_J2, couleurJ1, couleurJ2, tour, rayon, variantes)

            else :
                plusthunes = False
                PasseJ1 = False
                efface('tour')
                rectangle(1240,20,1900,150,couleurJ2,epaisseur=10,tag='tour')
                texte(1570,60, "Au tour du J2", couleurJ2,'center', policevar, tag='tour')

                if variantes[2] == True :
                    if banqueboulesJ2 <= 9 :
                        faute(0,0,0,couleurJ2,'Tour passé pour J2')
                        plusthunes = True
                    else :
                        rayon,banqueboulesJ2 = choix_taille_boules(banqueboulesJ2,couleurJ1,couleurJ2, lst_boule_J1, lst_boule_J2, tour, fin_partie, variantes, liste_obstacle, banqueboulesJ1, banqueboulesJ2, PasseJ1=True)
                
                if plusthunes == False :
                    if variantes[0] == True :
                        affiche_fenetre_timer('Joueur 2',variantes,lst_boule_J1,lst_boule_J2,couleurJ2,couleurJ1)
                        Ox, Oy, fintps = timer(5,variantes,lst_boule_J1,lst_boule_J2,couleurJ1,couleurJ2)
                        if Ox == None :
                            faute(Ox, Oy, rayon, couleurJ2, 'FAUTE : Temps écoulé !')
                    else :
                        Ox, Oy, fin_partie, terme = clicOxOy(variantes,lst_boule_J1,lst_boule_J2,couleurJ1,couleurJ2,tour,fin_partie,terme)

                if Ox != None :
                    #Quitter
                    if 1360 < Ox < 1780 and 900 < Oy < 1000 :
                        if variantes[5] == False :
                            liste_obstacle = []
                        if variantes[2] == False :
                            banqueboulesJ1 = None
                            banqueboulesJ2 = None
                        sauvegarder(couleurJ1,couleurJ2, lst_boule_J1, lst_boule_J2, tour, fin_partie, variantes, liste_obstacle, banqueboulesJ1, banqueboulesJ2,PasseJ1=True)

                    pose_ronds(Ox, Oy, lst_boule_J2,lst_boule_J1, couleurJ2, couleurJ1, tour, rayon, variantes)
                
        if variantes[3] == True :
            if variantes[5] == False :
                liste_obstacle = []
            dynamique(lst_boule_J1,lst_boule_J2,couleurJ1,couleurJ2,5,variantes[5],liste_obstacle)

        if variantes[4] == True :
            variantes[4], fin_partie = terminaison(tour, fin_partie,couleurJ1)
        
        tour += 1
        if tour == fin_partie :
            lien = path.join(".","save","save.json")

            with open(lien,'w') as fichier :
                fichier.truncate()
            victoire = True
            fin = True

    # ============================================================================= AFFICHAGE DES SCORES ======================================================================= #

    if fin:
        scoreJ1 = calcul_score(tuple(lst_boule_J1))
        scoreJ2 = calcul_score(tuple(lst_boule_J2))
        
        # Détermination du résultat
        if scoreJ1 > scoreJ2:
            couleur, texte_victoire = couleurJ1, "VICTOIRE POUR JOUEUR 1"
        elif scoreJ1 < scoreJ2:
            couleur, texte_victoire = couleurJ2, "VICTOIRE POUR JOUEUR 2"
        else:
            couleur, texte_victoire = "black", "ÉGALITÉ"

        # Affichage des résultats
        rectangle(360, 315, 1560, 715, couleur, "white", epaisseur=5)
        texte(960, 450, texte_victoire, taille=60, ancrage="center", police=policevar)

        # Affichage des scores
        texte(960, 600, f"Score Joueur 1 : {scoreJ1}", taille=30, ancrage="center", couleur=couleurJ1, police=policevar)
        texte(960, 650, f"Score Joueur 2 : {scoreJ2}", taille=30, ancrage="center", couleur=couleurJ2, police=policevar)

        attente_clic()


if __name__ == "__main__":
    main()