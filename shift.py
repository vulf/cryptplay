#!/usr/bin/python3

def shift():
    m = input("enter message: ")
    m = m.lower()
    k = int(input("enter key: "))
    res = ''
    opt = input("encrypt or decrypt? (e/d): ")
    if opt == 'e':
        for i in m:
            res += chr( (((ord(i) - 97) + k) % 26)+97 )
        return print('secret: ' + res)
    elif opt == 'd':
        for i in m: 
            res += chr( (((ord(i) - 97) - k) % 26) + 97)
        return print('message: ' + res)

def main():
    shift()

if __name__ == '__main__':
    main()
