
import logging
import random
from classes.diceRoller import DiceRoller
from classes.radwolf import RadAdvice
from classes.rant import Rant
import constants

GOBLIN_ROLLER = DiceRoller(random)
GOBLIN_DB = constants.GOBLIN_DB

LOGGER = logging.getLogger(__name__)

async def roll(update, context):
    global GOBLIN_ROLLER
    terms = ''.join(context.args).replace(" ", "").split("+")

    withBless = True if GOBLIN_ROLLER.get_goblin_bless() > 0 else False

    text_roll = GOBLIN_ROLLER.process_roll(withBless, terms)
    await update.message.reply_text(text_roll)

async def roll_fours(update, context):
    global GOBLIN_ROLLER
    qty = ''.join(context.args).replace(" ", "")

    text_roll = GOBLIN_ROLLER.process_fours(qty)
    await update.message.reply_text(text_roll)

async def goblin_bless(update, context):
    global GOBLIN_ROLLER
    GOBLIN_ROLLER.add_goblin_bless()
    goblin_bless_text = random.choice(constants.GOBLIN_BLESS_FRASES)
    
    await update.message.reply_text(goblin_bless_text)

async def radwolf(update, context):
    global GOBLIN_DB
    rad = RadAdvice(GOBLIN_DB)
    rad_text = rad.advise()
    await update.message.reply_text(rad_text)

async def ty_radwolf(update, context):
    rad_text = random.choice(constants.TY_RADWOLF_SPONSOR_FRASES)
    await update.message.reply_text(rad_text)

async def orc_gang(update, context):
    orc_num = random.randrange(100) + 1
    orc_text = ""

    if orc_num == 69:
        orc_text = constants.DADDY_ORC_GANG_TEXT
    else:
        orc_text = constants.ORC_GANG_TEXT.format(orc_num)

    await update.message.reply_text(orc_text)

async def rant(update, context):
    global GOBLIN_DB
    ranter = Rant(GOBLIN_DB)
    rant_text = ranter.rant()
    await update.message.reply_text(rant_text)

async def start(update, context):
    await update.message.reply_text("Soy un bot goblin, hablenme!")

async def help(update, context):
    await update.message.reply_text(constants.HELP_TEXT)

async def error_callback(update, context):
    global LOGGER
    LOGGER.error(msg="Exception while handling an update:", exc_info=context.error)

COMMANDS = {
    'roll': roll,
    'bless': goblin_bless,
    'rad': radwolf,
    'radwolf': radwolf,
    'orcgang': orc_gang,
    'tyrad': ty_radwolf,
    'tyradwolf': ty_radwolf,
    'help': help,
    'fours': roll_fours,
    'rant': rant
}