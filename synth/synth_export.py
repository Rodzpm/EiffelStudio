#IMPORTS
import numpy as np

#sound like organ
def organ(frequency, duration, frames):
    arr = np.cos(2*np.pi*frequency*np.linspace(0,duration, frames))
    arr = arr + np.cos(4*np.pi*frequency*np.linspace(0,duration, frames))
    arr = arr + np.cos(6*np.pi*frequency*np.linspace(0,duration, frames))
    return arr/max(np.abs(arr))

#square wave
def square(frequency, duration, frames):
    arr = np.cos(2*np.pi*frequency*np.linspace(0,duration, frames))
    return np.clip(arr*10, -1, 1)

#triangular wave
def triangular(frequency, duration, frames):
    arr = np.cos(2*np.pi*frequency*np.linspace(0,duration, frames))
    arr = np.cumsum(np.clip(arr*10, -1, 1))
    arr = arr+np.sin(2*np.pi*frequency*np.linspace(0,duration, frames))
    return arr/max(np.abs(arr))

#syth function
def synth(frequency, song, duration=1.5, sampling_rate=44100):
    frames = int(duration*sampling_rate)
    if (song == "organ"):
        arr = organ(frequency, duration, frames)
    if (song == "square"):
        arr = square(frequency, duration, frames)
    if (song == "triangular"):
        arr = triangular(frequency, duration, frames)
    fade = list(np.ones(frames-4410))+list(np.linspace(1, 0, 4410))
    arr = np.multiply(arr, np.asarray(fade))
    return list(arr)