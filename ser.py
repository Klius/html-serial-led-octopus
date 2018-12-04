import serial
import time

def waitForArduino():

   # wait until the Arduino sends 'Arduino Ready' - allows time for Arduino reset
   # it also ensures that any bytes left over from a previous message are discarded
    
    msg = ""
    while msg.find("ready") == -1:

      while ser.inWaiting() == 0:
        pass
        
      msg = recvFromArduino()

      print (msg)
	  
def recvFromArduino():
  global startMarker, endMarker
  
  ck = ""
  x = "z" # any value that is not an end- or startMarker
  byteCount = -1 # to allow for the fact that the last increment will be one too many
  
  # wait for the start character
  while  ord(x) != startMarker: 
    x = ser.read()
  
  # save data until the end marker is found
  while ord(x) != endMarker:
    if ord(x) != startMarker:
      ck = ck + x.decode("utf-8")
      byteCount += 1
    x = ser.read()
  
  return(ck)
  
def sendToArduino(str):
	b = bytes(str, 'utf-8')
	ser.write(b)

startMarker = 60
endMarker = 62
port = 'COM3'
rate = '9600'
line = "00000000#00111100#01000010#01000010#01111110#01000010#01000010#01000010E"
ser =  serial.Serial(port, rate) # open connection 
waitForArduino()
sendToArduino(line)