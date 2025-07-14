from main import *

if __name__ == "__main__":
    # Set up the plugboard
    plugboard = Plugboard()
    plugboard_pairs = ["VH", "PT", "ZG", "BJ", "EY", "FS"]
    for pair in plugboard_pairs:
        plugboard.add(PlugLead(pair))
    
    # Set up the reflector
    reflector = Reflector("B")

    # Set up the rotors and reflector
    rotor1 = Rotor(name="III", ring_setting="10")
    rotor2 = Rotor(name="I", ring_setting="02")
    rotor3 = Rotor(name="Beta", ring_setting="23")

    rotor_positions = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = "CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH"
    crib = "UNIVERSITY"

    for position in rotor_positions:
        rotor1.position = ord(position) - ORDER_OF_A
        for position in rotor_positions:
            rotor2.position = ord(position) - ORDER_OF_A
            for position in rotor_positions:
                rotor3.position = ord(position) - ORDER_OF_A
                enigma = EnigmaMachine(plugboard, [rotor1, rotor2, rotor3], reflector)
                ciphertext = enigma.encode(plaintext)
   
                if crib in ciphertext:
                    print(f"Rotor 1 position: {enigma.rotors[0].position}, Rotor 2 position: {enigma.rotors[1].position}, Rotor 3 position: {enigma.rotors[2].position}.")
                    print(f'The ciphertext is: "{ciphertext}".')

                    

    


        