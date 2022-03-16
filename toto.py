import numpy as np
from PIL import Image



#img_arr = img_arr - 180
#new_img = Image.fromarray(img_arr)
#new_img.save("altered_img.png")

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

img_data = Image.open('montagne.jpg')
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






















#import base64

#
 
#with open("img.jpeg", "rb") as imageFile:
    
    #str = base64.b64encode(imageFile.read())
    #str1 = base64.b64decode(str)
    #print(str1)

#with open("sample.txt", "wb") as f:
    
    #f.write(str)


#with open("sample.txt", "rb") as f1:
    
    #for byte1 in f1:

        #binary_representation=bytes(byte1)

        #byte_list.append(binary_representation)





#for byte in str:
    
    #binary_representation=byte(byte[0])

    #byte_list.append(binary_representation)




#print(byte_list)
