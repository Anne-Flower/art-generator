from app import app

@app.route('/')
def home():
    return "Bienvenue dans la galerie d'art génératif !"
