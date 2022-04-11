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