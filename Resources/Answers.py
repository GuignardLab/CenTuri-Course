answer_dict = {
    1: """
a = 2.8e-4
b = 5e-3
tau = .1
k = -.005
size = 100
dx = 2. / size
T = 9.0
dt = .001
n = int(T / dt)""",

    2: """
c = a
a = b
b = c
OR
a, b = b, a""",

    3:"""
for t in range(n):
    a = a + da_alone(a, dt, k)""",

    4:"""
for t in range(n):
    old_a = A[-1]
    new_a = old_a + da_alone(old_a, dt, k)
    A.append(new_a)
OR
for t in range(n):
    A.append(A[-1] + da_alone(A[-1], dt, k))""",

    5:"""
for t in range(n):
    new_A = A[-1] + da(A[-1], I[-1], dt, k)
    new_I = I[-1] + di(I[-1], A[-1], dt, tau)
    I.append(new_I)
    A.append(new_A)

Note that in that case it is necessary
to make a temporary save of the concentration
values, maybe keep that in mind, this might
become handy later :| """,

    6:"""
def compute_AI(a, i, dt, k, tau, n): # Don't forget to add arguments
    A, I = [a], [i]
    for t in range(n):
        new_A = A[-1] + da(A[-1], I[-1], dt, k)
        new_I = I[-1] + di(I[-1], A[-1], dt, tau)
        I.append(new_I)
        A.append(new_A)
    return A, I""",

    7:"""
for test_tau in np.linspace(.05, 1, 5):
    for test_k in np.linspace(-1, 1, 5):
        A, I = answer_results(4, A=0.4, I=0.15, dt=dt, k=test_k, tau=test_tau, n=n)
        plot_concentration_1cell(A, I,
                                 save_path=folder / f'k{test_k}_tau{test_tau}.png')

Note that this answer uses the answer_results function
but you should use your own!""",
}

hint_dict = {
    3:"""
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

    4:"""
To access the last element of a list L
one can use L[-1].

To add an element to a list L, one can
use the function append:
L.append(<element>)""",

    5:"""
It is important to remember that
it is necessary to make a copy
of the latest values of the list
before manipulating them.""",

    6:"""
It is important to remember to
define the correct function
parameters and return values""",


    7:"""
Remember to use the `?` to call
the help of a function (np.linspace).

Because we want to make two parameters
vary simultaneously, we need to have
a for loop within another one!"""
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
    print(hint_dict.get(q, f"Unfortunately, there is no hint for question {q}"))