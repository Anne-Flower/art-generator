from PIL import Image, ImageDraw
import random
import os
from flask import request, send_file
from app import app
from app.generate_art import generate_geometric_art
from flask_cors import CORS

CORS(app)

def generate_geometric_art(width=800, height=600, background_color='#fceecc', num_frames=2, shape_types=['circle', 'rectangle', 'line']):
    images = []
    for _ in range(num_frames):
        image = Image.new("RGB", (width, height), background_color)
        draw = ImageDraw.Draw(image)

        for _ in range(3):
            shape_type = random.choice(shape_types)
        
            if shape_type == 'circle':
                x0 = random.randint(0, width)
                y0 = random.randint(0, height)
                x1 = random.randint(x0, width)
                y1 = random.randint(y0, height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                draw.ellipse([x0, y0, x1, y1], outline=color, fill=color)
        
            elif shape_type == 'rectangle':
                x0 = random.randint(0, width)
                y0 = random.randint(0, height)
                x1 = random.randint(x0, width)
                y1 = random.randint(y0, height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                draw.rectangle([x0, y0, x1, y1], outline=color, fill=color)
        
            elif shape_type == 'line':
                x0 = random.randint(0, width)
                y0 = random.randint(0, height)
                x1 = random.randint(0, width)
                y1 = random.randint(0, height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                draw.line([x0, y0, x1, y1], fill=color, width=3)

        images.append(image)

    return images

@app.route('/')
def home():
    return "Welcome to the Art Generator!"

@app.route('/generate', methods=['POST'])
def generate_art():
    print("Requête POST reçue à /generate")

    data = request.get_json()
    if not data:
        print("Aucune donnée reçue")
        return "Aucune donnée reçue", 400

    print(f"Données reçues: {data}")

    try:
        width = int(data.get('width', 800))
        height = int(data.get('height', 600))
        background_color = str(data.get('background_color', '#fceecc'))
        num_frames = int(data.get('frames', 2))
        shape_types = data.get('shapes', ['circle', 'rectangle', 'line'])

        print(f"Paramètres: width={width}, height={height}, background_color={background_color}, num_frames={num_frames}, shape_types={shape_types}")  # Log 4

        images = generate_geometric_art(width=width, height=height, background_color=background_color, num_frames=num_frames, shape_types=shape_types)
        image_dir = os.path.join(os.getcwd(), "static")
        gif_path = os.path.join(image_dir, "art.gif")

        os.makedirs(image_dir, exist_ok=True)

        images[0].save(gif_path, save_all=True, append_images=images[1:], loop=6, duration=600)
        print("GIF sauvegardé avec succès.")

    except Exception as e:
        print(f"Erreur lors de la génération de l'image : {e}")  # Log 6
        return f"Erreur lors de la génération de l'image : {e}", 500

    if os.path.exists(gif_path):
        print("GIF trouvé, envoi...")
        try:
            return send_file(gif_path, mimetype='image/gif')
        except Exception as e:
            print(f"Erreur lors de l'envoi du GIF : {e}")  # Log 8
            return f"Erreur lors de l'envoi du GIF : {e}", 500
    else:
        print("GIF non trouvé après tentative de sauvegarde.")  # Log 9
        return "GIF could not be generated.", 500

