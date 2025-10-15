from monApp import app, commands


def login(client, username, password, next_path):
    return client.post("/login/",
                       data={
                           "Login": username,
                           "Password": password,
                           "next": next_path
                       },
                       follow_redirects=True)


def test_livres_liste(client):
    response = client.get('/livres/')
    assert response.status_code == 200
    assert b'Test' in response.data


def test_livre_update_before_login(client):
    response = client.get('/livres/1/update/', follow_redirects=True)
    assert b"Login" in response.data


def test_livre_update_after_login(client, testapp):
    with testapp.app_context():
        response = client.get('/livres/1/update/', follow_redirects=False)
        assert response.status_code == 302
        assert "/login/?next=%2Flivres%2F1%2Fupdate%2F" in response.headers[
            "Location"]
        response = login(client, "CDAL", "AIGRE", "/livres/1/update/")
        assert response.status_code == 200
        assert b"Modification" in response.data


def test_livre_view(client, testapp):
    with testapp.app_context():
        response = client.get('/livres/1/view/')
        print(response.data)
        assert response.status_code == 200
        assert b"Consultation" in response.data
