import os
import requests
from io import BytesIO
from PIL import Image
from rembg import remove
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
TIENDA_ID = os.getenv('TIENDA_ID')
USER_AGENT = os.getenv('USER_AGENT')

API_URL = f'https://api.tiendanube.com/v1/{TIENDA_ID}/products'
HEADERS = {
    'Authentication': f'bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json',
    'User-Agent': USER_AGENT
}

def obtener_productos():
    response = requests.get(API_URL, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def procesar_imagen_url(url, output_path, gray_color=(120, 120, 120)):
    resp = requests.get(url)
    resp.raise_for_status()
    img_original = Image.open(BytesIO(resp.content))
    img_no_bg = remove(img_original)
    img_with_gray_bg = Image.new('RGB', img_no_bg.size, gray_color)
    if img_no_bg.mode == 'RGBA':
        img_with_gray_bg.paste(img_no_bg, (0, 0), img_no_bg)
    else:
        img_with_gray_bg.paste(img_no_bg, (0, 0))
    img_with_gray_bg.save(output_path)
    print(f'✔ Procesada y guardada: {output_path}')

def main():
    output_folder = './output_images'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    productos = obtener_productos()
    for producto in productos:
        nombre = producto.get('name', {}).get('es', 'producto')
        id_producto = producto.get('id')
        imagenes = producto.get('images', [])
        for idx, imagen in enumerate(imagenes):
            url = imagen.get('src')
            if url:
                nombre_archivo = f'{id_producto}_{idx}.jpg'
                output_path = os.path.join(output_folder, nombre_archivo)
                try:
                    procesar_imagen_url(url, output_path)
                except Exception as e:
                    print(f'❌ Error procesando {url}: {str(e)}')

if __name__ == '__main__':
    main() 