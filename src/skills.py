import components
import systems
from datetime import datetime
import math

def logarithmic(time_trained):
    return int(math.log(time_trained.total_seconds()))

class Skill(components.Component):
    def __init__(self, component, levelcurve):
        Skill.__init__(self)
        self.component = component
        self.training_start = None
        self.time_trained = 0
        self.time_trained_previous = 0
        self.levelcurve = levelcurve
    @property
    def level(self):
        return self.levelcurve(seconds_trained)

class Experience(systems.System):
    def tick(self, dt):
        skill_store = self.manager.component_stores[Skill]

        for uuid in skill_store:
            for skill in skill_store[uuid]:
                if skill.training_start is not None:
                    skill.time_trained = skill.time_trained_previous + (datetime.now() - skill.training_start)
                else:
                    skill.time_trained_previous = skill.time_trained
