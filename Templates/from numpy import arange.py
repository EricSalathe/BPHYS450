from numpy import arange
from matplotlib.pyplot import \
    plot,xlabel,ylabel,legend,show, \
    figure, subplot, title, tight_layout
from scipy.fftpack import fft
import scipy.io.wavfile as wav 
# time dimension

file_name='../Sounds/Whip-poor-will.wav' # Path to your downloaded sound file
Fs, f =wav.read(file_name)
nt = len(f)

t= arange(nt)/Fs
plot(t,f)
xlabel('Time (s)')
ylabel('Amplitude')
legend(['Sound Wave'])
show()