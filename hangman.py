import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_________        ",
              "|                ",
              "|                ",
              "|        |       ",
              "|        0       ",
              "|       /|\      ",
              "|       / \      ",
              "|                "
               ]
    rletters = list(word) # List to keep track of the letters in the word given.
    board = ["_"] * len(word) # Creates a board that the user's letters will go on.
    win = False # initialization of win variable to track if a win occurs
    print "Welcome to Hangman!"
    while wrong < len(stages) - 1:
        print "\n"
        msg = "Guess a letter: "
        char = raw_input(msg)
        if char in rletters:
            cind = rletters\
                   .index(char)
            board[cind] = char
            rletters[cind] = "$" # This prevents the loop from stopping.
        else:
            wrong += 1
        print " ".join(board)
        e = wrong + 1
        print "\n".join(stages[0:e])
        if "_" not in board:
            print "You Win! It was "+"".join(board)+"!"
            win = True
            break
    if not win:
        #print "\n".join(stages[0:wrong])
        print "You Lose! It was {}!".format(word)

#+++++++++++++ Challenge - To make a list of words to be selected randomly by th computer+++++++++++++++++++++++++++++
words = ["cat","dog","lion","tiger"]
words_len = len(words) - 1
wordind = random.randint(0,words_len)
word = words[wordind]
hangman(word)