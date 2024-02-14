#!python

from platform import python_version

version = [eval(i) for i in python_version().split(".")]

ok = True

if 3 <= version[0] <= 3 and version[1] >= 8:
    print(
        f"\33[32mYou are using Python version ({python_version()}). It is recent enough for this course \t \33[0m"
    )
else:
    ok = False
    print(
        f"\n\33[41mYour Python version ({python_version()}) is too old, please update \t \33[0m"
    )

try:
    import numpy

    print(f"\33[32mNumpy version ({numpy.__version__}) is installed \t \33[0m")
except Exception:
    ok = False
    print("\n\33[41mNumpy is not correctly installed \t \33[0m")

try:
    import scipy

    print(f"\33[32mScipy version ({scipy.__version__}) is installed \t \33[0m")
except Exception:
    ok = False
    print("\n\33[41mScipy is not correctly installed \t \33[0m")

try:
    import matplotlib

    print(
        f"\33[32mMatplotlib version ({matplotlib.__version__}) is installed \t \33[0m"
    )
except Exception:
    ok = False
    print("\n\33[41mMatplotlib is not correctly installed \t \33[0m")

if ok:
    print("\n\n\33[32m \t Everything's good \t \n\n \33[0m")
else:
    print("\n\n\33[41m \t\t You got something wrong :( \t\t\33[0m \n\n")
