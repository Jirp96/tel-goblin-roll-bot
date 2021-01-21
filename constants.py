TELEGRAM_BOT_API_TOKEN='***REMOVED***'
HEROKU_APP_NAME='tel-goblin-roll-bot'

#AVAILABLE_DICE = ["d2","d4","d6","d8","d10","d12","d20","d100"]
AVAILABLE_DICE = [2,4,6,8,10,12,20,100]

RADWOLF_FRASES = [
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
        "El destino es algo extraño, nunca se sabe como van a resultar las cosas; pero si se mantiene la mente y corazon abiertos, encontraras tu propio destino algun dia.",
        "Es importante adquirir el conocimiento de diferentes opiniones, y puntos de vista. Si lo haces desde uno solo te vuelves rígido, y tedioso. Si entiendes el resto, serás mas completo.",
        "Es importante creer en uno mismo, pero una pequeña ayuda de los demás es una gran bendición.",
        "Si buscas la luz, a menudo podrás encontrarla. Pero si buscas la oscuridad, es todo lo que verás siempre. ",
        "Puede que la vida no tenga un plan para nosotros, y las cosas sean juegos del caos y el azar. Tal vez entonces esta en cada uno encontrar significado donde tal vez no haya, y darle propósito. A ojos del universo es insignificante, pero a ojos de tu vida, puede ser toda tu vida.",
        "Nunca debes rendirte a la desesperación. Si te permites ir por ese camino, te rendirás a tus instintos mas bajos. En tiempos oscuros, la esperanza es algo que te das a vos mismo. Ese es tal vez el significado de verdadera fuerza interior.",
        "No hay nada de malo en dejar que quienes te quieren te ayuden.",
        "Muchas cosas que parecen amenazantes en la oscuridad, se vuelven agradables cuando las iluminamos.",
        "Tu vida es donde quiera que estés, te gusto o no.",
        "El orgullo no es lo opuesto de la vergüenza, sino su fuente; la humildad es el único antídoto a la vergüenza.",
        "Sigue tu pasión, y la vida te apremiará. Y si no lo hace, lo esta haciendo, porque estas siguiendo tu pasión. ",
        "A veces la mejor forma de resolver tus problemas, es ayudando a alguien mas.",
        "No hay nada de malo en una vida de paz y prosperidad. Te sugiero que pienses que es lo que realmente querés en la vida, y por que.",
        "A veces es mejor reconocer los errores en su momento y también tratar de enmendarlos, pero si los esta persiguiendo un Terrasque, corran. ",
        "Tu destino depende de vos.",
        "Hoy el destino es nuestro amigo.",
    ]

TY_RADWOLF_SPONSOR_FRASES = [
     "Este bot está auspiciado por Garbarino", 
     "Es solo un lobo con camisa! Nada más", 
     "Licenciado* Radwolf", 
     "Por favor, ya no más",        
]

VALID_ROLL_FORMAT_EXAMPLE = "/roll 2d20 + 3d6 + 5 - 1d4"

HELP_TEXT = '''Stoi chikito, así que no me pidan mucho
- /help 
    Te tiro este texto
- /roll 2d20 + 3d6 + 5 - 1d4
     Tira dados
- /rad o /radwolf
    Invoca la sabiduría milenaria de un lobo con camisa
- /tyrad o /tyradwolf
     Para agradecer la incontable sabiduría
'''