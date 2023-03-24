# This imports xrd data from multiple files and organizes data to plot
# one graph with diferent age samples
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Make list to hold XRD data for each PC composition

Centroid_150 = []
Centroid_160 = []
Mg_axial_158 = []

Data_lable = ['Zero background plate', 'bakcfill spinner']

#%% Import and organize XRD data 

# This function extracts just the 2theta and intensity data
# fram_index is the index of the postion of the frame you want inside
# the "dataframe_of_frames" 
def my_data_extract(fram_index): 
    tempArray = dataframe_of_frames[fram_index]
    a = np.array(tempArray.loc[:,'Angle'])
    b = np.array(tempArray.loc[:,' Intensity'])
    scale = np.amax(b) #find max intensity
    c = b / scale * 100 #scale to 100% intencity
    tempMatrix = np.vstack((a,c))
    return  tempMatrix


# Use "f_name" to know what file is in what
# position. The index of "f_name" matches the index of "dataframe_of_frames"

# Import data
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Spin_V_0_background' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
print('List of files', pd.DataFrame(f_name))
print('Check that index matches with data sotored to named array')
f_howmany = range(len(f_name))
dataframe_of_frames = []

for x in f_howmany:
    temp_df=pd.read_csv(os.path.join(datpath, f_name[x]),skiprows=(range(0, 25)))
    dataframe_of_frames.append(temp_df)

Centroid_150.append(my_data_extract(0))
Centroid_160.append(my_data_extract(1))
Mg_axial_158.append(my_data_extract(2))

Centroid_150.append(my_data_extract(3))
Centroid_160.append(my_data_extract(4))
Mg_axial_158.append(my_data_extract(5))



#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 0.0 #used to shift graphs up or down
lnthikness= 0.5
xlimits = [ 5, 65]
ylimits = [0, 110]
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
    ax.plot(xrd_data[n][0,:], xrd_data[n][1,:], 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])
    n=1 
    ax.plot(xrd_data[n][0,:], xrd_data[n][1,:], 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])
    # ax.axhline(y=0.0, color='#808080', lw=lnthikness, ls=':')
        
    # ax.plot(xrd_data[n][0,:], xrd_data[0][1,:] / xrd_data[1][1,:], plots the diferance
    # linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])

    ax.set_xlabel("2θ (degrees)", fontsize=9)
    ax.set_ylabel("Intensity (%)", fontsize=9)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(xlimits)
    ax.set_ylim(ylimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticks([0, 50, 100])
    # ax.tick_params(axis='y',length=0)
    plt.title(plt_title)
    
    #Revers order of legend lables
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])

    svg_name_path = 'Plots/28day_to_28day_mirror/' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig


#%% Mg-Axial

xrd_quad_plot(Mg_axial_158 , Data_lable , ColorPalet_1, 'spinV0bkg_Mg_Axial',\
              'Mg-Axial')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Centroid plot

xrd_quad_plot(Centroid_150 , Data_lable , ColorPalet_1, 'spinV0bkg_Centroid_150',\
               'centroid_150')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Centroid plot

xrd_quad_plot(Centroid_160 , Data_lable , ColorPalet_1, 'spinV0bkg_Centroid_160',\
               'centroid_150')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

