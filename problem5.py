# Project Euler Problem #3
# Find the palindrome of the multiplication of 2 3 digit numbers
# @author: Shotaro Ikeda
# @netid: ikeda2
# @email: ikeda.shot@gmail.com
# @github: shotaroikeda
import math


def primefactor(num, primelist, factors):
    while not isprime(num):
        for i in primelist:
            if num % i == 0:
                if i in factors:
                    factors[i] += 1
                else:
                    factors.update({i: 1})
                num /= i
                break
    if isprime(num):
        if num in factors:
            factors[i] += 1
        else:
            factors.update({num: 1})


def primenum(num):
    primelist = []
    operate = num
    while operate > 1:
        if isprime(operate):
            primelist.append(operate)
        operate -= 1
    primelist.reverse()
    return primelist


def isprime(operate):
    if operate == 2:
        return True
    elif operate % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(operate)) + 1, 2):
        if operate % i == 0:
            return False
    return True


def newprimefactor(num):
    factors = {}
    primelist = primenum(num)
    primefactor(num, primelist, factors)
    return factors


def main():
    num = 20
    fact_list = []
    for i in range(2, num):
        fact_list.append(newprimefactor(i))
    maxval = {}
    for i in fact_list:
        for key, value in i.items():
            if key not in maxval:
                maxval.update({key: value})
            else:
                curr = maxval.get(key)
                if key ** curr < key ** value:
                    maxval.update({key: value})
    ans = 1
    for key, value in maxval.items():
        ans *= key**value
    return ans


def test():
    num = 4
    a = newprimefactor(num)
    return a

if __name__ == '__main__':
    print main()
