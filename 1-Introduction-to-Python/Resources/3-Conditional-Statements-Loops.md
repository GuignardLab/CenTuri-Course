[&larr; previous](2-Data-Structures.md) - [next &rarr;](4-Some-Exercises.md)

# Table of contents
0. [Introduction](0-Introduction.md)
1. [Variables](1-Variables.md)
2. [Data structures](2-Data-Structures.md)
3. [Conditional statements and loops](3-Conditional-Statements-Loops.md) &larr; ([Notebook](../3-Conditional-Statements-Loops.ipynb))
4. [Some exercises](4-Some-Exercises.md)
5. [Introduction to functions](5-0-Introduction-function.md)
    1. [File manipulation](5-1-File-manipulation.md)
6. [From 0D to 1D](6-1-From-0D-to-1D.md)
    1. [Adding lateral diffusion](6-2-Adding-lateral-diffusion.md)
7. [From 1D to 2D](7-From-1D-to-2D.md)
8. [Playing with the model](8-Playing-with-the-model.md)

## 3. Conditional statements and loops
---
### 3.1 Conditional statements
Another important part of coding are the conditional statements.

Conditional statements allow you to perform a given set of instruction(s) if a statement is true.

If necessary, it is possible to run a different set of instructions when the statement is false.

More information about conditional statements can be found [there](https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions) for example

This is usually called an `if`/`else` statement:


```python
a_number = eval(input('Please enter a number and press enter: '))
if a_number == 2:
    print('the number is equal to 2')
else:
    print('the number is not equal to 2')
```

Note the function `input` which allows the user to ask for an input.
Note also the function `eval` which allows you to evaluate the input from the user.
In place of `eval` could be used the function `int` which would transform the input into an integer.
If that was the case, the Python interpreter could not take as an input a decimal value like `0.9` for example.
To do so the function `float` could have been used. Now, with `eval`, one can even enter an operation such as `1+1` and it will be evaluated and then treated as `2` in that case.

You can try to play with the function `eval` with the example above.

If multiple conditions need to be checked, the `elif` statement can be used:


```python
a_number = eval(input('Please enter a number and press enter: '))
if a_number < 2:
    print('the number is stricly smaller than 2')
elif a_number == 2:
    print('the number is equal to 2')
elif 2 < a_number < 10:
    print('the number is strictly between 2 and 10')
else:
    print('the number is larger or equal to 10')
```

> _**To go a little bit further:**_
>
> `if`/`else` statements can be used within a line of code to assign values for example:


```python
previous_number = eval(input('Please enter a number and press enter: '))
a_number = 1 if 10 <= previous_number else 'Strictly smaller than 10'
print(f'a_number --> {a_number}')

# The previous line is equivalent to the following ones:
if 10 < previous_number:
    a_number = 1
else:
    a_number = 'Strictly smaller than 10'
```

### 3.2 Loops
---
Loops are probably the core of coding! They are the reason why computers are so useful!

In Python two types of loops exist: the `for` loop and the `while` loop.
The difference between the two kinds of loops can be small but basically you can almost alway make one with the other though making some `while` loops using `for` loops is sometimes a bit convoluted (but these are thoughts for another time).

A `for` loop in Python allows you to iterate over the items of any sequence (`list`, `str` for example). Note that it is different from loops in C, C++ or Pascal for example.

A `while` loop allows you to iterate as long as a given condition is `True`.

The syntax for a `for` loop is the following:
```python
for item in sequence:
    # do_something
```

The syntax for a `while` loop is the following:
```python
while condition:
    # do_something
```

Here is an example of a `for` loop:


```python
words = ['Hello,', 'how', 'are', 'you?']
for w in words:
    print(w, end=' ')
```

Here the loop iterates over the items of the sequence `words` (which is a `list`) and prints them.

The equivalent with a `while` loop would look like that:


```python
i = 0
while i<len(words):
    print(words[i], end=' ')
    i = i + 1
```

One can easily see that in that context, the `while` loop is a bit more convoluted.

Now, here is an example where the `while` loop is _better_.


```python
stopping_value = 35
i = 0
number_sum = 0
while number_sum < stopping_value:
    i += 1
    number_sum += i
print(f'{i = }, {number_sum = }')
```

The equivalent `for` loop would be the following:


```python
number_sum = 0
for i in range(stopping_value+1): # Here we assume that the maximum value
                                  # necessary to stop is the stopping value itself
    number_sum += i
    if stopping_value <= number_sum:
        break
print(f'{i = }, {number_sum = }')
```

Note that in the case of the `for`, it is necessary to use the ```break``` statement to stop the loop according to a given condition.

> _**To go a little bit further (not required):**_
> Note that if you exchange lines 5 and 6 in the `while` loop you do not get the same result, can you find out why?


```python
i = 0
number_sum = 0
while number_sum < stopping_value:
    number_sum += i
    i += 1
print(f'{i = }, {number_sum = }')
```

**More on `for` loops can be found [there](https://docs.python.org/3/tutorial/controlflow.html#for-statements)**

[&larr; previous](2-Data-Structures.md) - [next &rarr;](4-Some-Exercises.md)