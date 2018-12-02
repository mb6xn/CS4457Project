import socket
import numpy as np
from scipy.io.wavfile import write
import scikits.audiolab
#from rtlsdr import *


TCP_IP = '172.25.79.75' # Saad's IP
TCP_PORT = 4000
BUFFER_SIZE = 1024

def gen_tone(amplitude, tone_duration, frequency):
    x = np.arange(44100)
    tone = amplitude * np.sin(2 * np.pi * frequency/44100 * x)

    return tone

def modulateFSK(array, tone1, tone2):
    for i in array:
        if i == 1:
            scikits.audiolab.play(tone1)
        else:
            scikits.audiolab.play(tone2)

def main():
    tone1 = gen_tone(100,1, 100)
    tone2 = gen_tone(100,1, 900)

    MESSAGE = ("this is the pepsi and saad is very sexy")
    bin_data = bin(int.from_bytes(MESSAGE.encode(), 'big'))
    msg = [int(i) for i in bin_data[2:]]
    print(msg)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    while True:
        modulateFSK(msg, tone1, tone2)
        s.sendall(msg)
        msg = s.recv(BUFFER_SIZE)

    s.close()
    print(msg)

if __name__ == '__main__':
    main()
