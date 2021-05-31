#testing this here
users = ["user1", "user2","user3"]
password = ["pass1", "pass2", "pass3"]
username = False
passx = False
attempts = 1


while (((username == False) or (passx == False)) and (attempts <= 3)):
    i = input ("Please enter your username: ")
    j = input ("Please enter your password: ")
    attempts+=1

    for x, z in enumerate(users):
        if ((z == i) and (password[x] == j)):
            username = True
            passx = True
      
    
           
   

if ((username == True) and (passx == True)):
    print("Login successful")
else:
    print("Login failed")
