from telebot.types import Audio
import config
import telebot
import os
import speech
import time

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["text"])
def send_message(message):

    chatId = message.chat.id
    bot.send_message(chatId, "Жди, я готовлю аудио файл...")

    speech.text_to_voice("""%s""" % message.text, str(message.id))

    for f in os.listdir():
        name, ext = os.path.splitext(f)
        if ext == ".wav":
            print(f)
            audio_file = open(f, 'rb')
            bot.send_audio(chatId, audio_file)
            audio_file.close()
            time.sleep(1)
            os.remove(f)

    # print(message.text)
    


bot.infinity_polling()