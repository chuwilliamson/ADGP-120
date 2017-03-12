from game import Game
from game import LiamsGame
from gameobject import GameObject
def main():
    game = LiamsGame("Liams game")
    player = GameObject("liam", (400, 300), 30, 30)
    game.addtobatch(player)
    game.run()

if __name__ == "__main__":
    main()