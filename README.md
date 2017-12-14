![alt text](https://github.com/LPvdT/ml-algorithms/blob/master/data/header.png)

# Machine Learning Algorithms
Some basic exploration and re-creation of machine learning algorithms.

## Description

This project uses simple machine learning algorithms on financial and breast cancer data. There is also code to build the algorithms from scatsch, without the use of libraries.

## Prerequisites

Some of the code requires some, or all of, the following libraries.

```
pandas
quandl
numpy
scikit-learn
pickle
matplotlib
```

as in

```Python
import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
```

## Acknowledgements

* This project is inspired by and built upon fundamentals of [Sentdex](http://sentdex.com/)
* Some of the code uses a breast cancer [dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)) from the University of Wisconsin
