import matplotlib.pyplot as plt

# Center of circles
x0, y0 = 0, 0

# Radii of circles
radii = [1, 2, 3, 4, 5]

# Plot circles
for r in radii:
    circle = plt.Circle((x0, y0), r, fill=False)
    plt.gca().add_artist(circle)

# Add labels to plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Five circles with different radii and the same center')

# Display plot
plt.show()
