#!/usr/bin/python3
'''
A program that reads a test file and prints it out
'''

def read_file(filename=""):
    with open(filename, mode = 'r', encoding = 'utf-8') as file:
        print(file.read())
