#!/usr/bin/env python3

"""Draw the diagram of the Solar System.

__author__ = "Zhu Qi"
__pkuid__  = "1800011808"
__email__  = "1800011808@pku.edu.cn"
"""

import math as m
import turtle as t


t.bgcolor('black')

Mer=t.Turtle()
Ven=t.Turtle()
Ear=t.Turtle()
Mar=t.Turtle()
Jup=t.Turtle()
Sat=t.Turtle()
Sun=t.Turtle()

Mer.shape("circle")
Ven.shape("circle")
Ear.shape("circle")
Mar.shape("circle")
Jup.shape("circle")
Sat.shape("circle")

Mer.color('#FFFFFF')
Ven.color('#00FF00')
Ear.color('#0000FF')
Mar.color('#FFFF00')
Jup.color('#FF00FF')
Sat.color('#00FFFF')
Sun.color('#FF0000')

Sun.turtlesize(2,2)
Mer.turtlesize(0.5,0.5)
Ven.turtlesize(0.85,0.85)
Ear.turtlesize(1,1)
Mar.turtlesize(0.65,0.65)
Jup.turtlesize(1.7,1.7)
Sat.turtlesize(1.3,1.3)

Mer.width(2)
Ven.width(2)
Ear.width(2)
Mar.width(2)
Jup.width(2)
Sat.width(2)

Mer.speed(0)
Ven.speed(0)
Ear.speed(0)
Mar.speed(0)
Jup.speed(0)
Sat.speed(0)


def ellipse(e,p,tur,ang):
    """Move to a point whose angle with pole and pole axis is "ang" on a ellipse with Eccentricity e and Focal distance p using turtle "tur".
    """
    if ang==0:
        tur.pu()
        tur.goto(e * p / (1 - e), 0)
        tur.pd()
    else:
        r = e * p / (1 - e * m.cos(ang / 100))
        tur.goto(r * m.cos(ang / 100), r * m.sin(ang / 100))


def main():
    """main module
    """
    Sun.shape('circle')
    i=0
    while 1:
        ellipse(0.20563, 200, Mer, 5.68376 * i)
        ellipse(0.0068, 11000, Ven, 4.22519 * i)
        ellipse(0.016710, 7000, Ear, 3.36896 * i)
        ellipse(0.0934, 1700, Mar, 2.72788 * i)
        ellipse(0.004839, 46000, Jup, 1.91554 * i)
        ellipse(0.054151, 5500, Sat, 1.0218 * i)
        i = i + 1
    t.mainloop()


if __name__ == '__main__':
    main()

