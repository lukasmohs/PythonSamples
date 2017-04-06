# Author's name:            Lukas Mohs
# Creation Date:            04/06/17
# Last Modification Date:   04/06/17
# Brief Description:
# This program consists out of four functions (including the main function), which provide different samples about how to
# deal with data structures in python. The listTest() function captures user input, stores and processes it from a list.
# It calculates the min/max, average and sum form the input values.
# The stringTest() function formats an input String from camelCase to a normal format with the first word capitalized.
# It also makes  use of list to store the individual words that are derived from the input String.
# The dictionaryTest() function provides a quiz to the user by asking for the capitals of 10 different US states,
# which are retrieved from a dictionary. Each answer is evaluated and the user receives a feedback after all
# questions have been answered or the user typed the 'EXIT' keyword.
# Finally the main() function executes all of these three functions in the presented order

import re

# This function queries the user for the rainfall of 12 months in total, stores the input as integer values in a list.
# The list is sorted for the identification of the smallest and highest value. Additionally, a loop is used that iterates
# over all values to calculate the sum. Also the average is calculated by the total number of months and the sum.
# Finally, all the calculated values are printed to the screen. In case wrong input was provided, the execution halts
# and the user is notified.
def listTest():
    rainfallList = []
    for i in range(12):
        userInput = input("Please enter the rainfall for month number " + str(i) + ": ")
        try:
            rainfallList.append(int(userInput))
        except:
            print("Please just input numbers! \nProgram was terminated")
            return
    rainfallList.sort()
    total = 0
    for value in rainfallList:
        total += value
    print("The total rainfall of the year was: " + str(total))
    print("The lowest reported rainfall was: " + str(rainfallList[0]))
    print("The highest reported rainfall was: " + str(rainfallList[len(rainfallList)-1]))
    print("The average rainfall was: " + str(total/len(rainfallList)) + "\n")

# This function takes an input Sttring from a user that is written in camelCase and splits it by the contained upper case letters.
# All words except for the first one are then converted to lower case strings and printed to the screen in form of a loop.
# In case the input String had a bad format, the function is exited and the user is notified.
def stringTest():
    try:
        userInput = input("Please input an entire sentence written in camel case "
                          + "(no space between words and first letter uppercase):\n")
        splitInput = re.findall('[A-Z][a-z]*', userInput)
        output = []
        output.append(splitInput[0])
        for i in range(1,len(splitInput)):
            output.append(splitInput[i].lower())
        for word in output:
            print(word, end=' ')
    except:
        print("The provided input String seems to be invalid. \nProgram was terminated")

# This function makes use of a dictionary containing 10 US states as keys and their capitals as values.
# A loop asks the user for the capital each state and validates the input until the dictionary is empty.
# Finally, the number of correct and incorrect answers is printed to the screen.
# In case the user wants to exit the program earlier, he can enter 'EXIT' as an answer.
def dictionaryTest():
    print("\n\nThis test will check your knowledge about 10 capitals of different US states. "
          + "Whenever you want to exit, write 'EXIT' as an answer")
    statesWithCapitals = {
        "Alabama":"Montgomery",
        "Arizona":"Phoenix",
        "Pennsylvania":"Harrisburg",
        "Massachusettts":"Boston",
        "New York":"Albany",
        "North Carolina":"Raleigh",
        "North Dakota":"Bismarck",
        "Wisconsin":"Madison",
        "Wyoming":"Cheyenne",
        "West Virginia":"Charleston"
        }
    numberCorrect = 0
    numberIncorrect = 0
    while bool(statesWithCapitals):
        pair = statesWithCapitals.popitem()
        answer = input("What is the capital of " + pair[0] + ": ")
        if(answer.upper() == "EXIT"):
            break
        if(answer.upper() == pair[1].upper()):
            numberCorrect = numberCorrect + 1
        else:
            numberIncorrect = numberIncorrect + 1
    print("Number of correct answers: "  + str(numberCorrect))
    print("Number of incorrect answers: " + str(numberIncorrect))

# Main function that welcomes the user and calls all other functions sequentially
def main():
    print("Welcome to the data structure testing lab\n")
    listTest()
    stringTest()
    dictionaryTest()    

main()
