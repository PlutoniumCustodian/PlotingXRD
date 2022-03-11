import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Import data
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/New_V_Old_centroid' # directory where data is stored relative to py script location
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
CenNew = my_data_extract(0)
CenOld = my_data_extract(1)


#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 6000 #used to shift graphs up or down
lnthikness= 0.5
ylimits = [ 5, 65]
xlimits = [-300, 5.5e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Ploting XRD data (Al 1mL NaOH per gram)

ColorPalet = ['#0b173a', '#245e99', '#00b4ff']

fig, ax = plt.subplots(figsize=(7.08,3)) #size is in inches

ax.plot(CenOld[0,:], CenOld[1,:] + 1*off_set, label='Dried 5 days', 
        linewidth=lnthikness, color=ColorPalet[1])#Graph 2
ax.plot(CenNew[0,:], CenNew[1,:] + 0*off_set, label='Dried 2 days', 
        linewidth=lnthikness, color=ColorPalet[0])#Graph 1
ax.set_xlabel("Two Theta (degrees)", fontsize=9)
ax.set_ylabel("Intensity", fontsize=9)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
ax.set_xlim(ylimits)
ax.set_ylim(xlimits)
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
plt.legend()
plt.legend(loc=legspot)
print(ax.get_ylim())

# Uncomment this line to save the figure.
fig.savefig('Plots/Old_Vs_new.svg', transparent=False, bbox_inches="tight")

#