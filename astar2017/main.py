'''main file'''
from random import randrange
from steeringbehavioursgame import SteeringBehavioursGame
from agent import Agent
from vector import Vector2



def main():
    '''main execution func'''
    game = SteeringBehavioursGame("SteeringBehaviours")

    for _ in range(10):
        pos = Vector2(randrange(0, 800), randrange(0, 800))
        vel = Vector2(1, 0)
        agent = Agent("agent", pos, vel)
        game.addtobatch(agent)
    game.run()


if __name__ == "__main__":
    main()
