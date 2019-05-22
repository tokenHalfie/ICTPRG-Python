import matplotlib.pyplot as plt
import math

points= []
stepVal=0.001
sinVal=0

while sinVal < math.pi*12:
    points.append(math.sin(sinVal))
    sinVal+=stepVal




plt.plot(points)
plt.ylabel('some numbers')
plt.show()