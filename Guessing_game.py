#Number guessing game using python global variable, functions with outputs
#best way to modify a global variable using functions with outputs
#choosing a random number between 1 - 100
from random import randint
from art import logo
EASY_TURNS =  10 #global variable number of attempts for easy level
HARD_TURNS = 5 #global variable  number of attempts for hard level

#a function to check difficulty
def check_difficulty():
    level  = input('Choose difficulty. Type easy or hard: ').lower()
    if level == 'easy':
        return EASY_TURNS #returns 10
    elif level == 'hard':
        return HARD_TURNS #return 5

#function to check the user guess aganst the random_number
def check_answer(guess,random_number,turns):
    '''That checks the guess against the answer and returns the number of turns remaining'''
    if guess>random_number:
        print('Too high')
        return turns -1 # reduce the number of turns by 1
    elif guess< random_number:
        print('Too low')
        return turns -1 #reduce the numbr of turns by 1
    else:
        print(f'You guessed right, the answer is {random_number}')

def game():
    random_number = randint(1,100)
    print(logo)
    print('Welcome to the Guessing game!')
    print('I am thinking of a number between 1-100')
    # print(random_number)
    turns = check_difficulty() #global variable to store the number of turns from check_difficulty functions

    #Repeat the functionality to make the user guess again
    guess = 0 #set guess = 0
    while guess != random_number:
        print(f'You have {turns} attempts remaining')
        #make the user to guess a number
        guess = int(input('Make a guess: '))
        #track the number of turns and reduce by 1 if the user get it wrong.
        #set the turns to the new value from check_Answer functions
        turns = check_answer(guess,random_number,turns)
        if turns == 0:
            print(f'You ran out of guesses, you lose.\nThe number is {random_number}')
            return #ends the game by ending the function
        elif guess != random_number:
            print('Guess again')
game() #call the call game function
