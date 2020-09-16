# Given the names and grades for each student in a class of  students, store them
# in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their
# names alphabetically and print each name on a new line.

# Input Format

# The first line contains an integer, , the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there
# are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 0
# Berry
# Harry

counts = dict()
lst = list()
lst2 = list()
lst3 = list()
for i in range(int(input())):
    name = input()
    score = float(input())
    # Make a dictionary of names and grades
    counts[name] = score

# convert the dictionary into a list
for key,value in counts.items():
    newtup = (value,key)
    lst.append(newtup)

min_score = min(lst)
min_score2 = min_score[0]

length = len(lst)

# Make a new list with the lowest grade removed
for s in range(length):
    if(lst[s][0] != min_score2):
        lst2.append(lst[s])

min_score3 = min(lst2)
min_score4 = min_score3[0]
length2 = len(lst2)

# Make a new list with only the second lowest grades
for k in range(length2):
    if (lst2[k][0] == min_score4):
        lst3.append(lst2[k][1])

# Printing the names in an alphabetical order
lst3.sort()
for a in range(len(lst3)):
    print(lst3[a])
