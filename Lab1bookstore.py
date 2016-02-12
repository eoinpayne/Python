shippingfirst = 3
shippingrest = .75

discount = .6
price = input("Enter price of book: ")
discount =  float (input ("Enter discount % :"))
discounttouse= (100 - discount)/100

discountedprice = (price * discounttouse)
ordernumber = input("Enter quantity: ")


shippingcost = (3 +((ordernumber - 1)*.75))

discountedorder = (discountedprice * ordernumber)

totalcost = (ordernumber * discountedprice + shippingcost)


print ("cost is:", (price * ordernumber))
print("with a discount of 40% is: ",(discountedprice * ordernumber))
print("total cost with shipping is: ", totalcost)
