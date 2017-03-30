'''main file'''
from steeringbehavioursgame import SteeringBehavioursGame
from agent import Agent
from vector import Vector2
from random import random

def main():
    '''main execution func'''
    game = SteeringBehavioursGame("SteeringBehaviours")

    pos = (400, 400)
    for _ in range(10):
        agent = Agent("agent", (0, 0), Vector2(random() * 400 + 50, random() * 400))
        game.addtobatch(agent)
    game.run()


if __name__ == "__main__":
    main()
