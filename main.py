class PlugLead:
    def __init__(self, mapping):
        self.mapping = mapping

    def encode(self, char):
        if char == self.mapping[0]:
            return self.mapping[1]
        elif char == self.mapping[1]:
            return self.mapping[0]
        else:
            return char

class Plugboard:
    def __init__(self):
        self.mapping_list = []

    def add(self, lead):
        if lead.mapping is not None:
            self.mapping_list.append(lead.mapping)

    def encode(self, char):
        for pair in self.mapping_list:
            if char == pair[0]:
                return pair[1]
            elif char == pair[1]:
                return pair[0]
        return char

if __name__ == "__main__":
    plugboard = Plugboard()
    plugboard.add(PlugLead("AB"))
    print(plugboard.encode("C"))