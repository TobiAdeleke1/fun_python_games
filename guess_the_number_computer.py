"""
The goal is to play a guee the number with the computer
"""
import random

def guess_number(guess_max):
   
    #1.get a random number between range 0 --> guess_max
    random_number = random.randint(0,guess_max)

    #2. Use a while loop to keep playing, untill guessed right
    while True:
        #3.. get user input and max sure as int, NOT NEED TO BE INSIDE LOOP
        user_guess = int(input('Please, input your guess: '))
        
        if user_guess in list(range(0,guess_max)):
            # Checking conditions 
            if user_guess == random_number:
                print(f"Congratulation, you guessed {random_number} right !!!")
                break
            
            elif user_guess < random_number:
                print('Ooops, Guess was too low')
            
            else:
                print('Ooops, Guess was too high')
        else:
            print(f'Please guess a number between 0 and {max_guess}')
        
if __name__ == '__main__':
    print('Welcome to Guess the number')
    max_guess = int(input('What is the range you want to play within, 0 --> your number '))
    guess_number(max_guess)