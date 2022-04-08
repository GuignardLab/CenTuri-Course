# Table of contents
0. [Introduction](0-Introduction.ipynb)
1. [Variables]() $\leftarrow$
2. [Data structures](2-Data-Structures.ipynb)
3. [Conditional statements and loops](3-Conditional-Statements-Loops.ipynb)
4. [Some exercises](4-Some-Exercises.ipynb)
5. [Introduction to functions](5-0-Introduction-function.ipynb)
    1. [File manipulation](5-1-File-manipulation.ipynb)
6. [From 0D to 1D](6-1-From-0D-to-1D.ipynb)
    1. [Adding lateral diffusion](6-2-Adding-lateral-diffusion.ipynb)
7. [From 1D to 2D](7-From-1D-to-2D.ipynb)
8. [Playing with the model](8-Playing-with-the-model.ipynb)

## 1. Variables
---
Variables are symbolic names where information or values can be stored.

They are the cornerstone of coding, they allow you to store in memory values and to access them later on. In our example the variables have been described earlier (`mu_a`, `tau`, `size`, ...)

To assign an information to a variable, the `=` operator is used.

> ⚠️ be careful, `=` is the assignment operator. To check the equality between two variables, the required operator is `==` ⚠️

For example after the following line of code is ran:


```python
a_number = 0
a_number = 10
another_number = 1
```

The variable `a_number` used to contain the value `0` and now contains the value `10`.

The variable `another_number` contains the values `1`.

It is possible to display what is contained in a variable using the function `print` for example:


```python
print(f'{a_number = }')
```

The content of a variable can be stored in another variable and then changed without altering it:


```python
a_number = 5
another_number = a_number
a_number = 1
print(f'{another_number = }')
print(f'{a_number = }')
```

Variables can contain most (computational) things (especially in Python).
For example they can contain different types of data such as `list`, `dictionary` or `ndarray` (we will see what they are right after)

In variables can also be stored the result of an operation:


```python
nb1 = 1
nb2 = 3
sum_nb1_2 = nb1 + nb2
print(f'{nb1 = }')
print(f'{nb2 = }')
print(f'{sum_nb1_2 = }')
```

### 1.1 Exercises:
Before any exercise, import the `Correction` module which allows you to check out the correction of the exercises the following way:
```python
Correction(<exo_num>)
```
You can import the function as shown just below. It needs to be imported only once.


```python
from Resources.Answers import answer
```

#### Exercise 1
Set the value of the variables necessary for the model as follow:
- mu_a: 0.0002.8
- mu_i: 0.005
- tau: 0.1
- k: -0.005
- size: 100 
- dx: 2 divided by the size of the grid
- dy: 2 divided by the size of the grid
- T: 9
- dt: 0.001
- n: number of iterations which is the total time `T` divided by the time step `dt`


```python
### Write the answer of the previous question here.
# You can check the answer by running answer(1)
```

#### Exercise 2
Given a variable `nb1` and a variable `nb2`, put the values of each other variables in the other one

(Note that we are using the library `random` to generate random numbers)


```python
from random import randint # To generate random numbers so you can't really cheat
nb1 = randint(0, 5)
nb2 = randint(6, 10)
print('before')
print(f'{nb1 = }')
print(f'{nb2 = }')
'''
To do: swap a and b values
'''
print('after:')
print(f'{nb1 = }')
print(f'{nb2 = }')
```
