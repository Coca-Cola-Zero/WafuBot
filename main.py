import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from config import BOT_TOKEN, MODEL_PATH, OUTPUT_PATH
import utils

def start(update, context):
    """Приветственное сообщение пользователю."""
    update.message.reply_text("Привет! Пришли мне изображение, и я его увеличу с помощью Waifu2x.")

def handle_image(update, context):
    """Обработка изображений, присланных пользователем."""
    chat_id = update.effective_chat.id
    
    # Скачиваем изображение
    photo = update.message.photo[-1]  # Получаем изображение в лучшем разрешении
    file_id = photo.file_id
    file = context.bot.get_file(file_id)
    file_path = f"temp_{file_id}.jpg"  # Формирование временного пути

    # Загружаем файл
    file.download(file_path)
    print(f"Загружен файл: {file_path}")

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл {file_path} не найден.")
        context.bot.send_message(chat_id=chat_id, text="Ошибка: Файл не найден.")
        return  # Выход из функции, если файл не найден

    try:
        # Увеличиваем изображение
        upscaled_img_path = utils.upscale_image(file_path, MODEL_PATH)
        
        # Проверка, существует ли увеличенное изображение
        if not os.path.exists(upscaled_img_path):
            raise FileNotFoundError(f"Увеличенное изображение не найдено: {upscaled_img_path}")

        # Отправляем результат
        with open(upscaled_img_path, 'rb') as f:
            context.bot.send_photo(chat_id=chat_id, photo=f)

        # Удаляем временные файлы
        os.remove(file_path)
        os.remove(upscaled_img_path)

    except Exception as e:
        context.bot.send_message(chat_id=chat_id, text=f"Ошибка при обработке изображения: {e}")

def main():
    """Запуск бота."""
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_image))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
