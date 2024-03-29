# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

n = 100
R, scatter, fig, ax = None, None, None, None


def init_rain():
    global n, R, scatter, fig, ax
    R = np.zeros(
        n,
        dtype=[
            ("position", float, (2,)),
            ("size", float, (1,)),
            ("color", float, (4,)),
        ],
    )
    fig = plt.figure(figsize=(6, 2), facecolor="white", dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)  # , aspect=1)
    scatter = ax.scatter(
        [], [], s=[], linewidth=0.5, edgecolors=[], facecolors="None"
    )


def rain_update(frame):
    global R, scatter

    R["color"][:, 3] = np.maximum(0, R["color"][:, 3] - 1 / len(R))
    R["size"] += 1 / len(R)

    i = frame % len(R)
    R["position"][i] = np.random.uniform(0, 1, 2)
    R["size"][i] = 0
    R["color"][i, 3] = 1

    scatter.set_edgecolors(R["color"])
    scatter.set_sizes(1000 * R["size"].ravel())
    scatter.set_offsets(R["position"])

    return (scatter,)


def run_rain():
    init_rain()
    global R, fig, ax
    R["position"] = np.random.uniform(0, 1, (n, 2))
    R["size"] = np.linspace(0, 1, n).reshape(n, 1)
    R["color"][:, 3] = np.linspace(0, 1, n)

    ax.set_xlim(0, 1), ax.set_xticks([])
    ax.set_ylim(0, 1), ax.set_yticks([])

    anim = animation.FuncAnimation(fig, rain_update, interval=10, frames=200)
    return anim
