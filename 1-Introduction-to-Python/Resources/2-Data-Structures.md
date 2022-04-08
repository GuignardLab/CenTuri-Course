[&larr; previous](1-Variables.md) - [next &rarr;](3-Conditional-Statements-Loops.md)

# Table of contents
0. [Introduction](0-Introduction.md)
1. [Variables](1-Variables.md)
2. [Data structures](2-Data-Structures.md) &larr;
3. [Conditional statements and loops](3-Conditional-Statements-Loops.md)
4. [Some exercises](4-Some-Exercises.md)
5. [Introduction to functions](5-0-Introduction-function.md)
    1. [File manipulation](5-1-File-manipulation.md)
6. [From 0D to 1D](6-1-From-0D-to-1D.md)
    1. [Adding lateral diffusion](6-2-Adding-lateral-diffusion.md)
7. [From 1D to 2D](7-From-1D-to-2D.md)
8. [Playing with the model](8-Playing-with-the-model.md)

## 2. Data structures
When coding, different data types and data structures can be used. For example we already saw few data types:
- Integers (referred to as `int` in Python): `0`, `1`, `-10`, ...
- Floating numbers (referred to as `float` in Python): `0.01`, `1.0`, `1.2e10`, ...
- Strings (referred to as `str` in Python): `'Hello'`, `"world"`, `'12+34'`, ...

But of course other data types exist:
- Lists (`list`): `[1, 2, 3]`, `[1, None, 0.4]`, `[1, [1, 2], [3], ['Hello'], 'World']`, ...
- Tuples (`tuple`): `(1, 2, 3)`, `(1, None, 0.4)`, ...
- Dictionaries (`dict`): `{'a': 10, 3:[2, 3, 4], '5': -0.2}`, ...

### 2.1 The lists: `list`
As their name suggests a `list` allows to store a list of elements. These elements can then be accessed via their position, starting at `0`.

There is a lot of possible operations on lists that can be found [there](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

The Python language is so that a `list` is surrounded by brackets:


```python
l1 = [1, 2, 3, 4]
print(f'{l1      = }')
print(f'positions: 0  1  2  3')
print(f'{l1[0] = }')
print(f'{l1[3] = }')
```

It is also possible to access to the values in a list using negative numbers, `-1` being the last element, `-2` the one before last and so on and so forth:


```python
print(f'{l1       = }')
print(f'positions: -4 -3 -2 -1')
print(f'{l1[-1] = }')
print(f'{l1[-3] = }')
```

It is also possible to access part of the list, it is called a slice.

To do so the syntax is the following:
```
list[start:stop:step]
```
`start` is included, `stop` is not, `step` is the step size.


```python
l1 = list(range(3, 13))
print(f'{l1          = }')
print(f'positions --> {list(range(len(l1)))}')
print(f'{l1[3:7]     = }')
print(f'{l1[:2]      = }')
print(f'{l1[6:]      = }')
print(f'{l1[1:7:2]   = }')
```

A `list` can be modified by adding values into them using the method `append`:


```python
l1 = [1, 2, 3, 4]
print(f'{l1    = }')
l1.append('hello')
print(f'{l1    = }')
print(f'{l1[4] = }')
```

They can also be modified by removing elements from it using the method `pop` which removes the last element of the list by default:


```python
l1 = [1, 2, 3, 4]
print(f'{l1 = }')
l1.pop()
print(f'{l1 = }')
```

By removing a specific element of the list using the method `remove`:


```python
l1 = [4, 5, 6, 7]
print(f'{l1 = }')
l1.remove(5)
print(f'{l1 = }')
```

Or by modifying already existing values by accessing them:


```python
l1 = [1, 2, 3, 4]
print(f'{l1 = }')
l1[1] = 3
print(f'{l1 = }')
l1[2] = l1[0]+1
print(f'{l1 = }')
```

Two lists can be concatenated together either by using the method `extend` or the `+` operator.

> ⚠️ It is important to remember that the `extend` method is performed 'in place' meaning that it modifies the list from which it is called from ⚠️


```python
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']
l3 = l1 + l2
print(f'{l3 = }')
l1.extend(l2)
print(f'{l1 = }')
l4 = l1 + l2
print(f'{l4 = }')
```

### 2.2 The dictionaries: `dict`
A dictionary is a data structure that maps a key to a value. It is somewhat similar to a `list` except that instead of referring to a value by its position in the `list` it is referred to by its key.

Dictionaries are defined using curved brackets `{}`:


```python
d1 = {4: '1', '3':'Hello'}
print(f'{d1      = }')
print(f'{d1[4]   = }')
print(f"{d1['3'] = }")
```

For reasons that we will not explain here, a `list` cannot be used as a key for a dictionary (though it can be used as values):


```python
d1 = {1: [1, 2, 3, 4], 4:4}
print(f'{d1 = }')
```


```python
try:
    d1 = {[1, 2]: 1}
except Exception as e:
    print(f'The error was:\n\t{e}')
```

Dictionaries can be modified but cannot be sliced (since there is no explicit order on the keys):


```python
d1 = {1: [1, 2, 3, 4], 4:4}
print(f'{d1 = }')
d1[3] = 5
d1[1].append(5)
print(f'{d1 = }')
```

You can find more information about dictionaries [there](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### 2.3 The numpy arrays `ndarray`
A very useful data structure is the `ndarray` from [NumPy](https://numpy.org/). It is usually very fast and allows you to manipulate arrays of $n$ dimensions (hence the name).

`ndarray` are complex data structures and we will not go in depth into what you can do with them here, we will only look at what we need along the class.
> _**To go a little bit further (not required):**_
>
> You can find more information about `ndarray` [there](https://numpy.org/doc/stable/reference/arrays.ndarray.html)
>
> If you want to learn interactively about `ndarray`, you can check out the [following exercises](https://www.machinelearningplus.com/python/101-numpy-exercises-python/).

Note that the previous exercises are not required but they could be very useful for the following classes.

To use `ndarray`, it is necessary to load the NumPy library (and therefore for it to be installed):


```python
import numpy as np
```

Then, one can create a `ndarray` the following ways (note that many other ways exist):


```python
arr1 = np.array([[1, 2, 3], [2, 3, 4]]) # Create an array from a list
arr2 = np.zeros((4, 4))                 # Create an array filled with 0s of size 4x4
arr3 = np.arange(10)                    # Create a 1d array with values from 0 to 9
print(f'arr1 -->\n{arr1}')
print(f'arr2 -->\n{arr2}')
print(f'arr3 -->\n{arr3}')
```

`ndarray` are useful because many operations can be performed on them in a direct and optimised way.

The same access operations and slicing as the ones for the `list` exists for the `ndarray`.

But on top of that, one can add a scalar to all the values in the array with the `+` operator.


```python
arr1 = np.arange(16).reshape(4, 4)
print(f'arr1 -->\n{arr1}')
arr1 = arr1 + 2
print(f'arr1 -->\n{arr1}')
```

Note the use of the function `reshape` which allows to change the dimensions (`shape`) of an array:


```python
arr1 = np.arange(16)
print(f'arr1 -->\n{arr1}')
print(f'arr1 (reshape(4,  4)) -->\n{arr1.reshape(4, 4)}')
print(f'arr1 (reshape(2, -1)) -->\n{arr1.reshape(2, -1)}')
```

Similar operations exist for the subtraction, multiplication or division or exponent (`**` in Python):


```python
arr1 = np.arange(16).reshape(4, 4)
print(f'arr1 -->\n{arr1}')
arr2 = arr1 * 2
print(f'arr1 * 2 -->\n{arr2}')
arr3 = arr1 ** 2
print(f'arr1 ** 2 -->\n{arr3}')
```

Operations between arrays are also possible.

The `*` will multiply all term of an array to their corresponding terms (note that it means that the two arrays need to be of the same size):


```python
arr1 = np.arange(16).reshape(4, 4)
arr2 = np.arange(16, 32).reshape(4, 4)
arr3 = arr1 * arr2
print(f'arr1 -->\n{arr1}')
print(f'arr2 -->\n{arr2}')
print(f'arr1 * arr2 -->\n{arr3}')
```

The matrix multiplication operator is the following: `@`.

Note: Again, when performing matrix multiplication, one has to remember that the matrix dimensions have to be matching.

Moreover, the `dot` function also exists, doing `A @ B` is equivalent to `np.dot(A, B)`.


```python
arr1 = np.arange(8).reshape(2, 4)
arr2 = np.arange(8).reshape(4, 2)
arr3 = arr1 @ arr2
arr4 = arr2 @ arr1
print(f'arr1 -->\n{arr1}')
print(f'arr2 -->\n{arr2}')
print(f'arr1 @ arr2 -->\n{arr3}')
print(f'np.dot(arr1, arr2) -->\n{np.dot(arr1, arr2)}')
print(f'arr2 @ arr1 -->\n{arr4}')
```

A lot of operations on `ndarray`s are available, for example computing the determinant (`np.linalg.det`) of a matrix or inversing (`np.linalg.inv`) it:


```python
arr1 = np.array([[6, 1, 1, 3],
                 [4, -2, 5, 1],
                 [2, 8, 7, 6],
                 [3, 1, 9, 7]])
print(f'arr1 -->\n{arr1}\n')
det = np.linalg.det(arr1)
arr1_inv = np.linalg.inv(arr1)
print(f'arr1 determinant -->\n{det}\n')
print(f'arr1_inv -->\n{arr1_inv}\n')
print(f'arr1 . arr1_inv -->\n{np.round(arr1 @ arr1_inv)}\n')
```

[&larr; previous](1-Variables.md) - [next &rarr;](3-Conditional-Statements-Loops.md)