#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:17:16 2019

@author: esalathe
"""

from numpy import linspace,array, log,exp,sin,cos,sqrt, pi,e
import numpy as np
from numpy import zeros, diagflat, ones, eye, matmul



# Solve Heat Equation numerically using a time and space mesh

# Parameters for the problem

# Spatial Grid
L = 15.  # Length of bar
dx = 0.1 # Spacing of points on bar
nx = int(L/dx+1)

x = linspace(0,L,nx)


# Time grid
stopTime = 20 # Time to run the simulation
dt = .01 # Size of time step
nt = int(stopTime/dt+1)

time = linspace(0,stopTime,nt)

# heat conduction
K = 0.5

# Create array to contain T(t,x)

T = zeros((nt,nx)) # nt times, nx positions

# Set the initial condition

T[0,:] = 50 # uniform initial state

# Boundary Condition

Ta = 100. # left side
Tb = 0. # right side
T[0,0] = Ta # fixed temperature
T[0,-1] = Tb # fixed temperature

# create heat source along bar as a vector

#qsource = zeros(nx,1)
#nx2 = floor(nx/2)
#qsource(1:nx2) = 10*(1 - (2/L)*x(1:nx2))
#plot(x,qsource)
#disp([x',qsource])
#return

# Create Matrix for iterating forward in time



Tdiag = eye(nx,nx,1) - 2*eye(nx) + eye(nx,nx,-1)
I = eye(nx)

M = K*dt/dx**2 * Tdiag + I

#disp(Tdiag(1:10,1:10))
#disp(K*dt/dx^2 * Tdiag(1:10,1:10))
#disp(M(1:10,1:10))


# loop forward in time and compute change in string
for it in range(1,nt):
    # Calculate the future temperature along the bar
    
    
    # center of bar in matrix form. Note that heat source is added at each
    # time step
    
    T[it,:] = matmul(M,T[it-1,:]) #  + qsource*dt
    
    # apply left side boundary condition
    T[it,0] = Ta # fixed temperature
    
    # apply right side boundary condition
    T[it,-1] = Tb ### T[it,-2] # fixed temperature
    # T[it,-1] = T[it,-2] # fixed temperature


# Make some plots
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show,figure,title, pause, subplots, ylim, xlim
from matplotlib import cm

figure(1)
plot(x, T[-1,:])
xlabel('Distance')
ylabel('Temperature')
title('Steady State Solution')
ylim([0,100])
xlim([0,L])


# Animated graph for every 10th time step
figure(2)
for it in range(0,nt-1,200):
    plot(x, T[it,:])
#    axis([0 L 0 100])
    xlabel('Distance')
    ylabel('Temperature')
    title('Transient Solution')
    ylim([0,100])
    xlim([0,L])


# suface plot
    

fig = figure(3)
ax = fig.add_subplot(projection='3d')

# Make data.
X, Y = np.meshgrid(x,time)

# Plot the surface.
surf = ax.plot_surface(X, Y, T, cmap=cm.inferno,
                       linewidth=0, antialiased=False)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
xlabel('Distance (cm)')
ylabel('Time (s)')
