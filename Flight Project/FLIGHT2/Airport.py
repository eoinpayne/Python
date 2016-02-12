import os
import csv
from math import sin,cos,acos,pi
radius_earth = 6371


class Airport:
    def __init__(self, airportID, airportName, cityName,country, airportCode, icaoCode,latitude, longitude, altitude, timeOffset, dst, tz):

        self.airportID = airportID #0
        self.airportName = airportName #1
        self.cityName = cityName #2
        self.country = country #3
        self.airportCode = airportCode #4
        self.icaoCode = icaoCode #5
        self.latitude = latitude #6 float
        self.longitude = longitude #7 float
        self.altitude = altitude #8
        self.timeOffset = timeOffset #9
        self.dst = dst #10
        self.tz = tz #11

    def __str__(self):
        return " {} (Name: {} {} {} lat: {} long: {})".format\
            (self.airportCode, self.airportName, self.cityName, self. country, self.latitude, self.longitude)

    def __repr__(self):
        return "{}".format(self.airportCode)



