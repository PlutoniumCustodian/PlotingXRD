# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:22:12 2023

@author: Titus
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties
#%% Set location of data
datpath = 'Files_organized_for_plots/Water_washed_5dayOld/' # directory where data is 
#stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
print(pd.DataFrame(f_name))
#%% Make list to hold XRD data for each PC composition

XRDdata = []

#Name your data
XRD_label = ['N-P', 'L-P', 'H-P', 'M-Mg', 'H-Mg','M-Al', 'H-Al']

#%% Import data
#This section will read only the diffraction data of the  xy  files in the folder
# at the path "datapath" into a data frame.

f_howmany = range(len(f_name))
dataframe_of_frames = []

for x in f_howmany:
    temp_df=pd.read_csv(os.path.join(datpath, f_name[x]), delim_whitespace=True, header=None)
    dataframe_of_frames.append(temp_df)

    
#%% Organize dat

# this section takes all of the x data and all of the y data and places them
# in one list

#fram_index is the index of the postion of the frame you whant
#inside the "dataframe_of_frames"
def my_data_extract(fram_index): 
    tempArray = dataframe_of_frames[fram_index]
    a = np.array(tempArray.iloc[:, 0])
    b = np.array(tempArray.loc[:,1])
    # scale = np.amax(b)
    # c = b / scale #scales intencity so max intcity is 100%
    tempMatrix = np.vstack((a,b))
    return  tempMatrix

# extracts the angle and intesity data from one xrd file into a array

for n in f_howmany:
    XRDdata.append(my_data_extract(n))
    
#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 4500 #used to shift graphs up or down
lnthikness= 1
xlimits = [ 5, 65]
ylimits = [.25, 3]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)
ColorPalet_1 = ['#c76f0a', '#626161', '#000000', '#58a265','#0e7723', '#5560a2', '#0e0e77']


#%% Ploting Function
test= 'Test_plot'

def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name, plt_title, offset):
    num_of_scans = range(len(xrd_data))
 
    for n in num_of_scans:
        ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*offset, 
        linewidth=lnthikness, label=plot_names[n],  color=ColorPalet[n]) #color=ColorPalet[n]

    ax.set_xlabel("2θ (degrees)", fontsize=14)
    ax.set_ylabel("Intensity", fontsize=14)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlim(xlimits)
    # ax.set_ylim(ylimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticklabels([])
    ax.tick_params(axis='y',length=0)
    # plt.title(plt_title)
    ax.spines[['right', 'top']].set_visible(False)
    
    # #Revers order of legend lables
    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(handles[::-1], labels[::-1],loc='upper right')

    svg_name_path = 'Plots/Washed_5_day_old/' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Plot
fig, ax = plt.subplots(figsize=(3.95,5.8)) #size is in inches
xrd_quad_plot(XRDdata, XRD_label, ColorPalet_1, 'All_5day_washed_stacked', '',3500 )

#%% Plot

fig, ax = plt.subplots(figsize=(3.3,5)) #size is in inches  
xrd_quad_plot(XRDdata, XRD_label, ColorPalet_1, 'All_5day_washed_003_peak_V2', '', 0)
ax.set_xlim([ 7.5, 15])
ax.set_ylim([0, 3500])

#%% plot a few plot (Centroid to no phosphate)
# n=4
# fig, ax = plt.subplots(figsize=(8,5)) #size is in inches
# ax.plot(XRDdata[n][0,:], XRDdata[n][1,:], 
#     linewidth=lnthikness, label=XRD_label[n]) #color=ColorPalet[n], , XRD_label[n]

# n=5
# ax.plot(XRDdata[n][0,:], XRDdata[n][1,:]+ 1*off_set, 
#     linewidth=lnthikness, label=XRD_label[n]) #color=ColorPalet[n], , XRD_label[n]

# n=6
# ax.plot(XRDdata[n][0,:], XRDdata[n][1,:]+ 2*off_set, 
#     linewidth=lnthikness, label=XRD_label[n]) #color=ColorPalet[n], , XRD_label[n]

# ax.set_xlabel("2θ (degrees)", fontsize=9)
# ax.set_ylabel("Intensity", fontsize=9)
# ax.tick_params(axis='x', labelsize=8)
# ax.tick_params(axis='y', labelsize=8)
# ax.set_xlim(xlimits)
# # ax.set_ylim(ylimits)
# ax.xaxis.set_minor_locator(MultipleLocator(2.5))
# ax.yaxis.set_ticklabels([])
# ax.tick_params(axis='y',length=0)
# # plt.title(plt_title)
# ax.spines[['right', 'top']].set_visible(False)

# # #Revers order of legend lables
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles[::-1], labels[::-1],loc='upper right')

# svg_name_path = 'Plots/Washed_5_day_old/' + 'Centroid_to_PO4Free_5day_washed_offset' + '.svg'
# # Uncomment this line to save the figure.
# fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")

# #%% plot a few plot (high Al ones)
# n=3
# fig, ax = plt.subplots(figsize=(8,5)) #size is in inches
# ax.plot(XRDdata[n][0,:], XRDdata[n][1,:], 
#     linewidth=lnthikness, label=XRD_label[n]) #color=ColorPalet[n], , XRD_label[n]

# n=2
# ax.plot(XRDdata[n][0,:], XRDdata[n][1,:]+ 1*off_set, 
#     linewidth=lnthikness, label=XRD_label[n]) #color=ColorPalet[n], , XRD_label[n]

# ax.set_xlabel("2θ (degrees)", fontsize=9)
# ax.set_ylabel("Intensity", fontsize=9)
# ax.tick_params(axis='x', labelsize=8)
# ax.tick_params(axis='y', labelsize=8)
# ax.set_xlim(xlimits)
# # ax.set_ylim(ylimits)
# ax.xaxis.set_minor_locator(MultipleLocator(2.5))
# ax.yaxis.set_ticklabels([])
# ax.tick_params(axis='y',length=0)
# # plt.title(plt_title)
# ax.spines[['right', 'top']].set_visible(False)

# # #Revers order of legend lables
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles[::-1], labels[::-1],loc='upper right')

# svg_name_path = 'Plots/Washed_5_day_old/' + 'High-Al_5day_washed' + '.svg'
# # Uncomment this line to save the figure.
# # fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
