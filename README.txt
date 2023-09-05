README - SPLAAATBALL [V.3.25]
Par BREDEAU Kellian
et CHEVALIER Hélèna

#Description
Splaaatball est un projet python réalisé lors de notre premier semestre de BUT informatique à Gustave-Eiffel. 
Règles du jeu :
Le but du jeu est d'avoir le plus gros territoire possible !
Plus le territoire est repeint par votre couleur plus vous gagnez de points. Vous avez pour cela plusieurs possibilités : Poser votre boule sans quelle dépasse sur les bords.
Cliquer dans la boule d'un autre joueur pour lui séparer sa boule en deux
Attention : Vous ne pouvez pas intersecter la boule d'un adversaire. Il est uniquement autorisé d'intersecter sa boule. Plusieurs variantes sont à votre disposition pour améliorer votre expérience du jeu !

##Importants
Toutes les variantes sont jouables.

### Prérequis
Afin de pouvoir exécuter le jeu, veuillez d’abord installer :
* Python3 (version minimum 3.8)

#### Installation
1. Décompresser l'archive dans un dossier unique
2. Vérifier que vous possédez les fichiers suivants :
	CHOIXOBS.py
	CHOIXSAVE.py
	COLORS.py
	CUSTOMCOLOR.py
	DEBUT.py
	SPLAAATBALL.py
	SPLAAATOMAKER.py
	upemtk.py
	VARIANTES.py
	icones
	|	icone-terminaison-couleur-reduit.png
	|	icone-score-couleur-reduit.png
	|	icone-sablier-couleur-reduit.png
	|	icone-obstacles-couleur-reduit.png
	|	icone-dynamique-couleur-reduit.png
	|	icone-choix-taille-boule-couleur-reduit.png
	|	icone-terminaison-gris-reduit.png
	|	icone-score-gris-reduit.png
	|	icone-sablier-gris-reduit.png
	|	icone-obstacles-gris-reduit.png
	|	icone-dynamique-gris-reduit.png
	|	icone-choix-taille-boule-gris-reduit.png
	|	LOGO.png
	|	LOGOMAKER.png
	saves_obstacles
	|	chenille.txt
	|	circle.txt
	|	city.txt
	|	maginot.txt
	|	splaatballe.txt
	|	triforce.txt
	save_variantes
	|	grossit_pas_trop.txt
	|	partie_rapide.txt
	save
	|	couleurs.txt
	|   	save.txt

##### Exécution
1. Exécuter le fichier SPLAAATBALL.py
Vous pouvez jouer !

###### Organisation du programme
Pour alléger le programme, nous avons choisis de faire des interfaces graphiques qui n'ont pas besoin de paramètres du code principale des modules (ex : la fonction choix couleur dans le module COLORS ou la fonction début dans le module DEBUT). Notre code est donc composé d'un fichier principal "Bataille_Boules.py", des modules (COLORS, DEBUT, Obstacles, Upemtk) et d'images au format .png.
Dans les fichiers pythons, tous respectent un plan précis : 
- Imports pour utiliser des fonctions inhérentes à python3 (comme la nécessité du module math, random ou os)
- Imports de nos modules (si besoin)
- Fonctions où on définit en amont les fonctions que nous avons écris
- Variables utiles pour le code principale
- Code principal (Composé pour le moment de trois phases de jeu ; création du terrain, jeu, affichage des scores à la fin)

####### Choix techniques
Pour parvenir à réaliser ce rendu, nous avons décidé de prendre des lignes directrices pour notre code :
Dans un premier temps nous avons réalisé une étude papier de tous les cas possibles du jeu afin de cerner quelles sont les possibilités lors de la pose de rond pendant une partie de Splaaatball.
Ensuite nous avons utilisé des fonctions qui offrent la possibilité d'être appelées plusieurs fois et permettent donc d'alléger le code.
Pour les fonctions dont les paramètres n'étaient utilisés dans le code principale nous les avons adaptés en tant que modules dans des fichiers pour encore une fois épurer le code principal. Les interfaces graphiques sont donc des fonctions appelées depuis des modules artisanaux.
Pour rendre ce projet similaire à un jeu que nous pourrions trouver sur n'importes quelles plateformes, nous avons pris la décision de réaliser un GUI (Graphical User Interface), qui permet à l'utilisateur de jouer sans avoir à interagir avec la console. Nous avons donc fait un menu et des boutons cliquables (grâce au module Upemtk) pour améliorer l'expérience utilisateur. De même, nous avons réalisés un module pour choisir la couleur de son équipe, afin de rajouter de l'immersion au jeu et impliquer les joueurs avant même le début de la partie.
Nous avons également pensé à créer l'image du projet Splaaatball pour se différencier de la concurrence, avec la création d'un logo et d'icônes de jeu uniques à Splaaatball (hors l'icône sablier et score qui sont attente d'amélioration). L'idée de rajouter des éléments cachés dans le jeu (Easter Eggs) est une décision prise pour permettre à l'utilisateur de s'amuser en explorant les recoins du projet.
Nous avons également choisi d'enregistrer la position de chaque boule posée ou présente sur l'aire de jeu pour faciliter l'analyse de la relation entre la nouvelle boule posée et les anciennes.
Pour nous, un tour correspond à la point de chaque rond des joueurs.
Le score est également calculé au fur et à mesure pour faciliter le développement de la variante score mais aussi pour éviter des problèmes lors des calculs de lentilles.
Le score est calculé à partir du nombre de pixel possédés par chaque joueurs sur la carte.
Pour réaliser le cas où un joueur clique dans une boule adverse, nous avons utilisé l'espace vectoriel de l'aire de jeu pour calculer la séparation de la boule adverse en deux boules.
Pour réaliser le cas où un joueur intersecte une de ces boules précédentes, nous avons utilisé la loi des cosinus et l'avons appliqué à notre cas pour le généraliser afin de calculer l'intersection entre les deux boules (lentille).
Nous avons utilisés les modules random (pour créer de l'aléatoire dans certains points du code comme la création d'obstacles), math (pour la fonction sqrt ), os (pour trouver le chemin absolu des images) et time (pour mesurer le temps nécéssaire à certains points du code comme le sablier en cours de développement).

######### Problèmes rencontrés
Nous avons rencontré quelques problèmes lors de la réalisation du projet. Premièrement, la formule de calcul de la lentille nous as pris plus de temps puisque nous étions partis sur l'application du théorème d'Héron, qui s'est avéré une méthode peu efficace pour notre projet. 
Dans un second temps, nous travaillons activement à trouver comment permettre à l'utilisateur d'appuyer sur les touches "s" et "t" pour appliquer les variantes score et terminaisons alors que son jeu est en cours (ou le programme attend un clic et donc refuse d'exécuter la boucle qui réalise l'évènement touche). Ce problème a été résolu.
Ensuite, la variante Dynamique nous a posé un problème dans son calcul ; lors de certains calculs, cela ne detectait pas toujours les ronds et obstacles
Ralissement des intersections d'obstacles lors de dynamique à cause de l'ajout des carrés en obstacle

######### Variantes
Les variantes disponibles sont : 
Timer : Cette variante permet de jouer une partie où les tours sont chronométrés (variable qui peut-être définie dans le code du jeu) (par défaut : 5 secondes)
Score : Le score peut-être affiché en appuyant sur la touche du clavier 's' et le score apparaitera hors de la zone de jeu pendant 2 secondes.
	ATTENTION : L'activation du score dans le timer va entrainer l'apparition du score mais empêchera la pose du rond pendant 2 secondes.
Choix Taille Boule : Avec une banque de points données (par défaut : 400), il est possible de choisir le rayon de la boule (entre 10 et 100). Si la banque atteint un nombre inférieur à 10, alors les tours restants seront passés(puisqu'il ne peut plus poser)
Dynamique : Chaque boule posée va s'incrémente de 5 de rayon à la fin de chaque tour. Si elle compte après incrémentation déborder sur un obstacle ou une boule ennemie, elle s'arrete de grandir avant.
Terminaison : Le joueur a la possibilité de terminer la partie dans 5 tours à partir de son tour actuel. On va demander à l'utilisateur à chaque fin de tour.
Obstacles : Nous avons rajouté la possibilité de charger une aire de jeu qui possède des obstacles où on ne peut pas poser de boules à proximité ou à l'intérieur. Les obstacles sont représentés par des boules noires de tailles aléatoires.

######### Bonus
Création d'obstacle (Splaaatomaker)
Pause et sauvegarde

######### Petit plus
Sauvegarder les variantes et le nombre de tour
En passant par CUSTOMCOLOR.py, vous pouvez entrer un code Hex couleur pour jouer votre couleur préférée.

########## Droits d'auteurs
Les images sont réalisées par nous avec le logiciel Krita
icone de la coupe : https://www.argentan.fr/marches-publics/attachment/ico_coupe_300px/
icone du sablier : https://www.flaticon.com/fr/icone-gratuite/sablier_1046401?term=sablier&page=1&position=16&page=1&position=16&related_id=1046401&origin=tag
Python3 : https://www.python.org/downloads/
Upemtk est le module de l'université Gustave Eiffel
