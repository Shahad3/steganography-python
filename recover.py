"""
           ========================================
                     Exam number:Y3876181        
                macOS: 10.14.5     Python: 3.8.1 
           ========================================
 
"""
from PIL import Image

# Function to convert bit to text
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

# An array used to collect all of least 4 bits in the image
message=[]
# The number of bits used in the hidden text
text_length = 71648

with Image.open("secret.png") as img:
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x,y)))
            # To get the last 4 bits
            pixel[0] = format(pixel[0]%16,'04b')
            pixel[1] = format(pixel[1]%16,'04b')
            pixel[2] = format(pixel[2]%16,'04b')
            # Append the last 4 bits in the array
            message.append(pixel[0])
            message.append(pixel[1])
            message.append(pixel[2])


data = "".join([str(x) for x in message])
data = text_from_bits(data[:text_length])
print(data)
