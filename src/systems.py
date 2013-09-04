import components
from uuid import uuid4 as get_uuid

class System(object):
    def __init__(self, manager):
        self.id = get_uuid()
        self.manager = manager
    def tick(self, dt):
        pass

class Movement(System):
    def tick(self, dt):
        position_store = self.manager.component_stores[components.Position]
        velocity_store = self.manager.component_stores[components.Velocity]

        for uuid in velocity_store:
            if not self.manager.has_component_of_type(uuid, components.Collided):
                position = position_store[uuid][0]
                velocity = velocity_store[uuid][0]
                position.vector = position.vector + dt * velocity.vector
                if position.vector[1] < 0:
                    position.vector[1] = 0
                    self.manager.add_component(uuid, components.Collided())
