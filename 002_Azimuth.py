import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import math
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None, 'display.max_columns', None)

Data = pd.read_excel("AllMicroSeismicPhase1.xlsx")
# print(Data)
event_x = Data["QC_LOC_X"]
event_y = Data["QC_LOC_Y"]

well_x = 335452
well_y = 4263040
X = (event_x - well_x)
Y = (event_y - well_y)
# print(Y)
# print(Y)
XY = X/Y

# for i in range(len(X)):
#     if X[i]>0 and Y[i]>0:
#         alpha1 = np.arctan(XY[i])       # in radian
#         alpha = alpha1 * 180 / np.pi    # in degree
#         azimuth = alpha
#         print(azimuth)
#     elif X[i]>0 and Y[i]<0:
#         alpha1 = np.arctan(XY[i])
#         alpha = alpha1 * 180 / np.pi
#         azimuth = 180 - abs(alpha)
#         print(azimuth)
#     elif X[i]<0 and Y[i]<0:
#         alpha1 = np.arctan(XY[i])
#         alpha = alpha1 * 180 / np.pi
#         azimuth = 180 + abs(alpha)
#         print(azimuth)
#     else:
#         alpha1 = np.arctan(XY[i])
#         alpha = alpha1 * 180 / np.pi
#         azimuth = 360 - abs(alpha)
#         print(azimuth)

az=[]
for i in range(len(X)):
    if X[i]>0 and Y[i]>0:
        alpha1 = np.arctan(XY[i])       # in radian
        alpha = alpha1 * 180 / np.pi    # in degree
        azimuth = alpha

    elif X[i]>0 and Y[i]<0:
        alpha1 = np.arctan(XY[i])
        alpha = alpha1 * 180 / np.pi
        azimuth = 180 - abs(alpha)

    elif X[i]<0 and Y[i]<0:
        alpha1 = np.arctan(XY[i])
        alpha = alpha1 * 180 / np.pi
        azimuth = 180 + abs(alpha)

    else:
        alpha1 = np.arctan(XY[i])
        alpha = alpha1 * 180 / np.pi
        azimuth = 360 - abs(alpha)
    az.append(azimuth)
az= pd.DataFrame({"Azimuth":az})
print(az)
azimuth_=az.to_excel('dataazimuth.xlsx')