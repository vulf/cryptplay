#!/usr/bin/python3

alphabet = [chr(ord('a')+x) for x in range(26)]
alph_bytes = [bytes(i, 'utf-8') for i in alphabet]
s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
s_bytes = bytes.fromhex(s)
msg = ''

for i in alph_bytes:
    for j in s_bytes:
        msg += (i ^ j)
    print(f'{i}: {msg}')
    msg = ''
