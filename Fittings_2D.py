import matplotlib.pyplot as plt
import numpy as np

def random_data(n):
    x = np.random.rand(n)
    y = 2 * x + 1 + np.random.normal(0, 0.5, n)  # Linear relation with some noise
    return x, y

if __name__ == "__main__":
    x,y=random_data(100)
    plt.scatter(x,y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
