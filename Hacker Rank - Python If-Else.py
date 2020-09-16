# Python If-Else - Hacker Rank Coding Challenge
# Task
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# Input Format
# A single line containing a positive integer, .

# Constraints
#  1 <= n <= 100

# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.

n = int(input('Enter a number between 1 and 100 inclusive: '))

if (n <= 0 or n > 100):
    print('You have entered a number that is out of range')
    quit()

def EvenOrOdd(x):
    if (x % 2 == 0):
        return True
    else:
        return False

if (not EvenOrOdd(n)):
    print('Weird')
elif(EvenOrOdd(n) and n in range(2,6)):
    print('Not Weird')
elif(EvenOrOdd(n) and n in range(6,21)):
    print('Weird')
elif(EvenOrOdd(n) and n > 20):
    print('Not Weird')
