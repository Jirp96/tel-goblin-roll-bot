import os

import logging
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

TELEGRAM_BOT_API_TOKEN='***REMOVED***'
HEROKU_APP_NAME='tel-goblin-roll-bot'

AVAILABLE_DICE = ["d2","d4","d6","d8","d10","d12","d20","d100"]

RADWOLF_FRASES = [
        "Este bot está auspiciado por Garbarino", 
        "Es solo un lobo con camisa! Nada más", 
        "Licenciado* Radwolf", 
        "Por favor, ya no más",
        "El consentimiento es fundamental para las relaciones interpersonales de todo tipo",
        "Sad al revés es Das, and das not good",
        "Los problemas pasan a ser enemigos que afrontar. Hacelos mierda",
        "Cuando entren a un lugar desconocido, es prudente avanzar muy lentamente porque el piso puede hundirse, no como pantano, sino como carne.",
        "Para fortalecer la voluntad hay que hacer al menos dos cosas que nos desagraden.",
        "Por favor, no toquen animales sin su consentimiento",
        "Por el amor de dios, es solo un lobo.",
        "Todos los caminos están cerrados si uno no tiene una idea clara de a dónde quiere llegar.",
        "Cuando un conejo sufre de polución nocturna, una gran calma se extiende sobre el bosque.",
        "A nadie le basta con que le expliquen los procesos; no hay más remedio que vivirlos, y al vivirlos es como se aprenden, pero también es como se cometen los errores y como uno pierde el rumbo.",
        "Para salir y vivir aventuras, es preciso dejarse crecer un bigote sedoso y espeso.",
        "Ante la fé menguante, para cualquier clérigo, es fundamental recuperar el contacto con el ser íntimo, con el ser que participa de algún modo secreto de la chispa divina que recorre infatigablemente el Universo y lo anima, lo sostiene, le presta realidad bajo su aspecto de cáscara vacía, castea Heal la puta que te pario.",
        "La comprensión es, a veces, un objeto tan real y vivo, como el daño que recibimos.",
        "Quien mira hacia afuera, duerme; quien mira hacia adentro, despierta.",
        "Ya desde los cuatro años los niños humanos pueden lograr una comprensión parcial de lo que sucede después de la muerte.",
        "Queremos ser felices de manera fácil, barata, rápida, indolora y sin mucho esfuerzo, pero cualquier atajo que pretenda evitar la realidad de la vida se convierte en una opción poco sana y algo inmadura.",
        "Paradójicamente, la transformación sólo se puede dar a partir de la aceptación: solamente podemos actuar sobre algo si previamente lo aceptamos, si nos hacemos cargo.",
        "La cosa más aterradora es aceptarse a sí mismo por completo. Tomar conciencia y aceptar nuestra luz y nuestra sombra nos librará del agotador esfuerzo que supone tratar de ser distintos a como realmente somos. +1 Will save.",
        "El conocimiento de tu propia oscuridad es el mejor método para hacer frente a las tinieblas de otras personas. +1 radiant dmg / d6 turnos.",
        "Allá donde miramos nos vemos a nosotros mismos, puesto que proyectamos lo propio en todo aquello que observamos.",
    ]

HELP_TEXT = '''Stoi chikito, así que no me pidan mucho
- /help 
    Te tiro este texto
- /roll d2 [+- num]
     Te tira una moneda y le suma/resta num
- /roll d4
     Te tira un d4 y le suma/resta num
- /roll d6
     Te tira un d6 y le suma/resta num
- /roll d8
     Te tira un d8 y le suma/resta num
- /roll d10
     Te tira un d10 y le suma/resta num
- /roll d12
     Te tira un d12 y le suma/resta num
- /roll d20
     Te tira un d20 y le suma/resta num
- /roll d100
     Te tira un d100 y le suma/resta num
- /rad o /radwolf
    Invoca la sabiduría milenaria de un lobo con camisa
'''

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def rollDice(max):
    return random.randrange(max) + 1

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def roll(update, context):
    dNum = context.args[0]  
    text_roll = "Dado inválido, opciones: {0}".format(AVAILABLE_DICE)

    if dNum in AVAILABLE_DICE:
        num = int(dNum[1:])
        result = rollDice(num)

        if len(context.args) > 1:
            addedNum = context.args[1]
            if RepresentsInt(addedNum):
                result += int(addedNum)

        text_roll = '=> {0}'.format(result)
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_roll)

def radwolf(update, context):
    rad_text = random.choice(RADWOLF_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rad_text)


def error(bot, update, error):
    LOGGER.warning('Update "%s" caused error "%s"', update, error)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot goblin, hablenme!")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stoi chikito, no entendí ese comando.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_TEXT)

def main():    

    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(token=TELEGRAM_BOT_API_TOKEN, use_context=True)    
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    roll_handler = CommandHandler('roll', roll)
    rad_handler = CommandHandler('rad', radwolf)
    radwolf_handler = CommandHandler('radwolf', radwolf)
    help_handler = CommandHandler('help', help)

    unknown_handler = MessageHandler(Filters.command, unknown)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(roll_handler)
    dispatcher.add_handler(rad_handler)
    dispatcher.add_handler(radwolf_handler)
    dispatcher.add_handler(help_handler)

    dispatcher.add_handler(unknown_handler)
    dispatcher.add_error_handler(error)
    
    updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=TELEGRAM_BOT_API_TOKEN)
    updater.bot.set_webhook("https://{0}.herokuapp.com/{1}".format(HEROKU_APP_NAME, TELEGRAM_BOT_API_TOKEN))
    updater.idle()


if __name__ == "__main__":
    main()