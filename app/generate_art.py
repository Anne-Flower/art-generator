from PIL import Image, ImageDraw
import random

def generate_geometric_art(width=800, height=600, background_color='#fceecc', num_frames=2, shape_types=['circle', 'rectangle', 'line', 'cat']):
    images = []
 
    for _ in range(num_frames):
        # Créer une nouvelle image pour chaque frame
        image = Image.new("RGB", (width, height), background_color)
        draw = ImageDraw.Draw(image)

        # Générer des formes aléatoires parmi celles sélectionnées
        for _ in range(3):
            shape_type = random.choice(shape_types)  # Choisir un type de forme parmi ceux sélectionnés
        
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


        # Ajouter l'image à la liste des frames
        images.append(image)

    return images
