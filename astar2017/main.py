'''main file'''
from Games.steeringbehavioursgame import SteeringBehavioursGame
from Games.liamsgame import LiamsGame
from Engine.gameobject import GameObject
from Utilities.vector import Vector2

def main():
    '''main execution func'''
    game = SteeringBehavioursGame("SteeringBehaviours")

    for i in range(25):
        pos = (400 + (i * i), 400 + (i * i))
        game.addtobatch(GameObject("agent", pos, 25, 25))
    game.run()


if __name__ == "__main__":
    main()
