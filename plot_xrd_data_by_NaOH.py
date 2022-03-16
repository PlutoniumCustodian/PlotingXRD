# This imports xrd data from multiple files and organizes data to plot
# one graph with all the activation concentration for a given PC chemistry
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Make data frames to hold XRD data for each PC composition

Al_axial = []
Al_corner = []
Centroid = []
Mg_axial = []
Mg_corner = []
P_axial = []
P_corner = []
Si_axial = []
Si_corner = []

#%% Import and organize XRD data 

#Import data for unactivated PC
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
# starts on row 26

# Name imported data
# Use this section to give your data a useful name manually
# This section also extracts and converts to an array the 
# angle and intesity data that was in a data frame. 

# fram_index is the index of the postion of the frame you want inside
# the "dataframe_of_frames" 
def my_data_extract(fram_index): 
    tempArray = dataframe_of_frames[fram_index]
    a = np.array(tempArray.loc[:,'Angle'])
    b = np.array(tempArray.loc[:,' Intensity'])
    tempMatrix = np.vstack((a,b))
    return  tempMatrix


# Use "f_name" to know what file is in what
# position. The index of "f_name" matches the index of "dataframe_of_frames"

# extracts the angle and intesity data from one xrd file into a array

Al_axial.append(my_data_extract(0))
Al_corner.append(my_data_extract(1))
Centroid.append(my_data_extract(2))
Mg_axial.append(my_data_extract(3))
Mg_corner.append(my_data_extract(4))
P_axial.append(my_data_extract(5))
P_corner.append(my_data_extract(6))
Si_axial.append(my_data_extract(7))
Si_corner.append(my_data_extract(8))

# Import data Na:Al = 1

#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Na_to_Al_1' # directory where data is 
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

Al_axial.append(my_data_extract(0))
Al_corner.append(my_data_extract(1))
Centroid.append(my_data_extract(2))
Mg_axial.append(my_data_extract(3))
Mg_corner.append(my_data_extract(4))
P_axial.append(my_data_extract(5))
P_corner.append(my_data_extract(6))
Si_axial.append(my_data_extract(7))
Si_corner.append(my_data_extract(8))

# Import data 1/2 mL NaOH per 1g PC
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Constant_NaOH_half_mL10M_to_1gPC' # directory where data is stored relative to py script location
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

Al_axial.append(my_data_extract(0))
Al_corner.append(my_data_extract(1))
Centroid.append(my_data_extract(2))
Mg_axial.append(my_data_extract(3))
Mg_corner.append(my_data_extract(4))
P_axial.append(my_data_extract(5))
P_corner.append(my_data_extract(6))
Si_axial.append(my_data_extract(7))
Si_corner.append(my_data_extract(8))

# Import data 1mL NaOH to 1g PC
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Constant_NaOH_1mL10M_to_1gPC' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
f_howmany = range(len(f_name))
dataframe_of_frames = []

for x in f_howmany:
    temp_df=pd.read_csv(os.path.join(datpath, f_name[x]),skiprows=(range(0, 25)))
    dataframe_of_frames.append(temp_df)

Al_axial.append(my_data_extract(0))
Al_corner.append(my_data_extract(1))
Centroid.append(my_data_extract(2))
Mg_axial.append(my_data_extract(3))
Mg_corner.append(my_data_extract(4))
P_axial.append(my_data_extract(5))
P_corner.append(my_data_extract(6))
Si_axial.append(my_data_extract(7))
Si_corner.append(my_data_extract(8))

#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 7500 #used to shift graphs up or down
lnthikness= 0.5
ylimits = [ 5, 65]
xlimits = [-300, 3e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Ploting Al-Axial
test= 'Test_plot'
ColorPalet_1 = ['#17045c', '#73005d', '#b20046', '#d80c1d']
def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name):
    num_of_scans = range(len(np.array(xrd_data)))
    fig, ax = plt.subplots(figsize=(7.08,3)) #size is in inches    
    for n in num_of_scans:
        ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])

    ax.set_xlabel("Two Theta (degrees)", fontsize=9)
    ax.set_ylabel("Intensity", fontsize=9)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(ylimits)
    ax.set_ylim(xlimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticklabels([])
    ax.tick_params(axis='y',length=0)
    
    #Revers order of legend lables
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])

    svg_name_path = 'Plots/' + svg_file_name + '.svg'
    fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

xrd_quad_plot(Al_axial, ['A','B','C','D'], ColorPalet_1, test)
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")


