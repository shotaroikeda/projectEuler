# Project Euler Problem #1
# Sum of Multiples of 3 and 5 below 1000

# @author: Shotaro Ikeda
# @netid: ikeda2
# @email: ikeda.shot@gmail.com
# @github: shotaroikeda
import math


def getprimeto(num):
    count = 2
    returned = 0
    while returned <= num:
        noreturn = False
        if count == 2:
            returned += 1
            yield count
        elif count % 2 == 0:
            count += 1
            continue
        for i in range(3, int(math.sqrt(count))+1, 2):
            if count % i == 0:
                noreturn = True
        count += 1
        if noreturn:
            continue
        else:
            returned += 1
            yield count - 1


def main():
    m = int(raw_input('Enter number: '))
    for i in getprimeto(m):
        prime = i
    print prime

if __name__ == '__main__':
    main()
