import os
import csv
#A319, A320, A321, A330, 737, 747, 757, 767, 777, BAE1, DC8, F50, MD11, A400M, C212, V22
class Aircraft:
    __fuel = 0 # private attribute containing current fuel in aircraft
    __fuelCheck = False # this is a Boolean flag for a pre-flight
    MIN_FUEL = 1000 # minimum amount of fuel for takeoff
    __flightClearance = False
    __flightNumber = ""


    aircraftDic = {}
    def __init__(self, planeCode = '747'): ##watch the default
        self.planeCode = planeCode

        if len(self.aircraftDic) == 0:
            self.buildPlaneDic("aircraft.csv")
        self.buildPlaneFromDic(planeCode)

    def __repr__(self):
        return "{} with range: {}".format(self.planeCode, self.planeRange)

    def buildPlaneDic(self, filename):
        try:
            with open(os.path.join(filename),"rt", encoding = "utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    try:                                                #key:value, where value is object 'Airport'
                        self.aircraftDic[line[0]] = line[0],line[1],line[2],line[3],int(line[4])
                    except UnicodeEncodeError:
                        continue                                        #continues with loop if airport code KEY not found
        except (IOError, FileNotFoundError) as errorMessage:   #IOError: #FileNotFoundError
            print (errorMessage)

    def buildPlaneFromDic(self, planeCode):
        for key in self.aircraftDic:
            if planeCode == key:
                self.planeCode = self.aircraftDic[key][0]
                self.planeType = self.aircraftDic[key][1] #jet etc
                self.planeUnits = self.aircraftDic[key][2] #metric
                self.planeManufacturer = self.aircraftDic[key][3] #airbus
                if self.planeUnits == "imperial":
                    self.planeRange = (self.aircraftDic[key][4] * 1.60934)
                else:
                    self.planeRange = (self.aircraftDic[key][4])

    def getPlane(self, airplanecode):
        while True:
            try:
                #self.airportDic[code.upper()]  ######should be upper, changed for testing
                self.aircraftDic[airplanecode.upper()]
            except KeyError as e:
                print ("Code", e , "is invalid")
                # code = (str(input("Please retype 3 letter airport code:").upper()))  ##user inputs are "handled" at the source. does this account for when they are hard passed as paramaters.
            else:
                return self.aircraftDic[airplanecode.upper()]

    def getRange(self, airplanecode):
        while True:
            try:
                #self.airportDic[code.upper()]  ######should be upper, changed for testing
                self.aircraftDic[airplanecode]
            except KeyError as e:
                print ("Code", e , "is invalid")
                # code = (str(input("Please retype 3 letter airport code:").upper()))  ##user inputs are "handled" at the source. does this account for when they are hard passed as paramaters.
            else:
                return self.aircraftDic[airplanecode.upper()].range


    def fuelCheck(self):  #checks planes fuel, changes variable only when above min.
        if self.__fuel <self.MIN_FUEL:
            print ("Fuel Check Failed: Current fuel below safe limit:", self.__fuel, " less than ", self.MIN_FUEL)
            self.__fuelCheck = False
        else:
            print("Fuel Check Complete. Fuel level is", self.__fuel, "max level is", self.planeRange)
            self.__fuelCheck = True

    def takeOff(self):
        #if self.__fuelCheck == True and self.__flightClearance == True:
        if self.preFlightCheck == True:
            print("Cleared for Takeoff! Fasten your seat-belt!")
            return True
        else:
            print("Take off Failed: Please complete pre-flight check first")
            print("fuel =", self.fuelCheck(), "clearance =", self.__flightClearance)

    def printStatus(self):
        print("Current fuel:", self.__fuel)

    def returnCurrentFuel(self):
        currentFuel = self.__fuel
        return float(currentFuel)

    def addFuel(self, volume):
        unusedFuel = 0
        if volume<0:
            print("No syphoning fuel!")
        elif self.__fuel + volume <= self.planeRange:
            self.__fuel = self.__fuel + volume
        elif self.__fuel + volume > self.planeRange:
            self.__fuel = self.planeRange
            unusedFuel = volume - self.__fuel
        return unusedFuel



    #     self.fuelCheck()
    #     self.flightClearanceCheck(dublinTower)
    #     if self.__fuelCheck == True and self.__flightClearance == True:
    #         print ("Preflight Check cleared")
    #         self.preFlightCheck = True
    #     else:
    #         print ("Pre flight check failed")
    #         self.preFlightCheck = False

    # def flightClearanceCheck(self, dublinTower):
    #     #if dublinTower.checkFlightNumberAgainstFlightList == True:
    #     if dublinTower.flightclearance == True:
    #         self.__flightClearance = True
    #     #else requetupdate

    # def setFlightNumber(self, aflightNumber): # sets flight number
    #     self.flightNumber = aflightNumber
    # def preFlightCheck (self, dublinTower):  #


def main():
    my737 = Aircraft("737")
    print (my737.planeRange)
    myA320 = Aircraft("A320")
    print (myA320.planeRange)

if __name__ == "__main__":
    main()