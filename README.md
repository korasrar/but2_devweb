# Dev Web

MAUBERT Célestin



# TP1 Flask

- Création d'une première application avec Flask
- Découverte de l'environnement de travail
- Création d'une vue simple
- Création des fichiers de configurations et des variables d'environnements
- Découverte de la structure de projet

# TP2 SQLAlchemy

- Modification de config.py pour l'ORM et de app.py pour l'activer
- Création de classes qui représente des tables et leur relation sous forme de classe python ( Livre et Auteur )
- Création d'un fichier commands.py qui permet de créer la base de données a partir d'un fichier de data et d'une nouvelle commande flask créer grace a une fonction ( loaddb )
- Interaction avec la bd depuis le shell Flask
- Requêtes et ajout de tuples dans la tables Auteur
- Requêtes avec relation ( ex: trouver les livres d'un auteur en paramètres )

# TP3 Templates HTML et static CSS

- Ajout des fichiers index.html, contact.html et about.html dans les templates de l'app
- Ajout d'un fichier de style dans le dossier static et changement dans les fichiers html
- Modification de views.py pour indiquer qu'elle template afficher a l'appelle de l'url spécifique ( route )
- Ajout de paramètre dans le render_templates pour afficher du texte différent sur la page en fonction de ces paramètres

# TP4 Bootstrap + Héritage et affichage de données

- Appel a la bd pour afficher des données par rapport aux auteurs et aux livres
- Héritage du fichier base.html pour le header (réduire les répétitions)
- Url dynamique avec paramètres pour changer l'affichage en fonction de ces paramètres
- Implémentation de bootstrap pour les templates et le front-end 

# TP5 Consultation/Modification/Création/Supression de données (WTF)

- Modification de base.html pour créer un nouvel auteur
- Création d'un formulaire a l'aide de WTF pour Modifier les informations d'un auteur (Nom)
- Création des autres formulaires pour le reste des changements pour Auteur
- Ajout d'une nouvelle ligne dans auteur_list.html afin de accéder a ces nouvelles pages(Voir, Editer)
- Création de fonction dans views.py pour commit les changements du formulaire fait par l'utilisateur dans la BD
- Pareil pour livre pour la partie view et update

# TP6 AUTH, Déconnexion, Redirection automatique et protection des vues

- Ajout d'un formulaire de connexion
- Modification de la navbar pour se connecter et se déconnecter
- Protection des vues et des fonctions si le user n'est pas login
- Redirection automatique d'un user si il tente de faire une action que nécessite de se connecter, si il se login, il sera automatiquement rediriger vers la page qu'il voulait accéder
- Création de commande flask pour créer un user et modifier son mot de passe

# TP7 Test, Coverage, Pytest

- Ajout de test et configuration d'une bd temporaire
- Création de rapport
- Création de test sur POST et GET
- Création de test sur forms et routes de auteur

## Lancer le projet

### Installation des dépendances

```bash
cd TutoFlask
virtualenv -p python3 venv
source venv/bin/activate  
pip install -r requirements.txt
```

### Initialiser la base de données

```bash
flask loaddb monApp/data/data.yml
```

### Créer un utilisateur (optionnel)

```bash
flask newuser <nom_utilisateur>
flask password <nom_utilisateur>
```

### Lancer l'application

```bash
flask run
```

L'application sera accessible à l'adresse : <http://127.0.0.1:5000/>

### Lancer les tests

```bash
coverage run -m pytest
```

### Générer le rapport de couverture

```bash
coverage report
coverage html
```
