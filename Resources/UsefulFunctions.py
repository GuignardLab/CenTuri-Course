import matplotlib.pyplot as plt

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
    return dt/tau * (a - i)

def plot_concentration_1cell(c1, c2=None, return_plot=False, save_path=None):
    """
    Plots the concentration evolution given a list of concentrations

    Args:
        c1 (list of floats): a list containing concentrations
        c2 (Optional, list of floats): a list containing concentrations
    """
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(c1, label='First concentration')
    if c2 is not None:
        ax.plot(c2, label='Second concentration')
        ax.legend()
    ax.set_xlabel('Time-point')
    ax.set_ylabel('Concentration')
    if save_path is not None:
        if save_path[-4:]!='.png':
            save_path += '.png'
        plt.savefig(save_path)
        plt.close(fig)
    if return_plot:
        return fig, ax

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

results_dict = {
    4: __question_4
}

params_dict = {
    4: """
    For this function, the following calling
    is expected (changing val as needed):
    answer_results(4, A=[val], I=[val],
                   dt=val, k=val, tau=val)
    """
}

def answer_results(q, **kwargs):
    """
    Returns the expected out for the question `q`

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
            print(params_dict.get(q, 'Unfortunately, no more help is there :/'))
            out = None
    else:
        print(f'Question {q} were not found')
        out = None
    return out
