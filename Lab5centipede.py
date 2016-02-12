#centipede.py lab 5

from turtle import *

def centipede (length, step, life):  ##length definesgth that snake can reach//step is how many places it jumps // life how long until it dies, how many steps it takes
    penup()      #draws depending on if up or down
    theta = 0 #turn value 1? more left?
    dtheta = 1   #turn value 2? more right?
    for i in range (life):      ## as long as it 'lives'
        forward(step)           ## move forward set amount
        left(theta)             ##turn left by set angle
        theta += dtheta         ## increase turn angle by 1 (as defined by dtheta)
        stamp()                 #leave a print??
        if i > length:          #if its body length surpasses it's life limit??
            clearstamps(1)      #remove 'tail' imprint that was made by speciified amount?  ##(NUMBER) is rate at which tail is deleted
        if theta >  15 or theta < -10:      #if the first defined turn angle (theta) becomes greater than range defined (too much turn??)
                dtheta = -dtheta            # reduce second turn value (dtheta) (so as to reduce the extremity of turn..to balance out?) and start moving the other way
        if ycor() > 350:                    #the height in the world the obeject is allowed to hit.. the height or wall
            left(30)

def main():
    setworldcoordinates (-400,-400,400,400)
    centipede (80,8,600)
    exitonclick()

main()