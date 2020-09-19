#!/usr/bin/python3
from base64 import b64decode

ct = input("enter the base64 encoded text: ")
msg = b64decode(ct).decode('utf-8')
print(f'secret: {msg}')
