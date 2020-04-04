import matplotlib.pyplot as pyplot
import numpy
import wave
import scipy.fftpack

wav = wave.open("assets/test2.wav", "r")
chosen_ms = int(input("Which millisecond do you want the fourier transformation for? "))

# Read the frames and convert them into a list
signal = numpy.frombuffer(wav.readframes(-1), numpy.int16)

# Number of frames / FPS = seconds
seconds = len(signal) / wav.getframerate()

# Find the set of frames in the chosen millisecond
framespermillisecond = int(wav.getframerate() / 1000)
chosenframeset = signal[chosen_ms*framespermillisecond::framespermillisecond]

# An evenly spaced list starting at 0, ending at seconds, with a length = frame count
timeaxis = numpy.linspace(0, seconds, num=len(signal))

# Fourier transform the selected data
ft = scipy.fftpack.rfft(chosenframeset)

if wav.getnchannels() == 1: # Can't process stereo - has to be mono audio
    # plot the audio data
    fig, ax = pyplot.subplots()
    ax.plot(timeaxis, signal)
    ax.set_xlabel('Time (s)')
    ax.set_title('Audio data')
    ax.set_ylabel('Signal')

    # plot the fourier transformed data
    fig, ax = pyplot.subplots()
    ax.plot(ft)
    ax.set_title(f"Fourier Transformation at {chosen_ms}ms")
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Amplitude (m?)')
    pyplot.show()
