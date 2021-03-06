import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties
#%% Import data
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Centroid_changing_NaOH' # directory where data is stored relative to py script location
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
#Use "f_name" to see what files are in what posistion
Cent0714mM = my_data_extract(0)
Cent0538mM = my_data_extract(1)
Cent01000mM = my_data_extract(2)
Cent0325mM= my_data_extract(3)

#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 6000 #used to shift graphs up or down
lnthikness= 0.5
ylimits = [ 5, 65]
xlimits = [-300, 3.0e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Ploting XRD data (Al 1mL NaOH per gram)

ColorPalet = ['#17045c', '#73005d', '#b20046', '#d80c1d']
LNames = ['3.25 M', '5.38 M', '7.14 M', '10.00 M'] #Enter the names for the legend


fig, ax = plt.subplots(figsize=(7.08,5)) #size is in inches
ax.plot(Cent0325mM[0,:], Cent0325mM[1,:], label=LNames[0], 
        linewidth=lnthikness, color=ColorPalet[0])#series 1
ax.plot(Cent0538mM[0,:], Cent0538mM[1,:] + 1*off_set, label=LNames[1], 
        linewidth=lnthikness, color=ColorPalet[1])#series 2
ax.plot(Cent0714mM[0,:], Cent0714mM[1,:] + 2*off_set, label=LNames[2], 
        linewidth=lnthikness, color=ColorPalet[2])#series 3 
ax.plot(Cent01000mM[0,:], Cent01000mM[1,:] + 3*off_set, label=LNames[3],
        linewidth=lnthikness, color=ColorPalet[3])#series 4
ax.set_xlabel("Two Theta (degrees)", fontsize=9)
ax.set_ylabel("Intensity", fontsize=9)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
ax.set_xlim(ylimits)
ax.set_ylim(xlimits)
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_ticklabels([]) # Removes numbers on y-axis
ax.tick_params(axis='y',length=0) # Removes y-axis tick marks 
# Reverses order of legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])

# Uncomment this line to save the figure.
# fig.savefig('Plots/Centroid_at_dif_NaOH_levels.svg', transparent=False, bbox_inches="tight")


