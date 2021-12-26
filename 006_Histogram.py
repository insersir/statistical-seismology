import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load Data
Data = pd.read_excel("AllMicroSeismicPhase1.xlsx")
Magnitude = Data['SP_MAGNITUDE']
# print(len(Magnitude))
# print('Minimum magnitude:',min(Magnitude), 'Maximum magnitude:', max(Magnitude))

# Histogram Normal
fig = plt.figure()
warna=fig.patch
warna.set_facecolor("#F5F5F5")
fig.add_subplot(1,1,1,facecolor ="#FFFFDF")

bin_width = 0.1 #Interval bin
bin_list1 = np.arange(min(Magnitude), max(Magnitude)+2*bin_width, bin_width)
# print('binlist:',bin_list)
bin_list = np.round(bin_list1,1)
# print('rounding:',bin_list1)
n, bins, patches = plt.hist(Magnitude,bins = bin_list,log= True, color=	'#808080',edgecolor='black', label='Non Cumulative')
plt.legend(loc='upper right')
# print('total bins:',len(bins))
# print(120*'-')
# print(bins,n)
plt.xlabel('Magnitude')
plt.ylabel('Number of Events')
plt.grid(alpha=0.5, color= '#607c8e')

firstbin_mid = (bins[0]+bins[1])/2
bin_mid= np.arange(firstbin_mid, bins[-1], bin_width)
print('bin mid:',bin_mid)
print('total bin_mid:',len(bin_mid),'total n:',len(n))

#Cumulative Number
cum= np.flipud(np.flipud(n).cumsum())
print('cum:',cum)

plt.plot(bin_mid,cum,'.',markersize=12, color='black',label='Cumulative')
plt.legend(loc='upper right')

# Magnitude Completeness
mc = np.where(n == np.amax(n))
mc = mc[0][0]
print("binmid_mc",bin_mid[mc])
sumbux = bin_mid[mc:len(bin_mid)]
print(len(sumbux))

cum1 = np.where(n == np.amax(n))
cum1 = cum1[0][0]
# print(cum[mc])
sumbuy = cum[cum1:len(cum)]
print(len(sumbuy))

plt.plot(bin_mid[mc],cum[mc],'.',color='red',label='Mc',markersize=13)
plt.legend()

# Regression Linear
sumbux = sumbux.reshape(-1,1)
sumbuy =sumbuy.reshape(-1,1)
print('sumbuy',sumbuy)

sumbuy_endpoint = sumbuy[-1]

if sumbuy_endpoint != 0:
    sumbuy = np.log10(sumbuy)
else:
    sumbuy = sumbuy[0:-1]
    sumbux = sumbux[0:-1]
    sumbuy = np.log10(sumbuy)

linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(sumbux, sumbuy)  # perform linear regression
Y_pred = linear_regressor.predict(sumbux)  # make predictions
r_sq = linear_regressor.score(sumbux,sumbuy)
slope = linear_regressor.coef_
intercept = linear_regressor.intercept_
bvalue = slope*-1
avalue = -1*(slope*intercept)
# print('intercept:', intercept)
# print('Slope:',slope)
print('b-value:',bvalue)
print('a-value:',avalue)
plt.title('FMD for Phase 3', fontsize= 13, fontweight='bold')
plt.xlabel('Magnitude')
plt.ylabel('Log10 (N)')
plt.grid(alpha=0.6, color= '#607c8e')
Y_pred_new = 10**Y_pred
plt.plot(sumbux, Y_pred_new,color= 'red', label='linear regression')
plt.figtext(.796, .76,' b-value     : %.4f'%bvalue,bbox={"facecolor":"white", "alpha":0.8})
plt.figtext(.796, .727,' a-value    : %.4f'%avalue,bbox={"facecolor":"white", "alpha":0.8})
plt.show()
