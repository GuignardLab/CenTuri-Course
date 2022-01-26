answer_dict = {
    1: """a = 2.8e-4
b = 5e-3
tau = .1
k = -.005
size = 100
dx = 2. / size
T = 9.0
dt = .001
n = int(T / dt)""",
    2: """c = a
a = b
b = c
OR
a, b = b, a"""

}

def answer(n):
    print(answer_dict.get(n, f"Question {n} not found"))