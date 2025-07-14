from Plugboard import *
from Rotor import *
from Reflector import *

class EnigmaMachine:
    def __init__(self, plugboard, rotors, reflector):
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector

    def encode(self, text):
        out_text = ""

        for char in text:
            # If both rotor 1 and 2 are on notch, rotor 1, 2 and 3 rotate
            if self.rotors[0].notch != None and self.rotors[0].position == self.rotors[0].notch_position:
                if self.rotors[1].notch != None and self.rotors[1].position == self.rotors[1].notch_position:
                    for i in range(3):
                        self.rotors[i].rotate()
                # If only rotor 1 is on notch, rotor 1, 2 rotate
                else:
                    for j in range(2):
                        self.rotors[j].rotate()
            
            # If rotor 2 is on its notch, rotor 1, 2 and 3 rotate
            elif self.rotors[1].notch != None and self.rotors[1].position == self.rotors[1].notch_position:
                for k in range(3):
                    self.rotors[k].rotate()
                        
            # If neither rotor 1 or 2 are on notch
            else:
                self.rotors[0].rotate()

            char = self.plugboard.encode(char)
            
            for rotor in self.rotors:
                char = rotor.encode_right_to_left(char)
            
            char = self.reflector.reflect(char)
            
            for rotor in reversed(self.rotors):
                char = rotor.encode_left_to_right(char)
            
            char = self.plugboard.encode(char)
            
            out_text += char

        return out_text
        
    def encode_code_breaking_5(self, text):
        out_text = ""

        for char in text:
            # If both rotor 1 and 2 are on notch, rotor 1, 2 and 3 rotate
            if self.rotors[0].notch != None and self.rotors[0].position == self.rotors[0].notch_position:
                if self.rotors[1].notch != None and self.rotors[1].position == self.rotors[1].notch_position:
                    for i in range(3):
                        self.rotors[i].rotate()
                # If only rotor 1 is on notch, rotor 1, 2 rotate
                else:
                    for j in range(2):
                        self.rotors[j].rotate()
            
            # If rotor 2 is on notch, rotor 1, 2 and 3 rotate
            elif self.rotors[1].notch != None and self.rotors[1].position == self.rotors[1].notch_position:
                for k in range(3):
                    self.rotors[k].rotate()
                        
            # If neither rotor 1 or 2 are on notch
            else:
                self.rotors[0].rotate()

            char = self.plugboard.encode(char)
            
            for rotor in self.rotors:
                char = rotor.encode_right_to_left(char)
            
            char = self.reflector.reflect_by_list(char)
            
            for rotor in reversed(self.rotors):
                char = rotor.encode_left_to_right(char)
            
            char = self.plugboard.encode(char)
            
            out_text += char

        return out_text
