#!/usr/bin/python3
# hex to base64
from base64 import b64encode, b64decode

msg = input('enter hex string: ')
msg_bytes = bytes.fromhex(msg)
b64_enc = b64encode(msg_bytes)
print(f'Base64 encoded data: {b64_enc.decode("utf-8")}')
b64_dec = b64decode(b64_enc)
print(f'Base64 decoded data: {b64_dec.decode("utf-8")}')
