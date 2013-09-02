import numpy as np
from uuid import uuid4 as get_uuid

class Component(object):
    def __init__(self):
        self.id = get_uuid()
    def __repr__(self):
        return "Component {%s: %s}" % (self.id, self.__class__.__name__)

class Name(Component):
    def __init__(self, name):
        Component.__init__(self)
        self.name = name

class Money(Component):
    def __init__(self, currency, amount):
        Component.__init__(self)
        self.amount = amount
        self.currency = currency

class XYZComponent(Component):
    def __init__(self, arraylike):
        Component.__init__(self)
        self.vector = np.array(arraylike).astype(np.float64)
    @property
    def x(self):
        return self.vector[0]
    @property
    def y(self):
        return self.vector[1]
    @property
    def z(self):
        return self.vector[2]
    @property
    def x(self, value):
        self.vector[0] = value
    @property
    def y(self, value):
        self.vector[1] = value
    @property
    def z(self, value):
        self.vector[2] = value

class Position(XYZComponent):
    pass

class Velocity(XYZComponent):
    pass

class Attitude(XYZComponent):
    pass

