rate = 1.37001

user_currency = str(input("Which curency? (sterling or euro:)"))
user_amount = float(input("Enter amount to convert: "))

if user_currency == ("sterling"):
    print(user_amount * rate)

else: print(user_amount / rate)

