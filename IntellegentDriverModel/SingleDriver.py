#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:22:40 2019

@author: esalathe
"""

## First we need to load a bunch of modules
from scipy.integrate import odeint
from numpy import linspace,array,zeros,log,exp,sin,cos,sqrt,pi,e
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot

# set parameters for the IDM
T = 1.8 # time headway
delta_exp = 4 # acceleration shape factor
L = 5 # car lenght
a_accel = 0.7 # acceleration parameter
b_decel = 2 # braking parameter
v0 = 28 # desired speed in m/s
s0 = 2.0 # minimum gap front to rear bumper (m)

# Put a stopped car down the road

Xblock = 5000. # front bumper of stopped car
Vblock = 0


## Define the rate function
def ratefunction(t, X):
# IDM Single driver model
    
    # unpack the dependent variables
    x = X[0]
    v = X[1]
    
    
    # Compute acceleration according to IDM
    
    s = Xblock - L - x # distance to rear bumper of stopped car
    delv = v - Vblock # approach speed to stopped car
    
    # Acceleration on an empty road. 
    # Here we use variable names defined below rather than the actual 
    # numerical values
    freeroad = (1 - (v/v0)**delta_exp)
    
    # Desired following distance 
    #     use parameters defined below
    sstar = s0 + v*T + v*delv/(2*sqrt(a_accel*b_decel))
    
    interaction = (sstar/s)**2    
    
    a_idm = a_accel*(freeroad - interaction) 
            
    # compute derivatives
    dx = v
    dv = a_idm # x component of acceleration
    
    # pack rate array
    rate = array([dx, dv])

    return rate




# set initial conditions
# note that we used v0 above, so call these xinit vinit
xinit = 0.
vinit = 0.

X0 = array([xinit,vinit])

# set the time interval for solving
Tstart=0
Tend = 5*60 # 5 minutes

# Form Time array

time = linspace(Tstart,Tend,400) # 400 steps for nice plot

# solve the ODE
X = odeint(ratefunction, X0, time, tfirst=True) 

# unpack the results. In the output array, variables are columns, times are rows

xout = X[:,0]
vout = X[:,1]


# Basic Plot
#figure(1)
#plot(time,xout)
#xlabel('time (s)')
#ylabel('distance (m)')
#
#figure(2)
#plot(time,vout)
#xlabel('time (s)')
#ylabel('velocity (m/s)')

# Fancier plots see https://matplotlib.org/examples/api/two_scales.html

fig=figure()

ax1 = subplot()
ax1.plot(time,xout,'b')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('distance (m)', color='b')
ax1.tick_params('y', colors='b')

ax2=ax1.twinx()
ax2.plot(time,vout,'r')
ax2.set_ylabel('velocity (m/s)', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
