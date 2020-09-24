#!/usr/bin/python3
# vigenere cipher
from math import ceil

s = input('enter message/ciphertext: ').lower().replace(' ','')
key = input('enter key: ').lower()
opt = input('encrypt or decrypt? (e/d): ')
msg = ''
if opt == 'e':
   key = key*ceil(len(s)/len(key))
   for i,j in zip(s,key):
       msg += chr( ( ( (ord(i)-97) + (ord(j)-97) ) % 26 ) + 97 )
   print(f'ciphertext: {msg}') 
elif opt == 'd':
    key = key*ceil(len(s)/len(key))
    for i,j in zip(s,key):
        msg += chr( ( ( (ord(i)-97) - (ord(j)-97) ) % 26 ) + 97)
    print(f'message: {msg}')
