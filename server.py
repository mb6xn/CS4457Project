import socket
import numpy as np
import pylab as plt
from rtlsdr import RtlSdr
import scipy.signal as signal
import sounddevice as sd

TCP_IP = '127.0.0.1'
TCP_PORT = 4000
BUFFER_SIZE = 4096

def gen_tone(amplitude, tone_duration, frequency):
    x = np.arange(44100)
    tone = amplitude * np.sin(2 * np.pi * frequency/44100 * x)
    return tone

tone1 = gen_tone(100, 1, 100)
tone2 = gen_tone(100, 1, 900)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

conn, addr = s.accept()
print ('Connection by', addr)

while 1:
    msg = conn.recv(BUFFER_SIZE)
    for i in list(msg):
        if i == 1:
            sd.play(tone1, blocking = True)
        else:
            sd.play(tone2, blocking = True)
    if not msg: break
    print ("Received Data:", msg)
    conn.sendall(msg)  # echo

conn.close()
