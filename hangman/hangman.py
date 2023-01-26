from words import getWordList
import random
import string

def hangman():
    print('Welcome to the Hangman Game !!! ')
    words_list = getWordList()
    word = random.choice(words_list).lower() # computer picks the word
    len_word = len(word) # TODO ; USE SET LENGTH INSTEAD OF WORD LENGTH
    
    len_chosen_word = len(set(word))
    alphabet_set = set(string.ascii_lowercase)
   
    guessed_word = set()
    guess_limit = len_chosen_word + 2 # you can allow users to change guess limits based on difficulty
    current_word = ''

    print('Hint, the word has',len_word,'characters')
    while guess_limit >0:

        # i want to create a display
        
        
        user_guess = input('Guess a character in the word: ')
        if user_guess in alphabet_set: # check if input word is valid    
            if user_guess in word:
                #create a list of previous guesses
                guessed_word.add(user_guess) # add the guess to 
        else:
            print('Not a valid charater, guess again')
        
        previous_list = []
        for letter in word:
            if letter in guessed_word:
                previous_list.append(letter)
            else:
                previous_list.append('_')
        current_word = ''.join(previous_list)
       
        print('Guesses ',  current_word)

        if current_word == word: #check word
            print('Congratulation, you guess the word:', word)
            break
       
             
        # if len(guessed_word) == len_word: 
        #     if ' '.join(guessed_word) == word:
        #         print('Congratulation, you guess the word', word)
        #     break
        

    
        guess_limit -=1
    
    if guess_limit == 0:
        print('Sorry, you ran out of chances, the word was:', word)

hangman()