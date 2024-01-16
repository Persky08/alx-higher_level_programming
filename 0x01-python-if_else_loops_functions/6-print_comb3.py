#!/usr/bin/python3
for first in range(10):
    for second in range(10):
        if first == 8 and second == 9:
            print("89")
        elif first < second:
            print(f"{first}{second}", end=", ")
