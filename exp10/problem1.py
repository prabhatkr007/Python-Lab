import math
import matplotlib.pyplot as plt

# Function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Points A and B
xA, yA = 2, 3
xB, yB = 8, 12

# Midpoints of AB
xM = (xA + xB) / 2
yM = (yA + yB) / 2

# Calculate distance between A and B
dist = distance(xA, yA, xB, yB)

# Plot points A, B, and M
plt.plot([xA, xB], [yA, yB], 'ro')
plt.plot(xM, yM, 'bo')

# Add distance label to plot
plt.annotate(f"{dist:.2f}", xy=((xA + xB) / 2, (yA + yB) / 2), xytext=(-20, 10),
             textcoords='offset points', ha='center', va='bottom')

# Add labels to plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Distance between two points')

# Display plot
plt.show()
