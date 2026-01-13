#!/usr/bin/python3
from numpy import pi

def bisect(f,a,b):

    if f(a)==0:
        return a
    if f(b)==0:
        return b


    if f(a)*f(b)>0:
        return "Initial guesses do not span root"

    N = 100 #  maximum of 100 iterations
    for i in range(N):
        x = # first guess is midpoint

        if f(x)==0:
            return x

        # Select next guess for a or b depending on sign of f(x)*f(a) and f(x)*f(b)
    return x


    
def height_test(h):
    
    #This function just returns the volume given by a test value of h
    #minus the known volume of a liquid. A good estimate for the height
    #for the newton method is around 3-4, as it should be ~relatively~ close
    #to the cubed root of the known volume
    
    known_volume = 45 #m^3
    tank_diameter = 10 #m
    c = 1/2
    
    volume_difference = (tank_diameter **3)*(c)*(pi / 12)*( 3*(h / tank_diameter)**2 - 2*(h / tank_diameter)**3 ) - known_volume
    
    return volume_difference

x = bisect(height_test, 0, 10)
