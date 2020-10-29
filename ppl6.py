# import turtle library
import turtle
arrow = turtle.Turtle()

class shapes:
    def __init__(self,name):
        self.name = name
        print("Shape of {} is".format(self.name))

class circle():

    def display(self):
        turtle.speed(5)
        for i in range(1):
            turtle.circle(150)


class star():
    def display(self):
        for i in range(10):
            arrow.forward(100)
            arrow.right(200)

class square():
    def display(self):
        for i in range(4):
            arrow.forward(200)
            arrow.right(90)

class hexagon():
    def display(self):
        my_num_sides = 6
        my_side_length = 100
        my_angle = 360.0 \
                   / my_num_sides
        for i in range(my_num_sides):
            arrow.forward(my_side_length)
            arrow.right(my_angle)
class tringle():
    def display(self):
        for i in range(1):


           arrow.forward(100)  # draw base

           arrow.left(120)
           arrow.forward(100)

           arrow.left(120)
           arrow.forward(100)


class rightangletriangle():
    def display(self):
       arrow.forward(100) # draw base
        
       arrow.left(90)
       arrow.forward(100)
        
       arrow.left(135)
       arrow.forward(142)





if __name__ == "__main__":
    while(1):

        print("a.square")
        print("b.cicle")
        print("c.star")
        print("d.triangle")
        print("e.hexagon")
        print("f.right angle triangle")
        print("enter the choice")
        ch = input()
        if(ch == 'a'):
            d = square()
            print(d.display())
            turtle.done()

        elif(ch=='b'):
            d = circle()
            print(d.display())
            turtle.done()


        elif (ch == 'c'):
            d = star()
            print(d.display())
            turtle.done()


        elif (ch == 'd'):
            d = tringle()
            print(d.display())
            turtle.done()


        elif (ch == 'e'):
            d = hexagon()
            print(d.display())
            turtle.done()


        elif (ch == 'f'):
            d = rightangletriangle()
            print(d.display())
            turtle.done()

        else:
            turtle.bgcolor("blue")




