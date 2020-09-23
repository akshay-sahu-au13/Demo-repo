# Q6. ​https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    L = s.split(" ")
    S = []
    for i in L:
        S.append(i.capitalize())
    Str = " ".join(S)
    return Str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
