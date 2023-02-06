import string
import random


def check_user_input(user_message):
    try:
        user_choice = int(input(user_message))
        return user_choice
    except ValueError:
        print('Invalid Integer')
        return False
    
def main():
    char_choice = string.ascii_letters + string.punctuation
    password_wanted = check_user_input('How many password would you like to generate ? ')
    password_length = check_user_input('What is the desired length of these passwords ? ')
    if password_wanted and password_length:
        for i in range(password_wanted):
            generates_password = ''
            for _ in range(password_length):
                generates_password += random.choice(char_choice)
            print(f'Password {i+1} is:',generates_password)


if __name__ == '__main__':
    main()