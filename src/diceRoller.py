import src.constants

class DiceRoller():    
    def __init__(self, random_module) -> None:
        self.AVAILABLE_DICE = [2,4,6,8,10,12,20,100]
        self.random = random_module
        self.GOBLIN_BLESSES = 0
            
    def addGoblinBless(self):
        self.GOBLIN_BLESSES += 1

    def resetGoblinBless(self):
        self.GOBLIN_BLESSES = 0
    
    def getGoblinBless(self):
        return self.GOBLIN_BLESSES
        
    def rollDice(self, max):
        return self.random.randrange(max) + 1

    def RepresentsInt(self, s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    def getRollNum(self, mult):
        num = 1
        if mult:
            num = int(mult)

        return num

    def processToken(self, token):
        if self.RepresentsInt(token):
            return int(token)
        
        dice = token.split("d")
        if len(dice) != 2 or not ((self.RepresentsInt(dice[0]) or not dice[0]) and self.RepresentsInt(dice[1])) :
            raise ValueError("Dato inválido, ejemplo de formato: {0}".format(self.constants.VALID_ROLL_FORMAT_EXAMPLE))
        
        result = 0        
        diceType = int(dice[1])
        if diceType not in self.AVAILABLE_DICE:
            raise ValueError("Dado inválido, opciones:{0}".format(" d".join(self.AVAILABLE_DICE)))

        numRolls = self.getRollNum(dice[0])
        for i in range(numRolls):
            result += self.rollDice(diceType)

        return result

    def processRoll(self, withBless, terms):
        result = 0
        text_roll = ""

        try:
            for term in terms:
                tokenList = term.split("-")

                result += self.processToken(tokenList[0])
                for minusToken in tokenList[1:]:
                    result -= self.processToken(minusToken)

            if withBless:
                result = self.applyGoblinBlesses(result)
                self.resetGoblinBless()

            text_roll = '=> {0}'.format(result)        
        except ValueError as err:
            text_roll = err
        
        return text_roll

    def applyGoblinBlesses(self, old_result):
        goblin_result = 'Blessed for {0}'
        toAdd = self.processToken("{0}d4".format(self.GOBLIN_BLESSES))

        randNum = self.random.randint(-5, 2)
        if randNum < 0:
            toAdd = -1 * toAdd        
        return "{0} ({1})".format(old_result + toAdd, goblin_result.format(toAdd))

    def processFours(self, qty):
        results = []

        if not self.RepresentsInt(qty):
            return "Dato inválido, ejemplo de formato: {0}".format(self.constants.VALID_ROLL_FOURS_FORMAT_EXAMPLE)

        for i in range(int(qty)):
            results.append(self.rollDice(6)) 
        
        return "{0} -> {1} victorias".format('; '.join(results), sum(1 for n in results if n >= 4))
