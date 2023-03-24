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


Data_lable = ['original', 'repeat','less oven']

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
off_set = 0.5 #used to shift graphs up or down
lnthikness= 0.5
ylimits = [ 5, 65]
xlimits = [-110, 110]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Ploting Function
test= 'Test_plot'
ColorPalet_1 = ['#000000', '#b30009', '#2e2382', '#d80c1d']
def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name, plt_title):
    # num_of_scans = range(len(np.array(xrd_data)))
    fig, ax = plt.subplots(figsize=(7.08,3)) #size is in inches    
    n=0 
    ax.plot(xrd_data[n][0,:], xrd_data[n][1,:]* -100, 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])
    n=1 
    ax.plot(xrd_data[n][0,:], xrd_data[n][1,:]* 100, 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])
    ax.axhline(y=0.0, color='#808080', lw=lnthikness, ls=':')
        
    # ax.plot(xrd_data[n][0,:], xrd_data[0][1,:] / xrd_data[1][1,:], plots the diferance
    # linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])

    ax.set_xlabel("2θ (degrees)", fontsize=9)
    ax.set_ylabel("Intensity (%)", fontsize=9)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(ylimits)
    ax.set_ylim(xlimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticks([-100, -50 ,0, 50, 100])
    # ax.tick_params(axis='y',length=0)
    plt.title(plt_title)
    
    #Revers order of legend lables
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])

    svg_name_path = 'Plots/28day_to_28day_mirror/' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Al-axial plot

# order of inputs for xrd_quad_plot
# xrd_data, plot_names, ColorPalet, svg_file_name, plt_title
xrd_quad_plot(Al_axial, Data_lable , ColorPalet_1,\
              'Al_axial_28to28day','Al-axial')
# Uncomment this line to save the figure.
# fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")

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

