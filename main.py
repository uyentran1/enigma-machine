from Plugboard import *
from Rotor import *
from Reflector import *
from EnigmaMachine import *

if __name__ == "__main__":
    plugboard2 = Plugboard()
    pairs = ["PC", "XZ", "FM", "QA", "ST", "NB", "HY", "OR", "EV", "IU"]
    for pair in pairs:
        plugboard2.add(PlugLead(pair))
    rotor1 = Rotor("I", "05", "P") # notch: Q
    rotor2 = Rotor("Beta", "03", "G") # notch: None
    rotor3 = Rotor("V", "24", "Z") # notch: Z
    rotor4 = Rotor("IV", "18", "E") # notch: J
    reflector = Reflector("A")
    enigma = EnigmaMachine(plugboard2, [rotor1, rotor2, rotor3, rotor4], reflector)
    
    message = "BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI"
    encoded_message = enigma.encode(message)
    print(encoded_message) 

    