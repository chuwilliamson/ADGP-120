'''node class'''

class Node(object):
    '''create a node with an identifier and the value it will contain'''
    def __init__(self, identifier, value):
        '''identifier is the name value is the data'''
        self._value = value
        self._identifier = identifier
        self._parent = None

    @property
    def value(self):
        '''get value'''
        return self._value

    @property
    def identifier(self):
        '''id'''
        return self._identifier

    def get_parent(self):
        '''get parent'''
        return self._parent

    def set_parent(self, value):
        '''private set on parent'''
        self._parent = value

    parent = property(get_parent, set_parent)

    def __str__(self):
        '''get info'''
        res = "ID: "
        res += str(self._identifier) + "\nValue: " + str(self._value)
        return res
