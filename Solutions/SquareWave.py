#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:42:59 2022

@author: salathe
"""

from numpy import linspace,array,zeros,log,exp,sin,cos,sqrt,pi,e, ones, arange, zeros, real, imag, sign
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot, title, tight_layout, stem

from scipy.fft import fft, fftshift

# time dimension

T = 10 # sec
nt = 2**11 # fft likes powers of 2
dt = T/nt # time step

t=arange(-T/2,T/2,dt)  #  -T/2 <= t < +T/2
nfmax = int(nt/2) # number of frequencies resolved by FFT


# frequency dimension

# Create the squar function in array f

f =  sign(t) # note that t is an array already

# take FFT
# use fftshift to shift function one half interval since fft assumes 0<t<T
F = fft(fftshift(f), nt)

# get the coeffs
a = 2*real(F[:nfmax])/nt # form the a coefficients
a[0] = a[0]/2

b = -2*imag(F[:nfmax])/nt # form the b coefficients

p = sqrt(a**2 + b**2) # form power spectrum

# Get the analytic coefficients

# initialize to zeros
aan = zeros(nfmax)
ban = zeros(nfmax)

for n in range(1,nfmax):
    ban[n]=2/(n*pi) * (1 - (-1)**n)

# Reconstruct the sawtooth by suming fourier series for small n
fr = ones(nt)*a[0] # fill time series with constant term

# Sum the Fourier Series
Nrecon = 10
for n in range(1,Nrecon+1):
    fr = fr + a[n]*cos(n/T * 2*pi*t) + b[n]*sin(n/T*2*pi*t)

## make some plots

subplot(2,2,1)
plot(t,f)
plot(t,fr)
title('Function')
xlabel('time')
ylabel('f(t)')

subplot(2,2,2)
plot(t, fr-f);
title('Difference')
xlabel('time')
ylabel('Error')


subplot(2,1,2)
plot(arange(0,10),b[0:10],'b|',label='FFT')
plot(arange(0,10),ban[0:10],'r_',label='Analytic')
xlabel('Index')
legend()


tight_layout() # prevent squished plot (matplotlib kludge)