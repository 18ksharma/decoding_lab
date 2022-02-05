#importing crypto library for python
from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad, unpad
#What we are given
plaintext = b"This is a top secret."
ciphertext = "f564ad4a41e84f44c776d146e1587f6d80e8c41c1ca2b6092fc5816c5ab9ff53"
iv = "010203040506070809000a0b0c0d0e0f"

# Converting iv and ciphertext so they are not in hex
iv = binascii.unhexlify(iv)
ciphertext = binascii.unhexlify(ciphertext)
#Checks plaintext is of size 21
if len(plaintext)== 21: 
    plaintext = pad(plaintext, 16)
    #Opening the file 
    with open("words.txt", "r") as myfile: 
        for line in myfile: 
            line = line.strip()
            if len(line)<16: 
                while(len(line)<16): 
                    line = line + "#"
            if len(line)>16: 
                line = line[:16]
            # for every key in the words.txt, we are getting an encrypted message
            cipher = AES.new(str.encode(line), AES.MODE_CBC, iv)
            msg = cipher.encrypt(plaintext)
            #Check if message matches original ciphertext
            if msg == ciphertext:
                print(msg)
                print(ciphertext)
                # print out the correct key. 
                print(str(line))