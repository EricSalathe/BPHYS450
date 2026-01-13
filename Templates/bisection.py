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

        # are we there yet?
        if f(x)==0:
            return x

        # Select next guess for a or b depending on sign of f(x)*f(a) and f(x)*f(b)
    return x