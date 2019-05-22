i = input ("Please enter a sentence: ").split()
x = len(i)
x = int(x)
if x<3:
    print(i[0])
else:
    print(i[2])
    for j, h in enumerate(i):
        if ((j != 0) and (j != x-1)) :
            print(h)
