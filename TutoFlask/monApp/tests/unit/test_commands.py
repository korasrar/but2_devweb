import pytest
import os
import tempfile
from monApp import db
from monApp.models import Auteur, Livre, User
from monApp.commands import loaddb, syncdb, newuser, newpasswrd
from hashlib import sha256


def test_syncdb_creates_tables(testapp, runner):
    with testapp.app_context():
        db.drop_all()

        result = runner.invoke(syncdb)

        assert result.exit_code == 0

        auteur = Auteur(Nom="Test Sync")
        db.session.add(auteur)
        db.session.commit()

        assert Auteur.query.count() == 1


def test_newuser_creates_user_with_hashed_password(testapp, runner):
    with testapp.app_context():
        login = "testuser"
        pwd = "testpassword"
        result = runner.invoke(newuser, [login, pwd])

        assert result.exit_code == 0

        user = User.query.get(login)
        assert user.Login == login

        m = sha256()
        m.update(pwd.encode())
        mdp_hash = m.hexdigest()
        assert user.Password == mdp_hash


def test_newpasswrd_changes_user_password(testapp, runner):
    with testapp.app_context():
        login = "changeuser"
        old_pwd = "oldpassword"
        m = sha256()
        m.update(old_pwd.encode())
        user = User(Login=login, Password=m.hexdigest())
        db.session.add(user)
        db.session.commit()

        ancien_hash = user.Password

        new_pwd = "newpassword"
        result = runner.invoke(newpasswrd, [login, new_pwd])

        assert result.exit_code == 0

        user = User.query.get(login)
        assert user.Password != ancien_hash

        m = sha256()
        m.update(new_pwd.encode())
        test_nv_hash = m.hexdigest()
        assert user.Password == test_nv_hash
