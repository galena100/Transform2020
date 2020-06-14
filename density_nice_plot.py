import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
#from gr_bound import *
import pandas as pd

#data2=np.loadtxt('test001_gamma.csv',skiprows=1,delimiter=',')

#SPECIAL FOR DENS
path1 = 'C:\\Users\\obeli\\Documents\\GitHub\\Transform2020_2\\t20-litho_boundary_from_gamma\\'
#dataraw=pd.read_csv('2_geophys.csv',delimiter=',')
dataraw=dataraw[dataraw['HOLEID']=='test001']
dataraw=dataraw[~np.isnan(dataraw['DENB_g_cc'])]
data2=dataraw[['DEPTH','DENB_g_cc']].values
data2[:,0]=data2[:,0]*-1.0
dtraw=data2[1,0]-data2[0,0]
dep=np.arange(np.min(data2[:,0]),np.max(data2[:,0]),dtraw)
#SPECIAL FOR DENS

#data2[:,0]=data2[:,0]*-1.0
data=data2[np.arange(0,data2.shape[0],10),:]
dt=data[1,0]-data[0,0]

dep=data[:,0]
#syntwave=data[:,1]
syntwave=savgol_filter(data[:,1], 51, 3)

fscales = np.arange(1, 100,1)
syntwave=(syntwave-np.mean(syntwave))/np.std(syntwave)
thres =0.5 # sample cut threshold per std

curve=syntwave
#[bo,bos,mosaic3,frequencies]=gr_bound(dep,syntwave,fscales,thres)
import pywt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
wavelet = 'gaus2'

dt=dep[1]-dep[0]
[cfs, frequencies] = pywt.cwt(curve, fscales, wavelet, dt)
#power = (abs(cfs)) ** 2
zcwt=cfs.T
#period = 1. / frequencies

#lev_contour=np.arange(np.min(zcwt),np.max(zcwt),7)


wavelet2 = 'gaus1'

[cfs, frequencies] = pywt.cwt(curve, fscales, wavelet2, dt)
#power = (abs(cfs)) ** 2
zcwt2=cfs.T
#period = 1. / frequencies


fig, (ax1, ax2,ax3) = plt.subplots(1,3,figsize=(8, 6))
ax1.plot(curve,dep)
ax1.set_ylim([np.min(dep),np.max(dep)])
ax1.invert_yaxis()
cs=ax2.contour(fscales,dep,zcwt,levels=[0.0], colors='k',extend='both')

ax2.invert_yaxis()
ax2.contourf(fscales,dep,zcwt2,levels=np.arange(np.min(zcwt),np.max(zcwt),1),
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
x0=x0-np.min(dep)
#x0[x0<0]=x0[x0<0]*-1.0
#rescale to a array position scale (to call the zcwt2)
x02=x0/dt
y02=(y0-np.min(y0))/(np.max(y0)-np.min(y0))*(len(fscales)-1)

z0=np.zeros([x0.shape[0]],dtype=float)

for i in range(z0.shape[0]):
   # if int(np.floor(x02[i])) < (zcwt2.shape[0]):
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

ax2.plot((bo[:,1]/fscales.shape[0])*(np.max(fscales)-np.min(fscales))+np.min(fscales),(bo[:,0])*dt+np.min(dep),'wo',markersize=5,markeredgecolor='y')
ax2.yaxis.set_visible(False)

#calculate the boundary strength & getting the signal polarity
bos=np.zeros([len(dep),2],dtype=float)
for i in range(0,bo.shape[0]):
    bos[int(np.round(bo[i,0])),0]=np.abs(bo[i,2])/np.max(np.abs(bo[:,2]))
    bos[int(np.round(bo[i,0])),1]=np.sign(curve[int(np.round(bo[i,0]))])

data=bos
mosaic=np.zeros([data.shape[0],100],dtype=int)*np.nan

colnum=1000
colrange=np.linspace(0,colnum,data.shape[0],dtype=int)

for i in range(0,data.shape[0]):
    if data[i,0] != 0.0:
        mosaic[i,0:int(np.floor(data[i,0]*100.0))]=colrange[i]
for i in range(0,data.shape[0]):
    if ~np.isnan(mosaic[i,0]):
        for j in range(0,100):
            if np.isnan(mosaic[i,j]):
                fl=i
                while True:
                    mosaic[fl,j-1]=mosaic[i,0]
                    fl=fl-1
                    if fl<0 or ~np.isnan(mosaic[fl,j-1]):
                        break
                break
for i in range(0,data.shape[0]):
    if ~np.isnan(mosaic[i,0]):
        for j in range(0,100):
            if np.isnan(mosaic[i,j]):
                fl=i+1
                while True:
                    mosaic[fl,j-1]=mosaic[i,0]+2
                    fl=fl+1
                    if fl>data.shape[0]-1 or ~np.isnan(mosaic[fl,j-1]):
                        break
                break
mosaic[0:np.where(data[:,0]==1.0)[0][0],99]=100.0
mosaic[np.where(data[:,0]==1.0)[0][0]:,99]=mosaic[np.where(data[:,0]==1.0)[0][0],0]
mosaic2=mosaic
pdmos=pd.DataFrame(mosaic)
pdmos=pdmos.T
pdmos=pdmos.fillna(method='bfill').T
mosaic=pdmos.values

mosaic3=mosaic[np.arange(0,data.shape[0],10),:]
x=np.where(~np.isnan(mosaic2))[0][:]
x=np.floor(x/10).astype(int)
y=np.where(~np.isnan(mosaic2))[1][:]
grids=np.zeros([mosaic3.shape[0],100])*np.nan
grids[x,y]=1.0

#ax3.barh(dep,bos[:,0])
#ax3.set_ylim([np.min(dep),np.max(dep)])
#ax3.invert_yaxis()
#ax3.set_aspect('auto')

ax3.imshow(mosaic3,cmap='Spectral_r')
ax3.imshow(grids,interpolation='none')
ax3.set_aspect('auto')
ax3.yaxis.set_visible(False)
