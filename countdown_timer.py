import time
import random


def count_down(t):
    computer_choices = ['Go Dancing', 'Go Swimming',
                    'Do Some-work', 'Go Eat Something',
                    'You Chose', 'Have a beautiful day ']
    random.shuffle(computer_choices)
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs) 
        print(timer, end='\n')
        t -= 1
        time.sleep(1)
    computer_output = random.choice(computer_choices)
    print("I command:", computer_output)


if __name__ == '__main__':
    print('hello')
    user_input = input("How long do you want the counter in secs: ")
    count_down(int(user_input))
