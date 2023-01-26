"""
Goal: a Guess the number,where the computer guess
"""

import random

def computer_guess(max_range):
    min_range = 0
    max_range= max_range
    user_input = ''

    while True:
        #let computer guess within the range
        comp_guess = random.randint(min_range,max_range)
        user_input = input(f'Is your number {comp_guess}. Input Yes(y), Higher(h) or Low(l): ').lower()

        if user_input[0] == 'y':
            print(f'Yayy, i guessed your number {comp_guess} right')
            break
        elif user_input == 'h':
            min_range = comp_guess
        elif user_input == 'l': # i want to explicitly  check
            max_range = comp_guess

    #TODO: can improve by keeping preious guesses and quite error prone


if __name__ == '__main__':
    print('Welcome to I guess your number')
    max_guess = int(input('What is the range you want to play within, 0 --> your number '))
    computer_guess(max_guess)



   