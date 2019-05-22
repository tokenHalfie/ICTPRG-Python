game = [[1, 2, 1],
	    [2, 2, 0],
	    [1, 2, 1]]

for x, y in enumerate (game):
    if game[x][0] == game[x][1] == game[x][2]:
        print ("player " + str(game[x][0]) + " wins")

for x, y in enumerate (game):
    if game[0][x] == game[1][x] == game[2][x]:
        print ("player " + str(game[0][x]) + " wins")

if game[0][0] == game[1][1] == game[2][2]:
    print ("player " + str(game[0][0]) + " wins")

if game[0][2] == game[1][1] == game[2][0]:
    print ("player " + str(game[0][0]) + " wins")