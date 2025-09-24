import click, logging as lg
from .app import app, db

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    '''Creates the tables and populates them with data.'''
    # création de toutes les tables
    db.drop_all()
    db.create_all()
    # chargement de notre jeu de données

    import yaml
    with open(filename, 'r') as file:
        lesLivres = yaml.safe_load(file)

        # import des modèles
        from . models import Auteur,Livre

        # première passe : création de tous les auteurs
        lesAuteurs = {}
        for livre in lesLivres :
            auteur = livre["author"]
            if auteur not in lesAuteurs :
                objet = Auteur(Nom=auteur)
                db.session.add(objet)
                lesAuteurs[auteur] = objet
        db.session.commit ()

        # deuxième passe : création de tous les livres
        for livre in lesLivres :
            auteur = lesAuteurs[livre["author"]]
            objet = Livre(Prix=livre["price"],
                    Titre=livre["title"],
                    Url=livre["url"],
                    Img=livre["img"],
                    auteur_id = auteur.idA)
            db.session.add(objet)
        db.session.commit()
        lg.warning('Database initialized!')

@app.cli.command()
def syncdb():
    '''Creates all missing tables.'''
    db.create_all()
    lg.warning('Database synchronized!')

@app.cli.command()
@click.argument('login')
@click.argument('pwd')
def newuser (login, pwd):
    '''Adds a new user'''
    from .models import User
    from hashlib import sha256
    m = sha256()
    m.update(pwd.encode())
    unUser = User(Login=login ,Password =m.hexdigest())
    db.session.add(unUser)
    db.session.commit()
    lg.warning('User ' + login + ' created!')

@app.cli.command()
@click.argument('login')
@click.argument('newpwd')
def newpasswrd(login, newpwd):
    """Change the password of the user in parameter

    Args:
        login (str): username
        newpwd (str): new password
    """
    from .models import User
    from hashlib import sha256
    m = sha256()
    m.update(newpwd.encode())
    user = db.session.get(User, login)
    user.Password = m.hexdigest()
    db.session.commit()
    lg.warning('User ' + login + ' as changed password!')
    """ 
    before : f3029a66c61b61b41b428963a2fc134154a5383096c776f3b4064733c5463d90
    after : c605615716a2873b4ef95fb727e0fe0147ce55e0673c30d40b4c7e508924cccc 
    """