# Author's name:            Lukas Mohs
# Creation Date:            04/18/17
# Last Modification Date:   04/18/17
# Brief Description:
# This program provides a small interactive game for two players,
# which anser 10 questions out of the field of simple maths.
# The questions are based on the question class, which is used
# in the main method to instantiate 10 objects with corresponding
# questions answers and the provided correct answer.

# This class implements the question entity consisting out of
# four potential answers to a question and the correct answer.
# All these values have to be provided for the constructor and can
# be set and get with the corresponding accessors and mutators.
class Question:

    # Constructor taking the question, four answers and the correct answer
    def __init__(self, question, answer1, answer2, answer3, answer4, correctAnswer):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correctAnswer = correctAnswer

    # Accessors for the question, the four answers and the correct answer
    def get_question(self):
        return self.__question
    def get_answer1(self):
        return self.__answer1
    def get_answer2(self):
        return self.__answer2
    def get_answer3(self):
        return self.__answer3
    def get_answer4(self):
        return self.__answer4
    def get_correctAnswer(self):
        return self.__correctAnswer

    # Muttators for the question, the four answers and the correct answer
    def set_question(self,question):
        self.__question = question
    def set_answer1(self,answer1):
        self.__answer1 = answer1
    def set_answer2(self,answer2):
        self.__answer2 = answer2
    def set_answer3(self,answer3):
        self.__answer3 = answer3
    def set_answer4(self,answer4):
        self.__answer4 = answer4
    def set_correctAnswer(self,correctAnswer):
        self.__correctAnswer = correctAnswer

# Main function that welcomes the user, initiates all questions and
# stores them in a list. Then, both user are asked to provide their
# answers to the questions and their performance is measured.
# Finally, the results of both players are printed.
def main():
    print("Welcome to the the funny mini game\n")
    # create a questions list and add all new question objects
    questions = []
    questions.append(Question("What is 5+6?", "11","4","10","99",1))
    questions.append(Question("What is 5+5?", "1","4","10","99",3))
    questions.append(Question("What is 100/5?", "10","20","30","40",2))
    questions.append(Question("What is 500/100?", "5","10","15","20",1))
    questions.append(Question("What is 15%3?", "0","1","2","3",1))
    questions.append(Question("What is 20%3?", "0","1","2","3",3))
    questions.append(Question("What is 24%7?", "0","1","2","3",4))
    questions.append(Question("What is 5*5", "15","25","35","45",2))
    questions.append(Question("What is 7*7", "39","49","59","69",2))
    questions.append(Question("What is 8*8", "64","46","44","66",1))
    # Initialize a userPoints dictionary to store the number of correct answers
    userPoints = {}
    # Initialize a list for both user (change number to have more users)
    users = range(2)
    # For all users
    for user in users:
        # Set points to zero
        userPoints[user] = 0
        # Ask the question
        print("Questions for user number " + str(user))
        # Print all possible answers
        for q in questions:
            print("\n" + q.get_question())
            print("1: " + q.get_answer1())
            print("2: " + q.get_answer2())
            print("3: " + q.get_answer3())
            print("4: " + q.get_answer4())
            # Prompt for the user's for answer
            answer = input("Your answer: ")
            # As long as the user's input is invalid
            while (not answer.isdigit() or int(answer)<1 or int(answer)>4):
                # Prompt for the user's again for answer
                answer = input("Pleas enter a number between 1 and 4. \nYour answer: ")
            # Check the user's answer
            if str(q.get_correctAnswer()) == str(answer):
                # If the answer was correct, increase his point score
                userPoints[user] =  userPoints[user] + 1

        # Clear the screen to avoid cheating
        for i in range(50):
            print("")
    
    print("Total Scores\n")
    # Print the results of all players
    for user in users:
        print("Points of user number " +  str(user) + ":")
        print(str(userPoints[user]))
        print("\n")
# Call main() function
main()
