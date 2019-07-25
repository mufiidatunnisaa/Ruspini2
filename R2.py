#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading ruspini.csv
ruspini = pd.read_csv("ruspini.csv")
print(ruspini)

#visualization
plt.figure('Ruspini')
plt.scatter(ruspini['x'].values,
            ruspini['y'].values,
            color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()