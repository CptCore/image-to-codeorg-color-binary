from PIL import Image
import numpy as np

filename =  input("Enter the Image name (Very Case Sensitive) : ")
with Image.open(filename) as img:
    img = img.convert("RGB")
    img = img.resize ((75,75))

temprgbnum = 24
imagebinary = ""
imagebinary += ''.join(''.join(str((byte >> i) & 1) for i in range(7, -1, -1)) for byte in img.size[0].to_bytes(1,byteorder='big'))
imagebinary += ''.join(''.join(str((byte >> i) & 1) for i in range(7, -1, -1)) for byte in img.size[1].to_bytes(1,byteorder='big'))
imagebinary += ''.join(''.join(str((byte >> i) & 1) for i in range(7, -1, -1)) for byte in temprgbnum.to_bytes(1,byteorder='big'))

image_array = list(img.getdata())

for pixel in image_array:
    r = ''.join(''.join(str((byte >> i) & 1) for i in range(7, -1, -1)) for byte in pixel[0].to_bytes(1,byteorder='big'))
    g = ''.join(''.join(str((byte >> i) & 1) for i in range(7, -1, -1)) for byte in pixel[1].to_bytes(1,byteorder='big'))
    b = ''.join(''.join(str((byte >> i) & 1) for i in range(7, -1, -1)) for byte in pixel[2].to_bytes(1,byteorder='big'))
    rgb = r + g + b
    print(r,g,b)
    imagebinary += rgb

with open("output.txt", "w") as text_file:
    # Write the string to the file
    text_file.write(imagebinary)
    print("Saved to output.txt :3")

# Convert the RGB data to bytes
#image_array = bytes([value for pixel in image_array for value in pixel])
#image_array = ''.join(''.join(str((byte >> i) & 1) for i in range(7, -1, -1)) for byte in image_array)
#print(image_array)
