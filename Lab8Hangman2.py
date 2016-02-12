import random #importing random to allow random gneration of word from list.


HANGMANPICS = ['''
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']


#wordList = "cunning bats problem avacado boxing bright elbow knowlege strings integers mistake parsing error guitar road brick".split()  # SPLIT at end defaults as splitting where the space is and turning into a list.
#wordList = "cunning bats".split()

#List = open("filename.txt").readlines()

def pickRandomWord(fname):      #.readlines(), #line.split(), #for i in fname:  wordList.append(i.rstrip().split(','))
    wordList = open(fname).readlines()
    while True:   #loop to only allow words >=5 letters
        wordIndex = random.randint(0, len(wordList)-1)
        word = wordList[wordIndex]
        if len(word) >= 5:
            return word

    #print (word)
    #return word

def changeWordToStars (word):
    starVersionOfWord = "_" * len(word)     #creates starVersionOfWord list of starts (*) by multiplying the string value '*' by the amount of letters in the variable word.
    starVersionOfWord = list(starVersionOfWord)         # this converts the '*' version of the word into a list, to allow better indexing and replacing of letters, also comparing of lists.
    return starVersionOfWord

def convertStarsToList (starVersionOfWord):
    listStarVersionOfWord = list(starVersionOfWord)
    return listStarVersionOfWord

'''
def pickRandomWord(fname):
    wordList = []
    with open(fname) as inputfile:
        for line in inputfile:
            wordList.append(line.split())
    wordIndex = random.randint(0, len(wordList)-1)
    word = wordList[wordIndex]
    print (word)
    return word
'''

'''
def pickRandomWord (wordList):  # paramter is the list created above (which has been "split" where space are and turned into a list. Thus allowing indexing
    wordIndex = random.randint(0, len(wordList)-1)  #creating a varaible to use to pick a word at a random index. -1 as otherwise list index out of range
    word = wordList[wordIndex] # creates word variable (to be returned and used elsewhere) by calling the string that is at the index position in the word list.
    return word   #OTHER OPTION ##RANDOM.CHOICE(WORDLIST).LOWER WOULD WORK TOO??
'''

'''def pickRandomWord (wordList):
    wordList = importfromtxt()
    word = random.choice(wordList).lower
    return word
'''

def compareGuess (listStarVersionOfWord, word, word_listversion): # function asks for letter, compares against secret word
    print (listStarVersionOfWord)
    guesses_made = []
    lives = 6
    while(lives > 0 and listStarVersionOfWord != word_listversion):
        image_to_display = int(6 - lives)
        print (HANGMANPICS[image_to_display], "        lives = ", lives, "      ||   ", "guesses made so far", guesses_made)
        while True:
            guess = str.lower(input("enter letter or guess full word: "))
            if guess in guesses_made:
                print ("You have already guessed this, no lives lost. Guess again.")
                print ("guesses made so far", guesses_made)
            elif not guess.isalpha():
                print ("Please enter VALID letter")
            elif guess.isalpha() or word:
                guesses_made.append(guess)
                break
        print(listStarVersionOfWord)   ## this prints blank at start of guess
        if guess == word:
            print ("Great guess! You won the game! http://linuxart.com/stuff/gnome/gegl.png ")
            break
        elif guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    listStarVersionOfWord[i] = guess
                    print ("congratulations, correct guess")
                    print(listStarVersionOfWord)
        elif guess not in word:
            ### removes life if guess incorrect.
            print ("sorry, wrong guess")
            lives -= 1


def main():
    print ("####    Welcome to hangman    ####\n".center(50))

    players = input("1 or 2 player?: ")
    if players == "1":
        word = pickRandomWord("dictionary.txt")
    elif players == "2":
        while True:
            word = input("Player 2 please enter game word: ")
            if not word.isalpha() or len(word) < 5:
                print ("Word must be >5 & letters only.")
            else:
                print ("\n \n \n \n \n \n \n \n \n \n \n ")
                print ("Player 1's turn")
                break

    starVersionOfWord = changeWordToStars (word)
    listStarVersionOfWord = convertStarsToList (starVersionOfWord)

    word_listversion = list(word)  #converts "word" into a list.

    compareGuess (listStarVersionOfWord, word, word_listversion )  #this runs function where most of the work for the game is happening.

    print("THE END")
    print("The secret word =", word)

    playAgain = str.lower(input("Would you like to play again?")) ## play again, if yes, run main.
    if playAgain in "yes":
        main()

    print ("Goodbye")


main()
