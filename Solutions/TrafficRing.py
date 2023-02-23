#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:22:40 2019

@author: esalathe
"""

## First we need to load a bunch of modules
from scipy.integrate import odeint
from numpy import linspace,array,zeros,arange, sqrt, concatenate, sin,cos,pi
from matplotlib.animation import FuncAnimation

## Define the rate function
def ratefunction_eps(t, X):
# IDM Single driver model
    
    # unpack the dependent variables
    x = X[:ncar]
    v = X[ncar:]
        
    # Compute acceleration according to IDM
    dv = zeros(ncar)
    
            
    
    for i in range(ncar):
    # Acceleration on an empty road. 
        freeroad = (1 - (v[i]/v0)**delta_exp)
    # Desired following distance 
    #     use parameters defined below
    
        # if i==0: 
        #     # First car [i] follows last car [-1]
        #     # distance to last car -- note you need to subtract circumference 
        #     s = x[-1] + Circ - L - x[i]  
        #     delv = v[i] - v[-1] # approach speed to last car
        # else:
        #     s = x[i-1] - L - x[i] # distance to car ahead
        #     delv = v[i] - v[i-1] # approach speed to var ahead

        s = x[i-1] - L - x[i] # distance to car ahead
        if i==0: s = s + Circ  # Add circumf for distance between first car and last car

        delv = v[i] - v[i-1] # approach speed to var ahead

    
        sstar = s0 + v[i]*T + v[i]*delv/(2*sqrt(a_accel*b_decel))
        interaction = (sstar/s)**2    
    
        a_idm = a_accel*(freeroad - interaction) 
            
    # compute derivative of v
        dv[i] = a_idm # x component of acceleration
    
    # pack rate array
    
    dx = v
    rate = concatenate((dx, dv))

    return rate


# set parameters
T = 1.8 #time headway
delta_exp = 4
L = 5
a_accel = 1
b_decel = .3
v0 = 28 #desired speed in m/s
s0 = 2.0 #desired gap m

Circ = 1000
ncar = 10

# set initial conditions
# Cars initially spaced out by 10 lengths F to R
dx_start = Circ/ncar
xinit = -dx_start*arange(ncar) 

vinit = zeros(ncar) 

# Tweak the first car to start a traffic wave
vinit[0] = vinit[0] + 1

X0 = concatenate((xinit,vinit))

# set the time interval for solving
Tstart=0
Tend = 15*60 # 

# Form Time array

time = linspace(Tstart,Tend,400) # 400 steps for nice plot

# solve the ODE
X = odeint(ratefunction_eps, X0, time, tfirst=True) 

# unpack the results. In the output array, variables are columns, times are rows

xout = X[:,:ncar]
vout = X[:,ncar:]

# PLOTS

from matplotlib.pyplot import figure, subplot
fig=figure()

ax1 = subplot()
ax1.plot(time,xout[:,::5],'b') # just the first car
ax1.set_xlabel('time (s)')
ax1.set_ylabel('distance (m)', color='b')
ax1.tick_params('y', colors='b')

ax2=ax1.twinx()
ax2.plot(time,vout[:,::5],'r')
ax2.set_ylabel('velocity (m/s)', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()

