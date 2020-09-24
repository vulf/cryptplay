#!/usr/bin/python3
# Playfair cipher
from collections import OrderedDict

key = 'playfair example'
msg,msg_split = 'Hide the gold in the tree stump'.lower().replace(' ',''), list()
#key = input('enter key: ')                                              # ask key
#msg,msg_split = input('enter message: ').lower().replace(' ','') , list()
msg = list(msg.replace('j','i'))
key_nodups = ''.join(OrderedDict.fromkeys(key).keys()).replace(' ','')  # remove duplicate chars and spaces from key
keylen = len(key_nodups)                                                # get length of key 
abc = [chr(x+97) for x in range(26)]
if keylen < 25:
    for i in range(26):
        if abc[i]!='j' and abc[i] not in key_nodups : key_nodups += abc[i]
print(key_nodups)
table = list()                                                          # declare table is a list
i,rc,cc = 0,5,5                                                         # rc - row count, cc - column count
for r in range(rc):
    row = list() 
    for c in range(cc):
        row.append(key_nodups[i])
        i += 1
    table.append(row)
print('table')
for r in table: print(r)

# splitting the message
for i in range(0,len(msg),2):
    if i!=(len(msg)-1) and msg[i]!=msg[i+1]:
        msg_split.append(''.join(msg[i:i+2]))
    else:
        msg.insert((i+1), 'x')
        msg_split.append(''.join(msg[i:i+2]))

# encrypting msg_split
enc = ''
for pair in msg_split:
    f = False
    # rule 1 - same row
    for r in table:
        if pair[0] in r and pair[1] in r:
            index0 = r.index(pair[0])
            index1 = r.index(pair[1])
            enc += r[(index0+1) % 5] + r[(index1+1) % 5]
            f = True
    # rule 2 - same column
    if not f:
        for c in range(5):
            col = list()
            for r in range(5):
                col.append(table[r][c])
            if pair[0] in col and pair[1] in col:
                index0 = col.index(pair[0])
                index1 = col.index(pair[1])
                enc += table[(index0+1) % 5][c]
                enc += table[(index1+1) % 5][c]
                f = True
    # rule 3 - not on same row nor same column
    if not f:
        row0,col0,row1,col1 = 0,0,0,0
        for r in table:
            if pair[0] in r:
                row0 = table.index(r)
            elif pair[1] in r:
                row1 = table.index(r)
        # get column
        for r in range(5):
            for c in range(5):
                if table[r][c] == pair[1]:
                    col0 = c
                elif table[r][c] == pair[0]:
                    col1 = c
        enc += table[row0][col0]
        enc += table[row1][col1]

print(enc)

# decryption
ct = list(enc)
print(ct)
