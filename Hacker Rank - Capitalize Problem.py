# You are asked to ensure that the first and last names of people begin with a capital
# letter in their passports. For example, alison heck should be capitalised correctly
# as Alison Heck.

# Sample Input
# chris alan

# Sample Output
# Chris Alan

def solve(s):
    name = s.split(' ')
    # return(' '.join(word.capitalize() for word in name))
    if name[0][0].isupper() == False:
        first_name = list(name[0])
        a = first_name[0]
        b = a.upper()
        first_name[0] = b
        d = ''.join(map(str,first_name))

    if name[1][0].isupper() == False:
        last_name = list(name[1])
        e = last_name[0]
        f = e.upper()
        last_name[0] = f
        g = ''.join(map(str,last_name))

    return(d,g)

if __name__ == '__main__':
    n = input('')
    result = solve(n)
    print(" ".join(map(str,result)))
