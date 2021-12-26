import pandas as pd
import numpy as np
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None, 'display.max_columns', None)

from Function_New import StatisticalSeismology
Data = pd.read_excel("AllMicroSeismicPhase1.xlsx")
# print(Data)

Magnitude = Data['SP_MAGNITUDE']
print(len(Magnitude))

n, cum, bin_list, bvalue,avalue = StatisticalSeismology(Magnitude)
print("Non Cumulative Number:",n)
print("Cumulative Number:",cum)
print("Bin:", bin_list)
print("b-value:", bvalue, "&", "a-value:", avalue)
