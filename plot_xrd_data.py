import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Import data
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Constant_NaOH_1mL10M_to_1gPC' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
f_howmany = range(len(f_name))
dataframe_of_frames = []

for x in f_howmany:
    temp_df=pd.read_csv(os.path.join(datpath, f_name[x]),skiprows=(range(0, 25)))
    dataframe_of_frames.append(temp_df)
    # print(os.path.join(datpath, x))
# header=['Angle',' TimePerStep',' Intensity',' ESD'],
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
#%% Ploting XRD data (Al 1mL NaOH per gram)


#Values for setting that are used multple places
off_set = 8800 #used to shift graphs up or down
lnthikness= 0.5
ColorPalet = ['#0b173a', '#245e99', '#00b4ff']
ylimits = [ 5, 65]
xlimits = [-300, 3e4]

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)
x_lable = '2θ (degrees)'

fig, ax = plt.subplots(figsize=(7.08,3.5)) #size is in inches
ax.plot(Cent[0,:], Cent[1,:] + 2*off_set, label='Centroid', 
        linewidth=lnthikness, color=ColorPalet[0])#Graph 1
ax.plot(Alax[0,:], Alax[1,:] + 1*off_set, label='Al-Axial', 
        linewidth=lnthikness, color=ColorPalet[1])#Graph 3
ax.plot(Alco[0,:], Alco[1,:], label='Al-Corner', 
        linewidth=lnthikness, color=ColorPalet[2])#Graph 2
ax.set_xlim(ylimits)
ax.set_ylim(xlimits)
ax.set_xlabel(x_lable, fontsize=9)
ax.set_ylabel("Intensity", fontsize=9)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
plt.legend()

# Uncomment this line to save the figure.
fig.savefig('Plots/AL_1mL_to_1g_2.svg', transparent=False, bbox_inches="tight")

#%% Ploting XRD data (Mg 1mL NaOH per gram)


ColorPalet = ['#0d3a0c', '#0e8d13', '#00ea00']

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

fig, ax = plt.subplots(figsize=(7.08,3.5)) #size is in inches
ax.plot(Cent[0,:], Cent[1,:] + 2*off_set, label='Centroid', 
        linewidth=lnthikness, color=ColorPalet[0])#Graph 1
ax.plot(Mgax[0,:], Mgax[1,:] + 1*off_set, label='Mg-Axial', 
        linewidth=lnthikness, color=ColorPalet[1])#Graph 3
ax.plot(Mgco[0,:], Mgco[1,:], label='Mg-Corner', 
        linewidth=lnthikness, color=ColorPalet[2])#Graph 2
ax.set_xlim(ylimits)
ax.set_ylim(xlimits)
ax.set_xlabel(x_lable, fontsize=9)
ax.set_ylabel("Intensity", fontsize=9)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
plt.legend()

# Uncomment this line to save the figure.
fig.savefig('Plots/Mg_1mL_to_1g_2.svg', transparent=False, bbox_inches="tight")

#%% Ploting XRD data (Si 1mL NaOH per gram)

ColorPalet = ['#3a0b0c', '#961430', '#ff005e']

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

fig, ax = plt.subplots(figsize=(7.08,3.5)) #size is in inches
ax.plot(Cent[0,:], Cent[1,:] + 2*off_set, label='Centroid', 
        linewidth=lnthikness, color=ColorPalet[0])#Graph 1
ax.plot(Siax[0,:], Siax[1,:] + 1*off_set, label='Si-Axial', 
        linewidth=lnthikness, color=ColorPalet[1])#Graph 3
ax.plot(Sico[0,:], Sico[1,:], label='Si-Corner', 
        linewidth=lnthikness, color=ColorPalet[2])#Graph 2
ax.set_xlim(ylimits)
ax.set_ylim(xlimits)
ax.set_xlabel(x_lable, fontsize=9)
ax.set_ylabel("Intensity", fontsize=9)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
plt.legend()

# Uncomment this line to save the figure.
fig.savefig('Plots/Si_1mL_to_1g_2.svg', transparent=False, bbox_inches="tight")

#%% Ploting XRD data (P 1mL NaOH per gram)

# ylimits = [ 5, 65]
# xlimits = [-300, 3.5e4]
ColorPalet = ['#3a3914', '#788015', '#b6d100',]

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

fig, ax = plt.subplots(figsize=(7.08,3.5)) #size is in inches
ax.plot(Cent[0,:], Cent[1,:] + 2*off_set, label='Centroid', 
        linewidth=lnthikness, color=ColorPalet[0])#Graph 1
ax.plot(Pax[0,:], Pax[1,:] + 1*off_set, label='P-Axial', 
        linewidth=lnthikness, color=ColorPalet[1])#Graph 3
ax.plot(Pco[0,:], Pco[1,:], label='P-Corner', 
        linewidth=lnthikness, color=ColorPalet[2])#Graph 2
ax.set_xlim(ylimits)
ax.set_ylim(xlimits)
ax.set_xlabel(x_lable, fontsize=9)
ax.set_ylabel("Intensity", fontsize=9)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
plt.legend()

# Uncomment this line to save the figure.
fig.savefig('Plots/P_1mL_to_1g_2.svg', transparent=False, bbox_inches="tight")