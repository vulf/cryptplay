#!/usr/bin/python3

def xor(a, b):
    a_hexdec = bytes.fromhex(a)
    b_hexdec = bytes.fromhex(b)
    res = ''
    res = [hex(i ^ j).lstrip('0x') for i,j in zip(a_hexdec, b_hexdec)]
    res = ''.join(str(x) for x in res)
    return 'xor: ' + res

def main():
    a, b = input('enter 2 strings of equal length: '), input()
    if len(a) == len(b):
        print(xor(a,b))
    else:
        print('unequal lengths')

if __name__ == '__main__':
    main()
