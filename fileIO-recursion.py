# Author's name:            Lukas Mohs
# Creation Date:            03/30/17
# Last Modification Date:   03/30/17
# Brief Description:
# This program asks the user for a filename, where the program will write and
# read from. As the second input, the user has to provide the number of random
# files that should be written and read from the file.
# Then, the file is created (or overwritten) and the random numbers are written
# linewise to the file. Afterwards, the numbers are read from the file again,
# printed and finally summed up and the result printed as well.
# The printAsterics function is a recursive function that takes the number
# of requested outputlines as an argument and prints the linenumber
# together with the String "asterics" to the screen

import random

def writeRandomNumbersToFile(fileName, numberOfNumbers):
    file = open(fileName, 'w+')
    content = ""
    for num in range(numberOfNumbers):
        content += str(random.randint(0,500)) + "\n"
    file.write(content)
    file.close()

def readNumbersFromFile(fileName, numberOfLines):
    file = open(fileName, 'r')
    content = ""
    sum = 0
    for num in range(numberOfLines):
        content = file.readline()
        print(content)
        sum += int(content)
    print("\nThe sum of the numbers is: ", str(sum)) 
    file.close()

def printAsterics(depth):
    if depth > 0:
        printAsterics(depth-1)
        print(str(depth),"asterics")

def main():
    print("Welcome to the random number to file writer")
    fileName = input("Input the filename you want to write to:")
    numberOfNumbers = int(input("Input the number of random numbers you want to generate:"))
    writeRandomNumbersToFile("test.dat", numberOfNumbers)
    readNumbersFromFile("test.dat",numberOfNumbers)
    printAsterics(4)

main()
