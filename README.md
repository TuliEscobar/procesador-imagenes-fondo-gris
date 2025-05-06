# Procesamiento por Lotes de Imágenes con Fondo Gris Profesional

Este proyecto permite procesar múltiples imágenes en una carpeta, eliminando su fondo y añadiendo un fondo gris profesional de manera automática y en paralelo, utilizando todos los núcleos de tu CPU.

## Requisitos

- Python 3.8 o superior
- Los módulos listados en `requirements.txt`:
  - Pillow
  - rembg

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Uso

1. Coloca las imágenes que deseas procesar en la carpeta `input_images` (pueden ser `.jpg`, `.jpeg` o `.png`).
2. Ejecuta el script principal:

```bash
python procesar_imagen_multi.py
```

3. Las imágenes procesadas se guardarán en la carpeta `output_images` con el fondo gris aplicado.

## Descripción del Script

- **procesar_imagen_multi.py**: Procesa todas las imágenes de la carpeta `input_images`, elimina el fondo usando `rembg` y coloca el recorte sobre un fondo gris profesional. El procesamiento se realiza en paralelo para mayor velocidad.

## Personalización

Puedes cambiar el tono de gris modificando la variable `gris_oscuro` en el script principal.

---

¿Dudas o sugerencias? ¡Abre un issue o contacta al autor! 