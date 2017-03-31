from vector import Vector2

def test_movement(deltatime):
    mass = 1
    force = Vector2(0, 0)
    velocity = Vector2(0, 1)
    position = Vector2(400, 400)


    acceleration = force * (1 / mass) # 0,0
    velocity = velocity + acceleration * deltatime
    position = position + velocity * deltatime
    return position

def main():
    if test_movement(.03) == Vector2(400.03, 400):
        print 'pass'
    else:
        print test_movement(.03)
        print 'fail'
    if test_movement(1) == Vector2(401, 400):
        print 'pass'
    else:
        print test_movement(1)
        print 'fail'

main()