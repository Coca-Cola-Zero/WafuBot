import os

# Telegram API Token
BOT_TOKEN = "5891252491:AAE4-TXtKZmMZqfTGlqC2AQGa4Ht5lgdhIw"

# Путь к модели waifu2x-caffe
MODEL_PATH = "C:\TestBotWaifu\waifu2x-caffe\models\anime_style_art\noise3_model.json.caffemodel"


# Путь для сохранения улучшенных изображений
OUTPUT_PATH = "C:/TestBotWaifu/dsad"

# Создать папку, если она не существует
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)
