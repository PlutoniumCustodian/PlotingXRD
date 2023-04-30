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
datpath = 'Files_organized_for_plots/Water_wash_vs_others/' # directory where data is 
#stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
print(pd.DataFrame(f_name))
#%% Make list to hold XRD data for each PC composition

XRDdata = []
#Name your data
XRD_label = ['M-S-H Nied 2016', 'Phosphoric acid intercalated LDH', 'This study']

#%% Import data
#This section will read only the diffraction data of the  csv  files in the folder
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
    scale = np.amax(b)
    c = b / scale #scales intencity so max intcity is 100%
    tempMatrix = np.vstack((a,c))
    return  tempMatrix

# extracts the angle and intesity data from one xrd file into a array

for n in f_howmany:
    XRDdata.append(my_data_extract(n))
    
#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = .5 #used to shift graphs up or down
lnthikness= .5
xlimits = [ 5, 65]
ylimits = [.25, 3]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

#%% Ploting Function

ColorPalet_1 = ['#17045c', '#73005d', '#b20046', '#d80c1d']
def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name, plt_title):
    num_of_scans = range(len(xrd_data))
    fig, ax = plt.subplots(figsize=(7.08,6)) #size is in inches    
    for n in num_of_scans:
        ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])

    ax.set_xlabel("2θ (degrees)", fontsize=9)
    ax.set_ylabel("Intensity", fontsize=9)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(xlimits)
    ax.set_ylim(ylimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticklabels([])
    ax.tick_params(axis='y',length=0)
    plt.title(plt_title)
    
    #Revers order of legend lables
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1],loc='upper right')

    svg_name_path = 'Plots/Water_wash_vs_others/' + svg_file_name + '.svg'
    # Uncomment this line to save the figure.
    # fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Plot

xrd_quad_plot(XRDdata, XRD_label, ColorPalet_1, 'Water_wash_vs_others', '')

#%% manualy adjustable plot
ColorPalet_1 = ['#17045c', '#73005d', '#b20046', '#d80c1d']
fig, ax = plt.subplots(figsize=(7.08, 6)) #size is in inches    
n=0
ax.plot(XRDdata[n][0,:], XRDdata[n][1,:] - .45, linewidth=lnthikness, color=ColorPalet_1[n], label=XRD_label[n])
n=1
ax.plot(XRDdata[n][0,:], XRDdata[n][1,:] + .3, linewidth=lnthikness, color=ColorPalet_1[n], label=XRD_label[n])
n=2
ax.plot(XRDdata[n][0,:], XRDdata[n][1,:] + 1.2, linewidth=lnthikness, color=ColorPalet_1[n], label=XRD_label[n])

ax.set_xlabel("2θ (degrees)", fontsize=9)
ax.set_ylabel("Intensity", fontsize=9)
ax.tick_params(axis='x', labelsize=8)
ax.tick_params(axis='y', labelsize=8)
ax.set_xlim( [5, 65])
ax.set_ylim([0,2.5])
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_ticklabels([])
ax.tick_params(axis='y',length=0)
# plt.title(plt_title)
 
#Revers order of legend lables
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1],loc='upper right')
svg_name_path = 'Plots/Water_wash_vs_others/' + 'Water_wash_vs_others' + '.svg'
# Uncomment this line to save the figure.
fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
