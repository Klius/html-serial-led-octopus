import serial

port = 'COM3'
rate = '9600'
line = '00000000#00111100#01000010#01000010#01111110#01000010#01000010#01000010\n'
ser = serial.Serial()
ser.baudrate = rate
ser.port = port
ser.open()
ser.write(line.encode('ascii'))
b = line.encode('ascii')
print(b[0])