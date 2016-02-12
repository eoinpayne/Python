##davy-carson@hotmail.com

'''def convert_word_to_list(gameword):
    gamelist = list(gameword)
'''
def convert_word_to_blank (gameword):
    blank_guess_word = "*" * len(gameword)
    blank_guess_word_list = list(blank_guess_word)
    #print (blank_guess_word_list)
    return blank_guess_word_list

def check_user_letter_against_gameword (user_letter, gameword, blank_guess_word_list, lives):  ##should game word be paramater, or define within the function
    user_letter_list = list(user_letter)
    gamelist =list(gameword)

    guessed_list = []
    correct_guesses = []
    incorrect_guesses = []



    for i in range (len(gamelist)):
        blank_guess_word_list1 = blank_guess_word_list

        if user_letter == gamelist[i]:

            blank_guess_word_list1[i] = gamelist[i]
            blank_guess_word_list = blank_guess_word_list1

            guessed_list.append(user_letter)
            correct_guesses.append(user_letter)

            print ("this one", blank_guess_word_list1)
            return blank_guess_word_list


        elif user_letter not in gamelist:
            lives -= 1
            guessed_list.append(user_letter)
            incorrect_guesses.append(user_letter)
            print ("not in, life down")
            print (blank_guess_word_list)
            #return lives

    #print (blank_guess_word_list)

    #else:
       # lives += 1
   # return lives




def main():
    print ("lives: ", lives)
    gameword = ("doggy")
    gamelist =list(gameword)

    convert_word_to_blank(gameword)

    #blank_guess_word_list = convert_word_to_blank (gameword)
    #print(blank_guess_word_list)


    '''while True:
        while True:
            like_to_play = str.lower(input("Would you like to play? Yes / No: "))
            if like_to_play in "yes":
    '''
    '''
    while True:
        if lives <= 0 or blank_guess_word_list1 == gamelist:
            break
        else:
            user_letter = str.lower(input("Enter your letter: "))
            print ("lives: ", lives)
            blank_guess_word1 = check_user_letter_against_gameword (user_letter, gameword, blank_guess_word_list, lives)

            blank_guess_word = convert_word_to_blank (gameword)
            check_user_letter_against_gameword #(user_letter, gamelist, blank_guess_word, lives)


    print("game over: playa again?")
    '''
                      ##choice(list)
    #user_letter = str.lower(input("Enter your letter: "))
    print ("lives: ", lives)
    lives = 6
    while lives >0:
        user_letter = str.lower(input("Enter your letter: "))
        blank_guess_word_list = convert_word_to_blank (gameword)
        blank_guess_word = convert_word_to_blank (gameword)
        check_user_letter_against_gameword (user_letter, gameword, blank_guess_word_list, lives)


main()