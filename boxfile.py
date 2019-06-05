def PrintBoxByWidth(width, height, user):
    a = open("box.txt","w")
    row = 0
    
    while row < height: 
        col = 0
        while col < width:
            if (row == 0 or row == height-1) and (col == (width-1)/2):
                a.write("*")
            elif (row == 0 and col == 0) or (row == height-1 and col == width-1):
                a.write ("/")
            elif (row == 0 and col == width-1) or (row == height-1 and col == 0):
                a.write ("\\")
            elif (row == 0 or row == height-1) and (col != 0 or col != width-1 or col != (width-1)/2):
                a.write("-")
            elif ((col == 0 or col == width-1 or col == (width-1)/2)) and (row != 0 or row != width-1):
                a.write("|")
            elif (row == height/2 and col == 1) or (row == height/2 and col == (width+1)/2):
                a.write(user)
                col = col + len(user) - 1
            else:
                a.write(" ")
            col = col + 1   
                      
        a.write("\n")             
        row = row + 1
text = input("Please enter the word to be put in the box: ")
PrintBoxByWidth((len(text)*2+3), 8, text)
