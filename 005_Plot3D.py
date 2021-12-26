# # Import libraries
# # from mpl_toolkits import mplot3d
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # # Creating dataset
# # z = 4 * np.tan(np.random.randint(10, size=(500))) + np.random.randint(100, size=(500))
# # x = 4 * np.cos(z) + np.random.normal(size=500)
# # y = 4 * np.sin(z) + 4 * np.random.normal(size=500)
# #
# # # Creating figure
# # fig = plt.figure(figsize=(16, 9))
# # ax = plt.axes(projection="3d")
# #
# # # Add x, y gridlines
# # ax.grid(b=True, color='grey',
# #         linestyle='-.', linewidth=0.3,
# #         alpha=0.2)
# #
# # # Creating color map
# # my_cmap = plt.get_cmap('hsv')
# #
# # # Creating plot
# # sctt = ax.scatter3D(x, y, z,
# #                     alpha=0.8,
# #                     c=(x + y + z),
# #                     cmap=my_cmap,
# #                     marker='^')
# #
# # plt.title("simple 3D scatter plot")
# # ax.set_xlabel('X-axis', fontweight='bold')
# # ax.set_ylabel('Y-axis', fontweight='bold')
# # ax.set_zlabel('Z-axis', fontweight='bold')
# # fig.colorbar(sctt, ax=ax, shrink=0.5, aspect=5)
# #
# # # show plot
# # plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

phase1 = pd.read_excel("AllMicroSeismicPhase1.xlsx")
phase2 = pd.read_excel("AllMicroSeismicPhase2.xlsx")
phase3 = pd.read_excel("AllMicroSeismicPhase3.xlsx")

# x1 = phase1.SP_MAGNITUDE
# plt.hist(x1, bins = 20,cumulative=-1)
# plt.title('PHASE1')
# print(len(x1))


#Histogram Phase 1
Magnitude = phase1.SP_MAGNITUDE
plt.figure('Magnitudo')
plt.title('Magnitude Phase 1')
plt.hist(Magnitude)

bin_list = np.arange(-2.55, 0, 0.1)
# print(bin_list)
n, bins, patches =plt.hist(Magnitude,bins = bin_list,cumulative=-1 )
plt.xlabel('Magnitude')
plt.ylabel('Frequency')


# DISTRIBUSI NORMAL
Magnitude_normal =  phase1.SP_MAGNITUDE
plt.figure()
n1, bins1, patches1 =plt.hist(Magnitude_normal,bins = bin_list )
print('Magnitudo Normal',n1, bins1, patches1)
plt.xlabel('Magnitude')
plt.ylabel('Frequency')

print(n, bins, patches)
print(len(n), len(bins))
bin_mid = np.arange(-2.5, 0, 0.1)
plt.figure()
plt.plot(bin_mid,n, '.k')

plt.plot(bin_mid,n1,'.r')

plt.show()

sumbux= bin_mid.reshape((-1, 1))
sumbuy= n
df = pd.DataFrame(sumbux,sumbuy)
writer = pd.ExcelWriter('yok.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# model = LinearRegression()
# model.fit(sumbux, sumbuy)
# r_sq = model.score(sumbux, sumbuy)
# print('coefficient of determination:', r_sq)
# plt.plot(sumbux, sumbuy)
# plt.show()

# #Histogram Phase 2
# Magnitude = phase2.SP_MAGNITUDE
# plt.figure('Magnitudo')
# plt.title('Magnitude Phase 2')
# bin_list = np.arange(-2.55, 0, 0.1)
# # print(bin_list)
# n, bins, patches =plt.hist(Magnitude,bins = bin_list,cumulative=-1 )
# plt.xlabel('Magnitude')
# plt.ylabel('Frequency')
# # print(len(Magnitude))
# print(n, bins, patches)
# print(len(n), len(bins))
# bin_mid = np.arange(-2.5, 0, 0.1)
# plt.figure()
# plt.plot(bin_mid, n, '.k')
# plt.show()




# x1 = phase2.SP_MAGNITUDE
# plt.hist(x1,cumulative=-1)
# plt.title('PHASE2')
# plt.ylabel('cumulative numver')
# plt.xlabel('Magnitude')
# print(len(x1))
# #
# #
# # x3 = phase3.SP_MAGNITUDE
# # plt.hist(x3, bins = 20,cumulative=-1)
# # plt.title('PHASE3')
# # print(len(x3))
# plt.show()
