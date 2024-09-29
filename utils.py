import os
import subprocess

def upscale_image(image_path, model_path):
    """Увеличение изображения с помощью waifu2x-caffe."""
    output_image_path = os.path.splitext(image_path)[0] + "_upscaled.jpg"
    
    command = [
    r'C:\TestBotWaifu\waifu2x-caffe\waifu2x-caffe.exe',
    '-i', image_path,
    '-o', output_image_path,
    '--model_dir', model_path,  # Убедитесь, что это корректный путь
    '--scale_ratio', '2'
]

    
    try:
        subprocess.run(command, check=True)
        if not os.path.exists(output_image_path):
            raise FileNotFoundError(f"Увеличенное изображение не найдено: {output_image_path}")
        print(f"Увеличенное изображение сохранено по пути: {output_image_path}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ошибка при выполнении waifu2x: {e}")

    return output_image_path
