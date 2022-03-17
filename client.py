import socket
import os

import numpy as np
from PIL import Image

class Client:
    def __init__(self):

        print(self)
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = input('Enter ip --> ')
        self.target_port = input('Enter port --> ')

        self.s.connect((self.target_ip,int(self.target_port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))

    def main(self):
        while 1:
            file_name = input('Enter file name on server --> ')

            

    

            self.s.send(file_name.encode())

            confirmation = self.s.recv(1024)
            if confirmation.decode() == "file-doesn't-exist":
                print("File doesn't exist on server.")

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()

            else:        
                write_name = 'from_server_'+file_name





                if os.path.exists(write_name): os.remove(write_name)

                with open(write_name,'wb') as file:
                    while 1:
                        data = self.s.recv(1024)

                        if not data:
                            break

                        file.write(data)

                print(file_name,'successfully downloaded.')

                img_data = Image.open(write_name)
                img_arr = np.array(img_data)

                z =  len(img_arr)
                print(z)

                for i in img_arr.shape[1::-1]:

                    if(i%2 == 0):
                        print("pair")

                    else:
                        print("impair")

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()
                
client = Client()
