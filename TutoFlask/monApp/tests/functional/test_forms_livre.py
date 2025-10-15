from monApp.models import Livre
from monApp import db
from monApp.tests.functional.test_routes_auteur import login


def test_livre_save_success(client, testapp):
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert livre is not None
        idL = livre.idL
        ancien_prix = livre.Prix

        response = login(client, "CDAL", "AIGRE", "/livre/save/")
        response = client.post("/livre/save/",
                               data={
                                   "idL": idL,
                                   "Prix": 15.99
                               },
                               follow_redirects=True)
        assert response.status_code == 200
        assert f"/livres/{idL}/view/" in response.request.path

    with testapp.app_context():
        livre = Livre.query.get(idL)
        assert livre.Prix == 15.99
        assert livre.Prix != ancien_prix
