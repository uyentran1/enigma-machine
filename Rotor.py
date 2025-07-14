ORDER_OF_A = 65
NUM_OF_LETTERS = 26

class Rotor:
    mappings = {
        "Beta": "LEYJVCNIXWPBQMDRTAKZGFUHOS",
        "Gamma": "FSOKANUERHMBTIYCWLQPZXVGJD",
        "I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "IV": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "V": "VZBRGITYUPSDNHLXAWMJQOFECK"
    }

    notches = {
        "Beta": None,
        "Gamma": None,
        "I": "Q",
        "II": "E",
        "III": "V",
        "IV": "J",
        "V": "Z"
    }

    def __init__(self, name, ring_setting="01", position="A"):
        self.name = name
        self.mapping = self.mappings[name]
        self.ring_setting = int(ring_setting)
        self.ring_setting_gap = self.ring_setting - 1 # Gap between the actual ring setting with the default ring setting "01"
        self.position = ord(position) - ORDER_OF_A
        self.notch = self.notches[name]
        if self.notch != None:
            self.notch_position = ord(self.notch) - ORDER_OF_A

    def encode_right_to_left(self, char):
        index = (ord(char) - ORDER_OF_A - self.ring_setting_gap + self.position) % NUM_OF_LETTERS
        mapped_char = self.mapping[index]
        return chr(((ord(mapped_char) - ORDER_OF_A + self.ring_setting_gap - self.position)) % NUM_OF_LETTERS + ORDER_OF_A)

    def encode_left_to_right(self, char):
        new_char = chr((ord(char) - ORDER_OF_A - self.ring_setting_gap + self.position) % NUM_OF_LETTERS + ORDER_OF_A)
        index = self.mapping.index(new_char)
        return chr((index + self.ring_setting_gap - self.position) % NUM_OF_LETTERS + ORDER_OF_A)

    def rotate(self):
        self.position = (self.position + 1) % NUM_OF_LETTERS