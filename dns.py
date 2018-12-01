# #Step 2 of the Final Exam.
# filtering for bonus: bandpass filter (44.6, c=44.1, 44.5) rtlsdr queen state university - decimation
# scipy bandpass filter library
import socket, glob, json, time 
port = 53 
ip = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((ip, port))

def setHeaderAndAnswer(data):
	#print(type(data))
	resp = bytearray(data)
	resp[2] = 129 # Response 
	resp[7] = 1 # Answer 
	return resp

def getAnswer():
	answer = b''
	answer += b'\xc0\x0c' # CNAME
	answer += b'\x00\x01' # TYPE A
	answer += b'\x00\x01' # CLASS IN
	answer += b'\x00\x00\x00\x1b' # TTL
	answer += b'\x00\x04' # RDLENGTH
	answer += b'\xac\x19\x4f\x5c' #RDATA
	return answer

def GetFinalPacket(data):
	return setHeaderAndAnswer(data) + getAnswer()

while 1:
	data, addr = sock.recvfrom(512)
	packet = GetFinalPacket(data)
	print(packet)
	sock.sendto(packet, addr)

# 0001010000010000000000000131013001300331323707696e2d61646472046172706100000c0001
# 0002010000010000000000000131013001300331323707696e2d61646472046172706100000c0001

#b'\x00\x01*\x01\x01*\x00\x01Hend\x00\x00\x00\x00Qend\xc0\x0c\x03156\x03174\x0225\x03172\x07in-addr\x04arpa\x00\x00\x0c\x00\x01'
#      0000 0001									
# 172.25.79.92 - AC.19.4F.5C
# http://172.25.79.92/