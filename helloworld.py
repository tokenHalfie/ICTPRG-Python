x = 0
y = 0
z = 0
op = 0
results =[]

def menu():
    global results
    f=open("numbers.txt","r")
  
    print ("Please choose a menu item")
    print ("1. Do an equation")
    print ("2. Previous results")
    print ("3. Quit")
    m = input ("")
    if m.isdigit():
        m = int(m)
        if m == 1:
            firstInput()
            secInput()
            opInput()
            results.append(z)
            print(z)
            menu()
        elif m == 2:
            for i in results:
                print(i)
            menu()        
        elif m == 3:
            save()
            print("Thank you, exiting now")
            exit   
    else:
        print("Please enter a valid selection")
        menu()
        
def firstInput():
    global x
    x = input("Please enter your first number: ")
    if x.isdigit():
        x = int(x)
    else:
        print("That's not a number")
        firstInput()

def secInput():        
    global y
    y = input("Please enter your second number: ")
    if y.isdigit():
        y = int(y)
    else:
        print("That's not a number")
        secInput()

def opInput ():
    global op
    global z
    op = input("What do you want to do to them? + - * / ")
    
    if op == "+":
        z = int(x + y)
    elif op == "-":
        z = int(x - y)
    elif op == "*":
        z = int(x * y)
    elif op == "/":
        z = int(x / y)
    else:
        op = ""
        print("Please choose a mathmatical operator")

def save():
    f = open("numbers.txt","a")
    for i in results:
        f.write(i)
    f.close()    
menu()