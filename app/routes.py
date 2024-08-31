import os
from flask import send_file
from app import app
from app.generate_art import generate_geometric_art


@app.route('/')
def home():
    return "Welcome to the Art Generator!"


@app.route('/generate')
def generate_art():
    image = generate_geometric_art()
    image_dir = os.path.join(os.getcwd(), "static")
    image_path = os.path.join(image_dir, "art.png")

    # Assurer que le dossier static existe
    os.makedirs(image_dir, exist_ok=True)

    print(f"Tentative de sauvegarde de l'image à : {image_path}")
    # Sauvegarder l'image
    try:
        image.save(image_path)
        print("Image sauvegardée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de l'image : {e}")
        return f"Erreur lors de la sauvegarde de l'image : {e}", 500

    # Vérifier si le fichier existe avant de l'envoyer
    if os.path.exists(image_path):
        print("Fichier trouvé, envoi de l'image...")
        try:
            return send_file(image_path, mimetype='image/png')
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'image : {e}")
            return f"Erreur lors de l'envoi de l'image : {e}", 500
    else:
        print("Fichier non trouvé après tentative de sauvegarde.")
        return "Image could not be generated.", 500
