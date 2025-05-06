import numpy as np

from PIL import Image
from rembg import remove

def remove_background_and_add_gray(input_image_path, output_image_path, gray_color=(220, 220, 220)):
    """
    Quita el fondo de una imagen usando rembg y añade un fondo gris profesional.
    
    Args:
        input_image_path: Ruta a la imagen original
        output_image_path: Ruta donde guardar la imagen procesada
        gray_color: Tono de gris a usar como fondo (RGB). Por defecto un gris claro.
    """
    print("1. Cargando imagen original...")
    
    input_image_path = "Imagen.jpg"
    output_image_path = "./output_images/Imagen_procesada.jpg"

    # Cargar la imagen original
    img_original = Image.open(input_image_path)
    
    print("2. Removiendo el fondo de la imagen con rembg...")
    
    # Usar rembg para quitar el fondo (devuelve una imagen RGBA con transparencia)
    img_no_bg = remove(img_original)
    
    print("3. Procesando imagen con fondo transparente...")
    
    # Crear una nueva imagen con fondo gris
    img_with_gray_bg = Image.new('RGB', img_no_bg.size, gray_color)
    
    # Pegar la imagen sin fondo sobre el fondo gris
    # Si la imagen tiene un canal alfa (transparencia), lo utilizamos como máscara
    if img_no_bg.mode == 'RGBA':
        img_with_gray_bg.paste(img_no_bg, (0, 0), img_no_bg)
    else:
        img_with_gray_bg.paste(img_no_bg, (0, 0))
    
    # Guardar la imagen resultante
    img_with_gray_bg.save(output_image_path)
    print(f"3. Imagen con fondo gris guardada en: {output_image_path}")
    
    return True

# Ejemplo de uso
if __name__ == "__main__":
    # Rutas de ejemplo
    input_path = "foto_original.jpg"  # Cambia esto a la ruta de tu imagen
    output_path = "foto_profesional.jpg"
    
    # Puedes ajustar el tono de gris según lo que consideres más profesional
    # gris_claro = (230, 230, 230)  # Casi blanco
    # gris_medio = (180, 180, 180)  # Gris medio
    gris_oscuro = (120, 120, 120)  # Gris más oscuro
    
    # Procesar la imagen
    try:
        remove_background_and_add_gray(input_path, output_path, gray_color=gris_oscuro)
        print("¡Imagen procesada con éxito!")
    except Exception as e:
        print(f"Error al procesar la imagen: {str(e)}")
