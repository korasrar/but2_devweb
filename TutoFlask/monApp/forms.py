from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField
from wtforms.validators import DataRequired
from .models import User
from hashlib import sha256

class FormAuteur(FlaskForm):
    idA=HiddenField('idA')
    Nom = StringField ('Nom', validators =[DataRequired()])

class FormLivre(FlaskForm):
    idL=HiddenField('idL')
    Prix = StringField ('Prix', validators =[DataRequired()])


class FormCreateLivre(FlaskForm):
    Titre = StringField ('Titre', validators =[DataRequired()])
    Prix = StringField ('Prix', validators =[DataRequired()])
    Url = StringField ('Url', validators =[DataRequired()])
    Img = StringField ('Img', validators =[DataRequired()])
    Auteur_idA = StringField ('Auteur_idA', validators =[DataRequired()])


"""idL = db.Column(db.Integer, primary_key=True)
    Prix = db.Column(db.Float)
    Titre = db.Column(db.String(255))
    Url = db.Column(db.String(255))
    Img = db.Column(db.String(255))
    auteur_id = db.Column (db.Integer , db.ForeignKey ("auteur.idA") )
    auteur = db.relationship ("Auteur", backref =db.backref ("livres", lazy="dynamic") )"""
class LoginForm(FlaskForm):
    Login = StringField ('Identifiant')
    Password = PasswordField ('Mot de passe')
    next = HiddenField()

    def get_authenticated_user (self):
        unUser = User.query.get(self.Login.data)
        if unUser is None:
            return None
        m = sha256 ()
        m.update(self.Password.data.encode())
        passwd = m.hexdigest()
        return unUser if passwd == unUser.Password else None

class FavoriForm(FlaskForm):
    idF = HiddenField('idF')
    livre_id = StringField('Livre ID', validators=[DataRequired()])