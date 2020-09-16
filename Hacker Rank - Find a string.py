# In this challenge, the user enters a string and a substring. You have to print
# the number of times that the substring occurs in the given string. String traversal
# will take place from left to right, not from right to left.

# Input Format

# The first line of input contains the original string. The next line contains
# the substring.

# Output Format

# Output the integer number indicating the total number of occurrences of the
# substring in the original string.

# Sample Input
# ABCDCDC
# CDC

# Sample Output 
# 2

def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string)):
        a = string[i:(len(sub_string)+i)]
        if sub_string in a:
            cnt +=1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
