# Project Euler Problem #2
# Find sum of even-valued terms to 4 million of Fibonacci Sequence
# @author: Shotaro Ikeda
# @netid: ikeda2
# @email: ikeda.shot@gmail.com
# @github: shotaroikeda
n = 4000000


def main():
    sumfib = 0
    print evenfib()
    for num in evenfib():
        sumfib += num
    print sumfib


def evenfib():
    fibseq = [2, 8]
    while fibseq[-1] < n:
        fibseq.append(fibseq[-2] + 4 * fibseq[-1])
    fibseq.pop()
    return fibseq

if __name__ == '__main__':
    main()
