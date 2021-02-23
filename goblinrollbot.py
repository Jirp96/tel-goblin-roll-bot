import os

import logging
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import constants

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
LOGGER = logging.getLogger(__name__)

GOBLIN_BLESSES = 0

def rollDice(max):
    return random.randrange(max) + 1

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def getRollNum(mult):
    num = 1
    if mult:
        num = int(mult)

    return num

def processToken(token):
    if RepresentsInt(token):
        return int(token)
    
    dice = token.split("d")
    if len(dice) != 2 or not ((RepresentsInt(dice[0]) or not dice[0]) and RepresentsInt(dice[1])) :
        raise ValueError("Dato inválido, ejemplo de formato: {0}".format(constants.VALID_ROLL_FORMAT_EXAMPLE))
    
    result = 0        
    diceType = int(dice[1])
    if diceType not in constants.AVAILABLE_DICE:
        raise ValueError("Dado inválido, opciones:{0}".format(" d".join(constants.AVAILABLE_DICE)))

    numRolls = getRollNum(dice[0])
    for i in range(numRolls):
        result += rollDice(diceType)

    return result

def processRoll(terms):
    result = 0
    text_roll = ""

    try:
        for term in terms:
            tokenList = term.split("-")

            result += processToken(tokenList[0])
            for minusToken in tokenList[1:]:
                result -= processToken(minusToken)
            
        text_roll = '=> {0}'.format(result)        
    except ValueError as err:
        text_roll = err
    
    return text_roll

def roll(update, context):
    terms = ''.join(context.args).replace(" ","").split("+")
    
    text_roll = processRoll(terms)

    global GOBLIN_BLESSES
    try:

        if GOBLIN_BLESSES > 0:
            text_roll = applyGoblinBlesses(text_roll)        
            GOBLIN_BLESSES = 0
    except Exception as err:
        text_roll = err
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_roll)

def applyGoblinBlesses(normal_result):
    global GOBLIN_BLESSES
    goblin_result = 'Blessed for {0}'
    toAdd = processToken("{0}d4".format(GOBLIN_BLESSES))

    randNum = random.randint(-5, 2)
    if randNum < 0:
        toAdd = -1 * toAdd        
    return "{0} ({1})".format(int(normal_result)+ toAdd, goblin_result.format(toAdd))

def goblinBless(update, context):
    global GOBLIN_BLESSES
    GOBLIN_BLESSES += 1
    goblin_bless_text = random.choice(constants.GOBLIN_BLESS_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=goblin_bless_text)

def radwolf(update, context):
    rad_text = random.choice(constants.RADWOLF_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rad_text)

def tyradwolf(update, context):
    rad_text = random.choice(constants.TY_RADWOLF_SPONSOR_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rad_text)

def error(bot, update, error):
    LOGGER.warning('Update "%s" caused error "%s"', update, error)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot goblin, hablenme!")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stoi chikito, no entendí ese comando.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constants.HELP_TEXT)

def main():    

    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(token=constants.TELEGRAM_BOT_API_TOKEN, use_context=True)    
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    roll_handler = CommandHandler('roll', roll)
    bless_handler = CommandHandler('bless', goblinBless)
    rad_handler = CommandHandler('rad', radwolf)
    radwolf_handler = CommandHandler('radwolf', radwolf)
    tyrad_handler = CommandHandler('tyrad', tyradwolf)
    tyradwolf_handler = CommandHandler('tyradwolf', tyradwolf)
    help_handler = CommandHandler('help', help)

    unknown_handler = MessageHandler(Filters.command, unknown)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(roll_handler)
    dispatcher.add_handler(bless_handler)
    dispatcher.add_handler(rad_handler)
    dispatcher.add_handler(radwolf_handler)
    dispatcher.add_handler(tyrad_handler)
    dispatcher.add_handler(tyradwolf_handler)
    dispatcher.add_handler(help_handler)

    dispatcher.add_handler(unknown_handler)
    dispatcher.add_error_handler(error)
    
    updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=constants.TELEGRAM_BOT_API_TOKEN)
    updater.bot.set_webhook("https://{0}.herokuapp.com/{1}".format(constants.HEROKU_APP_NAME, constants.TELEGRAM_BOT_API_TOKEN))
    updater.idle()


if __name__ == "__main__":
    main()