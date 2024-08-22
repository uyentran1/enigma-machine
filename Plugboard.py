class PlugLead:
    def __init__(self, mapping):
        self.mapping = {mapping[0]: mapping[1], mapping[1]: mapping[0]}

    def encode(self, char):
        return self.mapping.get(char, char)

class Plugboard:
    def __init__(self):
        self.mapping_dict = {}

    def add(self, lead):
        self.mapping_dict.update(lead.mapping)

    def encode(self, char):
        return self.mapping_dict.get(char, char)