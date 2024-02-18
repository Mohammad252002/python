import matplotlib.pyplot as plt
def show(solution, n):
    plt.figure(figsize=(5,5))
    for i in range(n+1):
        plt.plot([0, n*2], [i*2, i*2], color='black')
        plt.plot([i*2, i*2], [0, n*2], color='black')

    for i in range(n):
        plt.scatter([i*2+1], [solution[i]*2+1], color='red')

    plt.show()