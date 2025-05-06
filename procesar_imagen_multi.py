import os
from multiprocessing import Pool, cpu_count

from PIL import Image
from rembg import remove

def remove_background_and_add_gray(task):
    input_image_path, output_image_path, gray_color = task
    try:
        print(f"Procesando: {input_image_path}")
        
        img_original = Image.open(input_image_path)
        img_no_bg = remove(img_original)
        
        # Crear una nueva imagen con fondo gris del mismo tamaño que la imagen sin fondo
        img_with_gray_bg = Image.new('RGB', img_no_bg.size, gray_color)
        
        # Si la imagen sin fondo tiene canal alfa (transparencia), usarlo como máscara para pegarla sobre el fondo gris
        if img_no_bg.mode == 'RGBA':
            img_with_gray_bg.paste(img_no_bg, (0, 0), img_no_bg)
        else:
            # Si no tiene canal alfa, pegar la imagen directamente
            img_with_gray_bg.paste(img_no_bg, (0, 0))
        
        img_with_gray_bg.save(output_image_path)
        print(f"✔ Guardado: {output_image_path}")
    except Exception as e:
        print(f"❌ Error en {input_image_path}: {str(e)}")

def batch_process_images(input_folder, output_folder, gray_color=(120, 120, 120)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Preparar lista de tareas
    tasks = []
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_procesada.jpg")
            tasks.append((input_path, output_path, gray_color))
    
    print(f"Se encontraron {len(tasks)} imágenes para procesar.")
    
    # Usar todos los núcleos disponibles
    num_workers = max(cpu_count() - 1, 1)
    print(f"Usando {num_workers} procesos en paralelo...")
    
    with Pool(processes=num_workers) as pool:
        pool.map(remove_background_and_add_gray, tasks)
    
    print("✅ Procesamiento por lote finalizado.")

if __name__ == "__main__":
    input_folder = './input_images'
    output_folder = './output_images'
    gris_oscuro = (120, 120, 120)

    batch_process_images(input_folder, output_folder, gray_color=gris_oscuro)
