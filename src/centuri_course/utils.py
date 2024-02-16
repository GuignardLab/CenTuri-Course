import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from IPython.display import HTML
from matplotlib import animation
from scipy.ndimage import convolve


def da_alone(a, dt, k):
    """
    Computes the change of concentration given an initial concentration `a`,
    a time increment `dt` and a constant `k`. Note that there is no `i` in
    the equation since it is supposed to be `a` alone.

    Args:
        a (float): The initial concentration value
        dt (float): the time increment
        k (float): the constant k

    Returns:
        (float): the change of concentration
    """
    return dt * (a - a**3 + k)


def da(a, i, dt, k):
    """
    Computes the change of concentration given an initial concentration `a`,
    a time increment `dt` and a constant `k`.

    Args:
        a (float): the initial concentration value
                   of the activator
        i (float): the initial concentration value
                   of the inhibitor
        dt (float): the time increment
        k (float): the constant k

    Returns:
        (float): the change of concentration
    """
    return dt * (a - a**3 - i + k)


def di(i, a, dt, tau):
    """
    Computes the change of concentration given an initial concentration `i`,
    a time increment `dt` and a constant `k`.

    Args:
        a (float): the initial concentration value
                   of the activator
        i (float): the initial concentration value
                   of the inhibitor
        dt (float): the time increment
        tau (float): the constant tau

    Returns:
        (float): the change of concentration
    """
    return dt / tau * (a - i)


def plot_concentration_1cell(c1, c2=None, return_plot=False, save_path=None):
    """
    Plots the concentration evolution given a list of concentrations

    Args:
        c1 (list of floats): a list containing concentrations
        c2 (Optional, list of floats): a list containing concentrations
    """
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(c1, label="First concentration")
    if c2 is not None:
        ax.plot(c2, label="Second concentration")
        ax.legend()
    ax.set_xlabel("Time-point")
    ax.set_ylabel("Concentration")
    fig.tight_layout()
    if save_path is not None:
        save_path = save_path.with_suffix(".png")
        plt.savefig(save_path)
        plt.close(fig)
    if return_plot:
        return fig, ax


def plot_concentration_1D(
    c1, c2=None, return_plot=False, save_path=None, step=100
):
    """
    Plots the concentration evolution given 1 or 2 array(s) of cells
    and concentrations. When two array are combined, the firs concentration
    is in the green and the second in the red. Both values are mixed.

    Args:
        c1 ndarray (n, m): array of concentration of n cells
                           over m time-points
        c2 ndarray (n, m): array of concentration of n cells
                           over m time-points
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    if c2 is None:
        im = ax.imshow(c1[:, ::step], interpolation="nearest")
        cbar = plt.colorbar(im)
        cbar.set_label("Concentration")
    else:
        max_ = np.max([c1, c2])
        min_ = np.min([c1, c2])
        rgb = np.array([c1, c2, np.zeros_like(c1)]).transpose(1, 2, 0)
        rgb = (rgb - min_) / (max_ - min_)
        im = ax.imshow(rgb[:, ::step, :], interpolation="nearest")
    ax.set_xlabel("Time-point")
    ax.set_ylabel("Cell #")
    ax.set_xticks(np.linspace(0, c1.shape[1] // step, 6).astype(int)[:-1])
    ax.set_xticklabels([f"{v*step:.0f}" for v in ax.get_xticks()])
    fig.tight_layout()
    if save_path is not None:
        save_path = save_path.with_suffix(".png")
        plt.savefig(save_path)
        plt.close(fig)
    if return_plot:
        return fig, ax


def __compute_AI(a, i, dt, k, tau, n):
    A, I = [a], [i]
    for t in range(n - 1):
        new_A = A[-1] + da(A[-1], I[-1], dt, k)
        new_I = I[-1] + di(I[-1], A[-1], dt, tau)
        I.append(new_I)
        A.append(new_A)
    return A, I


def retrieve_compute_AI():
    """
    Returns the function compute_AI
    """
    return __compute_AI


def __get_random_table(n, m, seed=0):
    np.random.seed(seed)
    return np.random.rand(n, m)


def get_random_table(n, m, seed=0):
    """
    Return a array of size n by m filled with
    random values between 0 and 1. The random
    values will always be the same thanks to the
    seed. The seed can be changed

    Args:
        n (int): first dimension of the array
        m (int): second dimension of the array
        seed (int): Determine the seed for the
                    random draw. Default 0.
                    If None, it will be different
                    each time it is ran.

    Returns:
        ndarray (n, m)
    """
    # Nope, you will not see the code in here!
    # I mean, if you really want to you can,
    # but that's cheating ...
    return __get_random_table(n, m, seed=seed)


def __question_4(*, A, I, dt, k, tau, n):
    if not isinstance(A, list):
        A = [A]
    if not isinstance(I, list):
        I = [I]
    for t in range(n):
        new_A = A[-1] + da(A[-1], I[-1], dt, k)
        new_I = I[-1] + di(I[-1], A[-1], dt, tau)
        I.append(new_I)
        A.append(new_A)
    return A, I


def __question_13(*, A, I, dt, k, tau, n):
    A = np.copy(A)
    I = np.copy(I)
    for cell_num, (a, i) in enumerate(zip(A[:, 0], I[:, 0])):
        A_cell, I_cell = __compute_AI(a, i, dt, k, tau, n)
        A[cell_num, :] = A_cell
        I[cell_num, :] = I_cell
    return A, I


def __question_14(*, A, I, dt, k, tau, dx, mu_a, mu_i):
    new_A = np.zeros_like(A)
    new_I = np.zeros_like(I)
    new_A[1:-1] = A[1:-1] + dt * (
        dx * mu_a * (A[:-2] + A[2:] - 2 * A[1:-1])
        + A[1:-1]
        - A[1:-1] ** 3
        - I[1:-1]
        + k
    )
    new_A[0] = A[0] + dt * (
        dx * mu_a * (A[1] - A[0]) + A[0] - A[0] ** 3 - I[0] + k
    )
    new_A[-1] = A[-1] + dt * (
        dx * mu_a * (A[-2] - A[-1]) + A[-1] - A[-1] ** 3 - I[-1] + k
    )

    new_I[1:-1] = I[1:-1] + dt / tau * (
        dx * mu_i * (I[:-2] + I[2:] - 2 * I[1:-1]) + A[1:-1] - I[1:-1]
    )
    new_I[0] = I[0] + dt / tau * (dx * mu_i * (I[1] - I[0]) + A[0] - I[0])
    new_I[-1] = I[-1] + dt / tau * (
        dx * mu_i * (I[-2] - I[-1]) + A[-1] - I[-1]
    )
    return new_A, new_I


def __question_16(*, arr, nb_neighbs, kernel, mu, dx, dy):
    to_cell = convolve(arr, kernel, mode="constant", cval=0)
    from_cell = nb_neighbs * arr
    out = mu * (to_cell - from_cell) / (dx * dy)
    return out


def __diffusion(arr, nb_neighbs, kernel, mu, dx, dy):
    to_cell = convolve(arr, kernel, mode="constant", cval=0)
    from_cell = nb_neighbs * arr
    out = mu * (to_cell - from_cell) / (dx * dy)
    return out


def __question_17(*, dt, k, tau, size, T, mu_a, mu_i, dx, dy, seed=0):
    n = int(T / dt)
    A = np.zeros((size, size, n))
    I = np.zeros((size, size, n))
    np.random.seed(seed)
    A[..., 0] = np.random.random((size, size))
    np.random.seed(seed + 1)
    I[..., 0] = np.random.random((size, size))

    kernel = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    mask = np.ones_like(A[..., 0])
    nb_neighbs = convolve(mask, kernel, mode="constant", cval=0)

    for t in range(1, n):
        diff_A = __diffusion(A[:, :, t - 1], nb_neighbs, kernel, mu_a, dx, dy)
        A[..., t] = A[..., t - 1] + dt * (
            diff_A + A[..., t - 1] - A[..., t - 1] ** 3 - I[..., t - 1] + k
        )
        diff_I = __diffusion(I[:, :, t - 1], nb_neighbs, kernel, mu_i, dx, dy)
        I[..., t] = I[..., t - 1] + dt / tau * (
            diff_I + A[..., t - 1] - I[..., t - 1]
        )

    return A, I


results_dict = {
    4: __question_4,
    13: __question_13,
    14: __question_14,
    16: __question_16,
    17: __question_17,
}


params_dict = {
    4: """
    For this function, the following calling
    is expected (changing val as needed):
    answer_results(4, A=[<val>], I=[<val>],
                   dt=<val>, k=<val>, tau=<val>)
    """,
    13: """
    For this function, the following calling
    is expected (changing val as needed):
    answer_results(13, A=A, I=I,
                   dt=<val>, k=<val>, tau=<val>)
    With A and I your tables with the first value
    initialized.
    """,
    14: """
    For this function, the following calling
    is expected (changing val as needed):
    answer_results(14, A=A, I=I,
                   dt=<val>, k=<val>, tau=<val>,
                   dx=<val>, mu_a=<val>, mu_i=<val>)
    With A and I a table of size nb_cells*1.
    """,
    16: """
    For this function, the following calling
    is expected (changing val as needed):
    answer_results(16, arr=arr, nb_neighbs=nb_neighbs,
                   kernel=kernel, mu=<val>, dx=<val>, dy=<val>)
    With arr and nb_neighbs a table of size `size`*`size`
    and kernel a table of `size` `s`*`s` with `s<=size`.
    """,
    17: """
    For this function, the following calling
    is expected (changing val as needed):
    answer_results(17, dt=<val>, k=<val>, tau=<val>,
                   size=<val>, T=<val>, mu_a=<val>,
                   mu_i=<val>, dx=<val>, dy=<val>, seed=0)
    with seed being a seed for the random generation
    of the initial concentrations
    """,
}


def answer_results(q, **kwargs):
    """
    Returns the expected output for the question `q`

    Args:
        q (int): the number of the question
        kwargs: the potential args of question q

    Returns:
        ??? It depends on which question was asked
    """
    if q in results_dict:
        try:
            out = results_dict[q](**kwargs)
        except Exception as e:
            print(e)
            print(
                params_dict.get(q, "Unfortunately, no more help is there :/")
            )
            out = None
    else:
        print(f"Question {q} were not found")
        out = None
    return out


from scipy.ndimage import gaussian_filter1d


def __build_curve(
    length=500,
    freq=0.03,
    min_height=1,
    max_height=10,
    start=15,
    start_freq=0.25,
    sigma=3,
):
    """
    Function that builds a curve with randomly positioned spikes.

    Params:
        length (int): length of the curve to create
        freq (float): floating number between 0 and 1.
            It is the frequency at which spikes happen
        min_height (float): minimum height of the spikes
        max_height (float): maximum height of the spikes
        start (float): Percentage at which the spikes start (delay)
        start_freq (float): frequency at wich the traces will
            actually start with a delay
        sigma (float): for nicer rendering, the curve is smoothed
            by a gaussian with the provided sigma

    Returns:
        curve (np.array): a 1d ndarray
    """
    spikes = np.random.rand(length) < freq
    start = start if start_freq < np.random.rand() else 0
    if start != 0:
        spikes[: int(length * start / 100) + sigma] = 0
        spikes[int(length * start / 100) + sigma] = True
    height = min_height + np.random.rand(length) * (max_height - min_height)
    curve = np.zeros_like(spikes, dtype=float)
    curve[spikes] = height[spikes]
    curve = gaussian_filter1d(curve, sigma=sigma)
    return curve


def __solution_1():
    nb_plots = 50
    max_height = 5
    min_height = 1
    length = 500
    freq = 0.03
    sigma = 3
    start = 25
    start_freq = 0.25
    cmap = mpl.cm.get_cmap("Spectral")
    fig, ax = plt.subplots(figsize=(10, 8))
    X = np.linspace(0, 10, length)
    for i in range(nb_plots):
        Y = build_curve(
            length, freq, min_height, max_height, start, start_freq, sigma
        )
        ax.plot(X, 3 * Y + i, color="k", linewidth=5, zorder=nb_plots - i)
        ax.plot(X, [i] * len(Y), color="k", linewidth=5, zorder=nb_plots - i)
        color = cmap(i / nb_plots)
        ax.fill_between(X, 3 * Y + i, i, color=color, zorder=nb_plots - i)

    ax.yaxis.set_tick_params(tick1On=False)
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, nb_plots + max_height)
    ax.axvline(10 * start / 100, ls="--", lw=0.75, color="black", zorder=250)
    ax.set_xticks(range(1, 10, 2))
    ax.spines["bottom"].set_bounds(1, 9)
    ax.yaxis.set_tick_params(labelleft=True)
    ax.set_yticks(np.arange(nb_plots))
    ax.set_yticklabels([f"Trace {i:02d}" for i in range(1, nb_plots + 1)])
    ax.set_xlabel(r"Time [$min$] (fake)")
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(10)
        tick.label.set_verticalalignment("bottom")

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    # Here is the offset
    ax.spines["bottom"].set_position(("outward", 2))

    fig.tight_layout()
    fig.savefig("Resources/exercice_1.png")


def __solution_2(data1):
    fig, ax = plt.subplots(figsize=(6, 5))
    for bin_num in range(10, 52, 20):
        ax.hist(
            data1,
            bins=bin_num,
            histtype="step",
            cumulative=True,
            lw=3,
            label=f"{bin_num} bins",
            alpha=0.75,
        )
    Y = np.ones_like(data1).cumsum()
    X = np.sort(data1)
    ax.plot(X, Y, lw=3, label="'inf' bins", alpha=0.75)
    ax.set_xlim(np.min(data1), np.max(data1))
    ax.set_ylim(0, len(data1) + 1)
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig("Resources/exercise_2.png")


def __solution_3():
    X1 = np.linspace(0, 2 * np.pi)
    X2 = np.linspace(0, 2 * np.pi)
    Y1 = np.sin(X1 * 2) / 2
    Y2 = np.cos(X2)

    def update(t):
        l1.set_data(X1[:t], Y1[:t])
        l2.set_data(X2[:t], Y2[:t])
        if 5 <= t < 30:
            ax.collections.clear()
            ax.fill_between(X1[5:t], Y1[5:t], Y2[5:t], color="y")

    fig, ax = plt.subplots(figsize=(10, 3))
    (l1,) = ax.plot(X1, Y1, "-o", label="sin", lw=5, ms=10, markevery=[-1])
    (l2,) = ax.plot(X2, Y2, "-o", label="cosin", lw=3, ms=10, markevery=[-1])
    ax.legend(loc="lower left")
    sns.despine(trim=True, offset=15, ax=ax)
    fig.tight_layout()
    anim = animation.FuncAnimation(fig, update, frames=50, interval=50)
    HTML(anim.to_jshtml())
    anim.save("Resources/cos-sin.gif")


def __solution_4():
    np.random.seed(1)
    nb = 200
    positions = np.random.uniform(0, 10, size=(nb, 2))

    def update(t):
        global scatter
        scatter.set_facecolors(colors[: t + 1])
        scatter.set_offsets(positions[:t, ...])
        scatter.set_sizes(sizes[:t])
        return (scatter,)

    cmap = mpl.cm.get_cmap("viridis")
    colors = np.linspace(0, 1, nb)
    sizes = np.linspace(10, 600, nb)
    np.random.shuffle(sizes)
    np.random.shuffle(colors)
    colors = cmap(colors)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect("equal")
    scatter = ax.scatter([], [], edgecolor="k", alpha=0.6)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis("off")
    fig.tight_layout()
    anim = animation.FuncAnimation(fig, update, frames=nb, interval=15)
    HTML(anim.to_jshtml())
    anim.save("Resources/square.gif")


def __solution_5():
    np.random.seed(1)
    nb = 150
    found = 0
    positions = []
    while found < nb:
        next_pos = np.random.uniform(1, 9, size=2)
        if np.sum((next_pos - [5, 5]) ** 2) < 4**2:
            positions.append(next_pos)
            found += 1
    positions = np.array(positions)
    # positions = np.random.uniform(1, 9, size=(nb, 2))

    # positions = positions[np.sum((positions - [5, 5])**2, axis=1)<16]

    def update(t):
        global scatter
        scatter.set_facecolors(colors[: t + 1])
        scatter.set_offsets(positions[:t, ...])
        scatter.set_sizes(sizes[:t])
        return (scatter,)

    cmap = mpl.cm.get_cmap("viridis")
    colors = np.linspace(0, 1, nb)
    sizes = np.linspace(10, 600, nb)
    np.random.shuffle(sizes)
    np.random.shuffle(colors)
    colors = cmap(colors)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect("equal")
    scatter = ax.scatter([], [], edgecolor="k", alpha=0.6)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.axis('off')
    fig.tight_layout()
    anim = animation.FuncAnimation(fig, update, frames=nb, interval=25)
    HTML(anim.to_jshtml())
    anim.save("Resources/circle.gif")


def build_curve(
    length=500,
    freq=0.03,
    min_height=1,
    max_height=10,
    start=15,
    start_freq=0.25,
    sigma=3,
):
    """
    Function that builds a curve with randomly positioned spikes.

    Params:
        length (int): length of the curve to create
        freq (float): floating number between 0 and 1.
            It is the frequency at which spikes happen
        min_height (float): minimum height of the spikes
        max_height (float): maximum height of the spikes
        start (float): Percentage at which the spikes start (delay)
        start_freq (float): frequency at wich the traces will
            actually start with a delay
        sigma (float): for nicer rendering, the curve is smoothed
            by a gaussian with the provided sigma

    Returns:
        curve (np.array): a 1d ndarray
    """
    return __build_curve(
        length=length,
        freq=freq,
        min_height=min_height,
        max_height=max_height,
        start=start,
        start_freq=start_freq,
        sigma=sigma,
    )
