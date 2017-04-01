'''main file'''
from random import randrange
from steeringbehavioursgame import SteeringBehavioursGame
from prey import Prey
from predator import Predator
from vector import Vector2



def main():
    '''main execution func'''
    game = SteeringBehavioursGame("SteeringBehaviours")

    for _ in range(1):
        pos = Vector2(randrange(0, 800), randrange(0, 800))
        vel = Vector2(randrange(0, 800), randrange(0, 800)).normalized
        agent0 = Prey("max", pos, vel)
        pos = Vector2(randrange(0, 800), randrange(0, 800))
        vel = Vector2(randrange(0, 800), randrange(0, 800)).normalized
        agent1 = Prey("donray", pos, vel)
        pos = Vector2(randrange(0, 800), randrange(0, 800))
        vel = Vector2(randrange(0, 800), randrange(0, 800))
        agent2 = Predator("trent", pos, vel, [agent0, agent1])

        agent0.set_target(agent2)
        agent1.set_target(agent2)

        game.addtobatch(agent0)
        game.addtobatch(agent1)
        game.addtobatch(agent2)
    game.run()


if __name__ == "__main__":
    main()
