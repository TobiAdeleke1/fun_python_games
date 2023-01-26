# https://github.com/Xethron/Hangman/blob/master/words.txt to get words

import os

def getWordList():
    path = os.path.dirname(__file__)
    filepath = path+'/words.txt'
    print(filepath)
    with open(filepath,'r') as f:
        # line = f.readlines()
        words_list = [line.strip() for line in f.readlines()]
    #use strip() to remove '/n'
    f.close()
    return words_list
