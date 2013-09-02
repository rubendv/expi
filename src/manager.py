from uuid import uuid4 as get_uuid

class EntityManager(object):
    def __init__(self):
        self.id = self.basic_entity()
        self.ids_to_tags = {}
        self.tags_to_ids = {}
        self.component_stores = {}
    def basic_entity(self):
        return get_uuid()
    def tagged_entity(self, *tags):
        uuid = self.basic_entity()
        self.ids_to_tags[uuid] = tags
        for tag in tags:
            if tag in self.tags_to_ids:
                self.tags_to_ids[tag].append(uuid)
            else:
                self.tags_to_ids[tag] = [uuid]
        return uuid
    def add_component(self, uuid, component):
        if component.__class__ not in self.component_stores:
            self.component_stores[component.__class__] = {}
        
        store = self.component_stores[component.__class__]

        if uuid in store:
            if component not in store[uuid]:
                store[uuid].append(component)
        else:
            store[uuid] = [component]
    def has_component_of_type(self, uuid, component_class):
        if component_class not in self.component_stores:
            return False
        else:
            store = self.component_stores[component_class]
            return uuid in store and len(store[uuid]) > 0
    def has_component(self, uuid, component):
        if component_class not in self.component_stores:
            return False
        else:
            store = self.component_stores[component.__class__]
            return uuid in store and component in store[uuid]
    def get_component(self, uuid, component_class):
        return self.component_stores[component_class][uuid][0]

