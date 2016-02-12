
def book_store (book_price, book_quantity, shipping_cost, discount):
    total = ((book_price * book_quantity + shipping_cost)*discount)
    return total


def main():
    book_price = float(input("Enter price: "))
    book_quantity = int(input("How many copies?: "))
    shipping_cost = float((3 +((book_quantity - 1)*.75)))
    discount = .6
    total = book_store (book_price, book_quantity, shipping_cost, discount) ## issue here, where i did not "call" the book store function to allow the 2main" function to know where total w\as to be printed from. i.e. 2total"
                                                                           # could not be defined in the main function, as it was a local variable of another function... so THAT function had to be called to pull it's local variable.
    print ("Shipping cost is: " , shipping_cost)
    print ("Total cost is" , total)


main()


