# This imports xrd data from multiple files and organizes data to plot
# one graph with all the activation concentration for a given PC chemistry
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Make list to hold XRD data for each PC composition

Centroid = []
Cent_label = []

#%% Import and organize XRD data 


#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Centroid_age' # directory where data is 
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


# This function extracts just the 2theta and intnsity data
# fram_index is the index of the postion of the frame you want inside
# the "dataframe_of_frames" 
def my_data_extract(fram_index): 
    tempArray = dataframe_of_frames[fram_index]
    a = np.array(tempArray.loc[:,'Angle'])
    b = np.array(tempArray.loc[:,' Intensity'])
    tempMatrix = np.vstack((a,b))
    return  tempMatrix


# extracts the angle and intesity data from one xrd file into a array

for n in f_howmany:
    Centroid.append(my_data_extract(n))
    
#%% Name things
Cent_label.append('1 day')
Cent_label.append('7 days')
Cent_label.append('14 days')
Cent_label.append('28 days')
Cent_label.append('510 days')

#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 0 #4500 #used to shift graphs up or down
lnthikness= .5
ylimits = [ 5, 65]
xlimits = [-300, 4.0e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Set up plotting function
# test= 'Test_plot'

ColorPalet_1 = ['#478d02', '#008068', '#00699c','#02458d','#000000']

def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name, plt_title):
    num_of_scans = range(len(np.array(xrd_data)))
    fig, ax = plt.subplots(figsize=(3, 3)) #size is in inches    
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
    ax.tick_params(axis='y',length=0)
    #plt.title(plt_title)
    # ax.legend()
    #Revers order of legend lables
    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(handles[::-1], labels[::-1])
    ax.spines[['right', 'top']].set_visible(False) # get rid of box around plot

    svg_name_path = 'Plots/1_to_740days/ForACerS_2023/' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Centroid plots

xrd_quad_plot(Centroid, Cent_label , ColorPalet_1,\
              'Centroid_at_different_age_ACerS_no_offset5','Centroid')


