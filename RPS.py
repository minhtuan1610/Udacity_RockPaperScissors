import random


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        choice = None
        while choice not in moves:
            choice = input(
                "What is your choice? rock, paper, scissors\n"
            ).lower()
        return choice


class ConsistentPlayer(Player):
    def move(self):
        return "rock"


# Random move each round
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Remember the last move of opponent, play the same move in this round
class ReflectPlayer(Player):
    def __init__(self):
        self.opponent_move = None

    def move(self):
        if self.opponent_move is None:
            return random.choice(moves)
        return self.opponent_move

    def learn(self, their_move):
        self.opponent_move = their_move


# Remember the last move of opponent, play the next move in this round
class CyclePlayer(Player):
    def __init__(self):
        self.update_move = None

    def move(self):
        if self.update_move is None:
            return random.choice(moves)
        return self.update_move

    def learn(self, last_move):
        """
        Returns the cycle move of players
        Args: last_move: string
        Returns: self.update_move: string
        """
        if last_move == "rock":
            self.update_move = "paper"
        elif last_move == "paper":
            self.update_move = "scissors"
        else:
            self.update_move = "rock"

        return self.update_move


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self, point1, point2):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            pass
        elif beats(move1, move2):
            point1 += 1
        else:
            point2 += 1

        if self.p2 is ReflectPlayer():
            self.p2.learn(move1)
        elif self.p2 is CyclePlayer():
            self.p2.learn(move2)

        return point1, point2

    def play_game(self, point1, point2):
        print("Game start!")

        for round in range(3):
            print(f"Round {round}:")

            point1, point2 = self.play_round(point1, point2)

            print(f"Player 1: {point1} points  Player 2: {point2} points")

        if point1 > point2:
            print(f"Player 1 won {point1} - {point2} ")
        elif point1 < point2:
            print(f"Player 2 won {point2} - {point1} ")
        else:
            print(f"Both players tie at {point1} - {point2} ")

        print("Game over!")


if __name__ == "__main__":
    game = Game(
        HumanPlayer(),
        random.choice(
            [
                ConsistentPlayer(),
                RandomPlayer(),
                ReflectPlayer(),
                CyclePlayer(),
            ]
        ),
    )

    point1 = 0
    point2 = 0

    moves = ["rock", "paper", "scissors"]

    game.play_game(point1, point2)
