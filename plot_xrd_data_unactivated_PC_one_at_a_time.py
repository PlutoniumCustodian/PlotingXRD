import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Make list to hold XRD data for each PC composition

RGPC = []
RGPC_label = []

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

# extracts the angle and intesity data from one xrd file into a array

for n in f_howmany:
    RGPC.append(my_data_extract(n))

#Name things
RGPC_label.append('Al-Axial')
RGPC_label.append('Al-Corner')
RGPC_label.append('Centroid')
RGPC_label.append('Mg-Axial')
RGPC_label.append('Mg-Corner')
RGPC_label.append('P-Axial')
RGPC_label.append('P-Corner')
RGPC_label.append('Si-Axial')
RGPC_label.append('Si-Corener')
RGPC_label.append('PO4_free')
#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 7500 #used to shift graphs up or down
lnthikness= .5
ylimits = [ 5, 65]
xlimits = [-300, 3e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Set up plotting function

def xrd_single_plot(xrd_data, plot_names, svg_file_name, plt_title,n):
    fig, ax = plt.subplots(figsize=(3,2.5)) #size is in inches
    ax.plot(xrd_data[n][0,:], xrd_data[n][1,:], 
    linewidth=lnthikness, label=plot_names[n])
    ax.set_xlabel("Two Theta (degrees)", fontsize=9)
    ax.set_ylabel("Intensity", fontsize=9)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(ylimits)
    # ax.set_ylim(xlimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticklabels([])
    ax.tick_params(axis='y',length=0)
    #plt.title(plt_title)
    # ax.legend()
    #Revers order of legend lables
    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(handles[::-1], labels[::-1])
    svg_name_path = 'Plots/PC/' + svg_file_name[n] + '.svg'
    # Uncomment this line to save the figure.
    # fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Ploting XRD data
num_of_scans = range(len(np.array(RGPC)))    
for n in num_of_scans:
    xrd_single_plot(RGPC, RGPC_label, RGPC_label, RGPC_label, n)
    
#%% Manual plot just one

n=9
xrd_single_plot(RGPC, RGPC_label, RGPC_label, RGPC_label, n)
