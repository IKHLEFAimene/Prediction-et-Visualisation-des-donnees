# Partie visualisation
## Structure du projet
### data_prep.py
Script contenant la fonction **df_departement()** qui permet de traiter les données en entrée et avoir en sortie un dataframe qui contient la consomation moyenne annuelle par département.
### main.py
Script principale du projet.

Permet de faire appel à la fonction du script precedent dans une fonction appelé **data_per_depart** qui permet de derouler les differentes années disponibles dans les données en entrées et afficher pour chaque années la consomation annuelle de chaque département.

Pour à la fin afficher la carte interactive de la france qui montre la consomation annuelle par département.
### diagramme.py
Permet la visualisation des données traitées en un histograme.
### test_main.py
Permet de testet la fonction **data_per_depart** du script main.

## Détails
- Ajout des librairies nécéssaires au développement du l'application 
- Ajout de la fonctionnalité de la création de la carte 
- Ajout de la fonctionnalité d'ouverture automatique de la carte 
- Ajout de lecture du ficher .csv 
- Manipulation du fichier .csv 
- Création d'une class Test pour les tests unitaires.
- Utilisation de sphinx pour générer la documentation.
- Calcul du temps d'éxecution du script main. et affichage de l'espace memoire occupés par les blocs de code 
