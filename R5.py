#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading ruspini.csv
ruspini = pd.read_csv("ruspini.csv")
ruspini_array = np.array(ruspini, dtype = float)
ruspini_array = impy.mean(ruspini_array)


#reading data_ruspini_missing.csv
ruspini_missing = pd.read_csv("data_ruspini_missing.csv")


#filling missing values and save into 'new_ruspini.csv'
new_ruspini = ruspini_missing.replace("?", np.nan)
new_ruspini_array = np.array(new_ruspini, dtype = float)
new_ruspini_array = impy.mean(new_ruspini_array)
new_ruspini.to_csv('new_ruspini.csv')
print(new_ruspini)


#make a dataframe
data_frame_ruspini = pd.DataFrame({
    'x': ruspini_array[:, 0],
    'y': ruspini_array[:, 1],
    'label': ruspini_array[:, 2],
})

data_frame_new_ruspini = pd.DataFrame({
    'x': new_ruspini_array[:, 0],
    'y': new_ruspini_array[:, 1],
    'label': new_ruspini_array[:, 2],
})

#visualization
plt.figure('Ruspini')
plt.scatter(data_frame_ruspini['x'].values,
            data_frame_ruspini['y'].values,
            color='blue')
plt.xlabel('X')
plt.ylabel('Y')

plt.figure('New Ruspini')
plt.scatter(data_frame_new_ruspini['x'].values,
            data_frame_new_ruspini['y'].values,
            color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
