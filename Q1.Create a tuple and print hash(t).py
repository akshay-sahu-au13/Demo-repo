# Q1. ​https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    I = list(integer_list)

    t = tuple(I)

    print(hash(t))

