from telebot.types import Message
from utils.misc.video_verification import is_video_available
from loader import bot
from exceptions.video_exceptions import NotSquare, Not360, WrongDuration
import stickers
import random
from config_data import config


@bot.message_handler(content_types=['video'])
def make_circle(message: Message):
    try:
        if is_video_available(message.video):
            file_info = bot.get_file(message.video.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            bot.send_video_note(message.chat.id, downloaded_file)
            bot.send_message(config.ADMIN_ID, "@{user} сделал circle".format(user=message.from_user.username))

    except NotSquare:
        sticker = random.choice(stickers.ERROR_STICKERS)
        bot.send_sticker(message.chat.id, sticker)
        bot.send_message(message.chat.id, "Кажется, это не квадрат!\n"
                                          "Еще раз посмотрите как подготовить видео, нажав /help")
    except Not360:
        sticker = random.choice(stickers.ERROR_STICKERS)
        bot.send_sticker(message.chat.id, sticker)
        bot.send_message(message.chat.id, "Видео не в 360p!\nЕще раз изучите как подготовить видео, нажав /help")

    except WrongDuration:
        sticker = random.choice(stickers.ERROR_STICKERS)
        bot.send_sticker(message.chat.id, sticker)
        bot.send_message(message.chat.id, "Похоже видео больше, чем 60 секунд!\n"
                                          "Еще раз изучите как подготовить видео, нажав /help")

    except Exception as e:
        bot.send_message(config.ADMIN_ID, "неизвестная ошибка {e}".format(e=type(e).__name__))

