
def check_word(word):

    if len(word) <=1:
        print ("Please type word")

    else:
        translation = ((word[1:]) + (word[0] + "ay"))
        #translation = (word[1] + "ay")
        return translation


def main():
    word = str(input("Enter word: "))
    translation = (check_word(word))
    print (translation)

main()
