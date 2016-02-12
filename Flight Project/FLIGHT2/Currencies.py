import os
import csv
from FLIGHT2.AirportAtlas import *

class CountryCurrency:
    def __init__(self, countryName, countryCode, currencyCode,toEuro, fromEuro, currencyName): #fromEuro ):
        self.countryName = countryName
        self.countryCode = countryCode
        self.currencyCode = currencyCode
        self.toEuro = toEuro
        self.fromEuro = fromEuro
        self.currencyName = currencyName


    def __str__(self):
        return " countryName: {}, country code: {}, currencyCode: {}, toEuro: {}, fromEuro: {}, currencyName: {}".format\
            (self.countryName, self.countryCode, self.currencyCode, self.toEuro, self.fromEuro, self.currencyName,)

    def __repr__(self):
        return " countryName: {}, country code: {}, currencyCode: {}, toEuro: {}, fromEuro: {}, currencyName: {}".format\
            (self.countryName, self.countryCode, self.currencyCode, self.toEuro, self.fromEuro, self.currencyName,)

class CountryCurrencyAtlas:
    currencyCurrencyList = []

    countryCurrency_fn = "countrycurrency.csv"
    currencyRates_fn = "currencyrates.csv"
    airports_fn = "airport.csv"

    def __init__(self, ratesFile = currencyRates_fn, countryFile = countryCurrency_fn, airportFile = airports_fn):
        self.currencyRatesList = self.readCurrencytoList(ratesFile)
        self.countryCurrencyList = self.readCountiestoList(countryFile)
        self.countryCurrencyDic = self.buildCountryCurrencyAtlasDic()

    def readCurrencytoList(self, filename):   #Reads currency csv to list
        currencyRatesList = []
        try:
            with open(os.path.join(filename),"rt", encoding = "utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    try:
                        currencyRatesList.append([str(line[1]).upper(), float(line[2]), float(line[3]), str(line[0]).upper()])
                    except KeyError:
                        continue
        except (IOError, FileNotFoundError) as errorMessage:
            print (errorMessage)
        return currencyRatesList


    def readCountiestoList(self, filename):         #Reads countrycurrency csv to list
        countryCurrencyList = []
        try:
            with open(os.path.join(filename),"rt", encoding = "utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    if "name" not in line[0]:
                        try:
                            #[0] = country, [3] = ISO3166-1-Alpha-3 , [14] =currency_alphabetic_code
                            countryCurrencyList.append([line[0].upper(), line[3], line[14]])
                        except KeyError:
                            continue
        except (IOError, FileNotFoundError) as errorMessage:   #IOError: #FileNotFoundError
            print (errorMessage)
        return countryCurrencyList

    def buildCountryCurrencyAtlasDic(self): #combines currencyRatesList & countryCurrencyList, returns dictionary of CountryCurrency objects
        countryCurrencyDic = {}
        currencyRatesList = self.currencyRatesList
        countryCurrencyList = self.countryCurrencyList

        for i in currencyRatesList: ##for 5 airport codes in list, build the atlas of objects?
            for k in countryCurrencyList:
                if k[2] == i[0]:
                    countryCurrencyDic[k[0]] = CountryCurrency(k[0], k[1], i[0], i[1], i[2], i[3])

        # for i in countryCurrencyDic.key():
        #     print (i)


        return countryCurrencyDic

    def getCurrency(self, country):                     #takes country name as KEY and returns details of the corresponding Airport object
        while True:
            try:
                self.countryCurrencyDic[country]     ##WATCH OUT FOR UPPER ####
            except KeyError as e:
                print ("Code", e , " is invalid")
                # continue
                #code = (str(input("Please retype 3 letter airport code:").upper()))  ##user inputs are "handled" at the source. does this account for when they are hard passed as paramaters.
            else:
                return self.countryCurrencyDic[country]



def main():
    myAtlas = AirportAtlas()
    myCurrencyAtlas = CountryCurrencyAtlas()
    #myCurrency = CountryCurrency()

    def getMultipleInputCodes():  #complies multiple airports given by user, and puts them in a list "userAirportCodeList"

        user_airport_code_1 = "SSN"
        user_airport_code_2 = "ORD"
        user_airport_code_3 = "LGW"
        userAirportCodeList = [user_airport_code_1, user_airport_code_2, user_airport_code_3]
        return userAirportCodeList


    def getMultipleAirports(inputList):
        airportObjectList = []
        for i in inputList:
            airportObjectList.append(myAtlas.getAirport(i))
        # for h in airportObjectList:
        #     print (str(h))
        return airportObjectList

    def getCurencyForAirport(airportObjectList): #takes a list of airport objects and finds the corresponding currency information.
        currencyblep = [] # list to store currency results in?

        for airport in airportObjectList:
            countrykey = airport.country.upper()
            currencyInformation = (myCurrencyAtlas.getCurrency(countrykey))
            print("for", airport.airportName, "conversion rate for 1 ",currencyInformation.currencyName, "to euro is €", currencyInformation.toEuro, )



    userCodeList = getMultipleInputCodes()
    airportObjectList = getMultipleAirports(userCodeList)

    getCurencyForAirport(airportObjectList)



if __name__ == "__main__":
    main()
