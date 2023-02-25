import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Import data
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/PC' # directory where data is 
#stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
f_howmany = range(len(f_name))
dataframe_of_frames = []

for x in f_howmany:
    temp_df=pd.read_csv(os.path.join(datpath, f_name[x]),skiprows=(range(0, 25)))
    dataframe_of_frames.append(temp_df)
    # print(os.path.join(datpath, x))
# header=['Angle',' TimePerStep',' Intensity',' ESD'] If header is not
# correct in "dataframe_of_frame" change data file so that the headers
# start on row 26

#%% Name imported data
#Use this section to give your data a useful name manually

#fram_index is the index of the postion of the frame you whant
#inside the "dataframe_of_frames"
def my_data_extract(fram_index): 
    tempArray = dataframe_of_frames[fram_index]
    a = np.array(tempArray.loc[:,'Angle'])
    b = np.array(tempArray.loc[:,' Intensity'])
    tempMatrix = np.vstack((a,b))
    return  tempMatrix
#takes extracts the angle and intesity data from one xrd file into a array
Alax = my_data_extract(0)
Alco = my_data_extract(1)
Cent = my_data_extract(2)
Mgax = my_data_extract(3)
Mgco = my_data_extract(4)
Pax = my_data_extract(5)
Pco = my_data_extract(6)
Siax = my_data_extract(7)
Sico = my_data_extract(8)

#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 7000 #used to shift graphs up or down
lnthikness= 0.5
xlimits = [ 5, 65]
ylimits = [-300, 3.3e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Ploting XRD data 

Color = '#145092'

fig1, ax1 = plt.subplots()

ax1.plot(figsize=(4.5,5.5)) #size is in inches
ax1.plot(Cent[0,:], Cent[1,:] + 4*off_set, label='Centroid', 
        linewidth=lnthikness, color = Color )#Graph 1

ax1.plot(Mgax[0,:], Mgax[1,:] + 3*off_set, label='Mg-Axial', 
        linewidth=lnthikness , color = Color )#Graph 3
ax1.plot(Mgco[0,:], Mgco[1,:] + 2*off_set, label='Mg-Corner', 
        linewidth=lnthikness, color = Color )#Graph 2

ax1.plot(Alax[0,:], Alax[1,:] + 1*off_set, label='Al-Axial', 
        linewidth=lnthikness, color = Color )#Graph 3
ax1.plot(Alco[0,:], Alco[1,:] + 0*off_set, label='Al-Corner', 
        linewidth=lnthikness, color = Color)#Graph 2

ax1.set_xlabel("Two Theta (degrees)", fontsize=9)
ax1.set_ylabel("Intensity", fontsize=9)
ax1.tick_params(axis='x', labelsize=8)
ax1.tick_params(axis='y', labelsize=8)
ax1.set_xlim(xlimits)
ax1.set_ylim(ylimits)
ax1.xaxis.set_minor_locator(MultipleLocator(2.5))
ax1.yaxis.set_ticklabels([])
ax1.tick_params(axis='y',length=0)
plt.legend(loc=legspot)

# Uncomment this line to save the figure.
fig1.savefig('Plots/ALL_PC_1.svg', transparent=False, bbox_inches="tight")

#%% 2nd plot

Color = '#145092'

fig2, ax2 = plt.subplots()

ax2.plot(Siax[0,:], Siax[1,:] + 3*off_set, label='Si-Axial', 
        linewidth=lnthikness, color = Color)#Graph 3
ax2.plot(Sico[0,:], Sico[1,:] + 2*off_set, label='Si-Corner', 
        linewidth=lnthikness, color = Color)#Graph 2

ax2.plot(Pax[0,:], Pax[1,:] + 1*off_set, label='P-Axial', 
        linewidth=lnthikness, color = Color)#Graph 3
ax2.plot(Pco[0,:], Pco[1,:], label='P-Corner', 
        linewidth=lnthikness, color = Color)#Graph 2

ax2.set_xlabel("Two Theta (degrees)", fontsize=9)
ax2.set_ylabel("Intensity", fontsize=9)
ax2.tick_params(axis='x', labelsize=8)
ax2.tick_params(axis='y', labelsize=8)
ax2.set_xlim(xlimits)
ax2.set_ylim(ylimits)
ax2.xaxis.set_minor_locator(MultipleLocator(2.5))
ax2.yaxis.set_ticklabels([])
ax2.tick_params(axis='y',length=0)
plt.legend(loc=legspot)

# Uncomment this line to save the figure.
fig2.savefig('Plots/ALL_PC_2.svg', transparent=False, bbox_inches="tight")