'''main file'''
from steeringbehavioursgame import SteeringBehavioursGame
from liamsgame import LiamsGame
from gameobject import GameObject
from gameobject import Agent
from vector import Vector2

def main():
    '''main execution func'''
    game = SteeringBehavioursGame("SteeringBehaviours")

    for i in range(25):
        pos = (400 + (i * i), 400 + (i * i))
        game.addtobatch(Agent("agent", pos))
    game.run()


if __name__ == "__main__":
    main()
