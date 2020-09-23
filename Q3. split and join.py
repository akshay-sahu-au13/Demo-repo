#Q3. ​https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    line = line.split()
    joinedLine = "-".join(line)

    return joinedLine

if __name__ == '__main__':