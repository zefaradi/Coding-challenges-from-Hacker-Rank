# Text wrap

# You are given a string  and width S.
# Your task is to wrap the string into a paragraph of width w.

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output 0
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap
def wrap(string, max_width):
    a = ''
    for i in range(0, len(string), max_width):
        a = a + string[i:i+max_width] + '\n'
    return(a)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = (wrap(string, max_width))
    print(result)
