from bitarray import bitarray
#PacketStructure

#Instructions: This standalone code constructs an example packet we want to send.  Here, I define the header as headerLength and payloadSize.
#So payloadSize is fixed as 8 bits -> corr. to one ASCII character.  For payload I have .zfill(8) which turns payload into 01100001.
#Essentially we fill to our fixed max payloadSize.  Note that we only want to use OTP to encrypt our payload.  So implenting in client.py,
#we would set payload=encrypt.zfill(8) for example.  Finally we have the checksum in parity bit form.  Add 1 to some number, mod2, for each
#bit in the bitstring to get a single  bit we append at the end.  Thus our packet is constructed, as it should be in client.py.
#Finally make it a numpy array, etc.

#When receiving this packet we need to turn it into a bitstring again (from numpy array), and perform the #checksum loop on all but the last bit.
#This is using the checksum for error-checking: we want to get the sent checksum bit from #checksum.  Finally we isolate the payload and XOR
#the encrypted message with our key to get the decrypted message.

headerLength = '1000'
payloadSize = '1000' #max payload size
payload = '1100001'.zfill(8) #payload="a"     #fill in '8' with payloadSize
checksum = 0

thePacket=headerLength+payloadSize+payload
#print(thePacket)
#checksum
for i in thePacket:
    if i=='1':
        checksum = (checksum+1)%2
#print(checksum)
thePacket+=str(checksum)
#print(thePacket)