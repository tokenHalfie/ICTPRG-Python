a = open("input.txt","r")
string = a.read()
num = string.split("|")
total = 0
for x in num:
    total = total + int(x)
print("Sum of all Numbers is: ‭" + str(total) + "\n")