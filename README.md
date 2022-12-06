# Thème: Consommation de l'éléctricité en France
Le projet consiste à gérer des ensembles de données sur la consommation d'électricité française avec la motivation de créer :
- Visualisation des données sur une carte interactive(Clickable) de la France au niveau de la ville affichant la consommation annuelle moyenne d'électricité des ménages entre 2018 et 2021. 
- Prédiction de la consommation du jeudi 8 décembre sur l'ensemble de la journée.
## Group Membres

Ce Projet comporte deux  Parties la prédiction traitée par ABDOULAYE DIOP et la visualisation des données traitée par IKHLEF AIMENE

IKHLEF Aimene  : aimene.ikhlef@etu.umotpellier.com

DIOP Abdoulaye : abdoulaye.diop@etu.umontpellier.com 

## Workplan
### Prédiction

-  Nettoyage des données qui consiste à évaluer les valeurs manquantes 
		Dans ce projet le nettoyage sera simple car les valeurs manquantes ne sont dépendantes de la prédiction 

-  La variable Target qui est la variable Consommation annnuelle Tracer la courbe de la consommation annnuelle en fonction du temps pour voir la narure de la série temporelle  
		L' index d'une série temporelles doit etre le temps donc dans ce projet on va indexer la variable Année et le convertir à todate_time

- Faire une prédiction par le modéle ARIMA
### Visualisation
- Ajout des librairies nécéssaires au développement du l'application 
- Ajout de la fonctionnalité de la création de la carte 
- Ajout de la fonctionnalité d'ouverture automatique de la carte 
- Ajout de lecture du ficher .csv 
- Manipulation du fichier .csv 
- Création d'une class Test pour les tests unitaires.
- Utilisation de sphinx pour générer la documentation.
- Calcul du temps d'éxecution du script main. et affichage de l'espace memoire occupés par les blocs de code 

