from Plugboard import *

if __name__ == "__main__":
    plugboard = Plugboard()
    plugboard.add(PlugLead("AB"))
    plugboard.add(PlugLead("UI"))


    print(plugboard.encode("Y"))