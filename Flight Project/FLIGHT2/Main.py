from FLIGHT2.Currencies import *
from FLIGHT2.AirportAtlas import *
from FLIGHT2.buildItinerary import *
from FLIGHT2.Airport import *
from FLIGHT2.Aircraft import *
from FLIGHT2.Itinerary import *
from FLIGHT2.GUI import *

from tkinter import *
clicks = 0
nightmode = 1



def menu():
    print("A == Airport Details")
    print("C == Calculate Cheapest Route from Itineraries in CSV")
    print("I == Input 5 custom Airports + Aircraft to calculate Cheapest Route")
    print("M == Find what currency a Country is using")
    print("P == Airplane Details")
    print()
    print("Q == Quit")

    while True:
        menuChoice = str.upper(input("Enter letter for menu choice: "))
        if len(menuChoice)<1 or  len(menuChoice)>1:
            print ("Choice must be 1 letter")
        elif not menuChoice.isalpha():
            print ("valid letters only")
        elif not menuChoice in "ACIMPQ":
            print ("please choose one from menu list")
        elif menuChoice in "ACIMPQ":
            return menuChoice

def main():
    #### instanciating relevant classes
    myAircraft = Aircraft()
    myAtlas = AirportAtlas()
    myCurrencyAtlas = CountryCurrencyAtlas()
    myItinerary = BuildItinerary(myAtlas, myCurrencyAtlas, myAircraft)

    ####################################################################################################################################################################################

    RUN_UI_loopControl = True               #Main control loop for the UI. If user chooses to quit, "return = False" will end this.
    while RUN_UI_loopControl:
        menuChoice = menu()     #To get user's choice, we call menu() function. This returns user's menuChoice.

        if menuChoice == "Q":   #To Quit
            print("Goodbye, have a nice day")
            return False

        #### #### Airport Details
        if menuChoice == "A" :
            loop_A = True           #Airport loop. Set to False to break loop.
            while loop_A:           #loops until satisfactory input attained
                    airportChoice = str.upper(input("choose Airport "))
                    if len(airportChoice)<3 or len(airportChoice)>3:      #ensures input conforms code naming standard
                        print ("Choice must be 3 digits long. ")
                    elif not airportChoice in myAtlas.airportDic:           #Confirms code in AirportDictionary
                        print ("Invalid Airport.... Try again. ")
                    elif airportChoice in myAtlas.airportDic:               #If it is, details are returned
                        port = myAtlas.getAirport(airportChoice)
                        print("Chosen Airport: {} {} {} {}".format(port.airportName, port.country,
                                                                   port.latitude, port.longitude,))
                        ReturnQuit_loopControl = True                       #enters loop to query if to return to menu or quit.
                        while ReturnQuit_loopControl == True:               #loops until satisfactory input attained
                            returnOrQuit = str.upper(input("(R) = Return to Menu.   (Q) = Quit "))
                            if len(returnOrQuit)<1 or len(returnOrQuit)>1:
                                print ("Choice must be 1 letter")
                            elif not returnOrQuit in "RQ":
                                print ("please choose one from menu list")
                            elif returnOrQuit == "R":
                                print("Returning to Menu!")
                                # returnOrQuit = menu()
                                ReturnQuit_loopControl = False         #breaks loop querying if to return to menu or quit
                                loop_A = False             # breaks Airport loop and breaks the
                            elif returnOrQuit == "Q":
                                print("Goodbye!")
                                return False

        #### #### Calculate cheapest route
        if menuChoice == "C":
            loop_C = True
            while loop_C:

                CSVin_loopControl = True
                while CSVin_loopControl:  #loop until satisfactory input achieved.
                    CustomCSV_in = str(input("Please name of .csv file of itineraries you wish to use -- ENDING with .csv "))
                    if len(CustomCSV_in)<5:     #5 covers the .csv + 1 letter required for name.
                        print ("Filename must be atleast 1 letter with .CSV ending.")
                    elif not ".csv" in CustomCSV_in:
                        print ("Filename must be atleast 1 letter with .CSV ending.")

                    else:
                        CSVin_loopControl = False

                CSVout_loopControl = True
                while CSVout_loopControl:
                    CustomCSV_out = str(input("Please type .csv file you wish to write to (.csv included) "))
                    if len(CustomCSV_out)<5:     #5 covers the .csv + 1 letter required for name.
                        print ("Filename must be atleast 1 letter with .CSV ending.")
                    elif not ".csv" in CustomCSV_out:
                        print ("Filename must be atleast 1 letter with .CSV ending.")
                    else:

                        custom_cheapest_route = BuildItinerary(myAtlas, myCurrencyAtlas, myAircraft, CustomCSV_in, CustomCSV_out)
                        CSVout_loopControl = False

                    ReturnQuit_loopControl = True
                    while ReturnQuit_loopControl == True:
                        returnOrQuit = str.upper(input("(R) = Return to Menu.   (Q) = Quit "))
                        if len(returnOrQuit)<1 or len(returnOrQuit)>1:
                            print ("Choice must be 1 letter")
                        elif not returnOrQuit in "RQ":
                            print ("please choose one from menu list")
                        elif returnOrQuit == "R":
                            print("Returning to Menu!")
                            ReturnQuit_loopControl = False
                            loop_C = False  ### change to loop  = false

                        elif returnOrQuit == "Q":
                            print("Goodbye!")
                            RUN_UI_loopControl == False
                            return False

        #### #### Input custom itinerary
        if menuChoice == "I" :
            loop_D = True
            while loop_D:
                # customRoute = ["SNN","ORK","MAN","CDG","SIN"]
                customRoute=[] #appends the user's chosen airports
                customItinerary = [] #appending each itinerary (made of routes objects and aircraft object)
                customItineraryList = [] #appends customItinerary to a list, as the method for caluclating  shortest
                                        # distance will iterate through a list
                for i in range (0, 5):      # 5 airports + the first repeated.
                    userAirport_loopControl = True
                    while userAirport_loopControl:
                        ##If statments allow active string printing when requesting input.
                        if i == 0:
                            whatUserIsEntering = "home airport: "
                        elif i == 1:
                            whatUserIsEntering = "2nd airport: "
                        elif i == 2:
                            whatUserIsEntering = "3rd airport: "
                        elif i == 3:
                            whatUserIsEntering = "4th airport: "
                        elif i == 4:
                            whatUserIsEntering = "5th airport: "

                        userAirport_i_input= str.upper(input("Choose " + str(whatUserIsEntering)))
                        userAirport_input = userAirport_i_input
                        if userAirport_input not in myAtlas.airportDic:
                            print ("Invalid Airport.... Try again")
                        else:
                            # customRoute.append(myAtlas.getAirport(userAirport_input))
                            customRoute.append(userAirport_input)
                            # print(customRoute)
                            userAirport_loopControl = False

                userAircraft_loopControl = True
                print ("List of available Aircrafts:\n"
                       "Airbus = A319, A320, A321, A330, \n"
                       "Boeing = 737, 747, 757, 767, 777, \n"
                       "Other  = BAE1, DC8, F50, MD11, A400M, C212, V22")
                while userAircraft_loopControl:
                    userAircraft_input= str.upper(input("Choose aircraft: " ))
                    if userAircraft_input not in myAircraft.aircraftDic:
                        print ("Invalid Aircraft.... Try again")
                    else:
                        userAircraft_loopControl = False

                    try:
                        customAircraft = userAircraft_input
                        #creating airport and aircraft objects by passing user input through to Itinerary class
                        customItinerary = Itinerary(customRoute, customAircraft, myAtlas)
                        #appending itinerary to list, to allow iteration wheb calculating cheapetest distance.
                        customItineraryList.append(customItinerary)
                    except KeyError:
                        continue                    #continues with loop if airport code KEY not found

                #permutates custom route
                permutatedCustomItineraryList = myItinerary.permutateItineraryList(customItinerary.routes)
                #calculates cheapest route of all permutations of custom route.
                cheapestCustomRoute = myItinerary.findCheapestDistance(myAtlas, myCurrencyAtlas,
                                                                       permutatedCustomItineraryList, customItineraryList)
                cheapestCustomRouteList = [cheapestCustomRoute]
                exhangeRateRanking_List = myItinerary.rankExchangeRates(myCurrencyAtlas,customItineraryList )
                numberToRanking_List = myItinerary.addNumberToRanking(exhangeRateRanking_List)
                quantityToFuelAtHome_List = myItinerary.efficientFuelingAtHome(myAircraft, myCurrencyAtlas, numberToRanking_List,
                                                                   myAtlas, cheapestCustomRoute, customItineraryList )


                myItinerary.printCheapest(cheapestCustomRouteList, customItineraryList, quantityToFuelAtHome_List)
                ReturnQuit_loopControl = True
                while ReturnQuit_loopControl == True:
                    returnOrQuit = str.upper(input("(R) = Return to Menu.   (Q) = Quit "))
                    if len(returnOrQuit)<1 or len(returnOrQuit)>1:
                        print ("Choice must be 1 letter")
                    elif not returnOrQuit in "RQ":
                        print ("please choose one from menu list")
                    elif returnOrQuit == "R":
                        print("Returning to Menu!")
                        ReturnQuit_loopControl = False
                        loop_D = False
                    elif returnOrQuit == "Q":
                        print("Goodbye!")
                        return False

        #### #### Country currencty details
        if menuChoice == "M" :
            loop_M = True
            while loop_M:
                countryChoice = str.upper(input("Choose country to find it's currency "))
                if len(countryChoice)<3:
                    print ("Choice must be atleast 3 letters long")
                elif countryChoice.isdigit():   #country should be only letters.
                    print ("letters only")
                 #country must be one of the keys to the countryCurrencyDictioanry
                elif not countryChoice in myCurrencyAtlas.countryCurrencyDic:
                    print ("please choose a Country from the list")
                elif countryChoice in myCurrencyAtlas.countryCurrencyDic:
                    currency = (myCurrencyAtlas.getCurrency(countryChoice))
                    print(currency)
                    print("Chosen country: {}  currencyName: {}  toEuro: {}  fromEuro: {}  countryCode: {}"
                                                .format(currency.countryName, currency.currencyName, currency.toEuro,
                                                                              currency.fromEuro, currency.countryCode))

                    ReturnQuit_loopControl = True
                    while ReturnQuit_loopControl == True:
                        returnOrQuit = str.upper(input("(R) = Return to Menu.   (Q) = Quit "))
                        if len(returnOrQuit)<1 or len(returnOrQuit)>1:
                            print ("Choice must be 1 letter")
                        elif not returnOrQuit in "RQ":
                            print ("please choose one from menu list")
                        elif returnOrQuit == "R":
                            print("Returning to Menu!")
                            ReturnQuit_loopControl = False
                            loop_M = False
                        elif returnOrQuit == "Q":
                            print("Goodbye!")
                            return False

        #### #### Aircraft Details
        if menuChoice == "P":
            loop_P = True
            while loop_P:
                aircraftList = ["A319", "A320", "A321", "A330", "737", "747", "757", "767", "777", "BAE1", "DC8",
                                "F50", "MD11", "A400M", "C212", "V22"]
                print ("Please choose from the following:\n"
                       "Airbus = 1.A319, 2.A320, 3.A321, 4.A330, \n"
                       "Boeing = 5.737, 6.747, 7.757, 8.767, 9.777, \n"
                       "Other  = 10.BAE1, 11.DC8, 12.F50, 13.MD11, 14.A400M, 15.C212, 16.V22")
                aircraftChoice = str.upper(input("choose Aircraft "))
                if len(aircraftChoice)<3 or len(aircraftChoice)>5:
                    print ("Choice must be 3-5 long")   ##accounts for all lengths of aircrafts
                elif not aircraftChoice.isalnum():
                    print ("letters/ numbers only")   #allows numbers and letters
                elif not aircraftChoice in aircraftList:
                    print ("please choose Aircraft from the list")
                elif aircraftChoice in aircraftList:
                    craft = (myAircraft.getPlane(aircraftChoice))
                    print("Chosen Plane: {}  Plane Type: {}  Imperial/Metric: {}  Manufacturer: {}  Range: {}"
                                                            .format(craft[0], craft[1], craft[2], craft[3], craft[4]))
                    ReturnQuit_loopControl = True
                    while ReturnQuit_loopControl == True:
                        returnOrQuit = str.upper(input("(R) = Return to Menu.   (Q) = Quit "))
                        if len(returnOrQuit)<1 or len(returnOrQuit)>1:
                            print ("Choice must be 1 letter")
                        elif not returnOrQuit in "RQ":
                            print ("please choose one from menu list")
                        elif returnOrQuit == "R":
                            print("Returning to Menu!")
                            ReturnQuit_loopControl = False
                            loop_P = False
                        elif returnOrQuit == "Q":
                            print("Goodbye!")
                            return False

        # myGUI()



# myGUI = FlightGui
main()