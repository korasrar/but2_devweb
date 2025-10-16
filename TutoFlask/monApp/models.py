from .app import db, login_manager
from flask_login import UserMixin

class Auteur(db.Model):
    idA = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String(100))

    def __init__(self, Nom):
        self.Nom = Nom

    def __repr__ (self ):
        return "<Auteur (%d) %s>" % (self.idA , self.Nom)

class Livre(db.Model):
    idL = db.Column(db.Integer, primary_key=True)
    Prix = db.Column(db.Float)
    Titre = db.Column(db.String(255))
    Url = db.Column(db.String(255))
    Img = db.Column(db.String(255))
    auteur_id = db.Column (db.Integer , db.ForeignKey ("auteur.idA") )
    auteur = db.relationship ("Auteur", backref =db.backref ("livres", lazy="dynamic") )

    def __init__(self, Prix, Titre, Url, Img, auteur_id):
        self.Prix = Prix
        self.Titre = Titre
        self.Url = Url
        self.Img = Img
        self.auteur_id = auteur_id

    def __repr__ (self ):
        return "<Livre (%d) %s>" % (self.idL , self.Titre)
    
class User(db.Model, UserMixin):
    Login = db.Column (db.String(50), primary_key=True)
    Password = db.Column (db.String(64))

    def get_id(self):
        return self.Login
    
    @login_manager.user_loader
    def load_user(username):
        return User.query.get(username)

class Favori(db.Model):
    idF = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(50), db.ForeignKey('user.Login'))
    livre_id = db.Column(db.Integer, db.ForeignKey('livre.idL'))
    user = db.relationship('User', backref=db.backref('favoris', lazy='dynamic'))
    livre = db.relationship('Livre', backref=db.backref('favoris', lazy='dynamic'))

    def __init__(self, user_login, livre_id):
        self.user_login = user_login
        self.livre_id = livre_id

    def __repr__(self):
        return f"<Favori ({self.idF}) User: {self.user_login}, Livre ID: {self.livre_id}>"