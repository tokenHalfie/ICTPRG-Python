import re
def InputNumber():
    while True:
        try:
            number = int(input("Enter a Number: "))
            print(number)
            break
        except:
            print("That's not a number")

def GetElementAt(array,index):
    try:
        print(array[index])
        return array[index]
    except:
        print("Index is Out of Bounds")

def GetIpAddress():
    while True:
        try:
            ip = input("Enter an IP Address: ")
            test = ip.split(".")
            if len(test)!=4:
                print("Not a valid IP, incorrect number of numbers")
                raise ValueError
            if test[0] == 0:
                print("0 isnt valid")
                raise ValueError
            for x in test:
                x = int(x)
                if x > 255 or x < 0:
                    print("Not a valid IP, number is too large")
                    raise ValueError
            print (ip)
            return ip
        except:
            print("whoops")
            

def GetEmailAddress():
    while True:
        try:
            email = input("Enter an Email Address: ")
            test = email.split("@")
            for x in test:
                if len(x) > 16 or len(x) < 3:
                    raise ValueError
            if  "." in test[1]:
                print("Thats a valid email")
                print(email) 
                return email
            else:
                raise ValueError
        except:
            print("whoops")
            

def GetPassword():
    while True:
        try:
            cap = False
            low = False
            sym = False
            num = False
            symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
            password = input("Please enter a password: ")
            if len(password) < 7:
                print("too short")
                raise ValueError
            if "password" in password:
                print("Password is not a valid password,  duh")
                raise ValueError
            if (symbols.search(password) == None):
                sym = False
            else:
                sym = True
            for x in password:
                if cap == False:
                    if x.isupper():
                        cap = True
                if low == False:
                    if x.islower():
                        low = True
                if num == False:
                    if x.isdigit():
                        num = True
            if cap == True and low == True and sym == True and num == True:
                print("Congrats, your password is valid")
                return password  
            else:
                raise ValueError  
        except:
            print("whoops")
            
def GetWordsFromUser(min, max):
    while True:
        try:
            if (min >= max):
                print("Your min is higher or equal to your max")
                break
            words = input("Please enter a sentence between " + str(min) +" and " + str(max) + " words: ")
            words = words.lower()
            test = words.split(" ")
            if len(test) < min or len(test) > max:
                raise ValueError
            else:
                print("Good job, you follow the instructions")
                print(test)
                return test
        except:
            print("whoops")
GetWordsFromUser(3, 4)