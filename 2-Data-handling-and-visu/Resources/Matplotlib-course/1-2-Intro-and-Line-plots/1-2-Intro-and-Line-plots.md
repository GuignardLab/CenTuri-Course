&larr; previous - [home](https://guignardlab.github.io/CenTuri-Course-2022/) - [next &rarr;](1-Variables.md)

# Table of contents
* [1-2-Introduction and Line plots](2-Data-handling-and-visu/Resources/1-2-Intro-and-Line-plots/1-2-Intro-and-Line-plots.md) &larr;
* [3-4-Figures-and-Subplots](2-Data-handling-and-visu/Resources/3-4-Figures-and-Subplots/3-4-Figures-and-Subplots.md)
* [Data structures](2-Data-Structures.md)
* [Conditional statements and loops](3-Conditional-Statements-Loops.md)
* [Some exercises](4-Some-Exercises.md)
* [Introduction to functions](5-0-Introduction-function.md)
    * [File manipulation](5-1-File-manipulation.md)
* [From 0D to 1D](6-1-From-0D-to-1D.md)
    * [Adding lateral diffusion](6-2-Adding-lateral-diffusion.md)
* [From 1D to 2D](7-From-1D-to-2D.md)
* [Playing with the model](8-Playing-with-the-model.md)

# Visualising data using matplotlib

__*We will not look at 3D plots!*__

In this course we will look at how to plot data using `matplotlib`.
The following [cheatsheets](https://matplotlib.org/cheatsheets/) will be quite useful, for the class and for later.
Also, I used a lot the following [book](https://github.com/rougier/scientific-visualization-book) to prepare this course together with the original matplotlib [manual](https://matplotlib.org/stable/index.html).

You are strongly advised to have a look at these links for the course.

In this course, we will have a look at usual line plots, box plots, violin plots, scatter plots and how to make animations.

## 1. Loading the necessary libraries
---
The first step is to import matplotlib and its main class pyplot


```python
import matplotlib as mpl
import matplotlib.pyplot as plt
```

Then, we can use a special matplotlib command:
```python
%matplotlib inline
```
to be able to easily visualize the plot in our notebook.

Note that it is not necessary to run that line in all browsers.
Moreover, you can use the following line:
```python
%matplotlib notebook
```

It gives more freedom with the plots but I personally like it less since it puts the focus on the figure and requires more steps to go back to the code.


```python
%matplotlib inline
```

## 2. Line plots
---

Now that we are set up, let's create our first plot.

But first, we need to create the data that we will want to plot:




```python
import numpy as np
Y = np.sin(np.linspace(-np.pi, 2*np.pi, 30))
```

We can then plot the line that we created the following way:


```python
plt.plot(Y)
```




    [<matplotlib.lines.Line2D at 0x10fda0e20>]




    
![png](output_8_1.png)
    


We are plotting what we want but, the `x` values are not the correct ones (in $[0, 30|]$ instead of $[-\pi, 2\pi]$).

The reason is that we are only giving the `y` axis values (note that they are indeed ranging in $[-1, 1]$). So let's give the `x` values:




```python
X = np.linspace(-np.pi, 2*np.pi, 30)
Y = np.sin(X)
plt.plot(X, Y)
```




    [<matplotlib.lines.Line2D at 0x10ff973d0>]




    
![png](output_10_1.png)
    


Matplotlib, by default, shows us such data as blue lines between data points. We can change that and show only the measured points in red:


```python
plt.plot(X, Y, marker='o', linestyle='', color='red')
```




    [<matplotlib.lines.Line2D at 0x11e80f220>]




    
![png](output_12_1.png)
    


You can find all the different kind of markers, line styles and colours in the [cheatsheet](https://github.com/matplotlib/cheatsheets#cheatsheets) mentioned before.

Moreover, matplotlib is "nice" and, because the marker, linestyle and colour are properties that are often changed they allow an easier way to modify them:


```python
plt.plot(X, Y, 'or')
```




    [<matplotlib.lines.Line2D at 0x11e87ef20>]




    
![png](output_14_1.png)
    



```python
plt.plot(X, Y, 'b-.>')
```




    [<matplotlib.lines.Line2D at 0x11e8e2aa0>]




    
![png](output_15_1.png)
    

