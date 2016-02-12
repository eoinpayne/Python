# def pickRandomWord(fname):
#     wordList = []
#     with open(fname) as inputfile:
#         for line in inputfile:
#             wordList.append(line.split())
#     wordIndex = random.randint(0, len(wordList)-1)
#     word = wordList[wordIndex]
#     print (word)
#     return word

def num_of_lines(fname):
    word_list = []
    with open(fname) as f:
        list = f.read().split()
    i = 0
    for position in list:
        print(i, position, sep=".")
        #print(i, position, end="")
        i += 1







def main():
    name_of_file = "dictionary.txt"
    num_of_lines(name_of_file)


main()

