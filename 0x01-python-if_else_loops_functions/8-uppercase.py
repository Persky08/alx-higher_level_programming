#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            upper_str += chr(ord(char) - 32)
        else:
            upper_str += char
    print("{}".format(upper_str))
