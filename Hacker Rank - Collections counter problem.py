# Task
#
# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of their desired size.
#
# Your task is to compute how much money Raghu earned.

# Input Format
# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size desired by
# the customer and Xi, the price of the shoe.

# Sample Input
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# Sample Output
# 200

from collections import Counter

no_of_shoes = int(input(''))
shoe_size = Counter(map(int, input().split()))
no_of_customers = int(input(''))

money = 0

for i in range(no_of_customers):
    size, price = map(int, input().split())
    if shoe_size[size] != 0:
        money = money + price
        shoe_size[size] = shoe_size[size] - 1

print(money)
