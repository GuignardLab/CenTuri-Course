answer_dict = {
    1: """
mu_a = 2.8e-4
mu_i = 5e-3
tau = .1
k = -.005
size = 100
dx = dy = 2. / size
T = 9.0
dt = .001
n = int(T / dt)""",
    2: """
c = a
a = b
b = c
OR
a, b = b, a""",
    3: """
for t in range(n):
    a = a + da_alone(a, dt, k)""",
    4: """
for t in range(n):
    old_a = A[-1]
    new_a = old_a + da_alone(old_a, dt, k)
    A.append(new_a)
OR
for t in range(n):
    A.append(A[-1] + da_alone(A[-1], dt, k))""",
    5: """
for t in range(n):
    new_A = A[-1] + da(A[-1], I[-1], dt, k)
    new_I = I[-1] + di(I[-1], A[-1], dt, tau)
    I.append(new_I)
    A.append(new_A)

Note that in that case it is necessary
to make a temporary save of the concentration
values, maybe keep that in mind, this might
become handy later :| """,
    6: """
def compute_AI(a, i, dt, k, tau, n): # Don't forget to add arguments
    A, I = [a], [i]
    for t in range(n-1): # the -1 is because the first value
                         # is already in the array
        new_A = A[-1] + da(A[-1], I[-1], dt, k)
        new_I = I[-1] + di(I[-1], A[-1], dt, tau)
        I.append(new_I)
        A.append(new_A)
    return A, I""",
    7: """
for test_tau in np.linspace(.05, 1, 5):
    for test_k in np.linspace(-1, 1, 5):
        A, I = answer_results(4, A=0.4, I=0.15, dt=dt, k=test_k, tau=test_tau, n=n)
        plot_concentration_1cell(A, I,
                                 save_path=folder / f'k{test_k}_tau{test_tau}.png')

Note that this answer uses the answer_results function
but you should use your own!""",
    8: """
for file in p.iterdir(): f
    name = file.name  # get the name of the of the file
    if 'png' in name: # check if the file is a png file
                      # Note that it is always safer to
                      # check that you are actually working
                      # with the intended files to avoid
                      # removing unintended files!
        k_val, tau_val_png = name.split('_') # That is assuming that
                                             # your files have the format
                                             # described earlier
        new_folder = p / k_val # k_val is the name of the new folder
                               # p is the path to the folder containing
                               # the new folder, hence new_folder is the
                               # path to the new folder.
        if not new_folder.exists(): # checking if the new folder already exists
            Path.mkdir(new_folder)  # Create it if it does not
        file.rename(new_folder / name) #
        # Path.rename(f, new_folder / name) # Equivalent to the previous line""",
    9: """
A = np.zeros((size, n))""",
    10: """
out = A[:3, -8:]""",
    11: """
A[:, 0] = np.random.random(100)""",
    12: """
I = np.zeros((size, n))
I[:, 0] = np.random.random(100)""",
    13: """
# Compressed solution:
for cell_num, (a, i) in enumerate(zip(A[:, 0], I[:, 0])):
    A_cell, I_cell = compute_AI(a, i, dt, k, tau, n)
    A[cell_num, :] = A_cell
    I[cell_num, :] = I_cell

# Other solution:
for cell_num in range(size):
    a = A[cell_num, 0]
    i = I[cell_num, 0]
    A_cell, I_cell = compute_AI(a, i, dt, k, tau, n)
    A[cell_num, :] = A_cell
    I[cell_num, :] = I_cell

""",
    14: """
def dA_I(A, I, dt, k, tau, dx, mu_a, mu_i):
    new_A = np.zeros_like(A)
    new_I = np.zeros_like(I)
    # Global solution
    new_A[1:-1] = (A[1:-1] +
                   dt * (mu_a/dx*(A[:-2] + A[2:] - 2*A[1:-1]) +
                         A[1:-1] - A[1:-1]**3 - I[1:-1] + k))

    new_I[1:-1] = (I[1:-1] +
                   dt/tau * (mu_i/dx*(I[:-2] + I[2:] - 2*I[1:-1]) +
                             A[1:-1] - I[1:-1]))

    # Edge case handling: first (0) and last (-1) cells
    new_A[0] = (A[0] +
                dt * (mu_a/dx*(A[1] - A[0]) +
                      A[0] - A[0]**3 - I[0] + k))
    new_A[-1] = (A[-1] +
                 dt * (mu_a/dx*(A[-2] - A[-1]) +
                       A[-1] - A[-1]**3 - I[-1] + k))

    new_I[0] = (I[0] +
                dt/tau * (mu_i/dx*(I[1] - I[0]) +
                          A[0] - I[0]))
    new_I[-1] = (I[-1] +
                 dt/tau * (mu_i/dx*(I[-2] - I[-1]) +
                           A[-1] - I[-1]))
    return new_A, new_I""",
    16: """
def diffusion(arr, nb_neighbs, kernel, mu, dx, dy):
    to_cell = convolve(arr, kernel, mode='constant', cval=0)
    from_cell = nb_neighbs*arr
    out = mu*(to_cell - from_cell)/(dx*dy)
    return out""",
    17: """
def compute_turing(dt, k, tau, size, T,
                   mu_a, mu_i, dx, dy, seed=0):
    n = int(T/dt)
    A = np.zeros((size, size, n))
    I = np.zeros((size, size, n))
    np.random.seed(seed)
    A[:, :, 0] = np.random.random((size, size))
    np.random.seed(seed+1)
    I[:, :, 0] = np.random.random((size, size))

    kernel = [[0, 1, 0],
              [1, 0, 1],
              [0, 1, 0]]
    mask = np.ones_like(A[:, :, 0])
    nb_neighbs = convolve(mask, kernel, mode='constant', cval=0)

    for t in range(1, n):
        diff_A = diffusion(A[:, :, t-1], nb_neighbs, kernel, mu_a, dx, dy)
        A[..., t] = A[..., t-1] + dt*(diff_A + A[..., t-1] - A[..., t-1]**3 - I[..., t-1] + k)
        diff_I = diffusion(I[:, :, t-1], nb_neighbs, kernel, mu_i, dx, dy)
        I[..., t] = I[..., t-1] + dt/tau*(diff_I + A[..., t-1] - I[..., t-1])

    return A, I""",
}

hint_dict = {
    3: """
Don't forget that the function
returns the change, therefore,
that value needs to be added to
the original value to be valid.

Moreover, keep in mind that the
number of iterations that you
would like to do is calculated
and stored in the variable n.

Finally, the function da_dt_alone
can be called the following way:
da_dt_alone(a, dt, k)""",
    4: """
To access the last element of a list L
one can use L[-1].

To add an element to a list L, one can
use the function append:
L.append(<element>)""",
    5: """
It is important to remember that
it is necessary to make a copy
of the latest values of the list
before manipulating them.""",
    6: """
It is important to remember to
define the correct function
parameters and return values""",
    7: """
Remember to use the `?` to call
the help of a function (np.linspace).

Because we want to make two parameters
vary simultaneously, we need to have
a for loop within another one!""",
    8: """
Look at the following cells to see some advanced help""",
}


def answer(q):
    """
    Print the answer of the question `q`

    Args:
        q (int): the number of the question
    """
    print(answer_dict.get(q, f"Question {q} not found"))


def hint(q):
    """
    Print the hint of the question `q`

    Args:
        q (int): the number of the question
    """
    print(
        hint_dict.get(q, f"Unfortunately, there is no hint for question {q}")
    )
