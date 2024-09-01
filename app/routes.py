import os
from flask import request, send_file
from app import app
from app.generate_art import generate_geometric_art


@app.route('/')
def home():
    return "Welcome to the Art Generator!"


@app.route('/generate')
def generate_art():
    # Paramètres de l'URL
    width = int(request.args.get('width', 800))
    height = int(request.args.get('height', 600))
    background_color = str(request.args.get('background_color', '#fceecc'))
    num_frames = int(request.args.get('frames', 10))
    
    image = generate_geometric_art(width=width, height=height, background_color=background_color, num_frames=num_frames)
    image_dir = os.path.join(os.getcwd(), "static")
    image_path = os.path.join(image_dir, "art.png")

    images = generate_geometric_art(width=width, height=height, background_color=background_color, num_frames=num_frames)
    image_dir = os.path.join(os.getcwd(), "static")
    gif_path = os.path.join(image_dir, "art.gif")

    # Assurer que le dossier static existe
    os.makedirs(image_dir, exist_ok=True)

    
    try:
        images[0].save(gif_path, save_all=True, append_images=images[1:], loop=6, duration=600)
        print("GIF sauvegardé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du GIF : {e}")
        return f"Erreur lors de la sauvegarde du GIF : {e}", 500

    # Vérifier si le fichier existe avant de l'envoyer
    if os.path.exists(gif_path):
        print("GIF trouvé, envoi...")
        try:
            return send_file(gif_path, mimetype='image/gif')
        except Exception as e:
            print(f"Erreur lors de l'envoi du GIF : {e}")
            return f"Erreur lors de l'envoi du GIF : {e}", 500
    else:
        print("GIF non trouvé après tentative de sauvegarde.")
        return "GIF could not be generated.", 500
