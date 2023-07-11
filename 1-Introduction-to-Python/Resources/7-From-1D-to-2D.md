[&larr; previous](6-2-Adding-lateral-diffusion.md) - [home](https://guignardlab.github.io/CenTuri-Course/) - [next &rarr;](8-Playing-with-the-model.md)

# Table of contents
0. [Introduction](0-Introduction.md)
1. [Variables](1-Variables.md)
2. [Data structures](2-Data-Structures.md)
3. [Conditional statements and loops](3-Conditional-Statements-Loops.md)
4. [Some exercises](4-Some-Exercises.md)
5. [Introduction to functions](5-0-Introduction-function.md)
    1. [File manipulation](5-1-File-manipulation.md)
6. [From 0D to 1D](6-1-From-0D-to-1D.md)
    1. [Adding lateral diffusion](6-2-Adding-lateral-diffusion.md)
7. [From 1D to 2D](7-From-1D-to-2D.md) &larr; ([Notebook](../7-From-1D-to-2D.ipynb))
8. [Playing with the model](8-Playing-with-the-model.md)

## 7. From 1 to 2D!

Now, we've seen diffusion in 1 dimension, expanding it to 2 dimensions is not that complicated.

First we need to create our array of cells. This is an array of dimension `(size, size, n)`. We will therefore have `size*size` cells over `n` time-points:


```python
# importing the numpy library
import numpy as np
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
```


```python
A = np.zeros((size, size, n))
I = np.zeros((size, size, n))
```

Then, initialise the first time-point:


```python
np.random.seed(0)
A[:, :, 0] = np.random.random((size, size))
np.random.seed(1)
I[:, :, 0] = np.random.random((size, size))
```

Now, the non-diffusive term of our equation are "simple":
```python
A[:, :, t] = A[:, :, t-1] + dt*(A[:, :, t-1] - A[:, :, t-1]**3 + k)
```
and
```python
I[:, :, t] = I[:, :, t-1] + dt/tau*(A[:, :, t-1] - I[:, :, t-1])
```

The diffusion term is slightly more complex since we have to look in the two dimensions as opposed to only one dimension as we did before.

Within each cell at a given position `i, j` at time `t` we want to add the concentration of the cells directly next to it at time `t-1`, this is the diffusion of the neighbouring cells to that cell:
```python
diff_A[i, j] = A[i-1, j, t-1] + A[i+1, j, t-1] + A[i, j-1, t-1] + A[i, j+1, t-1]
```
- `A[i-1, j  , t-1]` is the concentration value at time `t-1` of the left hand cell.
- `A[i+1, j  , t-1]` is the concentration value at time `t-1` of the right hand cell.
- `A[i  , j-1, t-1]` is the concentration value at time `t-1` of the lower cell.
- `A[i  , j+1, t-1]` is the concentration value at time `t-1` of the upper cell.

We then need to subtract 4 times the value at the concentration of that cell, this is the diffusion of that cell towards its 4 neighbours:

```python
diff_A[i, j] = diff_A[i, j] - 4*A[i, j, t-1]
```

This value needs to be normalised by the diffusion coefficient $mu_a$ or $mu_i$, the time step $\delta t$ and the spatial resolution in x and y $\delta x$ and $\delta y$:
```python
diff_A[i, j] = dt*mu_a(  A[i-1, j  , t-1]
                       + A[i+1, j  , t-1]
                       + A[i  , j-1, t-1]
                       + A[i  , j+1, t-1]
                       - 4*A[i, j, t-1])/(dx*dy)
```

(Note that the diffusion is shown for the activator `A` but it is similarly computed for the inhibitor `I`)

Now, there are two important things to notice in the computation of `diff_A` (resp. `diff_I`):
- we are adding the value of the cells around
- we are subtracting the value of the current cell as many times as it has neighbours.

There is a way to "directly" compute how much a cell is receiving from its neighbours by using the convolution operator.

For example, given an image `I` and a kernel `k`:
```python
k = [[ 0, .5,  0],
     [.5,  2, .5],
     [ 0, .5,  0]]
```
convolving `I` by `k` (giving the image `cI`) means that each pixel of `I` will be have a new value:
```python
cI[i, j] =(   .5 * I[i-1, j  ]
            + .5 * I[i+1, j  ]
            + .5 * I[i  , j-1]
            + .5 * I[i  , j+1]
            +  2 * I[i  , j  ] )
```

This is really close to what we want to do for our diffusion term.

What would be the kernel that we would like to have to compute the diffusion of neighbouring cells to any given cell?


```python
# Write here the kernel
# kernel = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
kernel = np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]])
    
```

Now we have our kernel and our initial image, we can use the convolve function from scipy:


```python
from scipy.ndimage import convolve
convolve?
```

We can use it the following way:


```python
to_cell = convolve(A[..., 0], kernel, mode='constant', cval=0)
```

Now, because we don't alway have the same number of neighbours, we need to calculate it before subtracting to have our full diffusion term.

Using the convolution, can you think of a way to count the number of neighbours for each cell?


```python
# Think about how to do it
nb_neighbs = ...
```

Assuming that we have computed the number of neighbours we can compute our diffusion term as follow:


```python
# to_cell = convolve(A[..., 0], k, mode='constant', cval=0)
# from_cell = nb_neighbs * A[..., 0]
# diff_A = to_cell - from_cell
```

### Exercise 16
Write a function `diffusion` that takes as an input an array of cells `arr`, the number of neighbours `nb_neighbs`, a kernel `kernel` a diffusion coefficient `mu` and the `dx` and `dy` resolution and outputs the diffusion term.


```python
## Here you write the function
def diffusion(arr, nb_neighbs, kernel, mu, dx, dy):
    arr_diff = np.zeros_like(arr)
    return arr_diff
    
```


```python
np.random.seed(0)
A[:, :, 0] = np.random.random((size, size))
np.random.seed(1)
I[:, :, 0] = np.random.random((size, size))

kernel = np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]])
mask = np.ones_like(A[:, :, 0])
nb_neighbs = convolve(mask, kernel, mode='constant', cval=0)

diff_A = diffusion(A[..., 0], nb_neighbs, kernel, mu_a, dx, dy)
diff_I = diffusion(I[..., 0], nb_neighbs, kernel, mu_i, dx, dy)
test_diff_A = answer_results(16, arr=A[:, :, 0], 
                             nb_neighbs=nb_neighbs,
                             kernel=kernel, mu=mu_a,
                             dx=dx, dy=dy)
test_diff_I = answer_results(16, arr=I[:, :, 0], 
                             nb_neighbs=nb_neighbs,
                             kernel=kernel, mu=mu_i,
                             dx=dx, dy=dy)
if np.alltrue(diff_A==test_diff_A) and np.alltrue(diff_I==test_diff_I):
    print('My results are the same as what is expected')
elif np.allclose(diff_A, test_diff_A) and np.allclose(diff_I, test_diff_I):
    print('My results are all close to what is expected')
else:
    print('My results are different to what was expected')
```

### Almost there!
Now, we know how to compute all the terms of the equation for both the activator and the inhibitor.

### Exercise 17
Write a function that takes as an input the parameters of the model and returns two arrays of size `size x size x n` with all the computed states of our turing model.


```python
import numpy as np
from scipy.ndimage import convolve
mu_a = 2.8e-4
mu_i = 5e-3
tau = .1
k = -.005
size = 100
dx = dy = 2. / size
T = 9.0
dt = .001

def diffusion(arr, nb_neighbs, kernel, mu, dx, dy):
    to_cell = convolve(arr, kernel, mode='constant', cval=0)
    from_cell = nb_neighbs*arr
    out = mu*(to_cell - from_cell)/(dx*dy)
    return out

# Write the function here:
def compute_turing(dt, k, tau, size, T,
                   mu_a, mu_i, dx, dy, seed=0):
    ...
    
# A, I = compute_turing(dt, k, tau, size, T, mu_a, mu_i, dx, dy)
```

## Displaying the result

We can now display the result of our modeling using matplotlib.

Though it is not completely trivial since it is a 3D data (2D + time).

First of, we can at least look at some specific time points using the function imshow of matplotlib:


```python
import matplotlib.pyplot as plt
# Recomputing the previous results if necessary. Comment if it is not necessary.
A, I = answer_results(17, dt=dt, k=k, tau=tau,
                      size=size, T=T, mu_a=mu_a,
                      mu_i=mu_i, dx=dx, dy=dy)
```


```python
plt.imshow(A[..., -1])
```

We can improve a bit the display:


```python
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(A[..., -1])
ax.set_axis_off()
fig.tight_layout()
```

We can show multiple time points at a time:


```python
nb_TP = 9
n = A.shape[-1]
x_dim = int(nb_TP**.5)
y_dim = nb_TP//x_dim
if  x_dim*y_dim < nb_TP:
    y_dim += 1
fig, axes = plt.subplots(x_dim, y_dim, figsize=(6, 6))
for i, ax in enumerate(axes.flatten()):
    ax.imshow(A[..., int(i*n/nb_TP)])
    ax.set_axis_off()
    ax.set_title(f'Time {int(i*n/nb_TP)*dt}')
fig.tight_layout()
# int(nb_TP**.5)
```

Now, we can also build animation of the model:


```python
from matplotlib import animation
from IPython.display import HTML

fig, ax = plt.subplots(figsize=(5, 5))
ax.axis('off')
im = ax.imshow(A[..., 0], interpolation='bilinear');
fig.tight_layout()

def init():
    im.set_data(A_anim[..., 0]);
    return(im,)

def animate(i):
    im.set_data(A_anim[...,i]);
    return(im,)

nb_times_im = 100
A_anim = A[..., ::A.shape[-1]//nb_times_im]
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nb_times_im, interval=25, 
                               blit=True);

HTML(anim.to_jshtml())
```


```python
anim.save('My-first-Turing-Pattern.gif')
```

[&larr; previous](6-2-Adding-lateral-diffusion.md) - [home](https://guignardlab.github.io/CenTuri-Course/) - [next &rarr;](8-Playing-with-the-model.md)