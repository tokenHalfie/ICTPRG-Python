
student_scores = {'Adama': 100, 'Starbuck': 75, 'Apollo': 80, 'Athena': 85, 'Agathon': 90}
fileO = open("text.txt","w")

for score in student_scores.items():
    score=str(score)
    fileO.write(score + '\n')

fileO.close