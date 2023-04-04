# This imports xrd data from multiple files and organizes data to plot
# one graph with diferent age samples
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Make list to hold XRD data for each PC composition


Al_corner = []
Centroid = []
Mg_corner = []

Data_lable = ['original', 'with corundum']

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

# Import data
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Quant' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
print('List of 28-day files', pd.DataFrame(f_name))
print('Check that index matches with data sotored to named array')
f_howmany = range(len(f_name))
dataframe_of_frames = []

for x in f_howmany:
    temp_df=pd.read_csv(os.path.join(datpath, f_name[x]),skiprows=(range(0, 25)))
    dataframe_of_frames.append(temp_df)

Al_corner.append(my_data_extract(0))
Al_corner.append(my_data_extract(1))
Centroid.append(my_data_extract(2))
Centroid.append(my_data_extract(3))
Mg_corner.append(my_data_extract(4))
Mg_corner.append(my_data_extract(5))




#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = .7 #6500 #used to shift graphs up or down
lnthikness= 0.5
xlimits = [ 5, 65]
ylimits = [0, 2]
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
    ax.set_xlim(xlimits)
    # ax.set_ylim(ylimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticklabels([])
    ax.tick_params(axis='y',length=0)
    plt.title(plt_title)
    
    #Revers order of legend lables
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])

    svg_name_path = 'Plots/Quant/' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig


#%% Al-corner plot

xrd_quad_plot(Al_corner , Data_lable , ColorPalet_1,\
              'Al_corner_Quant', 'Al-Corner')

#%% Mg-Corner plot

xrd_quad_plot(Mg_corner , Data_lable , ColorPalet_1, 'Mg_corner_Quant',\
              'Mg-Corner')

#%% Centroid plot

xrd_quad_plot(Centroid , Data_lable , ColorPalet_1, 'Centroid_Quant',\
               'centroid')



