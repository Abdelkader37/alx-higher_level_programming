#!/usr/bin/python3
for num in range(0, 99):
    print("{:02d}".format(num, hex(num)), end=', ')
print("{}".format(num + 1))
