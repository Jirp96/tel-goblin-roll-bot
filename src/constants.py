import os

GOBLIN_DB = os.environ["GOBLIN_DB"]
GEMINI_APIKEY = os.environ["GEMINI_APIKEY"]

TY_RADWOLF_SPONSOR_FRASES = [
    "Este bot está auspiciado por Garbarino",
    "Es solo un lobo con camisa! Nada más",
    "Licenciado* Radwolf",
    "Por favor, ya no más",
]

GOBLIN_BLESS_FRASES = [
    "El mundo ha sido bendecido por un Goblin.",
    "Un Goblin es una bendición.",
    "Pensaste en lo que estás haciendo?",
    "Sad goblin noises."
]

ROCK_AND_STONE = [
    "Rock and Stone!",
    "To the bone!",
    "For Karl!",
    "Leave no dwarf behind!",
    "Rock and Stone, brother!",
    "For Rock and Stone!",
    "Rock and Stone in the heart!",
    "Did I hear a Rock and Stone?",
    "Rock and Stone, everyone!",
    "Rock and Stone, yeah!",        
]

ORC_GANG_TEXT = "Orco número {} será recordado"
DADDY_ORC_GANG_TEXT = "Daddy(rip orco #69) será recordado. Murió por su avanzada edad..."

D2 = 2
D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20
D100 = 100

AVAILABLE_DICE = [D2, D4, D6, D8, D10, D12, D20, D100]

MAXIMUM_DICE_ROLLS = 100

# Useful Text Messages
VALID_ROLL_FORMAT_EXAMPLE = "/roll 2d20 + 3d6 + 5 - 1d4"

VALID_ROLL_FOURS_FORMAT_EXAMPLE = "/fours 7"

HELP_TEXT = '''Stoi chikito, así que no me pidan mucho
- /help 
    Te tiro este texto
- /roll 2d20 + 3d6 + 5 - 1d4
     Tira dados
- /bless
    Te "bendice" un goblin
- /fours 7
    Tira 7 d6 y te dice cuantos son por lo menos 4
- /rad o /radwolf
    Invoca la sabiduría milenaria de un lobo con camisa
- /tyrad o /tyradwolf
     Para agradecer la incontable sabiduría
- /orcgang
    Para rememorar a los orcos que se sacrificaron por nosotros
- /rant
    No nos hacemos responsables de que te triggerees
'''

RAD_IA_CONTEXT = "Eres un lobo terapeuta llamado Radwolf. Siempre das consejos que buscan mejorar la vida de quienes te leen. En realidad eres un lobo con camisa, y tus consejos son similares a los que daría Iroh de Avatar The Last Airbender. No saludes y ve directo al punto."