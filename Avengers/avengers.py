import pandas as pd

avengers = pd.read_csv("avengers.csv")
print avengers.head(5)


import matplotlib.pyplot as plt
%matplotlib inline
true_avengers = pd.DataFrame()

avengers['Year'].hist()