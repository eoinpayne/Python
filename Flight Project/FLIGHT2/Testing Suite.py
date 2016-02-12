import itertools
import unittest

from FLIGHT2.Currencies import *
from FLIGHT2.AirportAtlas import *
from FLIGHT2.buildItinerary import *
from FLIGHT2.Airport import *
from FLIGHT2.Aircraft import *

class KnownValues (unittest.TestCase):

    def setUp(self):
        self.myAircraft = Aircraft()
        self.myAtlas = AirportAtlas()
        self.myAirport = AirportAtlas()
        self.myCurrencyAtlas = CountryCurrencyAtlas()
        self.myBuilder = BuildItinerary(self.myAtlas, self.myCurrencyAtlas, self.myAircraft)
        self.knownAircraftValues = (("737", 5600, "Boeing", 9012.304), ("A320", 12000, "Airbus", 12000),
                                    ("777", 9700, "Boeing"))  #code, range, maker, rangeKM
        self.testPlane1 = Aircraft("737")
        self.testPlane2 = Aircraft("A320")
        self.testPlane3 = Aircraft("777")

        ############### Test Cheapest Fuel Rate ############
        self.knownCurrencyDetails = (("DUB to Euro = ", 1, "country =", "IRELAND"),
                                     ("GBP to Euro = ", 1.4029, "country =", "UNITED KINGDOM"))

        self.knownDistances = (("DUB to LHR KM= ", 448.8922295538067), ("SYD to JFK KM= ", 16013.523728949884), ("DUB to DUB KM= ", 0))

        self.myCurrency = CountryCurrencyAtlas()
        self.testAirportCurrencyDUB = self.myCurrency.getCurrency(self.myAirport.airportDic["DUB"].country.upper())
        self.testAirportCurrencyLHR = self.myCurrency.getCurrency(self.myAirport.airportDic["LHR"].country.upper())
        ########### Test Distances ##########
        self.testAirportDUB = self.myAirport.airportDic["DUB"]
        self.testAirportLHR = self.myAirport.airportDic["LHR"]
        self.testAirportSYD = self.myAirport.airportDic["SYD"]
        self.testAirportJFK = self.myAirport.airportDic["JFK"]
        # self.testAirportINVALID = self.myAirport.airportDic["lll"]
        # self.testAirportINVALID = self.myAirport.airportDic["123"]
        # self.testAirportINVALID = self.myAirport.airportDic["12"]
        # self.testAirportINVALID = self.myAirport.airportDic["ll"]

        # ############### Test Cheapest Fuel Rate ############
        # self.knownFuelRates = ((), ())
        # self.testRoute1 = self.myBuilder.itineraryList[0]
        # self.testRoute3 = self.myBuilder.itineraryList[2]


        ########### Test Permutation number ##########
        self.testAirportCodes = ["DUB", "MAN", "ORD", "PPP", "ORK"]


    def test_results_of_aircraft(self):
        Aircraft1_range = self.testPlane1.planeRange  #tests converted to KM also
        Aircraft1_manufacturer = self.testPlane1.planeManufacturer
        Aircraft2_range = self.testPlane2.planeRange
        Aircraft2_manufacturer = self.testPlane2.planeManufacturer
        ## the result of the test method "Aircraft1_range" should == the known value tuple position
        self.assertEqual(self.knownAircraftValues[0][3], Aircraft1_range)
        self.assertEqual(self.knownAircraftValues[0][2], Aircraft1_manufacturer)
        ## the result of the test method "Aircraft1_range" should == the known value tuple position
        self.assertEqual(self.knownAircraftValues[1][3], Aircraft2_range)
        self.assertEqual(self.knownAircraftValues[1][2], Aircraft2_manufacturer)

    def test_currency_details(self):
        DUB_currency_test_toEuro = self.testAirportCurrencyDUB.toEuro
        DUB_currency_test_country = self.testAirportCurrencyDUB.countryName
        LHR_currency_test_toEuro = self.testAirportCurrencyLHR.toEuro
        LHR_currency_test_country = self.testAirportCurrencyLHR.countryName
        self.assertEqual(self.knownCurrencyDetails[0][1], DUB_currency_test_toEuro)
        self.assertEqual(self.knownCurrencyDetails[0][3], DUB_currency_test_country)
        self.assertEqual(self.knownCurrencyDetails[1][1], LHR_currency_test_toEuro)
        self.assertEqual(self.knownCurrencyDetails[1][3], LHR_currency_test_country)

    def test_distance_of_airports(self):
        Airport_distance_LHR_DUB = self.myAtlas.getDistanceBetweenAirports(self.testAirportDUB.airportCode, self.testAirportLHR.airportCode)
        Airport_distance_SYD_JFK = self.myAtlas.getDistanceBetweenAirports(self.testAirportSYD.airportCode, self.testAirportJFK.airportCode)
        Airport_distance_DUB_DUB = self.myAtlas.getDistanceBetweenAirports(self.testAirportDUB.airportCode, self.testAirportDUB.airportCode)
        # Airport_distance_DUB_INVALID = self.myAtlas.getDistanceBetweenAirports(self.testAirportDUB.airportCode, self.testAirportINVALID.airportCode)
        self.assertEqual(self.knownDistances[0][1], Airport_distance_LHR_DUB)
        self.assertEqual(self.knownDistances[1][1], Airport_distance_SYD_JFK)
        self.assertEqual(self.knownDistances[2][1], Airport_distance_DUB_DUB)
        self.assertEqual(self.knownDistances[2][1], Airport_distance_DUB_DUB)


    def test_missing_input_file(self):            ##Commented out as designed to fail, which it does.
        ### tests invalid file to FileNotFoundError
        self.assertRaises(FileNotFoundError, self.myAtlas.buildAirportDic, "cookie.csv")

    def test_permutation_number(self):
        Code_Permutation_Tester = self.myBuilder.permutateItineraryList(self.testAirportCodes)
        self.assertEqual(len(Code_Permutation_Tester), 24)

        ########     System Test    #########
    def test_airport_correct_currency(self):
        Test_Airport_Currency_DUB_EURO = self.myCurrencyAtlas.getCurrency(self.myAtlas.getAirport("DUB").country).currencyName
        Test_Airport_Currency_DUB_RATE = self.myCurrencyAtlas.getCurrency(self.myAtlas.getAirport("DUB").country).toEuro
        Test_Airport_Currency_LHR_EURO = self.myCurrencyAtlas.getCurrency(self.myAtlas.getAirport("LHR").country).currencyName
        Test_Airport_Currency_LHR_RATE = self.myCurrencyAtlas.getCurrency(self.myAtlas.getAirport("LHR").country).toEuro
        # Test_Airport_Currency_DUB_EURO = self.myCurrencyAtlas.getCurrency(self.testAirportDUB.country()).currencyName
        # Test_Airport_Currency_DUB_RATE = self.myCurrencyAtlas.getCurrency(self.testAirportDUB.country()).toEuro
        # Test_Airport_Currency_LHR_EURO = self.myCurrencyAtlas.getCurrency(self.testAirportLHR.country()).currencyName
        # Test_Airport_Currency_LHR_RATE = self.myCurrencyAtlas.getCurrency(self.testAirportLHR.country()).toEuro

        self.assertEquals = (Test_Airport_Currency_DUB_EURO, "Euro")
        self.assertEquals = (Test_Airport_Currency_DUB_RATE, 1)
        self.assertEquals = (Test_Airport_Currency_LHR_EURO, "British Pound")
        self.assertEquals = (Test_Airport_Currency_LHR_RATE, 1.4029)




if __name__ == "__main__":
    # myAircraft =AirplaneBuilder()
    unittest.main()
