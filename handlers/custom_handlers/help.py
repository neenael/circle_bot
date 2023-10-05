from loader import bot
from telebot.types import Message
from stickers import HELLO_STICKERS
import random


@bot.message_handler(commands=["help", "start"])
def rules(message: Message):
    if message.text == "/start":
        sticker = random.choice(HELLO_STICKERS)
        bot.send_sticker(message.chat.id, sticker)
    instructions = "<b>Как подготовить видео</b>\n\n" \
                   "Всего правил три:\n1. Видео должно быть <b>квадратным</b>\n2. Разрешение <b>360p</b>.\n" \
                   "3. Не дольше 60 секунд\n" \
                   "Все эти параметры можно настроить в меню прямо перед отправкой видео.\n\n" \
                   "<b>Что потом делать с кружком?</b>\n\n" \
                   "Вы можете переслать кружок без пометки о пересылке. Для этого выделите кружок ->" \
                   " Переслать -> выберите из списка получателя -> " \
                   "в открывшемся диалоге снизу будет панель 'Переслать сообщение', нажимаем на эту " \
                   "панель -> выбираем 'Скрыть имя отправителя' ->" \
                   " Отправить сообщение"
    bot.send_message(message.chat.id, instructions, parse_mode="HTML")
