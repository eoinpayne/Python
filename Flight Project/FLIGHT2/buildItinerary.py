import os
import csv
import itertools
from operator import itemgetter, attrgetter

from FLIGHT2.Itinerary import *
from FLIGHT2.AirportAtlas import *
from FLIGHT2.Currencies import *
from FLIGHT2.Airport import *

class BuildItinerary:
    testroutes_fn = "testroutes.csv"             #assigning CSV files in directory to variable to use as defaults
    output_fn = "eoinoutput.csv"

    # upon creation, Instantiated AirportAtlas and CountryCurrencyAtlas will be passed through.
    def __init__(self, AirportAtlas, CountryCurrencyAtlas, Aircraft, routes_filename = testroutes_fn, output_filename = output_fn):

    #to create itineray list, constructItineraryList() is called passing through Instantiated Airport Atlas & .CSV
    #self.itineraryList = list of itineraryies from input csv file (i.e 4 rows from testroutes.csv), consisting
    # of aircraft object, and routes (which is made up of airport objects (ie Dub -> Dub)
        self.itineraryList = self.constructItineraryList(AirportAtlas, routes_filename)
        # self.permutatedItinerary_withRepeat = self.permutateItineraryList_withRepeat(self.itineraryList)

    # # orders exhange rate from low to high, numbers them accordingly
        self.exhangeRateRanking_List = self.rankExchangeRates(CountryCurrencyAtlas, self.itineraryList)
        self.numberToRanking_List = self.addNumberToRanking(self.exhangeRateRanking_List)

    #finds the cheapest permutation of routes
        self.cheapestRouteList = self.findBestRouteForEachItinerary(self.itineraryList, AirportAtlas, CountryCurrencyAtlas)

    # # compares exhange rate ranking to calculate how much fuel to be purchased at home.
        self.quantityToFuelAtHome_List = self.efficientFuelingAtHome(Aircraft, CountryCurrencyAtlas,
                                self.numberToRanking_List, AirportAtlas, self.cheapestRouteList, self.itineraryList )

    #formatted output. works with custom user itinerary defined in UI.
        self.printCheapest(self.cheapestRouteList, self.itineraryList, self.quantityToFuelAtHome_List)

    #wrtites cheapest list to csv file. This can be determined by the user in the UI.
        self.writeCheapestRoutestoCSV(output_filename)

    def __repr__(self):
        printItineraryList = ""
        for i in self.itineraryList:
            printItineraryList += str(i)
        return printItineraryList

    # # Takes CSV as input file and imports data to a list  of Itinerary Objects
    def constructItineraryList (self, atlas, filename):
        itineraryList = []
        try:
            with open(os.path.join(filename),"rt", encoding = "utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    try:                                                #key:value, where value is object 'Airport'
                        routes = [line[0], line[1], line[2], line[3], line[4]]  #each leg of journey. airportCodes.
                        aircraft = line[5]
                        itinerary = Itinerary(routes, aircraft, atlas)
                        itineraryList.append(itinerary)
                    except KeyError:
                        continue                                        #continues with loop if airport code KEY not found
        except (IOError, FileNotFoundError, ) as errorMessage:   #IOError: #FileNotFoundError
            print (errorMessage)
        return itineraryList

    # # Some Jazz -- ranking each airport by their exhange rates.
    # # find the toEuro rate of each leg of a journey, and sorts them by their rate.
    def rankExchangeRates(self, CountryCurrencyAtlas, itineraryList):
        exhangeRateRanking_List=[]
        for itinerary in itineraryList:
            temp_exhangeRateRanking_List = []     #temporary list to allow distinction between itineraries in main list.
            for route in itinerary.routes:      # breaking down to individual airports of itinerary to extract rate.
                rate = CountryCurrencyAtlas.getCurrency(route.country.upper()).toEuro
                temp_exhangeRateRanking_List.append((route, rate))
            # # using operator , itemgetter to append a sorted list of tuples bases on 2nd value
            exhangeRateRanking_List.append(sorted(temp_exhangeRateRanking_List,key=itemgetter(1))) #
        return exhangeRateRanking_List

    # #takes the ordered list of exhange rates and appends numbers to them.
    def addNumberToRanking(self, exhangeRateRanking_List):
        numberToRanking_List=[]
        for route in exhangeRateRanking_List:
            temp_numberToRanking_List = []
            # # To associate ranking with airport and exchange rate, a counter is kept for the leg of the route. This
            # number is added to the tuple that contains airport and exhange rate and appended to a temporary list.
            legCount = 0
            for leg in route:
                leg += (legCount,)
                legCount += 1
                temp_numberToRanking_List.append(leg)
            numberToRanking_List.append(temp_numberToRanking_List)
        return numberToRanking_List

    # # takes multiple itineraries, returns cheapest route for each one.
    def findBestRouteForEachItinerary(self, itineraryList, AirportAtlas, CountryCurrencyAtlas):
        cheapestRouteList = []
        cheapestRouteList_withRepeat = []
        self.newplaneCounter = 0
        # self.fuelRankingList_PositionCounter = 0
        for itinerary in itineraryList:
            permutatedItinerary = self.permutateItineraryList(itinerary.routes)
            permutatedItinerary_withRepeat = self.permutateItineraryList_withRepeat(itinerary.routes)

            cheapRoute = self.findCheapestDistance(AirportAtlas, CountryCurrencyAtlas, permutatedItinerary, itineraryList)
            #cheapRoute_withRepeat = self.findCheapestDistance(AirportAtlas, CountryCurrencyAtlas, permutatedItinerary_withRepeat, itineraryList)

            cheapestRouteList.append(cheapRoute)
            # cheapestRouteList_withRepeat.append(cheapRoute_withRepeat)
        print(cheapestRouteList)
        # print(cheapestRouteList_withRepeat)
            # self.newplaneCounter +=1##########################################################################################################
        return cheapestRouteList

    # # takes list of routes and permutates possible journeys with start and end remaining the same.
    def permutateItineraryList(self, itineraryRoutes):
            listOfPermutatedMiddleJourneys = []  # (list of tuples) all permutations of journey, without start/end
            permutatedItineraryLists = []       # rebuilt permutations.
            middleSliceOfJourney = itineraryRoutes[1:5]   # slices object for permutation
            for permutation in permutations(middleSliceOfJourney):
                listOfPermutatedMiddleJourneys.append(permutation)
            for middlePermutation in listOfPermutatedMiddleJourneys:            #rebuilds permutations, with start/end
                homeAirport = itineraryRoutes[0]                                 #assiging "home" city
                permutatedList_reubuilt_with_home = [homeAirport]                 #starts list with home airport
                permutatedList_reubuilt_with_home.extend(middlePermutation)        #adds middle list, no longer a tuple
                permutatedList_reubuilt_with_home.append(homeAirport)
                permutatedItineraryLists.append(permutatedList_reubuilt_with_home)
            return permutatedItineraryLists


    def permutateItineraryList_withRepeat(self, itineraryRoutes):
            listOfPermutatedMiddleJourneys_withRepeat = []  # (list of tuples) all permutations of journey, without start/end
            permutatedItineraryLists_withRepeat = []       # rebuilt permutations.
            itinerary_withRepeat = []
            for airport in itineraryRoutes:
                temp_itinerary_withRepeat = []
                temp_itinerary_withRepeat.insert(1,itineraryRoutes[1])
                temp_itinerary_withRepeat.insert(1,itineraryRoutes[2])
                temp_itinerary_withRepeat.insert(1,itineraryRoutes[3])
                temp_itinerary_withRepeat.insert(1,itineraryRoutes[4])
                temp_itinerary_withRepeat.insert(1, str(airport.airportCode))
                itinerary_withRepeat.append(temp_itinerary_withRepeat)

            for permutation in permutations(itinerary_withRepeat):
                listOfPermutatedMiddleJourneys_withRepeat.append(permutation)
            for middlePermutation in listOfPermutatedMiddleJourneys_withRepeat:            #rebuilds permutations, with start/end
                homeAirport = itineraryRoutes[0]                                 #assiging "home" city
                permutatedList_reubuilt_with_home = [homeAirport]                 #starts list with home airport
                permutatedList_reubuilt_with_home.extend(middlePermutation)        #adds middle list, no longer a tuple
                permutatedList_reubuilt_with_home.append(homeAirport)
                permutatedItineraryLists_withRepeat.append(permutatedList_reubuilt_with_home)
            return permutatedItineraryLists_withRepeat

    # # main algorithm to calculate the cheapest possible permutation of each itinerary.
    def findCheapestDistance(self, AirportAtlas, CountryCurrencyAtlas, aPermutatedList, anyitineraryList):
            listoOfCheapestJourneyRoute = []
            ##default error message will be changed unless leg cannot be completed with associated aircraft
            cheapestJourneyRoute= "ERROR: This route can't be achieved with this aircraft"
            cheapestJourneyCost = 100000000000000            #default number set high, so cheaper options can replace.
            for permutationOfRoute in aPermutatedList:    #iterates an input of permutated airports.
                airporta =0
                airportb =1
                costofEachJourney = 0     #combined cost of all legs, from home -> home
                # thiscounter = -1
                currentFuel = 0
                currentFuelPrice = 0
                for airport in range(0, len(aPermutatedList[0])-1):
                    # thiscounter +=1
                    # # staggered incrementation of airports to allow a->b, b->c, c->d etc..
                    airport1 = permutationOfRoute[airporta]
                    airport2 = permutationOfRoute[airportb]
                    # # gets distance between 2 airport objects, using their code attribute as parameters
                    distance = AirportAtlas.getDistanceBetweenAirports(str(airport1.airportCode), str(airport2.airportCode))
                    # # to track associated aircraft, "self.newplaneCounter" increases ecah loop in "findBestRouteForEachItinerary"
                    if distance > anyitineraryList[self.newplaneCounter].aircraft.planeRange:
                        distance = 99999999999999999999

                    currencyAtDestination = CountryCurrencyAtlas.getCurrency(str(airport2.country.upper()))   #passes COUNTRY as paramter to getCurrency method. returns an object

                    costOfFuel = currencyAtDestination.toEuro   # costOfFuel of fuel is conversion rate at destination



                    costOfEachLeg = distance * costOfFuel   ##finds cost of the flight leg to each city.
                    costofEachJourney += costOfEachLeg
                    airporta +=1
                    airportb +=1
                if costofEachJourney < cheapestJourneyCost:
                        cheapestJourneyCost = costofEachJourney
                        cheapestJourneyRoute = permutationOfRoute
                if cheapestJourneyCost == 100000000000000:
                        cheapestJourneyCost = 0
            listoOfCheapestJourneyRoute.append([cheapestJourneyRoute, cheapestJourneyCost])
            return listoOfCheapestJourneyRoute

    # # Jazz (sort of) -- Uses ranking of exhange rate to determine how much fuel to buy when starting off.
    # # given more time, this would evolve to keep track of how much fuel was saved over the whole flight from buying
    # greater amounts of fuel at cheaper locatons and, only what is necessary to continue when more expensive.
    #Returns a list of how many lires of fuel should be bought at begining of Journey.
    def efficientFuelingAtHome(self, Aircraft, CountryCurrencyAtlas, numberToRanking_List, AirportAtlas, cheapestRouteList, itineraryList):
        current_itinerary_counter = -1
        quantityToFuelAtHome_List = []          #stores the relevant values for each itinerary
        for itinerary in cheapestRouteList:  #iterates each of the previously calculated cheapest route.
            current_itinerary_counter +=1
            #Finds min fuel of aircraft associtated with itinerary, by using current_itinerary_counter
            minFuel = itineraryList[current_itinerary_counter].aircraft.MIN_FUEL
            currentAircraftRange = itineraryList[current_itinerary_counter].aircraft.planeRange
            accumulatedFuel = 0                 #for accumulating how many litres of fuel added
            accumulatedFuel_Price = 0            #for accumulating price * fuel
            try:
                firstAirport = itinerary[0][0][0].airportCode
                secondAirport = itinerary[0][0][1].airportCode
                distance = AirportAtlas.getDistanceBetweenAirports(firstAirport, secondAirport)  #find distance

                if distance < currentAircraftRange:
                    accumulatedFuel += minFuel  #default of adding minimum required fuel to fly.
                    accumulatedFuel_Price += minFuel * (CountryCurrencyAtlas.getCurrency(itinerary[0][0][0].country.upper()).toEuro)
                # # Following if statements search for home airport in list with ascending order of currency exhange rate
                # # If airport is ranked lowest, fill plane to capacity
                if itinerary[0][0][0].airportCode == numberToRanking_List[current_itinerary_counter][0][0].airportCode:
                        ToFuel = (float(currentAircraftRange) - (float(accumulatedFuel)))
                        accumulatedFuel += ToFuel
                        # # multiply litres of fuel by the associated exchange rate
                        accumulatedFuel_Price += (ToFuel * numberToRanking_List[current_itinerary_counter][0][1])
                # # If airport is ranked 2nd, fill plane to capacity
                elif itinerary[0][0][0].airportCode == numberToRanking_List[current_itinerary_counter][1][0].airportCode:
                        ToFuel = (float(currentAircraftRange) - (float(accumulatedFuel)))
                        accumulatedFuel += ToFuel
                        accumulatedFuel_Price += (ToFuel * numberToRanking_List[current_itinerary_counter][1][1])
                # # If airport is ranked 3rd, within 40$ of capacity.
                elif itinerary[0][0][0].airportCode == numberToRanking_List[current_itinerary_counter][2][0].airportCode:
                        ToFuel = ((float(currentAircraftRange) - (currentAircraftRange*.40))-(float(accumulatedFuel)))
                        accumulatedFuel += ToFuel
                        accumulatedFuel_Price += ToFuel * numberToRanking_List[current_itinerary_counter][2][1]
                # # Other wise, fill plane only with what is necessary
                else:
                    ToFuel = (distance - (float(accumulatedFuel)))
                    accumulatedFuel += ToFuel
                    accumulatedFuel_Price += ToFuel *(CountryCurrencyAtlas.getCurrency(itinerary[0][0][0].country.upper()).toEuro)
            except AttributeError:             #error handling accoutns for failed itinerarys.
                accumulatedFuel = 0         #0 means lists can be compared to associate correct values for itineraries.
            quantityToFuelAtHome_List.append(accumulatedFuel)  ## Compiles a list of how much fuel starting off.
        return quantityToFuelAtHome_List

    def printItinerary(self):
        for i in self.itineraryList:
            print(i)

    # # prints a formated version of "listoOfCheapestJourneyRoute"
    def printCheapest(self, listoOfCheapestJourneyRoute, itineraryList, quantityToFuelAtHome_List):
        count = 0
        for airport in listoOfCheapestJourneyRoute:
            print ("The original itinerary: {} using a {}KM.  Cheapest route is: {}, costing € {}. Advised to buy {} Litres of fuel at home airport"
                   .format(itineraryList[count].routes,itineraryList[count].aircraft, airport[0][0], airport[0][1], quantityToFuelAtHome_List[count]))
            count+=1

    # # writes results to a CSV
    def writeCheapestRoutestoCSV (self, filename):
        writeCount = 0       # for line in self.listoOfCheapestJourneyRoute:
        try:
            with open(os.path.join(filename),"w", encoding = "utf8", newline='') as f:  #'eggs.csv', 'w', newline='') as csvfile:
                for j in self.itineraryList:
                    writer = csv.writer(f, delimiter=',')
                    toWrite = ("Original Routes",   "Assigned Aircraft",  "Optimum Route", "Litres of fuel to buy at home", "\n")
                    toWrite = (self.itineraryList[writeCount].routes,self.itineraryList[writeCount].aircraft,  self.cheapestRouteList[writeCount],self.quantityToFuelAtHome_List[writeCount], "\n")
                    writer.writerow(toWrite)
                    writeCount+= 1
        except (IOError, FileNotFoundError) as errorMessage:   #IOError: #FileNotFoundError
            print (errorMessage)

def main():
    myAtlas = AirportAtlas()
    myCurrency = CountryCurrencyAtlas()
    myAircraft = Aircraft()
    myItinerary = BuildItinerary(myAtlas, myCurrency, myAircraft)

if __name__ == "__main__":
    main()
