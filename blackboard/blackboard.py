class Blackboard:
    def __init__(self):
        self.data = {}

    def add_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)


class KnowledgeResource:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def update_blackboard(self):
        pass


class Controller:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def update_assets(self):
        pass
