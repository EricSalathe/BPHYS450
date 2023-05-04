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
from matplotlib.pyplot import figure, subplot, show
import matplotlib.pyplot as plt


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
        #     s = x[-1] + Circ - L - x[i]  # distance to car ahead
        #     delv = v[i] - v[-1] # approach speed to var ahead
        # else:
        #     s = x[i-1] - L - x[i] # distance to car ahead
        #     delv = v[i] - v[i-1] # approach speed to var ahead

        s = x[i-1] - L - x[i] # distance to car ahead
        if i==0: s = s + Circ  # Add circumf for first car

        delv = v[i] - v[i-1] # approach speed to var ahead
    
    
        sstar = s0 + v[i]*T + v[i]*delv/(2*sqrt(a_accel*b_decel))
        interaction = (sstar/s)**2    
    
        a_idm = a_accel*(freeroad - interaction) 
            
    # compute derivative of v
        dv[i] = a_idm # x component of acceleration
    
    # pack rate array
    
    rate = concatenate((v, dv))

    return rate


# set parameters
T = 1.8 #time headway
delta_exp = 4
L = 5
a_accel = 0.3
b_decel = 3
v0 = 28 #desired speed in m/s
s0 = 2.0 #desired gap m

Circ = 1000
ncar = 20

# set initial conditions
# Cars initially spaced out by 10 lengths F to R
dx_start = Circ/ncar
xinit = -dx_start*arange(ncar) 

vinit = zeros(ncar) 
vinit[0] = vinit[0] + 5

X0 = concatenate((xinit,vinit))

# set the time interval for solving
Tstart=0
Tend = 15*60 #  15 minutes

# Form Time array

time = linspace(Tstart,Tend,400) # 400 steps for nice plot

# solve the ODE
X = odeint(ratefunction_eps, X0, time, tfirst=True) 

# unpack the results. In the output array, variables are columns, times are rows

xout = X[:,0:ncar]
vout = X[:,ncar:-1]

# PLOTS

fig=figure()

ax1 = subplot()
ax1.plot(time,xout[:,::5],'b')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('distance (m)', color='b')
ax1.tick_params('y', colors='b')

ax2=ax1.twinx()
ax2.plot(time,vout[:,::5],'r')
ax2.set_ylabel('velocity (m/s)', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()

show()

# import matplotlib.pyplot as plt

# fig, [dplt,vplt,v1plt] = plt.subplots(3) 

# fig.suptitle('Multiple Cars')

# dplt.plot(time/60,xout)
# dplt.set(ylabel='Distance (m)')
# dplt.label_outer()

# vplt.plot(time/60,vout)
# vplt.set(xlabel='Time (sec)', ylabel='Velocity (m/s)')
# vplt.label_outer()

# v1plt.plot(time/60,vout[:,0])
# v1plt.set(xlabel='Time (sec)', ylabel='Velocity (m/s)')

# fig = plt.figure()
# ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
# line, = ax.plot([], [], 'o')

# anim = FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=20, blit=True)

# anim.save('traffic_ring.gif', writer='imagemagick')

animate=True

if animate: 
    radius = Circ/pi/2
    x=zeros(ncar)
    y=zeros(ncar)
    
    for icar in range(ncar):
        theta = 2*pi*xout[0,icar]/Circ;
    
        x[icar] = radius*cos(theta);
        y[icar] = radius*sin(theta);
    
    # plt.plot(x,y,'o')
    
    
    fig = plt.figure(figsize=[6,6])
    ax = plt.axes(xlim=(-radius, radius), ylim=(-radius, radius))
    line, = ax.plot([], [], 'o')
    plt.xlim((-radius*1.05, radius*1.05)) 
    plt.ylim((-radius*1.05, radius*1.05)) 
    
    def init():
        line.set_data([], [])
        return line,
    def animate(i):
        for icar in range(ncar):
            theta = 2*pi*xout[i,icar]/Circ;
            x[icar] = radius*cos(theta);
            y[icar] = radius*sin(theta);
    
        line.set_data(x, y)
        return line,
    
    anim = FuncAnimation(fig, animate, init_func=init,
                                   frames=400, interval=25, blit=True, repeat=False)
    
    #anim.save('TrafficRing.gif', writer='imagemagick')


