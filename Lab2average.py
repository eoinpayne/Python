__author__ = 'D15123620'

#(1 point) Write a program average.py that calculates and prints the average of three
#numbers. Test it with 3, 5 and 6. Does it make a difference if you treat the input strings as
#float or int? what about if you print the output result as float or an int?

'''def what_is_average (num_1, num_2, num_3):  ###original way of doing it required that i enter in how many numbers there were
    average = ((num_1 + num_2 + num_3)/3)       ### to be averaged
    return average
'''


def what_is_average (num_1, num_2, num_3):

    numbers_to_average = [num_1, num_2, num_3]## this line sets list of numbers to be averaged
    to_divide_by = len(numbers_to_average)  ##this line counts the amount of items in list above

    average = ((num_1 + num_2 + num_3)/to_divide_by) ## this line divides list by the variable that counted the list
    return average



def main():
    num_1 = float(input("Enter number 1: "))
    num_2 = float(input("Enter number 2: "))
    num_3 = float(input("Enter number 3: "))
    average = what_is_average(num_1, num_2, num_3)
    print("%.2f" % average)

main()

'''
numstoAvg = [num1, num2, num3]   ## array / list

=len(mnumbstoAvg)    ##this counts how many in the list. this result can then be used to calculate as the dividing number.

'''