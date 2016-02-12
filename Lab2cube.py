'''def calc_vol (user_width):
    vol = user_width**3
    return vol


def calc_surface_area (user_width):
    surface_area = (user_width ** 2)*6
    return surface_area
'''
'''
def compare (): ##for loop to give results of both vol&surface within defined range.
    for user_width in range (1,20):
        vol = user_width**3
        surface_area = (user_width ** 2)*6
        print ("width is ", user_width, "vol is"  , vol, "surface is ", surface_area)

'''

def compare ():
    surface = 0 #predefine variables so as to have running total, thus allowing totals to be compared as a break condition for loop below.
    vol = -1  #-1 because the programme will see that 0 = 0 and not run loop.
    width = 0
    while vol != surface: #loop that calculates vol & furface as long as they are not outputting same answer.
        width += 1 #increase width first, else 0 values returned. Were trying to skip 0, without starting width on 1 (else will falsely return 7 as convergent point,a nd not 6)
        vol = width**3
        surface = (width ** 2)*6
        print ("w" , width, "s", surface,"v", vol)




def main ():
    compare()

    #user_width = float(input("Enter cube width: "))

    #surface_area = calc_surface_area (user_width)
    #vol = calc_vol(user_width)

    #print ("The surface area of the cube is: ", surface_area)
    #print ("The volume of the cube is: " , vol)




main()