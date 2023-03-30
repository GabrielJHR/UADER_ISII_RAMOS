import matplotlib.pyplot as plt
import numpy as np

def collatz_sequence():
    ax = []
    ay = []
    for i in range(1, 11):
        n = i
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = (3 * n) + 1
            count += 1
        
        ax.append(i)
        ay.append(count)
        
    # X axis parameter:
    xaxis = np.array(ax)

    # Y axis parameter:
    yaxis = np.array(ay)

    plt.plot(xaxis, yaxis)
    plt.show()

collatz_sequence()



