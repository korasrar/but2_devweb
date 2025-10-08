from monApp.models import User

def test_user_get_id():
    user = User(Login="testuser", Password="hashedpassword")
    assert user.get_id() == "testuser"

def test_user_loader(testapp):
    with testapp.app_context():
        user = User.query.get(1)
        print(User.load_user("CDAL"))
        assert User.load_user("CDAL").Login == "CDAL"