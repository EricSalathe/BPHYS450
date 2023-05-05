import random as rnd
import matplotlib.pyplot as plt, numpy as np
from numpy import linspace,array,arange, log,exp,sin,cos,sqrt, pi, zeros, ones, arctan
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot

        
def exchange(solid, N, L):               # iterate L times
    for i in range(L):
        take = rnd.randint(0, N-1) # random pair
        give = rnd.randint(0, N-1) 
        while solid[take] == 0:     # find a nonzero-energy cell
            take = rnd.randint(0, N-1)

        solid[take] -= 1            # exchange energy
        solid[give] += 1
    return solid

def sample(solid, N):                       # sample energy distribution
    qmax = int(np.max(solid))
    pn = zeros(qmax+1)
    for q in range(qmax+1):
        pn[q] = np.count_nonzero(solid==q)/float(N)
        
    # for q in solid:
    #     pn[int(q] = pn[q]+1/N
        
    error = np.sqrt(pn/N)                 # statistical error
    return qmax, pn, error


# set up solid
qavg = 100                              # avg  units of energy per oscillator
N = 400
L = N*1000

# Create a list containing the N values of energy, initially qavg
solid = qavg*ones(N)


# Simulate
Nint = 100
exchange(solid, N, L)         # thermalize, 100 interactions per oscillator 
qmax, pn, error = sample(solid, N)

# analytic Boltzmann dist, qavg = 1/(exp(1/kT)-1), 1/kT=ln(1+1/qavg)
kT = 1/np.log(1+1./qavg)

En = np.arange(qmax+1)

#C = np.max(pn)
C = 1/np.sum(exp(-En/kT))
pn_th = C*exp(-En/kT)

# Plot result
fig = plt.figure()

ax1 = subplot(1,2,1)
ax1.plot(En, pn, 'o')
ax1.errorbar(En, pn, error, ls='')
ax1.plot(En, pn_th, '-r')    #  theoretical result   
 
ax1.set_xlim(0,qmax)
ax1.set_xlabel('Energy units')
ax1.set_ylabel('Probability')
ax1.semilogy()        # semilog scale    

ax2 = subplot(1,2,2)
ax2.plot(En, pn, 'o')
ax2.errorbar(En, pn, error, ls='')
ax2.plot(En, pn_th, '-r')    #  theoretical result   
 
ax2.set_xlim(0,qmax)
ax2.set_xlabel('Energy units')
ax2.set_ylabel('Probability')

tight_layout()
