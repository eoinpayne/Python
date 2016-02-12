#conversionrate = 1.37001

#user_temperaturetype = str(input("Which temperature to convert? (c or f:)"))
#user_temperature = float(input("Enter temperature to convert: "))



#if user_temperaturetype == ("c"):
    #print(((user_temperature * 9/5) + 32), ("F"))

#else: print(((user_temperature - 32)* 5/9),("C"))



def C_to_F(user_temp_c):
    converted_to_f = ((user_temp_c * (9/5)) + 32)
    return converted_to_f

def main():
    user_temp_c = float(input("Enter celcius temperature to convert: "))
    converted_to_f = C_to_F(user_temp_c)
    print (converted_to_f)

main()