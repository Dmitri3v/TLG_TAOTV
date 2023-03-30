# from tel_config import *
import telebot
import requests

## Start Edited


### End Edited


tel_thonken = "5979217326:AAFgmiCJEXKgr44SwABNvhHpByn-2YFFE3Y"
bot = telebot.TeleBot(tel_thonken)
bot.set_webhook()



## Start Edited



### End Edited



    ### Este apartade es para definir los comandos principales
@bot.message_handler(commands=["start", "iniciar"])
def cmd_start(message):
    bot.reply_to(message, "Hola, soy el bot de TAOTV, actualmente me encuentro en desarrollo, por ello no tengo muchas funciones hasta el momento, sin embargo pronto sere completamente oficial")
    with open("/temp/vmk.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo=photo )

        
    ### Este apartado es para conseguir el ID
    
@bot.message_handler(commands=["chatid"])
def cht_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Tu id es {chat_id}")


    ### En este apartado de define el comando "acerca" para que sea ejecutado
@bot.message_handler(commands=["acerca"])
def cmd_who(message):
    bot.reply_to(message, "Actualmente me esta desarrollando Kepishdo, si lo quieres contactar escribe el comando /contacto y te enviare su correo")

    ### En este apartado se define el comando contact
@bot.message_handler(commands=["contacto"])
def cmd_contact(message):
    bot.reply_to(message, "Este es su correo: aleksander@duck.com , enviale saludos de mi parte!")

    ### En este apartado se define lo que se va a responder en caso de enviar algun comando que no este definido aun, y que se le va a responder en caso de que envie solo texto.
@bot.message_handler(content_types=["text"])
def bot_msg_txt(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Lo siento, pero ese comando no esta disponible, almenos no por el momento..")
    else:
        bot.send_message(message.chat.id, "Soy el bot de TAO TV!")



    ### Este es un bucle para que el bot no pare de correr
if __name__ == '__main__':
    print("El Bot esta actualmente activo")
    bot.infinity_polling()
    print("Bot desconectado")


# Actualmente el bot esta en desarrollo, no esperen que sea la gran maravilla señores.