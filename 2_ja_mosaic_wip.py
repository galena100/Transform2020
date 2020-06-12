import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

data2=np.loadtxt('C:\\t20-litho_boundary_from_gamma\\test001_gamma.csv',skiprows=1,delimiter=',')
#data2=np.loadtxt(data1 + 'test001_gamma.csv',skiprows=1,delimiter=',')
data2[:,0]=data2[:,0]*-1.0
data=data2[np.arange(0,36595,10),:]
dt=data[1,0]-data[0,0]

#wavelet calcs
#-------------

import pywt
wavelet = 'gaus2'
scales = np.arange(1, 500,10)
[cfs, frequencies] = pywt.cwt(data[:,1], scales, wavelet, dt)
power = (abs(cfs)) ** 2
zcwt=power.T
zcwt=np.log2(zcwt)
period = 1. / frequencies

#plotting
#--------

fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(15, 30))
#fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15, 30))
ax1.plot(data[:,1],data[:,0])
ax1.set_ylim([0,350])
ax1.invert_yaxis()
#ax2.contourf(scales,data[:,0],zcwt,levels=np.arange(np.min(zcwt),np.max(zcwt),1),
#             cmap="RdBu_r", extend='both')
ax2.contourf(scales
            ,data[:,0]
            ,zcwt
            ,levels=np.arange(np.min(zcwt),np.max(zcwt),2)
            ,cmap="RdBu_r"
            ,extend='both')
ax2.invert_yaxis()


ax3.mosaic(data[:,0]) #error here "AttributeError: 'AxesSubplot' object has no attribute 'mosaic'""
ax3.set_ylim([0,350])
ax3.inver_yaxis()
fig.colorbar()

'''
#real_x=scales
#real_y=data[:,0]
#dx = (real_x[1]-real_x[0])/2.
#dy = (real_y[1]-real_y[0])/2.
#extent = [real_x[0]-dx, real_x[-1]+dx,  real_y[-1]+dy,real_y[0]-dy]
#ax2.imshow(zcwt,extent=extent, interpolation='nearest', aspect='auto')
'''
print(f"this is level1 {np.min(zcwt)}, this is level2 {np.max(zcwt)}")
plt.show()
