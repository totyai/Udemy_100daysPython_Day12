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
life, thought = 0
def init():
    global logo, life, thought
    # TODO - Create user welcome & explain rules
    print(f"Welcome to\n{logo}.\nI have thought of a number between 1 and 100. You need to guess it under - for easy option 10, for hard option 5 - guesses. ")
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


# TODO - Check the guess against the number
print(f"You have {life} attempts remaining to guess.")
guess = input("Make a guess: ")

# TODO - Give feedback to the user & manage life
if guess > thought:
    life -= 1
    print(f"Too high.\nGuess again.\nYou have {life} attempts remaining to guess")

elif guess < thought:
    life -= 1
    print(f"Too low.\nGuess again\nYou have {life} attempts remaining")

else:
    print(f"You got it! The answer was {guess}")

def main():
    init()
# TODO - build up logic with fucntion declarations etc

if __name__ == "__main__":
    main()