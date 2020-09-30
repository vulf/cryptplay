#!/usr/bin/python3
import sys

uri = sys.argv[1]
#OF = 'etaoin shrdlu cmfwyp vbgkjq xz'.replace(' ','')                                   # order of frequency of letters in the English alphabet
OF = 'etaoin shrdlu'.replace(' ','')                                   # order of frequency of letters in the English alphabet
pt = list()
abc = [(chr(i+97)).upper() for i in range(26)]
#print(abc)
mgram_frq = dict().fromkeys(abc, 0)
with open(uri, 'r') as f:                                           # get frequency of letters in the ciphertext
    for line in f:
        for cw in line.split():                                     # cw - word
            for cl in cw:                                           # cl - letter
                mgram_frq[cl] += 1

with open(uri, 'r') as f:
    for line in f:
        for cw in line.split():

#print(frq)
ltrs = list(mgram_frq.keys())
ltr_freq = list(mgram_frq.values())
zipped_lists = zip(ltr_freq, ltrs)
sorted_zippedlists = sorted(zipped_lists, reverse=True)             # sort according to descending order of frequencies
mgrams = [i[1] for i in sorted_zippedlists]                         # generate a list from the characters in sorted_zippedlists
#print(mgrams)

with open(uri, 'r') as f:
    for line in f:
        for cw in line.split():
            for cl in cw:
                i = mgrams.index(cl)
                if i < len(OF):
                    pt.append(OF[i])
                else:
                    pt.append(cl)
            pt.append(' ')

for i,j in zip(mgrams, OF):
    print(f'{i}:{j}', end=' ')
print(f"\n{''.join(pt)}")
