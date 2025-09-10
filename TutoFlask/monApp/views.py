from .app import app
from flask import render_template
from config import ABOUT
from config import CONTACT

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html",title ="R3.01 Dev Web avec Flask",name="Cricri")

@app.route('/about/')
def about():
    return render_template("about.html",title ="Dev Web | About",nom="Célestin",prenom="Maubert",age="17 ans")

@app.route('/contact/')
def contact():
    return render_template("contact.html",title ="Dev Web | Contact")

if __name__ == "__main__":
    app.run()