from PIL import Image, ImageDraw


def generate_geometric_art(width=800, height=600):
    # Crée une image avec un fond bleu clair
    image = Image.new('RGB', (width, height), (173, 216, 230))  # Couleur RGB pour un bleu clair
    draw = ImageDraw.Draw(image)

    # Retourne l'image
    return image