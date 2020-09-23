# Q5. ​https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):

    S = string
    ss = sub_string
    Count = 0

    for i in range(0,len(S)-len(ss)+1):
        
        if S[i:i+len(ss)] == ss:

            Count += 1

    return Count

print(count_substring("ABCDCDC","CDC"))