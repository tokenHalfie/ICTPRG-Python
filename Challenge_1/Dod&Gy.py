import subprocess
import sys

# runExe takes two parameters and runs CrackMe.exe.  It will return the result of CrackMe.exe as a string
# username: string
# pin: int
# return: string
usernames=[ "ihencke0@about.me", "kbrimblecombe1@deviantart.com", "apurslow2@dyndns.org", "hmacsharry3@answers.com", "hdomleog@taobao.com", "rperl5@youku.com", 
"svany6@apple.com", "bhewlings7@tiny.cc", "wgounet8@ox.ac.uk", "gwebley4@rediff.com", "wcruxtona@apple.com", "vburkittb@webeden.co.uk", "iandrejsc@wordpress.com",
"ecockshutd@oakley.com", "jpoinsette@macromedia.com", "ghurlestonf@nydailynews.com", "jreyner9@wiley.com", "kcasserlyh@jugem.jp", "awhickmani@networksolutions.com"]
validUser=[]
validPin=[]
def runExe(username, pin):
    out = subprocess.check_output(["CrackMe.exe", username, str(pin)], shell=True)
    out = str(out, 'utf-8')
    out = out.strip()
    return out

# Checks each username with each possible pin
def crack():    
    for user in usernames:
        output = runExe(user, 000)
        if (output == "User not found"):
            print(output)
        else:
            print(user)
            for pi in range(000, 1000):
                pi = str("{:03}".format(pi))
                output = runExe(user, pi)
                if (output != "Incorrect Pin"):
                    validUser.append(user)
                    validPin.append(pi)
                    break
    print("Crack has finished")
    menu()
                
def menu():
    menuSel = input("Choose an option:\n1. Run Crack\n2. Display Found usernames and pins\n3. Quit\n")
    if menuCheck(menuSel):
        if (menuSel == "1"):
            crack()
        elif (menuSel == "2"):
            display()           
        elif (menuSel == "3"):
            sys.exit

def display():
    for x, z in enumerate(validUser):
        print(z +" " +validPin[x])
        
    menu()  

def menuCheck(check):
    if check.isdigit():
        check = int(check)
        if (check < 4):
            return True
        else:
            print("That's not an option")
            return False
    else:
        print("Please enter an number")
        return False
    
menu()
