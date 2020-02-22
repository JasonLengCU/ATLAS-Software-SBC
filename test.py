import serial
import socket

ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.bind(("192.168.43.84", 1995))
s.bind(("127.0.0.1", 1995))

s.listen(5)

serverSocket, address = s.accept()
print("Connection established!")

while True:
    commandCoded = serverSocket.recv(1024)
    command = commandCoded.decode("utf-8")
    # print(command)
    ser.write(bytes(command.encode("ascii")))
    # ser.read()
    line = ser.readline()
    print("Received: " + line)