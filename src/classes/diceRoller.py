import constants


class DiceRoller():
    def __init__(self, random_module) -> None:
        self.AVAILABLE_DICE = constants.AVAILABLE_DICE
        self.random = random_module
        self.GOBLIN_BLESSES = 0

    def add_goblin_bless(self):
        self.GOBLIN_BLESSES += 1

    def reset_goblin_bless(self):
        self.GOBLIN_BLESSES = 0

    def get_goblin_bless(self):
        return self.GOBLIN_BLESSES

    def roll_dice(self, max: int) -> int:
        return self.random.randrange(max) + 1

    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def get_roll_number(self, mult):
        num = 1
        if mult:
            num = int(mult)

        return num

    def process_token(self, token):
        if self.is_integer(token):
            return int(token)

        dice = token.split("d")
        if len(dice) != 2 or not ((self.is_integer(dice[0]) or not dice[0]) and self.is_integer(dice[1])):
            raise ValueError("Dato inválido, ejemplo de formato: {0}".format(
                constants.VALID_ROLL_FORMAT_EXAMPLE))

        diceType = int(dice[1])
        if diceType not in self.AVAILABLE_DICE:
            raise ValueError("Dado inválido, opciones:{0}".format(
                " d".join(self.AVAILABLE_DICE)))

        numRolls = self.get_roll_number(dice[0])
        
        if numRolls > constants.MAXIMUM_DICE_ROLLS:
            raise ValueError("No puedo tirar tantos dados, máximo {0}".format(constants.MAXIMUM_DICE_ROLLS))

        return sum([self.roll_dice(diceType) for _ in range(numRolls)])

    def process_roll(self, withBless, terms):
        result = 0
        text_roll = ""

        try:
            for term in terms:
                tokenList = term.split("-")

                result += self.process_token(tokenList[0])
                for minusToken in tokenList[1:]:
                    result -= self.process_token(minusToken)

            if withBless:
                result = self.apply_goblin_bless(result)
                self.reset_goblin_bless()

            text_roll = '=> {0}'.format(result)
        except ValueError as err:
            text_roll = str(err)

        return text_roll

    def apply_goblin_bless(self, old_result):
        goblin_result = 'Blessed for {0}'
        toAdd = self.process_token("{0}d4".format(self.GOBLIN_BLESSES))

        randNum = self.random.randint(-5, 2)
        if randNum < 0:
            toAdd = -1 * toAdd
        return "{0} ({1})".format(old_result + toAdd, goblin_result.format(toAdd))

    def process_fours(self, qty):
        results = []

        if not self.is_integer(qty):
            return "Dato inválido, ejemplo de formato: {0}".format(constants.VALID_ROLL_FOURS_FORMAT_EXAMPLE)
        elif int(qty) > constants.MAXIMUM_DICE_ROLLS:
            return "Ta muy grande, solo se contar hasta {0}".format(constants.MAXIMUM_DICE_ROLLS)

        for i in range(int(qty)):
            results.append(self.roll_dice(6))

        return "{0} -> {1} victorias".format('; '.join([str(e) for e in results]), sum(1 for n in results if n >= 4))
