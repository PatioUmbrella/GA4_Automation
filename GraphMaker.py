#run all at the same time

import csv
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

df = pd.read_csv("GA4_python_output4.csv") 

df2 = df.groupby(['month'])['totalUsers'].sum()

display(df2)

df2.plot(x="month", y="totalUsers", kind="bar")
plt.show() 