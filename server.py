import socket
import threading
import os
import numpy as np
from PIL import Image

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()
    
    def accept_connections(self):
        ip = '10.27.0.40'
        print (ip)
        port = int(input('Enter desired port --> '))

        self.s.bind((ip,port))
        self.s.listen(100)

        print('Running on IP: '+ip)
        print('Running on port: '+str(port))

        while 1:
            c, addr = self.s.accept()
            print(c)
            
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def handle_client(self,c,addr):
        data = c.recv(1024).decode()
        print(data)


        def fletcher32(length):
            w_len = length
            c0 = 0
            c1 = 0
            x = 0

            while w_len >= 360:
                for i in range (360):
                    c0 = c0 
                    c1 = c1 + c0
                    x = x + 1
                c0 = c0 % 65535
                c1 = c1 % 65535
                w_len = w_len - 360
            
            for i in range (w_len):
               c0 = c0 
               c1 = c1 + c0
               x = x + 1
            c0 = c0 % 65535
            c1 = c1 % 65535
            return (c1 << 16 | c0)

        img_data = Image.open(data)
        img_arr = np.array(img_data)



        h,w,_= img_arr.shape # Get the width and heigth of the image

        print(h)
        print(w)



        z =  len(img_arr)
        fletcher32(z)

        for i in img_arr.shape[1::-1]: # img.shape -> (width,height,channel)

            if(i%2 == 0):
                    
                print("pair")

            else:

                print("impair")

    
        if not os.path.exists(data):
            c.send("file-doesn't-exist".encode())

        else:
            c.send("file-exists".encode())
            print('Sending',data)
            if data != '':
                file = open(data,'rb')
                data = file.read(1024)
                while data:
                    c.send(data)
                    data = file.read(1024)

                c.shutdown(socket.SHUT_RDWR)
                c.close()
                

server = Server()
