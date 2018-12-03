import socket
import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd

TCP_IP = '127.0.0.1' # 172.25.98.219 Saad's IP
TCP_PORT = 4000
BUFFER_SIZE = 1024

def gen_tone(amplitude, tone_duration, frequency):
    x = np.arange(44100)
    tone = amplitude * np.sin(2 * np.pi * frequency/44100 * x)
    return tone

tone1 = gen_tone(100, 1, 100)
tone2 = gen_tone(100, 1, 900)

MESSAGE = ("Wagwan m8")
bin_data = bin(int.from_bytes(MESSAGE.encode(), 'big'))
msg = np.array(list(bin_data[2:]), dtype = 'uint8')
print(msg)

for i in np.nditer(msg):
    if i == 1:
        sd.play(tone1, blocking = True)
    else:
        sd.play(tone2, blocking = True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(msg)
msg = s.recv(BUFFER_SIZE)
s.close()

print("Data sent: ", msg)
