import math

class Shapes():
        class Elipse():
            def area(self):
                return self.aAxis * self.bAxis * math.pi
            def __init__(self,aAxis,bAxis):
                self.aAxis = aAxis
                self.bAxis = bAxis


        class Circle():
            def __init__ (self,radius):
                self.radius = radius

            def area(self):
                return self.radius * self.radius * math.pi

        class Rectangle():
            def area(self):
                return self.longSide *  self.shortSide

            def __init__(self,longSide,shortSide):
                self.longSide = longSide
                self.shortSide = shortSide


circ1 = Shapes.Circle(100)
print("Circle 1 area is: ", circ1.area())

rect1 = Shapes.Rectangle(5,10)
print("Area of the Rectangle is: ", rect1.area())

eclip1= Shapes.Elipse(1,10)
print("Area of the Elipse is ", eclip1.area())
