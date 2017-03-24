'''name mangling'''
class Cat(object):
    '''cat'''
    def __init__(self, name):
        self.name = name
class Dog(object):
    '''dog'''
    def __init__(self, name):
        self._name = name

def main():
    '''main'''
    cat = Cat('simba')
    dog = Dog('lassie')
    print cat
    print cat.name
    print dog
if __name__ == '__main__':
    main()
    