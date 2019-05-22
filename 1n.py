def number(z):
    y=0
    for x in range(z+1):
        y+=x
    return y

i = input("Please enter a number: ")
i=int(i)
print (number(i))
print (number(55))