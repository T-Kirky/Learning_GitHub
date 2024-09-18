import numpy as np
import matplotlib.pyplot as plt

# Generate data for the sine wave
x = np.linspace(0, 2 * np.pi, 1000)  # 1000 points between 0 and 2π
y_sin = np.sin(x)

# Create the plot
plt.plot(x, y_sin)

# Add labels and title
plt.title('Sine Wave - beeosahdkgasdf')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')

# Show the plot
plt.grid(True)  # Adds gridlines
plt.show()

# i don't know what is happening
#################
# Now I want to plot a cos function:
y_cos = np.cos(x)

plt.plot(x, y_cos)

plt.title('Cose wave')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')

# Show the plot
plt.grid(True)  # Adds gridlines
plt.show()
