from main import *

if __name__ == "__main__":
    # Set up the plugboard
    plugboard = Plugboard()
    plugboard_pairs = ["KI", "XN", "FL"]
    for pair in plugboard_pairs:
        plugboard.add(PlugLead(pair))
    
    # Reflector object possibilities
    reflectors = [Reflector("A"), Reflector("B"), Reflector("C")]
    
    for reflector in reflectors:
        # Reset the rotors for each reflector
        rotor1 = Rotor("V", "14", "M")
        rotor2 = Rotor("Gamma", "02", "J")
        rotor3 = Rotor("Beta", "04", "M")
        
        enigma = EnigmaMachine(plugboard, [rotor1, rotor2, rotor3], reflector)
        plaintext = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
        ciphertext = enigma.encode(plaintext)
    
        if "SECRETS" in ciphertext:
            print(f"The correct reflector is Reflector {enigma.reflector.name}.")
            print(f'The ciphertext is "{ciphertext}".')
