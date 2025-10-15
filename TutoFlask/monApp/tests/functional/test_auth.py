def login(client, username, password, next_path):
    return client.post("/login/",
                       data={
                           "Login": username,
                           "Password": password,
                           "next": next_path
                       },
                       follow_redirects=True)

def test_login_success_with_redirect(client, testapp):
    with testapp.app_context():
        response = client.post("/login/",
                               data={
                                   "Login": "CDAL",
                                   "Password": "AIGRE",
                                   "next": "/auteurs/1/update/"
                               },
                               follow_redirects=True)
        assert response.status_code == 200
        assert b"Victor Hugo" in response.data


def test_login_success_without_next(client, testapp):
    with testapp.app_context():
        response = client.post("/login/",
                               data={
                                   "Login": "CDAL",
                                   "Password": "AIGRE"
                               },
                               follow_redirects=True)
        assert response.status_code == 200
        assert b"CDAL" in response.data


def test_logout_redirect_to_index(client, testapp):
    with testapp.app_context():
        login(client, "CDAL", "AIGRE", "/")
        response = client.get("/logout/", follow_redirects=True)
        assert response.status_code == 200
        assert b"Cricri" in response.data
