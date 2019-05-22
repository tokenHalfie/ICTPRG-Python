prime = open("primenumbers.txt", "r")
happy = open("happynumbers.txt", "r")

primeNum = []
happyNum = []
happyPrime = []

num = prime.readline().rstrip()

while num:
    primeNum.append(num)
    num = prime.readline().rstrip()

num = happy.readline().rstrip()
while num:
    happyNum.append(num)
    num = happy.readline().rstrip()  

for x in primeNum:
    if x in happyNum:
        happyPrime.append(x)

print(happyPrime)