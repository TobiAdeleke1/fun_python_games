"""
YOU input your symbol and the computer choses with random 
"""
import random

def rockPaperScissor():
    print('Welcome, To this Rock, Paper and Scissor game')
    your_choice = input('Input R for Rock, S for Scissors and P for Paper: ').lower()
    computer_choice = random.choice(['r','p','s'])
    
   
    if your_choice == computer_choice:
        return 'Sorry, It\'s a tie'
    elif isWin(your_choice,computer_choice):
        print(f'my choice was {computer_choice}')
        return 'Congratulations, you won'
    else:
        print(f'Ooops, my choice was {computer_choice}')
        return 'You lost'


def isWin(user_choice, comp_choice):
    # rule for game: r> s, s> p, and p >r 
    if ((user_choice == 'r') and (comp_choice=='s')) or \
       ((user_choice == 's') and (comp_choice=='p')) or \
       ((user_choice == 'p') and (comp_choice=='r')):
          return True
    
    return False
          
if __name__ == '__main__':
    print(rockPaperScissor())