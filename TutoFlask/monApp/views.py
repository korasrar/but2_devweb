from .app import app
from config import ABOUT
from config import CONTACT

@app.route('/')
def index():
    return "Hello world !"

@app.route('/about/')
def about():
    return ABOUT

@app.route('/contact/')
def contact():
    return CONTACT

if __name__ == "__main__":
    app.run()