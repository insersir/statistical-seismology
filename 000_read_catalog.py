import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None, 'display.max_columns', None)

#collect all files path
path=[]
for file in os.listdir('.\Microseim_Event_Files'):
    file = [os.path.join('.\Microseim_Event_Files', file)]
    path.extend(file)
print(path)

#load data with pandas / dataframe
catalog = pd.DataFrame([])
for file in path:
    catalog = catalog.append(pd.read_excel(file))
catalog = catalog.drop([catalog.index[0]])
print(catalog)
# print(len(catalog))

# newcat = catalog[['JobTime', 'SP_MAGNITUDE']].copy()
# print(newcat)

# #histogram magnitude
# fig, ax = plt.subplots()
# # the histogram of the data
# num_bins = 25
# mag = newcat.SP_MAGNITUDE
#
# n, bins, patches = ax.hist(mag, num_bins)
# print(n, bins, patches)
#
# plt.show()