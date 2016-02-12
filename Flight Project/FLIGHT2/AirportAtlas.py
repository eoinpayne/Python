from FLIGHT2.Airport import *
from itertools import *

class AirportAtlas:
    airport_fn = "airport.csv"                                      #assigning CSV file in directory to variable

    def __init__(self, airport_file = airport_fn):                  #default paramater ='airportfn'
        self.airportDic = self.buildAirportDic(airport_file)        # assigning the return of method as the dictionary

    def buildAirportDic (self, filename):                           #reads a file, and populates dictionary
        airportDic={}

        try:
            with open(os.path.join(filename),"rt", encoding = "utf8") as f:  #opens file as variable "f"
                reader = csv.reader(f)  #assigns the csv.reader for the opened file as variable "reader"
                for line in reader:
                    try:                                                #key:value, where value is object 'Airport'
                        airportDic[line[4]] = Airport(line[0],line[1],line[2].upper(),line[3].upper(),line[4].upper(),line[5],
                                                       float(line[6]),float(line[7]),line[8],line[9],line[10],line[11])
                    except KeyError:
                        raise KeyError                                     #continues with loop if airport code KEY not found ############################
        except (FileNotFoundError, IOError) as e:  #error handling incase file not found.
            print (e)
        return airportDic                       # returns dictionary of all airports, where key is the airport code.

    def getAirport(self, code):                 #takes code as KEY and returns details of Airport object

            try:
                self.airportDic[code]
            except KeyError as e:
                print ("Code", e , "is invalid")
                ##user inputs are "handled" at the source. This is a contingency for special occoasion.
                # code = (str(input("Please retype 3 letter airport code:").upper()))

            else:
                return self.airportDic[code.upper()]

    #uses static methods to calculate distance between 2 airports
    def getDistanceBetweenAirports(self, code1, code2):
            #creating "airport1" object using 'code1' key (this returns the 'value' which is an object
            self.airport1 = self.getAirport(code1)
            self.airport2 = self.getAirport(code2)
            #pulls the latitude attribute from the Airport object.
            lat1 = self.airport1.latitude
            long1 = self.airport1.longitude
            lat2 = self.airport2.latitude
            long2 = self.airport2.longitude
            distance = AirportAtlas.calcDistance(lat1,lat2,long1,long2) #calling static method
            return distance #returns distance in KM between 2 airports

    @staticmethod
    def calcDistance(lat1,lat2, long1, long2):       #takes lats&longs converts to radials, returns distance.
        theta1, theta2, phi1, phi2 = AirportAtlas.definetheta(lat1, lat2, long1, long2)

        distance = (acos(sin(theta1)*sin(theta2)*cos(phi1-phi2)+(cos(theta1)*cos(theta2)))*radius_earth)
        return distance

    @staticmethod
    def definetheta(lat1,lat2, long1, long2):        #converts degrees to radians
        #90 - , as there are 2 pole points on earth, we need to know where our point is in relation to the equator/poles
        theta1 = 90 - lat1
        theta1 = theta1*((2*pi)/360)

        theta2 = 90 - lat2
        theta2 = theta2 * ((2*pi)/360)

        ###convert longitude radiants without 90-, as the equator doesn't have points/poles.
        phi1 = long1 * ((2*pi)/360)
        phi2 = long2 * ((2*pi)/360)
        return theta1, theta2, phi1, phi2

    ##NOT USED AT PRESENT ##
    def buildListOfPairedAirports(self, list):    ###build list, each item in this list is a pair of airports
        pairs = []
        for i in permutations(list, 2):
            pairs.append([i])
        return pairs

    ##NOT USED AT PRESENT ##
    def calcDistancesBetweenAirportPairs(self, pairs): #takes the list of airport pairs, cycles through and calculates the distance between them. Adds to a dictionary?
        distance_dic = {}
        for k in range (0, len(pairs)):
            code1 = pairs[k][0][0]
            code2 =  pairs[k][0][1]
            distance = self.getDistanceBetweenAirports(code1, code2)

    ##NOT USED AT PRESENT ##
    def buildListOfRoutes (self, list):         ###build list, each item in list 'routes' is a possible combination of all airports in list.
        routes = []
        for i in permutations(list):
            routes.append(i)
        print (routes)


def main():
    myAtlas = AirportAtlas()
    print(myAtlas.getAirport("SSN"))

if __name__ == "__main__":
    main()