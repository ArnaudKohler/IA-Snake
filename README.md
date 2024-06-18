# Projet d'IA - Q-Learning Snake

## Description du Projet

Ce projet implémente une intelligence artificielle pour jouer au jeu Snake en utilisant l'algorithme de Q-learning. Le but est de développer un agent capable d'apprendre à jouer de manière optimale en maximisant les récompenses obtenues au fil des épisodes.

## Structure du Projet

Le projet est structuré autour de plusieurs fichiers clés, notamment :

- `main.py`
- `agent.py`

### `main.py`

Le fichier `main.py` contient la boucle principale du programme. Cette boucle exécute un nombre défini d'épisodes, au cours desquels l'agent joue au jeu Snake, apprend et améliore sa stratégie. Voici un aperçu des fonctionnalités de `main.py` :

- Initialisation de l'environnement du jeu Snake.
- Boucle principale pour gérer le nombre d'épisodes.
- Appels à l'agent pour décider des actions à entreprendre.
- Mise à jour de l'environnement et gestion des récompenses.
- Sauvegarde de la Q-table à la fin de l'exécution.

Si `main.py` s'exécute jusqu'au bout, alors la Q-table est enregistrée localement. Pour charger la Q-table précédente au démarrage, l'utilisateur doit laisser les lignes suivantes dans `main.py` :

```python
try:
    agent.load_q_table('q_table.pkl')
    agent.epsilon = 0
    print("Q-table chargée avec succès.")
except FileNotFoundError:
    print("Aucune Q-table trouvée, création d'une nouvelle Q-table.")
