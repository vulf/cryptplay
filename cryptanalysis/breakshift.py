#!/usr/bin/python3
# Bruteforce shift cipher
import sys

res = list()
word_dec = ''
uri = sys.argv[1]
alphabet = [chr(x+97) for x in range(26)]
for key in alphabet:
    with open(uri,'r') as f:
        print(f'KEY = {key}')
        for line in f:
            for word in line.split():
                word = word.lower()
                for c in word:
                    word_dec += chr( ( ( (ord(c) - 97) - (ord(key) - 97) ) % 26 ) + 97 )
                res.append(word_dec)
                word_dec = ''
        s = ' '.join(res)
        print(f'{s}\n')
        res.clear()
