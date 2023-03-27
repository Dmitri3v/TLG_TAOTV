from tel_config import *
import telebot

bot = telebot.TeleBot(tel_thonken)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "Hola, soy el bot de TAOTV, actualmente me encuentro en desarrollo, por ello no tengo muchas funciones hasta el momento, sin embargo pronto sere completamente oficiaL, ¡¡HASTA LA VICTORIA SIEMPRE!!")


@bot.message_handler(content_types=["text"])
def bot_msg_txt(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Command not found")
    else:
        bot.send_message(message.chat.id, "Soy el bot de TAO TV!")


if __name__ == '__main__':
    print("Bot is active")
    bot.infinity_polling()
    print("Bot disconnect")
