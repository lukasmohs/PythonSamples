# Author's name:            Lukas Mohs
# Creation Date:            04/20/17
# Last Modification Date:   04/21/17
# Brief Description:
# This Application provides a demo for the realization of inheritance in
# Python. The Base class Beast is implemented as well as a subclass Dragon.
# The Beast class is initialized with a species.
# Beast implements a getSpecies() method that returns a String. Dragon furthermore
# implementes a speak() method, which prints a String. Two Dragons and one
# Beast in instantiated withint the main() function and their methods executed.

# This Beast class has an initializer that takes a species, which can
# be retrieved by the getSpecies() function.
class Beast:
    # initialiser that takes and sets the species
    def __init__(self,species):
        self.__species=species

    # Getter for the species 
    def getSpecies(self):
        return self.__species

# This class inherits from Beast and calls its initializer. It extends the
# Beast's functionality by the speak() method.
class Dragon(Beast):
    # Initializer that takes the species and calls the initializer of
    # the suberclass
    def __init__(self,species):
        Beast.__init__(self,species)

    # This method prints the String "AHHHH"
    def speak(self):
        print("AHHHH")

# The main() function instantiates two Dragons and one Beast, calls
# the first Dragon's speak() method and prints the species of all objects
def main():
    # Instantiate Beast
    beast = Beast("Demon")
    # Instantiate two Dragons
    dragon1 = Dragon("Basilisk")
    dragon2 = Dragon("Leviathan")
    # Call the speak method of first Dragon object
    dragon1.speak()
    # Print all of the Beast's species
    print(dragon1.getSpecies())
    print(dragon2.getSpecies())
    print(beast.getSpecies())

# Call main() method
main()
