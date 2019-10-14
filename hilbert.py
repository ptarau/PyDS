"""
more turtle demos at:

https://svn.python.org/projects/python/trunk/Demo/turtle/

This program draws a hilbert curve

The Hilbert class and the fractal-curve-
methods are taken from the PythonCard example
scripts for turtle-graphics.
"""
from turtle import *
from time import sleep, clock

class Hilbert(Pen):
    # example derived from
    # Turtle Geometry: The Computer as a Medium for Exploring Mathematics
    # by Harold Abelson and Andrea diSessa
    # p. 96-98
    def hilbert(self, size, level, parity):
        if level == 0:
            return
        # rotate and draw first subcurve with opposite parity to big curve
        self.left(parity * 90)
        self.hilbert(size, level - 1, -parity)
        # interface to and draw second subcurve with same parity as big curve
        self.forward(size)
        self.right(parity * 90)
        self.hilbert(size, level - 1, parity)
        # third subcurve
        self.forward(size)
        self.hilbert(size, level - 1, parity)
        # fourth subcurve
        self.right(parity * 90)
        self.forward(size)
        self.hilbert(size, level - 1, -parity)
        # a final turn is needed to make the turtle
        # end up facing outward from the large square
        self.left(parity * 90)

def main():
    pen = Hilbert()

    pen.reset()
    pen.speed(0)
    pen.ht()
    pen.pu() #up

    size = 20
    pen.setpos(-size*size, -size*size)
    pen.pd() #down
    
    pen.hilbert(size, 4, 1)

    return "done"

if __name__  == '__main__':
    msg = main()
    print(msg)
    mainloop()
