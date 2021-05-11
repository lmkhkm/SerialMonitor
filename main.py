import serial
import keyboard

portName = 'COM7'
baudRate = 115200

ser = serial.Serial(portName, baudRate, timeout=1)




while True:
    print("R: ", ser.readline())
    if :
        
