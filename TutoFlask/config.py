#>>>import random, string, os
#>>>"".join([random.choice(string.printable) for _ in os.urandom(24) ] )
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')

SECRET_KEY = "k_r&Kw?]ERsmw1@lx-Bow}4|"
ABOUT = "Bienvenue sur la page à propos de Flask !"
CONTACT = "<a href=""https://github.com/korasrar"">Github : @korasrar</a> "

BOOTSTRAP_SERVE_LOCAL = True