# Q2.​https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    S1 = ""
    for i in s:
        if i.islower():
            i = i.upper()
            
        elif i.isupper():
            i = i.lower()

        else:
            pass
        S1 += i
    return S1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)