import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None, 'display.max_columns', None)

# PHASE1
#collect all files path
path1=[]
for file1 in os.listdir('.\MicroseismicPhase1'):
    file1 = [os.path.join('.\MicroseismicPhase1', file1)]
    path1.extend(file1)
print(path1)

#load data with pandas / dataframe
catalog1 = pd.DataFrame([])
for file1 in path1:
    catalog1 = catalog1.append(pd.read_excel(file1))
catalog1 = catalog1.drop([catalog1.index[0]])
all_df_list = [catalog1]
appended_df = pd.concat(all_df_list)
appended_df.to_excel("AllMicroSeismicPhase1.xlsx", index=False)
# print(catalog1)
# print(len(catalog1))

# PHASE2
#collect all files path
path2=[]
for file2 in os.listdir('.\MicroseismicPhase2'):
    file2 = [os.path.join('.\MicroseismicPhase2', file2)]
    path2.extend(file2)
print(path2)

#load data with pandas / dataframe
catalog2 = pd.DataFrame([])
for file2 in path2:
    catalog2 = catalog2.append(pd.read_excel(file2))
catalog2 = catalog2.drop([catalog2.index[0]])
all_df_list = [catalog2]
appended_df = pd.concat(all_df_list)
appended_df.to_excel("AllMicroSeismicPhase2.xlsx", index=False)
# print(catalog2)
# print(len(catalog2))

# PHASE3
#collect all files path
path3=[]
for file3 in os.listdir('.\MicroseismicPhase3'):
    file3 = [os.path.join('.\MicroseismicPhase3', file3)]
    path3.extend(file3)
print(path3)

#load data with pandas / dataframe
catalog3 = pd.DataFrame([])
for file3 in path3:
    catalog3 = catalog3.append(pd.read_excel(file3))
catalog3 = catalog3.drop([catalog3.index[0]])
all_df_list = [catalog3]
appended_df = pd.concat(all_df_list)
appended_df.to_excel("AllMicroSeismicPhase3.xlsx", index=False)
# print(catalog3)
# print(len(catalog3))

#

well5832 =[335452,4263040]
well6832 =[335486,4263160]
well7832 =[335781,4262990]


# Plot Peta 2D Catalog 1
x1 = catalog1.QC_LOC_X
y1 = catalog1.QC_LOC_Y

fig = plt.figure(figsize=[7,6])
ax=plt.subplot(111)
warna=fig.patch
warna.set_facecolor("#E6E6FA")
ax.xaxis.grid() # horizontal lines
ax.yaxis.grid() # vertical lines
ax.ticklabel_format(useOffset=False, style='plain')

colors1 = catalog1.SP_MAGNITUDE
# sizes = 100 * rng.rand(100)

plt.scatter(x1, y1, c=catalog1.SP_MAGNITUDE,alpha=10,cmap='jet')
cbar= plt.colorbar()
cbar.set_label("Magnitude", labelpad=+3)
plt.plot(well5832[0],well5832[1],'v', markersize=8, linewidth=1, color= 'red',label='Well 58-32')
plt.plot(well6832[0],well6832[1],'v',markersize=8, linewidth=1, color= 'black',label='Well 68-32')
plt.plot(well7832[0],well6832[1],'v',markersize=8, linewidth=1,color= 'yellow',label='Well 78-32')
plt.legend()
plt.title('All Microseismic Phase1')
plt.ylim(4262900, 4263250)
plt.xlim (335000,335800)
plt.xlabel('Easting(m)')
plt.ylabel('Northing(m)')


# Plot Peta 2D Catalog 2
x2 = catalog2.QC_LOC_X
y2 = catalog2.QC_LOC_Y

fig = plt.figure(figsize=[7,6])
ax=plt.subplot(111)
warna=fig.patch
warna.set_facecolor("#E6E6FA")
ax.xaxis.grid() # horizontal lines
ax.yaxis.grid() # vertical lines
ax.ticklabel_format(useOffset=False, style='plain')

colors2 = catalog2.SP_MAGNITUDE


plt.scatter(x2, y2, c=catalog2.SP_MAGNITUDE,alpha=10,cmap='jet')
cbar=plt.colorbar()
cbar.set_label("Magnitude", labelpad=+3)
plt.plot(well5832[0],well5832[1],'v', markersize=8, linewidth=1, color= 'red',label='Well 58-32')
plt.plot(well6832[0],well6832[1],'v',markersize=8, linewidth=1, color= 'black',label='Well 68-32')
plt.plot(well7832[0],well6832[1],'v',markersize=8, linewidth=1,color= 'yellow',label='Well 78-32')
plt.legend()
plt.title('All Microseismic Phase2')
plt.xlabel('Easting(m)')
plt.ylabel('Northing(m)')
plt.ylim(4262900, 4263250)
plt.xlim (335000,335800)


# Plot Peta 2D Catalog 3
x3 = catalog3.QC_LOC_X
y3 = catalog3.QC_LOC_Y

fig = plt.figure(figsize=[7,6])
ax=plt.subplot(111)
warna=fig.patch
warna.set_facecolor("#E6E6FA")
ax.xaxis.grid() # horizontal lines
ax.yaxis.grid() # vertical lines
ax.ticklabel_format(useOffset=False, style='plain')

colors3 = catalog3.SP_MAGNITUDE
# sizes = 100 * rng.rand(100)

plt.scatter(x3, y3, c=catalog3.SP_MAGNITUDE,alpha=10,cmap='jet')
cbar=plt.colorbar()
cbar.set_label("Magnitude", labelpad=+3)
plt.plot(well5832[0],well5832[1],'v', markersize=8, linewidth=1, color= 'red',label='Well 58-32')
plt.plot(well6832[0],well6832[1],'v',markersize=8, linewidth=1, color= 'black',label='Well 68-32')
plt.plot(well7832[0],well6832[1],'v',markersize=8, linewidth=1,color= 'yellow',label='Well 78-32')
plt.legend()
plt.title('All Microseismic Phase3')
plt.xlabel('Easting(m)')
plt.ylabel('Northing(m)')
plt.ylim(4262900, 4263250)
plt.xlim (335000,335800)
plt.show()



