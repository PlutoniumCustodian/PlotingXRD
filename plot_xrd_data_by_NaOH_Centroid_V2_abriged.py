# This imports xrd data from multiple files and organizes data to plot
# one graph with all the activation concentration for a given PC chemistry
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Make list to hold XRD data for each PC composition

# Al_axial = []
# Al_corner = []
Centroid = []
# Mg_axial = []
# Mg_corner = []
# P_axial = []
# P_corner = []
# Si_axial = []
# Si_corner = []

# Al_a_label = []
# Al_c_label = []
Cent_label = []
# Mg_a_label = []
# Mg_c_label = []
# P_a_label = []
# P_c_label = []
# Si_a_label = []
# Si_c_label = []

#%% Import and organize XRD data 

#Import data for unactivated PC
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Centroid_changing_NaOH_V2' # directory where data is 
#stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
f_howmany = range(len(f_name))
dataframe_of_frames = []

for x in f_howmany:
    temp_df=pd.read_csv(os.path.join(datpath, f_name[x]),skiprows=(range(0, 25)))
    dataframe_of_frames.append(temp_df)
# header=['Angle',' TimePerStep',' Intensity',' ESD'] If header is not
# correct in "dataframe_of_frame" change data file so that the headers
# starts on row 26

# Name imported data
# Use this section to give your data a useful name manually
# This section also extracts and converts to an array the 
# angle and intesity data that was in a data frame. 

# This function extracts just the 2theta and intnsity data
# fram_index is the index of the postion of the frame you want inside
# the "dataframe_of_frames" 
def my_data_extract(fram_index): 
    tempArray = dataframe_of_frames[fram_index]
    a = np.array(tempArray.loc[:,'Angle'])
    b = np.array(tempArray.loc[:,' Intensity'])
    tempMatrix = np.vstack((a,b))
    return  tempMatrix

# This function takes the string that is the XRD file name and returns the
# the section of the string that has the NaOH molarty data and formats it.
def concentration_lable(name_index):
    molar_tag = f_name[name_index].find('M_',25)
    molar_value=(f_name[name_index][molar_tag-4:molar_tag-2]) + '.'\
        + (f_name[name_index][molar_tag-2:molar_tag]) + ' M'
    #removes leading zero from molarity value
    if molar_value[0]=='0': molar_value = molar_value.replace('0', '',1)
    return molar_value

# Use "f_name" to know what file is in what
# position. The index of "f_name" matches the index of "dataframe_of_frames"

# extracts the angle and intesity data from one xrd file into a array

for n in f_howmany:
    Centroid.append(my_data_extract(n))
    Cent_label.append(concentration_lable(n))
    
Cent_label[0] = 'Unactivated'


# Import data for centroid concentrations

# #This section will read only the diffraction data of the  csv  files in the folder
# # at the path "datapath" into a data frame.
# datpath = 'Files_organized_for_plots/Centroid_changing_NaOH_V2' # directory where data is 
# #stored relative to py script location
# f_name = (os.listdir(datpath))#list of files in the directory of datpath
# f_howmany = range(len(f_name))
# dataframe_of_frames = []

# for x in f_howmany:
#     temp_df=pd.read_csv(os.path.join(datpath, f_name[x]),skiprows=(range(0, 25)))
#     dataframe_of_frames.append(temp_df)
#     # print(os.path.join(datpath, x))
# # header=['Angle',' TimePerStep',' Intensity',' ESD'] If header is not
# # correct in "dataframe_of_frame" change data file so that the headers
# # start on row 26

# for n in f_howmany:
#     Centroid.append(my_data_extract(n))
#     Cent_label.append(concentration_lable(n))



#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 10000 #used to shift graphs up or down
lnthikness= 0.5
ylimits = [ 5, 65]
xlimits = [-300, 4.0e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Set up plotting function
# test= 'Test_plot'
ColorPalet_1 = ['#252089', '#6a3a9f', '#a05ab6', '#d17ecd', '#ffa5e6', 
                '#e27cb2', '#0b173a', '#245e99', '#00b4ff']
def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name, plt_title):
    # num_of_scans = range(len(np.array(xrd_data)))
    num_of_scans = range(6,9,1)
    fig, ax = plt.subplots(figsize=(7.08,5)) #size is in inches    
    for n in num_of_scans:
        ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])

    ax.set_xlabel("Two Theta (degrees)", fontsize=9)
    ax.set_ylabel("Intensity", fontsize=9)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(ylimits)
    # ax.set_ylim(xlimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticklabels([])
    plt.grid(which='both', axis='x')
    ax.tick_params(axis='y',length=0)
    plt.title(plt_title)
    # ax.legend()
    #Revers order of legend lables
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])

    svg_name_path = 'Plots/' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    # fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Centroid plots

xrd_quad_plot(Centroid, Cent_label , ColorPalet_1,\
              'Centroid_at_dif_NaOH_levelsV2_abriged2','Centroid')


