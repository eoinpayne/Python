##pig latin
#idea is to find the first constanant group (letters before first vowel) remove from the start of the word, add to the end and ad "ay"

##IMPROVE TO TAKE MORE THAN 1 WORD


def takeUserWord():     #validates user input
    #word = str.lower(input("Enter word: "))
    while True:
        word = str.lower(input("Enter word: "))
        if len(word) < 2:
            print ("Word must be longer than 2 letters")
        elif not word.isalpha():
            print ("valid letters only")

        else:
            return word


        # if len(word) > 2:
        #     wordoflist = []
        #     for i in range (0, len(word)): ##turning word into list to explore comparing using 'any'
        #         #if word[i] not in "abcdefghijklmnopqrstuvwxyz":
        #         wordoflist.append(word[i])
        #     print (wordoflist)
        # for i in range (0, len(word)):
        #     if wordoflist[i] not in alphalist:
        #         print ("illegal char")
        #     else:
        #         return word



    # alpha = "abcdefghijklmnopqrstuvwxyz"
    # alphalist = []
    # for i in range (0,len(alpha)): # creating list of aplhabet, to allow list comparisons.
    #     alphalist.append(alpha[i])
    # print (alphalist)
    #
    # while True:
    #     alpha = "abcdefghijklmnopqrstuvwxyz"
    #
    #     word = str.lower(input("Enter word: "))
    #     while len(word) <= 2:
    #         print ("Word must be longer than 2 letters")
    #         break
    #     if len(word) > 2:
    #         wordoflist = []
    #         for i in range (0, len(word)): ##turning word into list to explore comparing using 'any'
    #             #if word[i] not in "abcdefghijklmnopqrstuvwxyz":
    #             wordoflist.append(word[i])
    #         print (wordoflist)
    #     for i in range (0, len(word)):
    #         if wordoflist[i] not in alphalist:
    #             print ("illegal char")
    #         else:
    #             return word

                # if all[wordoflist] not in alphalist: ## exploring if any with li
                # print ("illegal char")

            #
            # else:
            #     return word

    # while True:
    #     word = str.lower(input("Enter word: "))
    #     if any([i > 'z' or i < 'a' for i in word]):    #compares each character in word against an index of a-z
    #         print ("Error: Contains illegal characters")
    #     elif len(word) <=2:
    #         print ("Word too short")
    #     else:
    #         return word



def findfirstvowel(word): #checks if first letter of word is a vowel
    i = 0
    if word[i] not in "aeiou":
        i += 1
    return i  ##returns position of first vowel


def translate (word):
    i = findfirstvowel(word)
    if i == 0:   ## if first letter was a vowel, just ad "ay"
        return word + "yay"
    elif i != 0: ## modifies based on position of first vowel
        return word[i:]+word[:i] + "ay"


def main():
    #word = str(input("Enter word: "))
    #translate(word)
    word = takeUserWord()
    print ("translation for ", word, "is: ", translate(word))





main()