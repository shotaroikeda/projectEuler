# Project Euler Problem #3
# Find the palindrome of the multiplication of 2 3 digit numbers
# @author: Shotaro Ikeda
# @netid: ikeda2
# @email: ikeda.shot@gmail.com
# @github: shotaroikeda
from modules.stringtolist import StringList
# Define a palindrome...
# Will be using my module 'StringList'
# Input will be in a list


def ispalindrome(a_list):
    if len(a_list) % 2 == 0:
        lookto = len(a_list) / 2
    else:
        lookto = len(a_list) / 2 - 1
    for num in range(0, lookto):
        if a_list[num] != a_list[-(1+num)]:
            return False
    return True


def maxpalindrome(digits):
    # digits is how many digits you are multiplying. 3 = 3x3, 2 = 2x2, etc.
    maxlist = ['9'] * digits
    conv = StringList()
    maxnum = int(conv.convert(maxlist * 2))
    maxdivide = int(conv.convert(maxlist))
    mindivide = 10 ** (digits-1)
    return (maxnum, maxdivide, mindivide)


def listmath(curr_list, element):
    conv = StringList()
    if curr_list[-1] == '0':
        curr_list.pop()
    if curr_list[element] == '0':
        listmath(curr_list, element-1)
        listreset(curr_list, element)
    elif (len(curr_list) - 1) / 2 == element and len(curr_list) % 2 != 0:
        curr_list[element] = str(int(curr_list[element-1])-1)
    else:
        curr_list[element] = str(int(curr_list[element])-1)
        curr_list[-(element+1)] = str(int(curr_list[-(element+1)])-1)
    return int(conv.convert(curr_list))


def listreset(curr_list, element):
    if (len(curr_list) - 1) / 2 == element and len(curr_list) % 2 != 0:
        curr_list[element] = '9'
    else:
        curr_list[element] = '9'
        curr_list[-(element+1)] = '9'


def checkdivisible(currentnum, maxnum, minnum):
    for i in range(maxnum, minnum - 1, -1):
        if currentnum % i == 0:
            if i < maxnum and currentnum / i < maxnum:
                return (True, currentnum, i, currentnum / i)
    return (False,)


def main():
    digits = 3
    maxnum = maxpalindrome(digits)
    conv = StringList()
    currentnum = maxnum[0]
    solved = False
    while not solved or currentnum == maxnum[0]:
        curr_list = conv.convert(str(currentnum))
        if len(curr_list) % 2 == 0:
            element = len(curr_list) / 2 - 1
        else:
            element = (len(curr_list) - 1) / 2
        currentnum = listmath(curr_list, element)
        check = checkdivisible(currentnum, maxnum[1], maxnum[2])
        solved = check[0]
        if solved:
            currentnum = 'The Palindrome %d is made by %d and %d' % (
                check[1], check[2], check[3])
    print currentnum


def test():
    a = ['9', '0', '0', '9']
    b = ['9', '0', '0', '0', '0', '0', '0', '9']
    c = ['9', '0', '0', '0', '9']
    print ispalindrome(a)
    # Test maxpalindrome
    print maxpalindrome(3)
    print maxpalindrome(9)
    # Test listmath()
    print listmath(a, 1)
    print listmath(b, 3)
    print listmath(c, 2)

if __name__ == '__main__':
    main()
