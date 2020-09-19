#!/usr/bin/python3

msg = input('enter msg: ').lower()
ct = input('enter ciphertext: ').lower()
diff = [abs(ord(i)-ord(j)) for i,j in zip(msg,ct)]
print(diff)
