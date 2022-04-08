# Table of contents
0. [Introduction](0-Introduction.ipynb)
1. [Variables](1-Variables.ipynb)
2. [Data structures](2-Data-Structures.ipynb)
3. [Conditional statements and loops](3-Conditional-Statements-Loops.ipynb)
4. [Some exercises](4-Some-Exercises.ipynb)
5. [Introduction to functions](5-0-Introduction-function.ipynb)
    1. [File manipulation](5-1-File-manipulation.ipynb)
6. [From 0D to 1D](6-1-From-0D-to-1D.ipynb)
    1. [Adding lateral diffusion](6-2-Adding-lateral-diffusion.ipynb)
7. [From 1D to 2D](7-From-1D-to-2D.ipynb)
8. [Playing with the model](8-Playing-with-the-model.ipynb) $\leftarrow$

# 8 Playing with the model and its parameters


```python
# importing the numpy library
import numpy as np
from scipy.ndimage import convolve
# importing the useful functions
from Resources.UsefulFunctions import *
from Resources.Answers import answer, hint

# and carrying over the previously declared variables
mu_a = 2.8e-4
mu_i = 5e-3
tau = .1
k = -.005
size = 100
dx = dy = 2. / size
T = 9.0
dt = .001
n = int(T / dt)

# redeclaring the diffusion function (put yours here)
def diffusion(arr, nb_neighbs, kernel, mu, dx, dy):
    to_cell = convolve(arr, kernel, mode='constant', cval=0)
    from_cell = nb_neighbs*arr
    out = mu*(to_cell - from_cell)/(dx*dy)
    return out
```


```python
T = 40
dt = .01
tau = 2
k = .05
A, I = answer_results(17, dt=dt, k=k, tau=tau,
                      size=size, T=T, mu_a=mu_a,
                      mu_i=mu_i, dx=dx, dy=dy)

```


```python
from matplotlib import animation
from IPython.display import HTML

fig, ax = plt.subplots(figsize=(5, 5))
ax.axis('off')
im = ax.imshow(A[..., 0], interpolation='bilinear')
fig.tight_layout()

def init():
    im.set_data(A_anim[..., 0])
    return(im,)

def animate(i):
    im.set_data(A_anim[...,i])
    return(im,)

nb_times_im = 50
A_anim = A[..., ::A.shape[-1]//nb_times_im]
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nb_times_im, interval=25, 
                               blit=True)

HTML(anim.to_jshtml())
```

## Oriented diffusion

The kernel we defined earlier shows a diffusion that is uniform in each direction.

We can change it to simulate oriented diffusion:

```python
kernel = np.array([[0, .5, 0],
                   [1,  0, 0],
                   [0, .5, 0]])
```
The kernel above just means that there is no diffusion from any cell to their right hand neighbors and that the "up" and "down" diffusion are twice as low as the diffusion towards the left.

Let see what it does to our model:


```python
def compute_turing_kernel(dt, k, tau, size, T,
                          mu_a, mu_i, dx, dy,
                          kernel, seed=0):
    n = int(T/dt)
    A = np.zeros((size, size, n))
    I = np.zeros((size, size, n))
    np.random.seed(seed)
    A[:, :, 0] = np.random.random((size, size))
    np.random.seed(seed+1)
    I[:, :, 0] = np.random.random((size, size))

    mask = np.ones_like(A[:, :, 0])
    nb_neighbs = convolve(mask, kernel, mode='constant', cval=0)

    for t in range(1, n):
        diff_A = diffusion(A[:, :, t-1], nb_neighbs, kernel, mu_a, dx, dy)
        A[..., t] = A[..., t-1] + dt*(diff_A + A[..., t-1] - A[..., t-1]**3 - I[..., t-1] + k)
        diff_I = diffusion(I[:, :, t-1], nb_neighbs, kernel, mu_i, dx, dy)
        I[..., t] = I[..., t-1] + dt/tau*(diff_I + A[..., t-1] - I[..., t-1])


    return A, I

T = 200
dt = .025
tau = 2
k = .05
kernel = [[0,  .5,  0],
          [1,   0,  0],
          [0,  .5,  0]]
A, I = compute_turing_kernel(dt, k, tau, size, T, mu_a, mu_i, dx, dy, kernel)
#Note that the only change we made was to change the kernel
```


```python
fig, ax = plt.subplots(figsize=(5, 5))
ax.axis('off')
im = ax.imshow(A[..., 0], interpolation='bilinear')
fig.tight_layout()

def init():
    im.set_data(A_anim[..., 0])
    return(im,)

def animate(i):
    im.set_data(A_anim[...,i])
    return(im,)

nb_times_im = 100
A_anim = A[..., ::A.shape[-1]//nb_times_im]
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nb_times_im, interval=25, 
                               blit=True)

HTML(anim.to_jshtml())
```

Now there is two perpendicular patterns.
The thing is that the right handside pattern might be due to odd things happening because we are at the edge and there is only latteral diffusion without any source effect.

Instead of a source effect we can actually make our sheet a "tube".
To do so, the only thing we have to do is to say that any intensity that is present in the left hand side of our grid is duplicated to the right hand side.
In practice, what it means is that the left and right most columns are actually the same in our model.

To copy such values we can simply do it the following way:
```python
A[:, -1, t] = A[:, 0, t]
I[:, -1, t] = I[:, 0, t]
```


```python
def compute_turing_kernel(dt, k, tau, size, T,
                          mu_a, mu_i, dx, dy,
                          kernel, seed=0):
    n = int(T/dt)
    A = np.zeros((size, size, n))
    I = np.zeros((size, size, n))
    np.random.seed(seed)
    A[:, :, 0] = np.random.random((size, size))
    np.random.seed(seed+1)
    I[:, :, 0] = np.random.random((size, size))

    mask = np.ones_like(A[:, :, 0])
    nb_neighbs = convolve(mask, kernel, mode='constant', cval=0)

    for t in range(1, n):
        diff_A = diffusion(A[:, :, t-1], nb_neighbs, kernel, mu_a, dx, dy)
        A[..., t] = A[..., t-1] + dt*(diff_A + A[..., t-1] - A[..., t-1]**3 - I[..., t-1] + k)
        diff_I = diffusion(I[:, :, t-1], nb_neighbs, kernel, mu_i, dx, dy)
        I[..., t] = I[..., t-1] + dt/tau*(diff_I + A[..., t-1] - I[..., t-1])
        # Here is our simple addition
        A[:, -1, t] = A[:, 0, t]
        I[:, -1, t] = I[:, 0, t]


    return A, I

T = 600
dt = .1
tau = 3
k = .05
kernel = [[0,  .5,  0],
          [1,   0,  0],
          [0,  .5,  0]]
A, I = compute_turing_kernel(dt, k, tau, size, T, mu_a, mu_i, dx, dy, kernel)
```


```python
fig, ax = plt.subplots(figsize=(5, 5))
ax.axis('off')
im = ax.imshow(A[..., 0], interpolation='bilinear')
fig.tight_layout()

def init():
    im.set_data(A_anim[..., 0])
    return(im,)

def animate(i):
    im.set_data(A_anim[...,i])
    return(im,)

nb_times_im = 100
A_anim = A[..., ::A.shape[-1]//nb_times_im]
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nb_times_im, interval=25, 
                               blit=True)

HTML(anim.to_jshtml())
```

### Changing the seed


```python
A, I = compute_turing_kernel(dt, k, tau, size, T, mu_a, mu_i, dx, dy, kernel, seed=2)
```


```python
fig, ax = plt.subplots(figsize=(5, 5))
ax.axis('off')
im = ax.imshow(A[..., 0], interpolation='bilinear')
fig.tight_layout()

def init():
    im.set_data(A_anim[..., 0])
    return(im,)

def animate(i):
    im.set_data(A_anim[...,i])
    return(im,)

nb_times_im = 100
A_anim = A[..., ::A.shape[-1]//nb_times_im]
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nb_times_im, interval=25, 
                               blit=True)

HTML(anim.to_jshtml())
```
