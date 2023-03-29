import matplotlib.pyplot as plt
import numpy as np

def draw_penrose_triangle():
    fig, ax = plt.subplots()

    A = np.array([0, 0])
    B = np.array([1, 0])
    C = np.array([0.5, np.sqrt(3) / 2])
    D = np.array([0.5, 1 / (2 * np.sqrt(3))])
    E = np.array([0.5, 0])

    def draw_line(start, end):
        ax.plot(*zip(start, end), color='black')

    draw_line(A, B)
    draw_line(B, C)
    draw_line(C, A)
    draw_line(D, E)
    draw_line(D, B)
    draw_line(A, E)

    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.axis("off")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

draw_penrose_triangle()
