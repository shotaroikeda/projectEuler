# Project Euler Problem #2
# Find sum of even-valued terms to 4 million of Fibonacci Sequence
# @author: Shotaro Ikeda
# @netid: ikeda2
# @email: ikeda.shot@gmail.com
# @github: shotaroikeda
import math

n = 600851475143
listprimes = [2]


def main(n):
    if isprime(n) is True:
        print 'Number ', n, ' cannot be divided anymore'
    else:
        print 'Dividing', isprime(n)
        main(isprime(n))


def isprime(n):
    sqrtn = math.sqrt(n)
    for num in range(3, int(sqrtn), 2):
        if n % num == 0:
            return n / num
        elif n % 2 == 0:
            return n / 2
    return True


if __name__ == '__main__':
    main(n)
