import random

moves = ["rock", "paper", "scissors"]


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


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
            return point1
        else:
            point2 += 1
            return point2

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        return point1, point2

    def play_game(self, point1, point2):
        print("Game start!")

        for round in range(3):
            print(f"Round {round}:")

            point1, point2 = self.play_round(point1, point2)

            print(f"Player 1: {point1} points  Player 2: {point2} points")

        print("Game over!")


if __name__ == "__main__":
    game = Game(RandomPlayer(), RandomPlayer())
    point1 = 0
    point2 = 0
    game.play_game(point1, point2)
    # test = RandomPlayer().move()
    # print(test)
