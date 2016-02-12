
# def pickRandomWord(fname):      #.readlines(), #line.split(), #for i in fname:  wordList.append(i.rstrip().split(','))
#     wordList = open(fname).readlines()
#     wordIndex = random.randint(0, len(wordList)-1)
#     word = wordList[wordIndex]
#     #print (word)
#     return word

def checkAvgLength(fname):
    length_of_all = open(fname).read()
    list_of_all = open(fname).readlines()
    average = (len(length_of_all) / len(list_of_all))
    #print ("Length of chars = " , length_of_all)
    print ("Length of chars = " , len(length_of_all))
    print ("Length of list items = " , len(list_of_all))
    print ("average =" , average )


def checkAvgLength(fname):
    list = []
    lib = open(fname).read().split()
    word_count = 0
    char_count = 0
    for i in lib:
        #list.append(i[:-1])
        char_count += len(i)
        word_count += 1




def main ():
    #enter_filename = input("Enter file name: ")
    enter_filename = "dictionary.txt"

    checkAvgLength(enter_filename)
    #calc (list)


main()