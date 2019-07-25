#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

#reading ruspini.csv
ruspini = pd.read_csv("ruspini.csv")

#reading data_ruspini_missing.csv
ruspini_missing = pd.read_csv("data_ruspini_missing.csv")

#filling missing values and save into 'new_ruspini.csv'
new_ruspini = ruspini_missing.replace("?", np.nan)
new_ruspini.to_csv('new_ruspini.csv')
print(new_ruspini)

#visualization
plt.figure('Ruspini')
plt.scatter(ruspini['x'].values,
            ruspini['y'].values,
            color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()