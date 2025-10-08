import pytest
from monApp import app,db, commands
from monApp.models import Auteur, Livre, User
from hashlib import sha256

@pytest.fixture
def testapp():
    app.config.update({"TESTING":True,"SQLALCHEMY_DATABASE_URI":
    "sqlite:///:memory:","WTF_CSRF_ENABLED": False})
    
    with app.app_context():
        db.create_all()
        # Ajouter un auteur de test
        auteur = Auteur(Nom="Victor Hugo")
        livre = Livre(Prix=3,Titre="Test", Url="Test", Img="test",auteur_id=1)
        #commands.newuser("CDAL","AIGRE") # fonctionne pas !!
        login = "CDAL"
        pwd = "AIGRE"
        m = sha256()
        m.update(pwd.encode())
        unUser = User(Login=login ,Password =m.hexdigest())
        db.session.add_all([auteur, livre, unUser])
        db.session.commit()
    yield app
        
    # Cleanup après les tests
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(testapp):
    return testapp.test_client()