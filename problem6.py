# Project Euler Problem #1
# Sum of Multiples of 3 and 5 below 1000

# @author: Shotaro Ikeda
# @netid: ikeda2
# @email: ikeda.shot@gmail.com
# @github: shotaroikeda


def main(num):
    sumsquared = (num * (num + 1) / 2) ** 2
    squaredsum = num * (num + 1) * (2 * num + 1) / 6
    return sumsquared - squaredsum

if __name__ == '__main__':
    print main(10)
    print main(100)
