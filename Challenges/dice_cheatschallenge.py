import random

class DicePlayer:
    def __init__(self, name):
        self.name = name
        self.dice = []

    def roll_dice(self, num_dice=2):
        self.dice = [random.randint(1, 6) for _ in range(num_dice)]
        return sum(self.dice)

    def display_dice(self):
        return f"{self.name}'s dice: {', '.join(map(str, self.dice))}"

class Cheater(DicePlayer):
    def cheat(self):
        pass  # Base class, no specific cheating behavior

class MulliganCheater(Cheater):
    def cheat(self, total):
        if total < 9:
            print(f"{self.name} takes a mulligan and re-rolls the dice!")
            return self.roll_dice()
        else:
            return total

class ExtraDieCheater(Cheater):
    def cheat(self, total):
        print(f"{self.name} rolls one additional die!")
        extra_die = random.randint(1, 6)
        return total + extra_die

class WeightedDieCheater(Cheater):
    def cheat(self):
        print(f"{self.name} uses a weighted die!")
        weighted_die = max(3, random.randint(1, 6))
        return weighted_die

class SabotageCheater(Cheater):
    def cheat(self, opponent):
        print(f"{self.name} sabotages {opponent.name}'s dice!")
        opponent.dice = [min(3, die) for die in opponent.dice]
        return sum(opponent.dice)

def play_game(player1, player2):
    total1 = player1.roll_dice()
    total2 = player2.roll_dice()

    print(player1.display_dice())
    print(player2.display_dice())

    if total1 > total2:
        print(f"{player1.name} wins!")
    elif total1 < total2:
        print(f"{player2.name} wins!")
    else:
        print("It's a tie!")

#Example:
player1 = DicePlayer("Alice")
player2 = MulliganCheater("Bob")

play_game(player1, player2)