from monApp.models import Auteur, Livre
from monApp import db
from monApp.tests.functional.test_routes_auteur import login


def test_auteur_save_success(client, testapp):
    # Créer un auteur dans la base de données
    with testapp.app_context():
        auteur = Auteur(Nom="Ancien Nom")
        db.session.add(auteur)
        db.session.commit()
        idA = auteur.idA
        # simulation connexion user et soumission du formulaire
        response = login(client, "CDAL", "AIGRE", "/auteur/save/")
        response = client.post("/auteur/save/",
                               data={
                                   "idA": idA,
                                   "Nom": "Alexandre Dumas"
                               },
                               follow_redirects=True)
        # Vérifier que la redirection a eu lieu vers /auteurs/<idA>/view/ et que le contenu
        # est correct
        assert response.status_code == 200
        assert f"/auteurs/{idA}/view/" in response.request.path
        assert b"Alexandre Dumas" in response.data  # contenu de la page vue
        # Vérifier que la base a été mise à jour

    with testapp.app_context():
        auteur = Auteur.query.get(idA)
        assert auteur.Nom == "Alexandre Dumas"


def test_auteur_insert_succes(client, testapp):
    with testapp.app_context():
        # Simulation connexion user et soumission du formulaire
        response = login(client, "CDAL", "AIGRE", "/auteur/insert/")
        response = client.post("/auteur/insert/",
                               data={"Nom": "Alexandre Dumas"},
                               follow_redirects=True)
        # Vérifier que la redirection a eu lieu et que le contenu est correct
        assert response.status_code == 200
        # Vérifier que l'auteur a été créé dans la base de données
        auteur = Auteur.query.filter_by(Nom="Alexandre Dumas").first()
        assert auteur is not None
        assert auteur.Nom == "Alexandre Dumas"
        assert f"/auteurs/{auteur.idA}/view/" in response.request.path

    with testapp.app_context():
        auteur = Auteur.query.filter_by(Nom="Alexandre Dumas").first()
        assert auteur is not None


def test_auteur_erase_success(client, testapp):
    # Créer un auteur dans la base de données pour le supprimer ensuite
    with testapp.app_context():
        auteur = Auteur(Nom="Auteur à Supprimer")
        db.session.add(auteur)
        db.session.commit()
        idA = auteur.idA

        # Simulation connexion user et soumission du formulaire de suppression
        response = login(client, "CDAL", "AIGRE", "/auteur/erase/")
        response = client.post("/auteur/erase/",
                               data={"idA": idA},
                               follow_redirects=True)
        # Vérifier que la redirection a eu lieu
        assert response.status_code == 200
        # Vérifier que l'auteur a été supprimé de la base de données
        auteur = Auteur.query.get(idA)
        assert auteur is None

    with testapp.app_context():
        auteur = Auteur.query.get(idA)
        assert auteur is None
