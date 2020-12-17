# Breizhibus

## Contexte du projet

Breizhibus souhaite informatiser la gestion de ses lignes de bus. Pour le moment, l'appli n'est prévue que pour une utilisation interne. Dans un second temps, elle sera peut-être ouvert au public (avec, par exemple, une fonctionnalitée de calcul d'itinéraire).

La DSI a décidé d'utiliser MySQL et Python pour ce projet. MySQL, car Breizhibus gère les transports de Ploukusanagi, une petit ville. Il n'y a donc pas beaucoup de données à stocker. Et Python, parce que la DSI a entendu dire que c'était bien pour faire des sites web et des calculs sur les données. Et à terme, c'est des projets qui pourraient se développer.

Votre première mission est de mettre en place les bases de cette appli. Vous devez créer et remplir la base de donnée comme demandé dans la documentation client (Kata 1 MySQL) et préparer un code Python qui affiche la liste des lignes. Ce code doit aussi, pour une ligne choisie, afficher la liste des arrêts de cette ligne. L'affichage en mode console suffit pour cette première phase, mais si vous avez le temps, vous pouvez préparer une interface plus évoluée.

Après discussion avec les collaborateurs, Breizhibus ne souhaite plus d'affichage console, qui est jugé pas UX du tout. Il vous faut développer une interface graphique, même rudimentaire. De plus, ils ont besoin de pouvoir gérer les bus. Il vous faut faire un formulaire qui permet d'ajouter des bus en base et de les assigner à une ligne (un bus ne peut avoir qu'une seule ligne, mais une ligne peut avoir plusieurs bus). Il faut aussi pouvoir les modifier et les supprimer; Enfin, lorsque vous affichez les arrêts par ligne, affichez aussi les bus par ligne.

## Fonctionnement de l'appli

L'application est divisé en 3 fichiers :

* `connecteur.py` : connexion et manipulation de la base de donnée
* `interface.py` : interface graphique de l'application
* `main.py` : fonction principale de l'application

[fenetre principale](../images/fenetre1.png)

L'application se lance depuis le fichier `main.py`. Elle est composé d'une fenêtre principale depuis laquelle nous pouvons avoir accès à deux fonctionnalité.
