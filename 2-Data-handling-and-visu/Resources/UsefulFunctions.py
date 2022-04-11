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

def __solution():
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