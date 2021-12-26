import pandas as pd
import os #membaca path/lokasi directory
import matplotlib.pyplot as plt
import numpy as np


#Histogram Phase 1
phase1 = pd.read_excel("AllMicroSeismicPhase1.xlsx")
Magnitude = phase1['SP_MAGNITUDE']
plt.figure('Magnitudo')
plt.title('Magnitude Phase 1')
bin_list = np.arange(-2.55, 0, 0.1)
# print(bin_list)
n, bins, patches =plt.hist(Magnitude,bins = bin_list,cumulative=-1 )
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
# print(len(Magnitude))
print(n, bins, patches)
print(len(n), len(bins))
bin_mid = np.arange(-2.5, 0, 0.1)
print(bin_mid)
plt.figure()
plt.plot(bin_mid, n, '.k')
plt.show()




# # Collect data with pandas phase 2
path=[]
for file in os.listdir(r'C:\Users\ASUS VIVO\PycharmProjects\FORGE\Data_Mikroseismik_Phase2'):
        file = [os.path.join(r'C:\Users\ASUS VIVO\PycharmProjects\FORGE\Data_Mikroseismik_Phase2', file)]
        path.extend(file)
# print(path)
#
# #Load data with pandas
catalog = pd.DataFrame([]) #DataFrame tabel objeknya pandas
for file in path:
    catalog = catalog.append(pd.read_excel(file))
catalog = catalog.drop([catalog.index[0]])
# # print(catalog)
#
# #Histogram
Magnitude = catalog['SP_MAGNITUDE']
plt.figure('Magnitudo')
plt.title('Magnitude Phase 2')
n, bins, patches =plt.hist(Magnitude, cumulative = -1)
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.show()
# print(n, bins, patches)

#
# # #Collect data with pandas phase 3
path=[]
for file in os.listdir(r'C:\Users\ASUS VIVO\PycharmProjects\FORGE\Data_Mikroseismik_Phase3'):
        file = [os.path.join(r'C:\Users\ASUS VIVO\PycharmProjects\FORGE\Data_Mikroseismik_Phase3', file)]
        path.extend(file)
# # print(path)
#
# #Load data with pandas
catalog = pd.DataFrame([]) #DataFrame tabel objeknya pandas
for file in path:
    catalog = catalog.append(pd.read_excel(file))
catalog = catalog.drop([catalog.index[0]])
# # print(catalog)
#
# #Histogram Phase 3
Magnitude = catalog['SP_MAGNITUDE']
plt.figure('Magnitudo')
plt.title('Magnitude Phase 3')
n, bins, patches =plt.hist(Magnitude, cumulative=-1)
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.show()
# print(n, bins, patches)


# new_catalog = catalog[['JobTime','SP_MAGNITUDE']].copy()
# print(new_catalog)
