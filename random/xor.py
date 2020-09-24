#!/usr/bin/python3

def xor(a, b):
    print(f"a = {a}\nb = {b}")
    print("\n****\nhex\n****")
    print(f"a = {hex(a)}\nb = {hex(b)}")
    print("\n******\nbinary\n******")
    d1,d2 = 0,0
    if len(bin(a)) > len(bin(b)):
        d2 = len(bin(a)[2:])
    elif len(bin(b)) > len(bin(a)):
        d1 = len(bin(b)[2:])
    print(f"a = {bin(a)[2:].zfill(d1)}\nb = {bin(b)[2:].zfill(d2)}")
    print("\n*******\nXORing..\n*******")
    print(f"{a} ^ {b} = {a^b}")

def main():
    a,b = int(input()),int(input())
    xor(a,b)

if __name__ == '__main__':
    main()
