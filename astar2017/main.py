'''main file'''
from steeringbehavioursgame import SteeringBehavioursGame
from gameobject import GameObject
from vector import *

def main():
    '''main execution func'''
    game = SteeringBehavioursGame("SteeringBehaviours")
    agent1 = GameObject("agent", (400, 300), 30, 30)
    agent2 = GameObject("agent", (200, 150), 30, 30)
    agent3 = GameObject("agent", (250, 450), 30, 30)
    agent1.add_force(Vector2(1, 0))
    agent2.add_force(Vector2(0, 1))
    agent3.add_force(Vector2(1, 1))
    game.addtobatch(agent1)
    game.addtobatch(agent2)
    game.addtobatch(agent3)
    for i in range(25):
        pos = (400 + (i * i), 400 + (i * i))
        game.addtobatch(GameObject("agent", pos, 25, 25))
    game.run()

if __name__ == "__main__":
    main()
