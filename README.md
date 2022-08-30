# steganography-python
A simple python code to create a hidden text in an image, and to recover the text from the image. This code was written for a university assignment.

i) Design and implement an image based steganographic system

The code in stega.py in appendix A provides a steganographic system that takes as inputs the text file that contains the secret message and an image. It uses the library Pillow to import the image and change its pixels values [1]. The output is a new image (secret.png) that has the secret file hidden inside the image. After converting the text file to bits [2], I have used the same method we practiced in the lab, replacing the least significant four bits of the image to bits from the text file [3].
To recover the hidden text, the program recover.py in appendix A takes the new image and the number of bits of the hidden text. First, the program will combine all of the least significant four bits in the image pixels. Then, it will decode the bits back to a text, taking in consideration the number of bits required for the text file. After that, it will print the hidden text.

To run the stega.py, put two files (Lena.png and verySecretTextFile.txt) in the same folder as the program. The output of stega.py is the image secret.png. This output file should exist in the same folder as recover.py to open the image and decode the text from the secret file.
