import matplotlib.pyplot as plt

# Define the vertices of the pentagon
vertices = [(0, 1), (1, 0.309), (0.809, -0.588), (-0.809, -0.588), (-1, 0.309)]

# Define the colors for each block
colors = ['red', 'green', 'blue', 'yellow', 'purple']

# Plot the pentagon and fill each block with a different color
fig, ax = plt.subplots()
for i in range(5):
    ax.fill([vertices[i][0], vertices[(i+1)%5][0], 0], [vertices[i][1], vertices[(i+1)%5][1], 0], color=colors[i])

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Pentagon with different color blocks')

# Set the aspect ratio to 1
ax.set_aspect('equal')

# Show the plot
plt.show()
