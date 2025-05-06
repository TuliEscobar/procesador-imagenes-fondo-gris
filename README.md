# Procesamiento por Lotes de Imágenes con Fondo Gris Profesional

Este proyecto permite procesar múltiples imágenes en una carpeta, eliminando su fondo y añadiendo un fondo gris profesional de manera automática y en paralelo, utilizando todos los núcleos de tu CPU. Además, puedes procesar directamente las imágenes de productos de tu tienda Tiendanube.

## Requisitos

- Python 3.8 o superior
- Los módulos listados en `requirements.txt`:
  - Pillow
  - rembg
  - requests
  - python-dotenv

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Uso

### Procesamiento de imágenes locales

1. Coloca las imágenes que deseas procesar en la carpeta `input_images` (pueden ser `.jpg`, `.jpeg` o `.png`).
2. Ejecuta el script principal:

```bash
python procesar_imagen_multi.py
```

3. Las imágenes procesadas se guardarán en la carpeta `output_images` con el fondo gris aplicado.

### Procesamiento de imágenes desde Tiendanube

1. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
ACCESS_TOKEN=TU_ACCESS_TOKEN_AQUI
TIENDA_ID=TU_ID_DE_TIENDA_AQUI
```

2. Ejecuta el script:

```bash
python descargar_y_procesar_tiendanube.py
```

Las imágenes procesadas de los productos de tu tienda se guardarán en la carpeta `output_images`.

## Descripción de los Scripts

- **procesar_imagen_multi.py**: Procesa todas las imágenes de la carpeta `input_images`, elimina el fondo usando `rembg` y coloca el recorte sobre un fondo gris profesional. El procesamiento se realiza en paralelo para mayor velocidad.
- **descargar_y_procesar_tiendanube.py**: Obtiene las imágenes de los productos de tu tienda Tiendanube usando la API, las procesa y guarda el resultado en `output_images`.

## Personalización

Puedes cambiar el tono de gris modificando la variable `gris_oscuro` en los scripts principales.

## Notas

- La carpeta `output_images/` está incluida en `.gitignore` y no se subirá al repositorio.
- Recuerda mantener tu archivo `.env` fuera del control de versiones para proteger tus credenciales.

---

¿Dudas o sugerencias? ¡Abre un issue o contacta al autor! 