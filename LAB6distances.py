from math import sin,cos,acos,pi

radius_earth = 6371

codes = ['dub', "lhr", "jfk", "aal","cdg","syd"] ### here, lists are created for each list
lats = [53.421333, 51.4775, 40.639751, 57.092789, 49.012779,-33.946111,]
longs = [-6.270075, -0.461389, -73.778925, 9.849164, 2.55, 151.177222]

airports = {"dub": [53.421333, -6.270075], "lhr": [51.4775, -0.461389], "jfk": [40.639751, -73.778925],  ## dictionary version of lists
            "aal": [57.092789, 9.849164], "cdg": [49.012779, 2.55], "syd":[-33.946111, 151.177222]}


def definetheta(lat1,lat2, long1, long2): ###converts degrees to radians
    theta1 = 90 - lat1              #90 - , as there are 2 pole points on earth, we need to know where our point is in relation to the equator/poles
    theta1 = theta1*((2*pi)/360)

    theta2 = 90 - lat2
    theta2 = theta2 * ((2*pi)/360)

    ###convert longitude radiants without 90-, as the equator doesn't have points/poles.
    phi1 = long1 * ((2*pi)/360)
    phi2 = long2 * ((2*pi)/360)

    return theta1, theta2, phi1, phi2  ## "releases" thetas and phis, by returning them after the lats and longs have been converted. Then used in function below.

'''       #here was 2 functions to do what could have been expressed in 1 function, as corrected below in 'calcDistance.'
def distance(theta1,theta2,phi1,phi2):
    d = (acos(sin(theta1)*sin(theta2)*cos(phi1-phi2)+(cos(theta1)*cos(theta2)))*6371)
    return d

def calc_distance(lat1,lat2, long1, long2):
    theta1, theta2, phi1, phi2 = definetheta(lat1, lat2, long1, long2)  ##declaring the variables that are to be used from the other function 'define theta',
                                                                        # which takes the lat1&2, long1&2 and converts from degrees to radials (theta & phi)
    d = distance(theta1,theta2,phi1,phi2)
    return d
'''
def calcDistance(lat1,lat2, long1, long2):  ##takes lats&longs (same paramaters as def definetheta above),converts them to radials, then uses the funcion 'd' to determine distance

    theta1, theta2, phi1, phi2 = definetheta(lat1, lat2, long1, long2)  ##declaring the variables that are to be used from the other function 'define theta',
                                                                        # which takes the lat1&2, long1&2 and converts from degrees to radials (theta & phi)
    d = (acos(sin(theta1)*sin(theta2)*cos(phi1-phi2)+(cos(theta1)*cos(theta2)))*radius_earth)
    return d

def getDistanceDictionary (airports,city1,city2):  ### Q4 defining variable from library

    location1 = airports[city1]  ## defining location1 as the position in list that user defined 'city1' matches
    location1lat = location1[0]       ## then using the list that was called above from library and taking list item 0 & 1 to define lay & long variable.
    location1long = location1[1]
    location2 = airports[city2]
    location2lat = location2[0]
    location2long = location2[1]

    distance_airports_from_library = calcDistance (location1lat, location2lat, location1long, location2long)
    print ("The distance between", city1, "&", city2, "is", ("%.2f" % distance_airports_from_library), "km")


def getDistanceList (codes,city1,city2, lats, longs):  ## Q3 Getting distance between 2 airports from lists.
    idx = codes.index(city1)  ##determiing the placeholder value of "city1" (our user defined location) in the list. Will return 0,1,2,3 etc. this will be used below to pick points in other lists to populate variables.
    idy = codes.index(city2)

        ### THIS ASSIGNS THE VARIABLES WITH THE VALUE OF LIST FROM ITS PLACE VALUE.
    lat1 = lats[idx]  ## here we assingning lat1 as the first position of the list it is being called from. i.e the place the loop is currently at [i], it will take from that position in list
    long1 = longs [idx]
    lat2 = lats [idy]
    long2 = longs[idy]

    distance_airports_from_list = calcDistance(lat1,lat2,long1,long2)
    print("List distnace From", codes[idx], "To", codes[idy], "is", ("%.2f" % distance_airports_from_list), "km")
    return distance_airports_from_list


def main():
##moved lists from main to top, not sure of there are hidden ramifications.


    ##Here is a loop to continue asking question until desired input received.
    while True:
        askUser = str.lower(input("Would you like to choose 2 cities? Yes or No: "))  # forces lower case string of input
        if askUser in "yes":   #allows input to be less that full word.
            break
        elif askUser in "no":
            break
        else:
            askUser = True
            print ("Please enter either 'yes' or 'no' when prompted")

    if askUser in "yes":    ##if above answer is yes, then new loop starts.
        table = []
        origin = []
        destination = []
        distance = []
        while len(table) < 18:
            while True:         ## loop ensures that input matches list options printed.
                print()
                print ("Choose from", codes)
                city1 = input("Enter first airport code: " )
                if city1 in codes:          #if input is in list, then loop will break and ask for city2.
                    #table.append(city1), origin.append(city1)
                    if city1 not in origin:
                        origin.append(city1)
                    break
                else:                        # if input is not contained in list, question will loop.
                    city1 = True

            if city1 != True:               #if city1 met conditions and broke from loop, it would be no longer "True" and city 2 can be asked.
                while True:
                    print()
                    print ("Choose from", codes)
                    city2 = input("Enter second airport code: " )
                    if city2 in codes:
                        #table.append(city2), destination.append(city2)
                        if city2 not in destination:
                            destination.append(city2)
                        break
                    else:
                        city2 = True

            ##asking if result to be picked from list or dictionary.
            while True:
                ask_user_list_or_dictionary = str.lower(input("From list or dictionary?: " ))
                if ask_user_list_or_dictionary in "list":
                    getDistanceList (codes,city1,city2, lats, longs)
                    distance_airports_from_list = getDistanceList (codes,city1,city2, lats, longs)
                    #table.append(distance_airports_from_list), distance.append(distance_airports_from_list)
                    distance.append(distance_airports_from_list)
                    break
                elif ask_user_list_or_dictionary in "dictionary":
                    getDistanceDictionary (airports,city1,city2)
                    table.append(getDistanceList (codes,city1,city2, lats, longs)), distance.append(getDistanceList (codes,city1,city2, lats, longs))
                    break
                else:
                    ask_user_list_or_dictionary = True
                    print ("Please enter either 'list' or 'dictionary' or 'dic' when prompted")

            if (city1, city2) not in table:
                table.append(city1)
                table.append(city2)
                table.append(getDistanceList (codes,city1,city2, lats, longs))

            print ("combined table that merges all into one = " , table)
            print ("origin: ", origin , "destination: ", destination, "distance: ", distance)


    else:
        print()
        print("Here is a default list of distances")

        ## here we assingning lat1 as the first position of the list it is being called from. i.e the place the loop is currently at [i], it will take from that position in list
        for i in range (0, len(codes)):
            lat1 = lats[i]
            long1 = longs [i]
            print()
            print("Distances calculated from ", codes[i], "airport: ")

            ##this loop is nested so as for every iteration of the parent loop, this will be interated from 0 to len(code) length of code
            for k in range (0, len(codes)):
                #if str(codes[k]) == str(codes [i]):  ## attempt to solve 0 distance answers as it measures dub to dub
                    #print ("yes")
                lat2 = lats [k]
                long2 = longs [k]

                default_distance_list = calcDistance(lat1,lat2,long1,long2)
                print ("The distance between", codes[i], "&", codes [k], "is", default_distance_list)



main()



