# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 08:14:17 2020

@author: leo.dinendra
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


data2=np.loadtxt('C:\\Users\\obeli\\Documents\\GitHub\\Transform2020_2\\t20-litho_boundary_from_gamma\\test001_gamma.csv',skiprows=1,delimiter=',')
#data2=np.loadtxt('test001_gamma.csv',skiprows=1,delimiter=',')
data2[:,0]=data2[:,0]*-1.0
data=data2[np.arange(0,36595,10),:]
dt=data[1,0]-data[0,0]

dep=data[:,0]
syntwave=savgol_filter(data[:,1], 51, 3)


syntwave=(syntwave-np.mean(syntwave))/np.std(syntwave)

#getting the cwt gauss1 and gauss2
import pywt

wavelet = 'gaus2'
scales = np.linspace(0.1,200,100)#np.arange(0.1, 100,10)

[cfs, frequencies] = pywt.cwt(syntwave, scales, wavelet, dt)
power = (abs(cfs)) ** 2
zcwt=cfs.T
period = 1. / frequencies

lev_contour=np.arange(np.min(zcwt),np.max(zcwt),7)


wavelet2 = 'gaus1'

[cfs, frequencies] = pywt.cwt(syntwave, scales, wavelet2, dt)
power = (abs(cfs)) ** 2
zcwt2=cfs.T
period = 1. / frequencies


fig, (ax1, ax2,ax3) = plt.subplots(1,3,figsize=(8, 6))
ax1.plot(syntwave,dep)
ax1.set_ylim([np.min(dep),np.max(dep)])
ax1.invert_yaxis()
cs=ax2.contour(scales,dep,zcwt,levels=[0.0], colors='k',extend='both')

ax2.invert_yaxis()
ax2.contourf(scales,dep,zcwt2,levels=np.arange(np.min(zcwt),np.max(zcwt),1),
             cmap="RdBu_r", extend='both')


#boundary
#get 0 level
thres=0.8 #percent from std threshold
x0=np.array([])
y0=np.array([])
i0=np.array([])
id0=0
ncdat=np.zeros([len(cs.allsegs[0])])
for i in range(0,len(cs.allsegs[0])):
    ncdat[i]=len(cs.allsegs[0][i])

for i in range(0,len(cs.allsegs[0])):
    if len(cs.allsegs[0][i])>(np.std(ncdat)*thres):
        dat0= cs.allsegs[0][i]
        y0 = np.hstack((y0, dat0[:,0]))
        x0 = np.hstack((x0, dat0[:,1]))
        i0 = np.hstack((i0, np.ones([len(dat0[:,1])])*id0))
        id0=id0+1

#rescale to a array position scale (to call the zcwt2)
x02=x0/dt
y02=(y0-np.min(y0))/(np.max(y0)-np.min(y0))*(len(scales)-1)

z0=np.zeros([x0.shape[0]],dtype=float)

for i in range(z0.shape[0]):
    z0[i]=zcwt2[int(np.floor(x02[i])),int(np.floor(y02[i]))]

#getting the boundary
bo=np.array([])
for i in range(0,id0):
    locmax=np.where(z0 == np.max(z0[i0==i]))[0][0]
    locmin=np.where(z0 == np.min(z0[i0==i]))[0][0]
    if z0[locmax]>0.0:
        if i==0 and bo.shape[0]==0:
            bo=np.hstack((bo, [x02[locmax],y02[locmax],z0[locmax]]))
        else:
            bo=np.vstack((bo, [x02[locmax],y02[locmax],z0[locmax]]))
    if z0[locmin]<0.0:
        if i==0 and bo.shape[0]==0:
            bo=np.hstack((bo, [x02[locmin],y02[locmin],z0[locmin]]))
        else:
            bo=np.vstack((bo, [x02[locmin],y02[locmin],z0[locmin]]))

bo=bo[bo[:,0].argsort()]

ax2.plot((bo[:,1]/scales.shape[0])*(np.max(scales)-np.min(scales))+np.min(scales),bo[:,0]*dt,'wo',markersize=5,markeredgecolor='y')
ax2.yaxis.set_visible(False)

#calculate the boundary strength & getting the signal polarity
bos=np.zeros([len(dep),2],dtype=float)
for i in range(0,bo.shape[0]):
    bos[int(np.round(bo[i,0])),0]=np.abs(bo[i,2])/np.max(np.abs(bo[:,2]))
    bos[int(np.round(bo[i,0])),1]=np.sign(syntwave[int(np.round(bo[i,0]))])

ax3.barh(dep,bos[:,0])
#ax3.set_ylim([0,350])
ax3.invert_yaxis()
ax3.set_aspect('auto')
ax3.yaxis.set_visible(False)
