# This imports xrd data from multiple files and organizes data to plot
# one graph with all the activation concentration for a given PC chemistry
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Make list to hold XRD data for each PC composition

Al_axial = []
Al_corner = []
Centroid = []
Mg_axial = []
Mg_corner = []
P_axial = []
P_corner = []
Si_axial = []
Si_corner = []

Al_a_label = []
Al_c_label = []
Cent_label = []
Mg_a_label = []
Mg_c_label = []
P_a_label = []
P_c_label = []
Si_a_label = []
Si_c_label = []

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

Al_axial.append(my_data_extract(0))
Al_corner.append(my_data_extract(1))
Centroid.append(my_data_extract(2))
Mg_axial.append(my_data_extract(3))
Mg_corner.append(my_data_extract(4))
P_axial.append(my_data_extract(5))
P_corner.append(my_data_extract(6))
Si_axial.append(my_data_extract(7))
Si_corner.append(my_data_extract(8))

x = 'Unactivated'
Al_a_label.append(x)
Al_c_label.append(x)
Cent_label.append(x)
Mg_a_label.append(x)
Mg_c_label.append(x)
P_a_label.append(x)
P_c_label.append(x)
Si_a_label.append(x)
Si_c_label.append(x)

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

Al_a_label.append(concentration_lable(0))
Al_c_label.append(concentration_lable(1))
Cent_label.append(concentration_lable(2))
Mg_a_label.append(concentration_lable(3))
Mg_c_label.append(concentration_lable(4))
P_a_label.append(concentration_lable(5))
P_c_label.append(concentration_lable(6))
Si_a_label.append(concentration_lable(7))
Si_c_label.append(concentration_lable(8))

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

Al_a_label.append(concentration_lable(0))
Al_c_label.append(concentration_lable(1))
Cent_label.append(concentration_lable(2))
Mg_a_label.append(concentration_lable(3))
Mg_c_label.append(concentration_lable(4))
P_a_label.append(concentration_lable(5))
P_c_label.append(concentration_lable(6))
Si_a_label.append(concentration_lable(7))
Si_c_label.append(concentration_lable(8))

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

Al_a_label.append(concentration_lable(0))
Al_c_label.append(concentration_lable(1))
Cent_label.append(concentration_lable(2))
Mg_a_label.append(concentration_lable(3))
Mg_c_label.append(concentration_lable(4))
P_a_label.append(concentration_lable(5))
P_c_label.append(concentration_lable(6))
Si_a_label.append(concentration_lable(7))
Si_c_label.append(concentration_lable(8))

#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 6500 #used to shift graphs up or down
lnthikness= 0.5
ylimits = [ 5, 65]
xlimits = [-300, 3.5e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Ploting Function
test= 'Test_plot'
ColorPalet_1 = ['#17045c', '#73005d', '#b20046', '#d80c1d']
def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name, plt_title):
    num_of_scans = range(len(np.array(xrd_data)))
    fig, ax = plt.subplots(figsize=(7.08,3)) #size is in inches    
    for n in num_of_scans:
        ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])

    ax.set_xlabel("2θ (degrees)", fontsize=9)
    ax.set_ylabel("Intensity", fontsize=9)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(ylimits)
    ax.set_ylim(xlimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticklabels([])
    ax.tick_params(axis='y',length=0)
    plt.title(plt_title)
    
    #Revers order of legend lables
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])

    svg_name_path = 'Plots/' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    # fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Al-axial plot

del Al_axial[1]
del Al_a_label[1]
xrd_quad_plot(Al_axial, Al_a_label , ColorPalet_1,\
              'Al_axial_NaOH_concentration','Al-axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Al-corner plot

del Al_corner[1]
del Al_c_label[1]
xrd_quad_plot(Al_corner , Al_c_label , ColorPalet_1,\
              'Al_corner_NaOH_concentration', 'Al-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Mg-Axial

xrd_quad_plot(Mg_axial , Mg_a_label , ColorPalet_1, 'Mg_Axial_concentration',\
              'Mg-Axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Mg-Corner plot

xrd_quad_plot(Mg_corner , Mg_c_label , ColorPalet_1, 'Mg_corner_concentration',\
              'Mg-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% P-Axial

xrd_quad_plot(P_axial , P_a_label , ColorPalet_1, 'P_Axial_concentration',\
              'P-axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% P-Corner plot

xrd_quad_plot(P_corner , P_c_label , ColorPalet_1, 'P_corner_concentration'\
              , 'P-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Si-Axial

xrd_quad_plot(Si_axial , Si_a_label , ColorPalet_1, 'Si_Axial_concentration'\
              , 'Si-axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Si-Corner plot

xrd_quad_plot(Si_corner , Si_c_label , ColorPalet_1, 'Si_corner_concentration',\
              'Si-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% single Al-Corner graph
lnthikness= 0.5
xlimits = [ 5, 65]
ylimits = [0, 1.2e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)
n=2

fig, ax = plt.subplots(figsize=(8.08,3)) #size is in inches

ax.plot(Al_corner[n][0,:], Al_corner[n][1,:], 
    linewidth=lnthikness, color='#176100')
ax.set_xlabel("Two Theta (degrees)", fontsize=9)
ax.set_ylabel("Intensity (counts)", fontsize=9)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
ax.set_xlim(xlimits)
ax.set_ylim(ylimits)
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
# ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
#plt.title(plt_title)
# fig.savefig('Plots/AL_for_IO_poster.svg', transparent=False, bbox_inches="tight")