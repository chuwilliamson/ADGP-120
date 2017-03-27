'''main file'''
from steeringbehavioursgame import SteeringBehavioursGame
from agent import Agent
from vector import Vector2


def main():
    '''main execution func'''
    game = SteeringBehavioursGame("SteeringBehaviours")

    pos = (400, 400)
    agent = Agent("agent", pos, Vector2(5, 0))
    game.addtobatch(agent)
    game.run()


if __name__ == "__main__":
    main()
