#Author: 
#Steven Richards <sbrichards@{mit.edu, gnu.org}>
#Binary Based AES256 Point-to-Point Laser Encoding

import audiere
import base64
import os
from Crypto.Cipher import AES
from time import sleep
from math import sqrt
key = raw_input("Enter a key with a length of 16, or 32 Characters: ")
mode = AES.MODE_ECB #ECB AES
encryptor = AES.new(key, mode)
#device = audiere.open_device()#Open and assign the audio device

openfile = raw_input("Enter path to file: ")#File to encrypt
f = open(openfile)
file_data = f.read()#Read whole file into memory

if len(key) == 16:
  file_data += "\n" * (16-len(file_data) % 16)#Make length of file data 16 
else:
  file_data += "\n" * (32-len(file_data) % 32)#Make length of file data 32

enc_file = base64.b64encode(encryptor.encrypt(file_data))#Encrypt
enc_file = (bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in enc_file), 0)))
enc_file = enc_file[2:]
brokenstring = ''
def new_frequency(char):
    sleep(0.001)
    if char == '1':
	return 500
    elif char == '0':
	return 1000

def toneplayer(char):
    tone = device.create_tone(new_frequency(char))
    tone.play()

for char in enc_file:
  toneplayer(char)
f.close()

#print brokenstring
#
#if len(key) == 16:
#  brokenstring += "\n" * (16-len(brokenstring) % 16)#Make length of file data 16 
#else:
#  brokenstring += "\n" * (32-len(brokenstring) % 32)
#string = encryptor.decrypt(base64.b64decode(brokenstring))
#
#print string