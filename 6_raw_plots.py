
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from striplog import Lexicon, Decor, Component, Legend, Interval, Striplog


#graph limits.  xl =  x upper limit, yl = y upper limit
xl = 250
yl = 350

#Import the data
path1 = 'C:\\Users\\obeli\\Documents\\GitHub\\Transform2020_2\\t20-litho_boundary_from_gamma\\'

data2=np.loadtxt(os.path.join(path1, 'test001_gamma.csv'),skiprows=1,delimiter=',')
#data2=np.loadtxt(data1 + 'test001_gamma.csv',skiprows=1,delimiter=',')
data3 = np.loadtxt('C:\\Users\\obeli\\Documents\\GitHub\\Transform2020_2\\t20-litho_boundary_from_gamma\\test001_gamma_5cm.csv',skiprows=1,delimiter=',')

#Original gamma (1cm data)
data2[:,0]=data2[:,0]*-1.0
data=data2[np.arange(0,36595,10),:]  #take every 10th value
dt2=data2[1,0]-data2[0,0]

#Filtered gamma (filtered data)
data3[:,0] = data3[:,0]*-1.0
data3 = data3[np.arange(0,data3.shape[0],2),:]  #use the shape (rowcount) of the array. This curve is already filtered by only taking every 5th value, then take every 2nd value
dt3 = data3[1,0]-data3[0,0]

# Pad out the filtered data set to be the same shape as first data set.
x = data2.shape[0] - data3.shape[0]
for idx in range(x):
    data3 = np.append(data3, np.array([[np.NaN,np.NaN]]), axis=0)

#Smoothed gamma (savgol smoothing)
dep=data2[:,0]
syntwave=savgol_filter(data2[:,1], 51, 3)  # filter in y direction only
syntwave2=(syntwave-np.mean(syntwave))/np.std(syntwave) #filter in y direction (?)

#--------
#plotting
#--------
with plt.rc_context({'xtick.color':'red', 'ytick.color':'red'}):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(15, 30))

#track 1
    ax1.set_title('Raw (10cm data)', color = 'tab:red')
    ax1.plot(data2[:,1],data2[:,0])
    ax1.set_ylim([0,yl])
    ax1.set_xlim([0,xl])
    ax1.invert_yaxis()

#track2
    ax2.set_title('Filtered (20cm data)', color = 'tab:red')
    ax2.plot(data3[:,1],data3[:,0])
    ax2.xaxis.label.set_color('red')
    ax2.set_ylim([0,yl])
    ax2.set_xlim([0,xl])
    ax2.invert_yaxis()

    #track3 smoothed
    ax3.set_title('Smoothed (Savgol x only smooth)', color = 'tab:red')
    ax3.plot(syntwave,dep)
    #ax3.set_ylim([np.min(dep),np.max(dep)])
    ax3.set_ylim([0,yl])
    ax3.set_xlim([0,xl])
    ax3.invert_yaxis()

    #track4 smoothed
    ax4.set_title('Smoothed (Savgol x/y smooth)', color = 'tab:red')
    ax4.plot(syntwave2,dep)
    #ax3.set_ylim([np.min(dep),np.max(dep)])
    ax4.set_ylim([0,yl])
    ax4.set_xlim([-3,5])
    ax4.invert_yaxis()

'''
fig, axs = plt.subplots(ncols=2, sharey=True)
axs[0] = strip.plot(ax=axs[0], legend=legend)
axs[1] = strip.plot_tops(axs[1], field='lithology', )
axs[1].axis('off')
plt.show()
'''

plt.show()
#plt.savefig('common_labels.png', dpi=300)
