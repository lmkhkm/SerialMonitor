import serial

ser = serial.Serial('COM7',115200, timeout=1)
while True:
    print("R: ", ser.readline())