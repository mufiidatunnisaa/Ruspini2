#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading ruspini.csv
ruspini = pd.read_csv("ruspini.csv")

#reading data_ruspini_missing.csv
ruspini_missing = pd.read_csv("data_ruspini_missing.csv")
print(ruspini_missing)

#visualization
plt.figure('Ruspini')
plt.scatter(ruspini['x'].values,
            ruspini['y'].values,
            color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()