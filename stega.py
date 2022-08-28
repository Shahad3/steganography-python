"""
           ========================================
                     Exam number:Y3876181        
                macOS: 10.14.5     Python: 3.8.1 
           ========================================
 
"""

from PIL import Image
import math

# To convert text file to binary
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
# Open the text file that contain the secret message
with open('verySecretTextFile.txt', encoding='cp1252') as f:
    data = f.read()
f.close()
# convert the text file to binary
bit = text_to_bits(data)
# Open the image to use it to hide the message
with Image.open("Lena.png") as img:
    i = 0 # counter for data length
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            # Get the original pixel value
            pixel = list(img.getpixel((x,y)))

            # Each pixel could hide 12 bits from the text file
            if (i+12 < len(bit)):
                pixel[0] = (math.floor(pixel[0]/16))*16+int(bit[i:i+4],2)
                pixel[1] = (math.floor(pixel[1]/16))*16+int(bit[i+4:i+8],2)
                pixel[2] = (math.floor(pixel[2]/16))*16+int(bit[i+8:i+12],2)
                i = i + 12
            # Save the new pixel values
            img.putpixel((x,y), tuple(pixel))
    # Save the new image
    img.save("secret.png", "PNG")
    print("The secret message is now hidden in the file (secret.png)")


