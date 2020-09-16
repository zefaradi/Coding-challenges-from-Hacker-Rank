# You are given a string and your task is to swap cases. In other words, convert
# all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
 
# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    lst = list()
    lst2 = list()
    length = len(s)

    for i in range(length):
        lst = []
        lst.append(s[i])
        if s[i] == ' ' or s[i] == '"' or s[i] == '.'or or s[i] == "'" or s[i].isdigit():
            lst2.append(s[i])
            continue
        a = "".join(map(str,lst))
        if a.isupper():
            b = a.lower()
            lst2.append(b)
        elif a.islower():
            c = a.upper()
            lst2.append(c)
    a = "".join(map(str,lst2))
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
