# Breizhibus

## Contexte du projet

Breizhibus souhaite informatiser la gestion de ses lignes de bus. Pour le moment, l'appli n'est prévue que pour une utilisation interne. Dans un second temps, elle sera peut-être ouvert au public (avec, par exemple, une fonctionnalitée de calcul d'itinéraire).

La DSI a décidé d'utiliser MySQL et Python pour ce projet. MySQL, car Breizhibus gère les transports de Ploukusanagi, une petit ville. Il n'y a donc pas beaucoup de données à stocker. Et Python, parce que la DSI a entendu dire que c'était bien pour faire des sites web et des calculs sur les données. Et à terme, c'est des projets qui pourraient se développer.

Votre première mission est de mettre en place les bases de cette appli. Vous devez créer et remplir la base de donnée comme demandé dans la documentation client (Kata 1 MySQL) et préparer un code Python qui affiche la liste des lignes. Ce code doit aussi, pour une ligne choisie, afficher la liste des arrêts de cette ligne. L'affichage en mode console suffit pour cette première phase, mais si vous avez le temps, vous pouvez préparer une interface plus évoluée.

Après discussion avec les collaborateurs, Breizhibus ne souhaite plus d'affichage console, qui est jugé pas UX du tout. Il vous faut développer une interface graphique, même rudimentaire. De plus, ils ont besoin de pouvoir gérer les bus. Il vous faut faire un formulaire qui permet d'ajouter des bus en base et de les assigner à une ligne (un bus ne peut avoir qu'une seule ligne, mais une ligne peut avoir plusieurs bus). Il faut aussi pouvoir les modifier et les supprimer; Enfin, lorsque vous affichez les arrêts par ligne, affichez aussi les bus par ligne.

## Fonctionnement de l'appli

L'application est divisée en 3 fichiers :

* `connecteur.py` : connexion et manipulation de la base de donnée
* `interface.py` : interface graphique de l'application
* `main.py` : fonction principale de l'application

L'application se lance depuis le fichier `main.py`. Elle est composée d'une fenêtre principale depuis laquelle nous pouvons avoir accès à deux fonctionnalités.

![fenetre principale](https://github.com/PaulSabia/Breizhibus/blob/main/images/fenetre1.PNG)

La première fonctionnalité permet de visualiser les différents arrêts d'une ligne en particulier, ainsi que de voir les différents bus qui déservent la ligne.

![fenetre secondaire](https://github.com/PaulSabia/Breizhibus/blob/main/images/fenetre2.PNG)

La deuxième fonctionnalité permet, quant à elle, de gérer les différents bus. Ajouter de nouveau bus, les attribuer à une ligne, ainsi que de pouvoir les modifier ou supprimer.

![fenetre tertiaire](https://github.com/PaulSabia/Breizhibus/blob/main/images/fenetre3.PNG)


## Choix techniques

L'applicationa est codé en objet. En effet cette méthode permet de mieux structurer celui-ci avec un minimum de répétitions, ainsi qu'une plus grande maintenabilité. 

Pour l'interface graphique, j'ai utilisé le GUI standart de Python : Tkinter. Mon choix s'est porté sur Tkinter car il y a beaucoup de documentations disponible sur le net. Cependant, avec un peu de pratique, le passage à un nouveau GUI, plus simple design est envisagé.

## Difficultés rencontrées 

Lors de ce projet, la principale difficultée rencontrée fut l'inteface graphique. Et plus particulièrement, les événements lors de l'appui d'un bouton, ainsi que le positionnement des différents widgets. Afin de surpasser celles-ci, il y a eu un part importante de veille et de recherche. Notamment sur le forum qui n'est plus à présenter : https://stackoverflow.com . 
Les autres projets réalisés en parrallèle de celui-ci m'ont également permis d'accroître ma compréhension et ma connaissance de Tkinter. 

Un [lien](https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter) particulièrement utile afin de switcher sur plusieurs pages dans une même fenêtre. 
