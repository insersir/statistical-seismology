import numpy as np
import matplotlib.pyplot as plt

magnitude = [3, 3.1, 3.2, 3.2, 3.5, 3.7, 4, 4.3, 4.5, 5, 5.2, 5.4, 5.5, 5.9, 6, 6.6, 6.8, 7, 7.1, 7.7]

#Regression Method
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
x = []
y = []
for i in range(len(magnitude)):
    if 3 <= magnitude[i] < 4:
        data1.append(magnitude[i])
    elif 4 <= magnitude[i] < 5:
        data2.append(magnitude[i])
    elif 5 <= magnitude[i] < 6:
        data3.append(magnitude[i])
    elif 6<= magnitude[i] < 7:
        data4.append(magnitude[i])
    else:
        data5.append(magnitude[i])
x.append(min(data1))
x.append(min(data2))
x.append(min(data3))
x.append(min(data4))
x.append(min(data5))
# print(x)
y.append(len(data1))
y.append(len(data2))
y.append(len(data3))
y.append(len(data4))
y.append(len(data5))
# print(y)
# print(data1)
# print(min(data1))
# print(len(data1))
y_log = np.log10(y).tolist()
print(y_log)
print(y)
x_average = np.average(x)
y_average = np.average(y_log)
# print(y_average)

x_selisih1 = []
x_kuadrat = []
y_selisih1 = []

for i in range(len(x)):
    x_selisih = x[i] - x_average
    x_kuadrat.append(x_selisih**2)
    x_selisih1.append(x_selisih)

x_kuadrat_total = sum(x_kuadrat)
# print(x_kuadrat_total)
# print(x_selisih1)
# print(x_kuadrat)

for j in range(len(y_log)):
    y_selisih = y_log[j]-y_average
    y_selisih1.append(y_selisih)
# print(y_selisih1)

perkalian_xy_selisih = np.multiply(x_selisih1,y_selisih1).tolist()
jumlah_perkalian_xy_selisih = sum(perkalian_xy_selisih)
m1 = b_value = jumlah_perkalian_xy_selisih/x_kuadrat_total
a_value = y_average - m1*x_average
print(m1)
print(a_value)







#Least square method
# N = len(y_log) or len(x)
#
# perkalian_xy = np.multiply(x,y_log)
# jumlah_perkalian_xy = sum(perkalian_xy)
# perkalian_total_xy = sum(x)*sum(y_log)
#
# x_power = []
# for l in range(len(x)):
#     x_power_iteration = x[l]**2
#     x_power.append(x_power_iteration)
# jumlah_x_power = sum(x_power)
# jumlah_x_total = (sum(x))**2
# m2 = ((N*jumlah_perkalian_xy)-perkalian_total_xy)/(N*jumlah_x_power-jumlah_x_total)
# print(m2)














