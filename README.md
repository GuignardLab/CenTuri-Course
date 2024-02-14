# Turing Centre for living systems's "Introduction to biological data analysis" course

The website version [here](https://guignardlab.github.io/CenTuri-Course/)

This is the repository for the introduction of the CENTURI "Introduction to biological data analysis" course.

This first day is split in 2 main parts:

1. [Introduction to coding with Turing patterns](1-Introduction-to-Python/Resources/0-Introduction.md)
2. [Data handling and visualisation](2-Data-handling-and-visu/Resources/Matplotlib-course/1-2-Intro-and-Line-plots/1-2-Intro-and-Line-plots.md)

## 0. Requirements for the course

### 0.1 Recommended software

This course is made on a [jupyter notebook](https://jupyter.org/) running on Python 3.8 or newer.

To install Python and the required dependencies we strongly recommend to use [conda](https://docs.conda.io/en/latest/), [mamba](https://mamba.readthedocs.io/en/latest/) or [pipenv](https://pipenv.pypa.io/en/latest/) (the teachers will use conda)

### 0.2 Installing conda

Conda can be installed multiple ways. We do not have any recommendations about how to but one can read [there](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for a likely exhaustive list on ways to install conda.

Note that we do not necessarily recommend installing Anaconda, we do have a slight preference towards [Miniconda](https://docs.conda.io/en/latest/miniconda.html) but that's just us.

Moreover, we advise to start jupyter notebooks from a shell/terminal/prompt to be able to better see the error messages.

### 0.3 Dependencies

While we tried to keep the dependencies as small as possible, few are still required:

- [Jupyter notebook](https://jupyter.org/)
- [NumPy](https://numpy.org/)
- [Scipy](https://scipy.org/)
- [Matplotlib](https://matplotlib.org/)

Note that other libraries might be necessary for the courses after.

To install them one can for example run the following command lines in a terminal, assuming that conda is installed:

```shell
conda create --name CenTuri-Course
```

to create the environment for the course. Then:

```shell
conda activate CenTuri-Course
```

to activate the course environment. And finally:

```shell
conda install notebook numpy scipy matplotlib
```

All dependencies should now be installed!

Enjoy!

### 0.4 Troubleshooting for MacOs M1 chips

The newly introduced M1 chips in the latest macbooks can create some difficulties for installation.

One way to solve the issue is to install [Miniforge](https://github.com/conda-forge/miniforge) and to then use it as Miniconda.

### 0.5 Testing your configuration

If you would like to test your configuration, you can run the following python file: `Configuration-test.py`.

One way to run it is the following:

From a terminal in the folder that contains `Configuration-test.py`:

```shell
python Configuration-test.py
```

You should get an output similar to the following one:
> You are using Python version (3.10.4). It is recent enough for this course
>
> Numpy version (1.21.5) is installed
>
> Scipy version (1.8.0) is installed
>
> Matplotlib version (3.5.1) is installed
>
> Everything's good
>
>

If your python version is too old or if you failed to install one of the libraries, you will get an error message.
