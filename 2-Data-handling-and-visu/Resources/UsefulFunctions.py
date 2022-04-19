from scipy.ndimage import gaussian_filter1d
import numpy as np

def __build_curve(length=500, freq=.03,
                  min_height=1, max_height=10,
                  start=15, start_freq=.25,
                  sigma=3):
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
    spikes = np.random.rand(length)<freq
    start = start if start_freq<np.random.rand() else 0
    if start!=0:
        spikes[:int(length*start/100)+sigma] = 0
        spikes[int(length*start/100)+sigma] = True
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
    freq = .03
    sigma = 3
    start = 25
    start_freq = .25
    cmap = mpl.cm.get_cmap("Spectral")
    fig, ax = plt.subplots(figsize=(10, 8))
    for i in range(nb_plots):
        Y = build_curve(length, freq, min_height, max_height,
                        start, start_freq, sigma)
        X = np.linspace(0, 10, len(Y))
        ax.plot(X, 3 * Y + i, color="k", linewidth=5, zorder=nb_plots - i)
        ax.plot(X, [i]*len(Y), color="k", linewidth=5, zorder=nb_plots - i)
        color = cmap(i / nb_plots)
        ax.fill_between(X, 3 * Y + i, i, color=color, zorder=nb_plots - i)
        
    ax.yaxis.set_tick_params(tick1On=False)
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, nb_plots+max_height)
    ax.axvline(10*start/100, ls="--", lw=0.75, color="black", zorder=250)
    ax.set_xticks(range(1, 10, 2))
    ax.spines['bottom'].set_bounds(1, 9)
    ax.yaxis.set_tick_params(labelleft=True)
    ax.set_yticks(np.arange(nb_plots))
    ax.set_yticklabels([f"Trace {i:02d}" for i in range(1, nb_plots+1)])
    ax.set_xlabel(r'Time [$min$] (fake)')
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(10)
        tick.label.set_verticalalignment("bottom")
        
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # Here is the offset
    ax.spines['bottom'].set_position(('outward', 2))

    fig.tight_layout()
    fig.savefig('Resources/exercice_1.png')

def __solution_2():
    fig, ax = plt.subplots(figsize=(6, 5))
    for bin_num in range(10, 52, 20):
        ax.hist(data1, bins=bin_num, histtype='step', cumulative=True,
                lw=3, label=f'{bin_num} bins', alpha=.75);
    Y = np.ones_like(data1).cumsum()
    X = np.sort(data1)
    ax.plot(X, Y, lw=3, label='\'inf\' bins', alpha=.75)
    ax.set_xlim(np.min(data1), np.max(data1))
    ax.set_ylim(0, len(data1)+1)
    ax.legend(loc='lower right')
    fig.tight_layout()
    fig.savefig('Resources/exercise_2.png')

def __solution_3():
    X1 = np.linspace(0, 2*np.pi)
    X2 = np.linspace(0, 2*np.pi)
    Y1 = np.sin(X1*2)/2
    Y2 = np.cos(X2)

    def update(t):
        l1.set_data(X1[:t], Y1[:t])
        l2.set_data(X2[:t], Y2[:t])
        if 5<=t<30:
            ax.collections.clear()
            ax.fill_between(X1[5:t], Y1[5:t], Y2[5:t], color='y')

    fig, ax = plt.subplots(figsize=(10, 3))
    l1, = ax.plot(X1, Y1, '-o', label='sin', lw=5, ms=10, markevery=[-1])
    l2, = ax.plot(X2, Y2, '-o', label='cosin', lw=3, ms=10, markevery=[-1])
    ax.legend(loc='lower left')
    sns.despine(trim=True, offset=15, ax=ax)
    fig.tight_layout()
    anim = animation.FuncAnimation(fig, update, frames=50, interval=50)
    HTML(anim.to_jshtml())
    anim.save('Resources/cos-sin.gif')

def __solution_4():
    np.random.seed(1)
    nb = 200
    positions = np.random.uniform(0, 10, size=(nb, 2))

    def update(t):
        global scatter
        scatter.set_facecolors(colors[:t+1])
        scatter.set_offsets(positions[:t, ...])
        scatter.set_sizes(sizes[:t])
        return scatter,

    cmap = mpl.cm.get_cmap('viridis')
    colors = np.linspace(0, 1, nb)
    sizes = np.linspace(10, 600, nb)
    np.random.shuffle(sizes)
    np.random.shuffle(colors)
    colors = cmap(colors)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect('equal')
    scatter = ax.scatter([], [], edgecolor='k', alpha=.6)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis('off')
    fig.tight_layout()
    anim = animation.FuncAnimation(fig, update, frames=nb, interval=15)
    HTML(anim.to_jshtml())
    anim.save('Resources/square.gif')

def __solution_5():
    np.random.seed(1)
    nb = 150
    found = 0
    positions = []
    while found<nb:
        next_pos = np.random.uniform(1, 9, size=2)
        if np.sum((next_pos - [5, 5])**2)<4**2:
            positions.append(next_pos)
            found+=1
    positions = np.array(positions)
    # positions = np.random.uniform(1, 9, size=(nb, 2))

    # positions = positions[np.sum((positions - [5, 5])**2, axis=1)<16]

    def update(t):
        global scatter
        scatter.set_facecolors(colors[:t+1])
        scatter.set_offsets(positions[:t, ...])
        scatter.set_sizes(sizes[:t])
        return scatter,

    cmap = mpl.cm.get_cmap('viridis')
    colors = np.linspace(0, 1, nb)
    sizes = np.linspace(10, 600, nb)
    np.random.shuffle(sizes)
    np.random.shuffle(colors)
    colors = cmap(colors)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect('equal')
    scatter = ax.scatter([], [], edgecolor='k', alpha=.6)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.axis('off')
    fig.tight_layout()
    anim = animation.FuncAnimation(fig, update, frames=nb, interval=25)
    HTML(anim.to_jshtml())
    anim.save('Resources/circle.gif')



def build_curve(length=500, freq=.03,
                min_height=1, max_height=10,
                start=15, start_freq=.25,
                sigma=3):
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
    return __build_curve(length=length, freq=freq,
                         min_height=min_height, max_height=max_height,
                         start=start, start_freq=start_freq,
                         sigma=sigma)