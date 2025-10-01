from monApp.models import Livre

def test_livre_init():
    livre = Livre(0,"Test", "Url", "Img", 1)
    assert livre.Prix == 0 and livre.Titre == "Test" and livre.Url == "Url" \
            and livre.Img == "Img" and livre.auteur_id == 1

def test_livre_repr(testapp):
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert repr(livre) == "<Livre (1) Test>"