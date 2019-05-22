dollars = 12345
def menu():

    print ("Enter Pin")
    m = input ("")
    if m.isdigit():
        if m == 1234:
            balance()
        else:
            print("PIN in incorrect")
            menu()
    else:
        print("Please enter a valid selection")
        menu()

def balance():
    print("Your balance is $" + dollars)    
    print("Please take your card")   

menu()