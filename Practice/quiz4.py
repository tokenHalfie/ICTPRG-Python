
def PrintBoxByWidth(width, height):
    
    for row in range(height): 
        for col in range(width):
            if ((col == 0 or col == width-1) or (row == 0 or row == height-1)):
                print("x", end="")
            elif (row == (height-1)/2) or((height % 2 == 0) and row == (height/2) or row == (height/2-1)):
                print("o", end='')
            else:
                print(" ", end='')
           
                      
        print("") 

            
PrintBoxByWidth(100, 100)