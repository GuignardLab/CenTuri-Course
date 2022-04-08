[&larr; previous](5-0-Introduction-function.md) - [home](https://guignardlab.github.io/CenTuri-Course-2022/) - [next &rarr;](6-1-From-0D-to-1D.md)

# Table of contents
0. [Introduction](0-Introduction.md)
1. [Variables](1-Variables.md)
2. [Data structures](2-Data-Structures.md)
3. [Conditional statements and loops](3-Conditional-Statements-Loops.md)
4. [Some exercises](4-Some-Exercises.md)
5. [Introduction to functions](5-0-Introduction-function.md)
    1. [File manipulation](5-1-File-manipulation.md) &larr; ([Notebook](../5-1-File-manipulation.ipynb))
6. [From 0D to 1D](6-1-From-0D-to-1D.md)
    1. [Adding lateral diffusion](6-2-Adding-lateral-diffusion.md)
7. [From 1D to 2D](7-From-1D-to-2D.md)
8. [Playing with the model](8-Playing-with-the-model.md)

### Exercise 7
**(With an intermezzo about file manipulation)**

You can play with the different parameters to see how the concentration dynamics change according to these parameters.

Here we would like you to systematically try different parameters and save the produced plots as png files with names containing the parameter values (for example `'test_a0.4_i0.15_dt0.001_k-0.005_tau0.1.png'`).

To save the produced plots, you can use the argument `save_path` of the function `plot_concentration_1cell`.
If you set its value to the file name and path you want to create, it will save it there under its name.

Before being able to do so, you might need some information about how to manipulate strings.
In the previous exercises you might have seen that it is possible to insert values from variables within a string using the curved brackets `{` and `}`.

Simply put, the way it works is by putting the character `f` before your string and then everything within curved brackets will be transformed into string if possible.
For example:
```python
f'test_a{A[0]}_i{I[0]}_dt{dt}'
```
will produce the following string:
```python
'test_a0.4_i0.15_dt0.001'
```
Note that if the `f` is not in front of the string, the curved brackets will be interpreted as normal characters.

**For more on string manipulation, you can read [there](https://docs.python.org/3/tutorial/inputoutput.html#input-and-output)**


```python
from Resources.UsefulFunctions import *
from Resources.Answers import answer, hint

# Carry over here the previously declared variables and the code from the previous exercises
mu_a = 2.8e-4
mu_i = 5e-3
tau = .1
k = -.005
size = 100
dx = dy = 2. / size
T = 9.0
dt = .001
n = int(T / dt)

def compute_AI(): # Don't forget to add arguments
    # A, I = [a], [i] 
    A, I = [0], [0]
    # Uncoment above and
    # Do something here
    return A, I

A, I = compute_AI()
```


```python
print(f'test_a{A[0]}_i{I[0]}_dt{dt}')
print('test_a{A[0]}_i{I[0]}_dt{dt}')
```

#### Avoiding cramping up you current folder
If you want to be a little bit cleaner, you can create a folder in which you will save your images.

You can create such a folder directly in python using `Path` from the `pathlib` library and the command:
```python
Path.mkdir('<folder_name>')
```
For example, to create a folder named `question_7` one could run the command
```python
Path.mkdir('question_7')
```

Though, if the folder already exists, the command line will not work and stop the notebook from running.
To avoid such a problem, it is possible to check whether the folder already exists using the method `exists` of `Path` as shown below.

Let's create the folder `question_7`:


```python
from pathlib import Path
folder = Path('question_7')
if not folder.exists():
    Path.mkdir(folder)
```

#### Path manipulation
Some of you might already be aware that playing with paths can be a pain.
The problem comes from the fact that Windows has a different way to represent a path to a folder than Linux and MacOs.

> **_Side Note: what's a path?!_**
>
> In a computer the folders and files are organised hierarchically.
> What it means is that each file or folder except for one, the root, is in a folder.
> For example, the folder you created earlier (`question_7`) is itself in a folder.
>
> To access a file or folder, it is sometimes necessary to know the sequence of folders it is in so there is no ambiguity for the computer.
> The sequence of folders a folder or a file belongs to is the **path** and it can be represented as a string.
> For example, you can call the function `Path.cwd` (for the current working directory).
> To query the list of directories your notebook is running in:


```python
print('Our current path:')
print(Path.cwd())
```

> You can maybe see that the folders are separated by a `/` (or a `\` for Windows).
> This difference between Linux or MacOs and Windows has been quite a source of trouble, some of you might have experienced it.

Now, to save an image in the folder `'question_7'`, as we would like to do, we just need to concatenate the image name to the folder name:
```python
folder / 'test_a0.4_i0.15_dt0.001.png'
```

Note that the `/` in this case is a concatenation operator specific to the objects of the `path` library. The operator concatenates two `Path` or a `Path` and a `str` putting the operating specific folder separator (
`/` or `\`).

**More info about the `pathlib` can be found [there](https://docs.python.org/3/library/pathlib.html)**


```python
## folder is the path previously created
# Concatenation of two Paths
print(folder / Path('test_a0.4_i0.15_dt0.001.png'))
# Concatenation of a Path and a str (same result)
print(folder / 'test_a0.4_i0.15_dt0.001.png')
```

Now we can *cleanly* answer question 6.
Let assumes that we want the following values:
- `tau` changes from `0.05` to `3` and that we want `5` values within that interval
- `k` changes from `-1` to `1` and that we also want `5` values within that interval
- and a fixed `dt=0.01`

**Write some lines of code to compute and save the requested plots**

Note: you can use the function `np.linspace` to generate the desired values


```python
import numpy as np
folder = Path('question_7')
for test_tau in np.linspace(.05, 1, 5):
    for test_k in np.linspace(-1, 1, 5):
        A, I = answer_results(4, A=0.4, I=0.15, dt=dt, k=test_k, tau=test_tau, n=n)
        plot_concentration_1cell(A, I,
                                 save_path=folder / f'k{test_k}_tau{test_tau}.png')
```

An interesting configuration where we can see some oscillations:
- `dt=0.01`
- `k=0.05`
- `tau=2`

You can manually change the parameters to try to find other *weird* configurations


```python
A, I = answer_results(4, A=0.4, I=0.15, dt=.01, k=.05, tau=2, n=n)
plot_concentration_1cell(A, I)
```

### Exercise 8
**This exercise is difficult, it might take a bit longer to solve. If you are stuck, don't hesitate to look at the following cells for some help**

For this exercise, we will discuss about file manipulation, in other words how to move files automatically.

**Attention here! Proceed with caution for this exercise but also in general. Files removed using Python (or the shell for example) do not end up in the trash but are directly removed!**

In this exercise we would like to sort the files created in the previous exercise. We would like to group the plots generated previously in folders by values of `k` and so that the folders are named according to that `k` value.

For example if you had the following files in your `exercise_7` folder:
```
exercise_7:
 | k0_tau0.png
 | k0_tau1.png
 | k0_tau2.png
 | k1_tau0.png
 | k1_tau1.png
 | k1_tau2.png
 | k2_tau0.png
 | k2_tau1.png
 | k2_tau2.png
```
We would like you to create the following hierarchy:
```
exercise_7:
 | k0:
   | k0_tau0.png
   | k0_tau1.png
   | k0_tau2.png
 | k1:
   | k1_tau0.png
   | k1_tau1.png
   | k1_tau2.png
 | k2:
   | k2_tau0.png
   | k2_tau1.png
   | k2_tau2.png
```

To do so you can use the following functions (assuming `p` is a `Path`):
- `Path.iterdir` allows to loop through all the files of a directory
- `p.name` retrieves the name of the file in `p` as a `str`
- `str.split` splits a string
- `Path.exists` see above
- `p.rename` allows to rename (and therefore move) `p`

Do not hesitate to look at the help of each of these functions (you should do it!).


```python
p = Path('question_7')
for file in p.iterdir():
    ## Do things here
    print(file)
```

### Help for exercise 8
Because the difficulty increased significantly with this exercise, here are some leads that hopefully will help you solve the exercise!

One way to solve a coding problem is to decompose it in multiple smaller problems.
There are often multiple ways to decompose a problem, we will show you one here, it might not be the optimal one (regardless of the optimal metric used) but it should be a working one.
To build that decomposition, it can sometimes be useful to rephrase the problem in terms of what you want the code to do:

<details>
    <summary><b>Click here to display the pseudo-code<b/></summary>
    
```
for each file in folder do (1)
    if the file is a png file do (2)
        k_value <- get what is the value of k for that file (3)
        if folder with k value does not exist do (4)
            create new folder with k value
        end if
        move file to folder with k value (5)
    end if
end for
```

</details>


This decomposition allows to identify the important points in the code and to organise the code to be produced.
Here, we want to loop on the files (1), check if the file is a file of interest (2), retrieve the value of `k` in the file name (3), create a folder with the `k` value if necessary (4) and move the file in the appropriate folder (5).
        
Now, one can try to solve the 5 problems independently and ultimately assemble them to answer the question.

[&larr; previous](5-0-Introduction-function.md) - [next &rarr;](6-1-From-0D-to-1D.md)