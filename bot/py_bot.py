from tel_config import *
import telebot

bot = telebot.TeleBot(tel_thonken)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "Hola, soy el bot de TAOTV, actualmente me encuentro en desarrollo, por ello no tengo muchas funciones hasta el momento, sin embargo pronto sere completamente oficial, ¡¡HASTA LA VICTORIA SIEMPRE!!")

@bot.message_handler(commands=["acerca"])
def cmd_who(message):
    bot.reply_to(message, "Actualmente me esta desarrollando Kepishdo, si lo quieres contactar escrie el comando '/contact' y te enviare su correo")

@bot.message_handler(commands=["contact"])
def cmd_contact(message):
    bot.reply_to(message, "Este es su correo ' aleksander@duck.com ', enviale saludes de mi parte!")
    
@bot.message_handler(content_types=["text"])
def bot_msg_txt(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Lo siento, pero ese comando no esta disponible, almenos no por el momento..")
    else:
        bot.send_message(message.chat.id, "Soy el bot de TAO TV!")


if __name__ == '__main__':
    print("Bot is active")
    bot.infinity_polling()
    print("Bot disconnect")
