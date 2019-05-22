def rat():
    for x in range(5):
       
        for z in range(5, x, -1):
            print ("x", end="")
        print ("")    

def pyr():
    v = 8
    w = v-3
    for x in range(0,v+3,+2):
        for z in range(w):
            print (" ",end="")
        w = w-1
        
        for z in range(x+1):
            print("x", end="")
            
       
        print("")

def border():
    a = ["Hello", "World", "in", "a", "frame","superlongword"]
    b = max(a, key=len)
    c = int(len(b))
    for f in range(c+4):
        print("*", end="")
    print("")    
    
    for i in a:
        z = int(len(i))
        if (z < c):
            print("*",i,end="")
            for f in range(c-z+1):
                print(" ",end="")
            print("*")  
          
        else:
            print("*",i, "*") 
    for f in range(c+4):
        print("*", end="")
border()
