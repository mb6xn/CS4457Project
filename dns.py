# #Step 2 of the Final Exam.
# from socket import *

# class DNSQuery:
# 	def __init__(self, data):
# 		self.data = data
# 		self.domain = ''
# 		resptype = (ord(str(data[2])) >> 3) & 15   # Opcode bits
# 		if resptype == 0:                     # Standard query
# 			ini = 12
# 			lon = ord(data[ini])
# 			while lon != 0:
# 				self.domain += data[ini + 1:ini + lon + 1] + '.'
# 				ini += lon + 1
# 				lon = ord(data[ini])
# 	def response(self, ip):
# 		packet=''
# 		if self.domain:
# 			packet+=self.data[:2] + "\x81\x80"
# 			packet+=self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'   # Questions and Answers Counts
# 			packet+=self.data[12:]                                         # Original Domain Name Question
# 			packet+='\xc0\x0c'                                             # Pointer to domain name
# 			packet+='\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'             # Response type, ttl and resource data length -> 4 bytes
# 			packet+=str.join('',map(lambda x: chr(int(x)), ip.split('.'))) # 4bytes of IP
# 		print(packet)
# 		return packet

# serverPort = 53
# ip='127.0.0.1'
# serverSocket = socket(AF_INET, SOCK_DGRAM)
# serverSocket.bind((ip, serverPort))
# try:
# 	while 1:
# 		data, addr = serverSocket.recvfrom(1024)
# 		p=DNSQuery(data)
# 		serverSocket.sendto(bytes(p.response(ip)), addr)
# 		print('Response: %s -> %s' % (p.domain, ip))
# except KeyboardInterrupt:
# 	print('Finalize')
# 	serverSocket.close()
# filtering for bonus: bandpass filter (44.6, c=44.1, 44.5) rtlsdr queen state university - decimation
# scipy bandpass filter library
import socket, glob, json, time 
port = 53 
ip = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

def load_zones():
	jsonzone = {}
	zonefiles = glob.glob('zones/*.zone')
	for zone in zonefiles:
		with open(zone) as zonedata:
			data = json.load(zonedata)
			zonename = data['$origin']
			jsonzone[zonename] = data
	return jsonzone

zonedata = load_zones()

def getflags(flags):
	byte1 = bytes(flags[:1])
	byte2 = bytes(flags[1:2])
	rflags = ''
	QR = '1'
	OPCODE = ''
	for bit in range(1, 5):
		OPCODE += str(ord(byte1)&(1<<bit))
	AA = '1'
	TC = '0'
	RD = '0'
	RA = '0'
	Z  = '000'
	RCODE = '0000'
	return int(QR+OPCODE+AA+TC+RD, 2).to_bytes(1, byteorder='big')+int(RA+Z+RCODE, 2).to_bytes(1, byteorder='big')



def buildquestion(domainname, rectype):
	qbytes = b''
	for part in domainname:
		length = len(part)
		qbytes += bytes([length])
	print(qbytes)

def buildresponse(data):
	TransactionID = data[:2]
	reply = bytearray(TransactionID)
	# Get Flags
	# Flags = getflags(data[2:4])
	reply += bytearray([132, 0])
	reply += bytearray([0,1,0,1,0,0,0,0])
	reply += bytearray( b'\x00\x01')
	reply += bytearray([192,12,0,1,0,1,0,0,0,0,0,4])
	reply += bytearray(socket.inet_aton(ip))
	# Question Count
	# QDCOUNT = b'\x00\x01'
	# Answer Count
	#getquestiondomain(data[12:])
	# ANCOUNT = len(getrecs(data[12:])[0]).to_bytes(2, byteorder='big')

	# # Nameserver Count
	# NSCOUNT = (0).to_bytes(2, byteorder='big')

	# # Additional Count
	# ARCOUNT = (0).to_bytes(2, byteorder='big')

	# dnsheader = TransactionID+Flags+QDCOUNT+ANCOUNT+NSCOUNT+ARCOUNT
	# dnsbody = b''
	# records, rectype, domainname = getrecs(data[12:])
	# dnsquestion = buildquestion(domainname, rectype)
	return reply

while 1:
	data, addr = sock.recvfrom(512)
	r = buildresponse(data)
	sock.sendto(r, addr)
	print(r)
	time.sleep(1)