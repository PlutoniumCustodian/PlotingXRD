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
# P_corner = []
Si_axial = []
Si_corner = []
PO4_free_NaOH = []


Data_lable = ['28-day', '134-day']

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
# P_corner.append(my_data_extract(8))
PO4_free_NaOH.append(my_data_extract(6))
Si_axial.append(my_data_extract(9))
Si_corner.append(my_data_extract(10))

# Import data 1mL NaOH to 1g PC aged 134 days
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/134_days' # directory where data is stored relative to py script location
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
# P_corner.append(my_data_extract(6))
PO4_free_NaOH.append(my_data_extract(6))
Si_axial.append(my_data_extract(7))
Si_corner.append(my_data_extract(8))


#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 0.25 #used to shift graphs up or down
lnthikness= 0.5
ylimits = [ 5, 65]
xlimits = [0, 1.3]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Ploting Function
ColorPalet_1 = ['#000000', '#822335', '#2e2382', '#d80c1d']
def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name, plt_title):
    num_of_scans = range(len(np.array(xrd_data)))
    fig, ax = plt.subplots(figsize=(7.08,3)) #size is in inches    

    for n in num_of_scans: #plots first line
        if n==0:
           ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
           linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])
           ax.fill_between(xrd_data[n][0,:], xrd_data[n][1,:]+ n*off_set, y2=0, 
                           color=ColorPalet[n], alpha=.4) # fils from y=0 to first line
        else:
            ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
                    linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])
            ax.fill_between(xrd_data[n][0,:], xrd_data[n][1,:]+ n*off_set, 
                            xrd_data[n-1][1,:]+ (n-1)*off_set, color=ColorPalet[n], alpha=.4) #fils from previous lin to this line
        
    # ax.plot(xrd_data[n][0,:], xrd_data[0][1,:] / xrd_data[1][1,:], plots the diferance
    # linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])

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

    svg_name_path = 'Plots/134_days/' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Al-axial plot

# order of inputs for xrd_quad_plot
# xrd_data, plot_names, ColorPalet, svg_file_name, plt_title
xrd_quad_plot(Al_axial, Data_lable , ColorPalet_1,\
              'Al_axial_28to134day','Al-Axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Al-corner plot

xrd_quad_plot(Al_corner , Data_lable , ColorPalet_1,\
              'Al_corner_28to134day', 'Al-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Mg-Axial

xrd_quad_plot(Mg_axial , Data_lable , ColorPalet_1, 'Mg_Axial_28to134day',\
              'Mg-Axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Mg-Corner plot

xrd_quad_plot(Mg_corner , Data_lable , ColorPalet_1, 'Mg_corner_28to134day',\
              'Mg-Corner')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% P-Axial

xrd_quad_plot(P_axial , Data_lable , ColorPalet_1, 'P_Axial_28to134day',\
              'P-Axial')

#%% Si-Axial

xrd_quad_plot(Si_axial , Data_lable , ColorPalet_1, 'Si_Axial_28to28day'\
              , 'Si-Axial')
#%% Si-Corner

xrd_quad_plot(Si_corner, Data_lable , ColorPalet_1, 'Si_Corner_28to28day'\
                  , 'Si-Corner')

#%% PO4Free plot

xrd_quad_plot(PO4_free_NaOH , Data_lable , ColorPalet_1, 'PO4FreeNaOH_28to134day',\
               'PO4Free_NaOH')

#%% Centroid plot

xrd_quad_plot(Centroid , Data_lable , ColorPalet_1, 'Centroid_2828to134day',\
               'Centroid')



