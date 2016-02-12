from FLIGHT2.Aircraft import *
from FLIGHT2.AirportAtlas import *

class Itinerary:
    def __init__(self, routes, aircraft, atlas):
        #takes a list of strings from constructItineraryList() method in "BuildItinerary" class.
        #makes variable route consisting of a list of airport objects made by using getAirport method.
        #Adds on home airport to end.
        self.routes = [atlas.getAirport(routes[0]), atlas.getAirport(routes[1]),atlas.getAirport(routes[2]),
                       atlas.getAirport(routes[3]), atlas.getAirport(routes[4]),atlas.getAirport(routes[0])]
        #makes an aircraft object
        self.aircraft = Aircraft(aircraft)

    def printRoutes(self):
        printroutes = ""
        for i in self.routes:
            printroutes += str(i)
        return printroutes

    def __repr__(self):
        printroutes = ""
        for i in self.routes:
            printroutes += str(i)
        printroutes += str(self.aircraft)
        return printroutes


def main():
    myRoute = Itinerary()

if __name__ == "__main__":
    main()
