#xor: https://stackoverflow.com/questions/2612720/how-to-do-bitwise-exclusive-or-of-two-strings-in-python

import os

def xor(a, b) :
    return bytes(x ^ y for x, y in zip(a, b))

message = b'\x12\x34\x56\x78\x90\xab' #placeholder for packet payload
packet_length = len(message) #i.e \x12\x34 = 2
key=os.urandom(packet_length) #"random" hex string
file = open("key.txt", "wb") #write key (binary) in file
file.write(key)
file.close()
#file = open("key.txt", "rb") #Test to read key from binary file i.e in another program- works
#key=file.read()
#file.close()
ciphertext = xor(message, key)
print("Message:",message.hex()) #comment out
print("Key:",key.hex())
print("Ciphertext:",ciphertext.hex())
print("C XOR K:", xor(ciphertext, key).hex()) #works
