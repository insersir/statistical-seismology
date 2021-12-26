# import numpy as np
# import mplstereonet
# import matplotlib.pyplot as plt

# strikes = np.concatenate([np.random.randint(0, 360, 60),
#                           np.random.randint(10, 60, 20),
#                           np.random.randint(190, 300, 20),
#                           np.random.randint(60, 90, 20),
#                          ])
#
# dips = np.concatenate([np.random.randint(0, 90, 60),
#                        np.random.randint(60, 90, 60),
#                          ])
# bin_edges = np.arange(-5, 366, 10)
# number_of_strikes, bin_edges = np.histogram(strikes, bin_edges)
# number_of_strikes[0] += number_of_strikes[-1]
#
# half = np.sum(np.split(number_of_strikes[:-1], 2), 0)
# two_halves = np.concatenate([half, half])
# fig = plt.figure(figsize=(16,8))
# ax = fig.add_subplot(121, projection='stereonet')


# ax.pole(strikes, dips, c='k', label='Pole of the Planes')
# ax.density_contourf(strikes, dips, measurement='poles', cmap='Reds')
# ax.set_title('Density coutour of the Poles', y=1.10, fontsize=15)
# ax.grid()

# ax = fig.add_subplot(111, projection='polar')
#
# ax.bar(np.deg2rad(np.arange(0, 360, 10)), two_halves,width=np.deg2rad(20), bottom=0.0, color='.8', edgecolor='k')
# ax.set_theta_zero_location('N')
# ax.set_theta_direction(-1)
# ax.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
# ax.set_rgrids(np.arange(1, two_halves.max() + 1, 2), angle=0, weight= 'black')
# ax.set_title('Rose Diagram of the "Fault System"', y=1.10, fontsize=15)
# # fig.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_excel("dataazimuth.xlsx")
azimuth= data["Azimuth"]

# azimuth = [20]
radians = np.deg2rad(azimuth)
# print(radians)
bin_size = 20 #degree
number_of_azimuth , bin_list=np.histogram(azimuth, bins=np.arange(0, 361, bin_size))
centers = np.deg2rad(np.ediff1d(bin_list)//2 + bin_list[:-1])
print(bin_list)
# print(np.ediff1d(bin_list))

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')
ax.bar(centers, number_of_azimuth, width=np.deg2rad(bin_size), bottom=0.0, color='purple', edgecolor='k')
ax.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
ax.set_theta_zero_location("N")
ax.set_title('Rose Diagram', y=1.10, fontsize=15)
ax.set_theta_direction(-1)
plt.show()