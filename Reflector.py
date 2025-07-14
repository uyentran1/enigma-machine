ORDER_OF_A = 65

class Reflector:
    mappings = {
        "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
        "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
    }

    def __init__(self, name):
        self.name = name
        self.mapping = self.mappings[name]

        self.original_mapping_list = []
        for char in self.mapping: 
            self.original_mapping_list.append(char)

        self.mapping_list = []
        for char in self.mapping: 
            self.mapping_list.append(char)

    def reflect(self, char):
        index = ord(char) - ORDER_OF_A
        return self.mapping[index]

    def reflect_by_list(self,char):
        index = ord(char) - ORDER_OF_A
        return self.mapping_list[index]