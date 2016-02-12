#user_width = float(input("Enter width: "))
#user_length = float(input("Enter length: "))

#perimiter = (user_length * 2)+(user_length * 2)

#print ("Perimiter = ", perimiter)

def what_is_perimiter (user_width, user_length):
    perimiter = ((user_width * 2) + (user_length * 2))
    return perimiter

def main ():
    user_length = float(input("Enter length: "))
    user_width = float(input("Enter width: "))
    perimiter = what_is_perimiter(user_width, user_length)
    print (perimiter)

main()