import tkinter
from Currencies import *
from AirportAtlas import *
from buildItinerary import *
from Airport import *
from Aircraft import *
from Itinerary import *

# from FLIGHT.MAINFLIGHT import *


class FlightGui:

    def __init__(self, frame): #master refers to mainGUI
        self.frame = frame
        frame.title("flight sim")
        frame.geometry("800x800")


        myAircraft = Aircraft()
        myAtlas = AirportAtlas()
        myCurrencyAtlas = CountryCurrencyAtlas()
        self.myItinerary = BuildItinerary(myAtlas, myCurrencyAtlas)


        # self.cheapestDist = self.myItinerary..........cheqapest()

        self.cheapestDist_Label_Text = StringVar()
        self.cheapestDist_Label_Text.set(self.cheapestDist)
        self.cheapestDist_Label = Label(frame, textvariable= self.cheapestDist_Label_Text)

        frame = Tk()

        # window.wm_iconbitmap('eoinlogo.ico') ##single quotes?

        frame.pack()

        self.printButton = Button(frame, text = "print message", command=self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quiteButton = Button(frame, text = "Quit", command = frame.quit)
        self.quiteButton.pack(side = LEFT)

        self.printscreen = Label(frame, text= "to print here")
        self.printscreen.pack(side = LEFT)




        picture = PhotoImage(file = "giphy.gif") #must be giff or pgm/ppm unless imaging library used.
        self.pic = Label(frame, image = picture)
        self.pic.grid(row=0)

        self.label1 = Label(frame, text="please enter... below")
        self.label1.grid(row=1,column=2)

        self.entry1 = Entry(frame)
        self.entry1.grid(row=1, column=3)

        self.button1 =Button(frame, text="click button for", fg = "red",  command=callback)
        self.button1.grid(row=2)


        self.clickMeCounter =Button(frame, text="click counter", fg = "blue", command=countClick)
        self.clickMeCounter.grid(row=3)#(side=LEFT)


        self.nightmodeButton = Button(frame, text="---Click for Nightmode---", command=nightMode)
        self.nightmodeButton.grid(row=4)#(side=RIGHT)


        self.printscreen = Label(frame, text="show here")
        self.printscreen.grid(row=5)


        self.checkbox1 = Checkbutton(frame, text = "Do you want.....")
        self.checkbox1.grid(row=6, columnspan = 2)

        self.TESTINGbutton = Button(frame, text = "TESTING")
        self.TESTINGbutton.bind("<Button-1>", frame)
        self.TESTINGbutton.grid(row=8, column=3)

        self.airport1_label = Label(frame, text="please enter home airport")
        self.airport2_label = Label(frame, text="please enter 2nd airport")
        self.airport3_label = Label(frame, text="please enter 3rd airport")
        self.airport4_label = Label(frame, text="please enter 4th airport")
        self.airport5_label = Label(frame, text="please enter 5th airport")
        self.airplane_label = Label(frame, text="please enter aircraft")
        self.airport1_entry = Entry(frame)
        self.airport2_entry = Entry(frame)
        self.airport3_entry = Entry(frame)
        self.airport4_entry = Entry(frame)
        self.airport5_entry = Entry(frame)
        self.airplane_entry = Entry(frame)

        self.airport1_label.grid(row=15, sticky=E)
        self.airport2_label.grid(row=16, sticky=E)
        self.airport3_label.grid(row=17, sticky=E)
        self.airport4_label.grid(row=18, sticky=E)
        self.airport5_label.grid(row=19, sticky=E)
        self.airplane_label.grid(row=20, sticky=E)
        self.airport1_entry.grid(row=15, column=1)
        self.airport2_entry.grid(row=16, column=1)
        self.airport3_entry.grid(row=17, column=1)
        self.airport4_entry.grid(row=18, column=1)
        self.airport5_entry.grid(row=19, column=1)
        self.airplane_entry.grid(row=20, column=1)


        counter = 0
        for i in options:
            # counter = 0
            button2 = Button(frame, text="click for " + i, command = lambda buttonTitle=i: callback(buttonTitle))
            # button2.pack(side=tkinter.LEFT)
            button2.grid(row = (9+counter))#(fill=X)
            counter +=1



    def printMessage(self,):
        # b=1
        # print("button clicked")
        # printscreen.configure(text= "!!TESTING!!")
        print("this worked")
        # cheapestRoute = self.myItinerary.printCheapest()
    #     self.printscreen.configure(text=(self.myItinerary.printCheapest()))#FFFFFF
    # frame = Tk()
    # myGUI = FlightGui(frame)
    # launchGUI()
    # frame.mainloop()
def launchGUI():
        frame = Tk()
        myGUI = FlightGui(frame)
        frame.mainloop()

def main():
    frame = Tk()
    myGUI = FlightGui(frame)
    # launchGUI()
    frame.mainloop()


