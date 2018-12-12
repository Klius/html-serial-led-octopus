import serial

class ser(object):
	def __init__(self,port,rate):
		self.startMarker = 60
		self.endMarker = 62
		#self.port = port
		#self.rate = rate
		self.ser =  serial.Serial(port, rate) # open connection 

	def waitForArduino(self):
	   # wait until the Arduino sends 'Arduino Ready' - allows time for Arduino reset
	   # it also ensures that any bytes left over from a previous message are discarded
		
		msg = ""
		while msg.find("ready") == -1:

			while ser.inWaiting() == 0:
				pass

			msg = recvFromArduino()

			print (msg)

	def recvFromArduino(self):
		
		ck = ""
		x = "z" # any value that is not an end- or startMarker
		byteCount = -1 # to allow for the fact that the last increment will be one too many
		
		# wait for the start character
		while  ord(x) != self.startMarker: 
			x = self.ser.read()
		
		# save data until the end marker is found
		while ord(x) != self.endMarker:
			if ord(x) != self.startMarker:
				ck = ck + x.decode("utf-8")
				byteCount += 1
				x = self.ser.read()
		
		return(ck)

	def sendToArduino(self,str):
		b = bytes(str, 'utf-8')
		self.ser.write(b)
