# This imports xrd data from multiple files and organizes data to plot
# one graph with diferent age samples
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
PO4_free_NaOH = []


Data_lable = ['original', 'repeat','difference']

#%% Import and organize XRD data 

# This function extracts just the 2theta and intensity data
# fram_index is the index of the postion of the frame you want inside
# the "dataframe_of_frames" 
def my_data_extract(fram_index): 
    tempArray = dataframe_of_frames[fram_index]
    a = np.array(tempArray.loc[:,'Angle'])
    b = np.array(tempArray.loc[:,' Intensity'])
    scale = np.amax(b)
    c = b / scale
    tempMatrix = np.vstack((a,c))
    return  tempMatrix


# Use "f_name" to know what file is in what
# position. The index of "f_name" matches the index of "dataframe_of_frames"

# Import data 1mL NaOH to 1g PC aged 28 day (Original)
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Constant_NaOH_1mL10M_to_1gPC_28Day' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
print('List of 28-day files', pd.DataFrame(f_name))
print('Check that index matches with data sotored to named array')
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
P_axial.append(my_data_extract(7))
P_corner.append(my_data_extract(8))
PO4_free_NaOH.append(my_data_extract(6))
Si_axial.append(my_data_extract(9))
Si_corner.append(my_data_extract(10))

# Import data 1mL NaOH to 1g PC aged 28 day repeat
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Constant_NaOH_1mL10M_to_1gPC_28Day_repeat' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
print('List of repeated 28-day files', pd.DataFrame(f_name))
print('Check that index matches with data sotored to named array')
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
PO4_free_NaOH.append(my_data_extract(7))
Si_axial.append(my_data_extract(8))
Si_corner.append(my_data_extract(9))
Centroid.append(my_data_extract(10))

#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 0.3 #used to shift graphs up or down
lnthikness= 0.5
ylimits = [ 0, 65]
xlimits = [0, 1.4]
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
    fig = plt.figure(figsize=[7.08, 6] ,constrained_layout=True) #size is in inche
    gs = fig.add_gridspec(4, 1)
    ax1 = fig.add_subplot(gs[:-1, :])
    for n in num_of_scans:
        ax1.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])
    ax3 = fig.add_subplot(gs[-1, :])    
    ax3.plot(xrd_data[n][0,:], xrd_data[0][1,:] - xrd_data[1][1,:], 
    linewidth=lnthikness, color='k', label=plot_names[n])
    ax3.set_ylabel("diferance (old/new)", fontsize=9)

    ax1.set_xlabel("2θ (degrees)", fontsize=9)
    ax1.set_ylabel("Intensity", fontsize=9)
    ax1.tick_params(axis='x', labelsize=8)
    ax1.tick_params(axis='y', labelsize=8)
    ax1.set_xlim(ylimits)
    ax1.set_ylim(xlimits)
    ax1.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax1.yaxis.set_ticklabels([])
    ax1.tick_params(axis='y',length=0)
    plt.title(plt_title)
    
    #Revers order of legend lables
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles[::-1], labels[::-1])

    svg_name_path = 'Plots/28day_to_28day' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Al-axial plot

# order of inputs for xrd_quad_plot
# xrd_data, plot_names, ColorPalet, svg_file_name, plt_title
xrd_quad_plot(Al_axial, Data_lable , ColorPalet_1,\
              'Al_axial_28to28day','Al-axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Al-corner plot

xrd_quad_plot(Al_corner , Data_lable , ColorPalet_1,\
              'Al_corner_28to28day', 'Al-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Mg-Axial

xrd_quad_plot(Mg_axial , Data_lable , ColorPalet_1, 'Mg_Axial_28to28day',\
              'Mg-Axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Mg-Corner plot

xrd_quad_plot(Mg_corner , Data_lable , ColorPalet_1, 'Mg_corner_28to28day',\
              'Mg-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% P-Axial

xrd_quad_plot(P_axial , Data_lable , ColorPalet_1, 'P_Axial_28to28day',\
              'P-axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% P-Corner plot

xrd_quad_plot(P_corner , Data_lable , ColorPalet_1, 'P_corner_28to28day'\
              , 'P-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Si-Axial

xrd_quad_plot(Si_axial , Data_lable , ColorPalet_1, 'Si_Axial_28to28day'\
              , 'Si-axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Si-Corner plot

xrd_quad_plot(Si_corner , Data_lable , ColorPalet_1, 'Si_corner_28to28day',\
               'Si-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Centroid plot

xrd_quad_plot(Centroid , Data_lable , ColorPalet_1, 'Centroid_28to28day',\
               'centroid')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

