from PIL import Image
import numpy as np
filename =  input("Enter the Image name (Very Case Sensitive) : ")
with Image.open(filename) as img:
    img.load()

img = img.convert("RGB")

temprgbnum = 24
imagebinary = ""
imagebinary += str(img.size[0].to_bytes(1,byteorder='big'))
imagebinary += str(img.size[1].to_bytes(1,byteorder='big'))
imagebinary += str(temprgbnum.to_bytes(1,byteorder='big'))

image_array = np.array(img)
image_array = image_array.tobytes()
print(image_array[:10])
