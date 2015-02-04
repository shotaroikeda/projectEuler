# Project Euler Problem #1
# Sum of Multiples of 3 and 5 below 1000

# @author: Shotaro Ikeda
# @netid: ikeda2
# @email: ikeda.shot@gmail.com
# @github: shotaroikeda
def main():
    n = 1000 #number to find sum up to is 1000
    result = 3 * tosum(333) + 5 * tosum(199)- 15 * tosum(66)
    print result

def tosum(endnum):
    return (endnum) * (endnum + 1) / 2





if __name__ == '__main__':
    main()








