import socket
import argparse

 


parser = argparse.ArgumentParser(description="Simple File image import")
    
parser.add_argument("filen", help="Image file name")


args = parser.parse_args()
    
filen = args.filen


msgFromClient       = filen # image name - for example image.jpeg 

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("10.27.0.40", 12345)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
