# [App to be built](https://appbrewery.github.io/python-day12-demo/)

# TODO - declare global variables
import random
logo = """
                                                  #                                         #                   
  :###:                                      #    #                                         #                   
 .#: .#                                      #    #                                         #                   
 #:     #   #   ###   :###:  :###:         #####  #:##:   ###          #:##:  #   #  ## #   # ##    ###    #:##:
 #      #   #     :#  #: .#  #: .#           #    #  :#     :#         #  :#  #   #  #:#:#  #   #     :#   ##  #
 #   ## #   #  #   #  #:.    #:.             #    #   #  #   #         #   #  #   #  # # #  #   #  #   #   #    
 #    # #   #  #####  .###:  .###:           #    #   #  #####         #   #  #   #  # # #  #   #  #####   #    
 #:   # #   #  #         :#     :#           #    #   #  #             #   #  #   #  # # #  #   #  #       #    
 :#. .# #:  #      #  #. :#  #. :#           #.   #   #      #         #   #  #:  #  # # #  #   #      #   #    
  :###: :##:#   ###:  :###:  :###:           :##  #   #   ###:         #   #  :##:#  # # #  # ##    ###:   #    
"""
life = 0
thought = 0
correct_answer = False

def init():
    global logo, life, thought
    # TODO - Create user welcome & explain rules
    print(f"Welcome to\n{logo}\nI have thought of a number between 1 and 100. You need to guess it under - for easy option 10, for hard option 5 - guesses. ")
    difficulty = input("Please choose difficulty. Type 'easy' or 'hard': ")
    if difficulty.lower() == "easy":
        life = 10
    elif difficulty.lower() == "hard":
        life = 5
    else:
        print("Invalid input, the program exits.")
        return
    # TODO - Select the number to guess
    thought = random.choice(range(1,101))

def guessing():
    global life, thought, correct_answer
    while not correct_answer and (life > 0):
        # TODO - Check the guess against the number
        print(f"You have {life} attempts remaining to guess.")
        guess = int(input("Make a guess: "))

        # TODO - Give feedback to the user & manage life
        if guess > thought:
            life -= 1
            print(f"Too high.\nGuess again.")

        elif guess < thought:
            life -= 1
            print(f"Too low.\nGuess again.")

        else:
            correct_answer = True
            print(f"You got it! The answer was {guess}.")

def main():
    init()
    guessing()
    if life < 1:
        print("You run out of lifes. You lost.")
# TODO - build up logic with fucntion declarations etc

if __name__ == "__main__":
    main()