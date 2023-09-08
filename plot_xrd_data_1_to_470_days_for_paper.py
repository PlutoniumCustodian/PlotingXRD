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
P_free = []


Data_lable = ['Unactivated','1 day', '28 days', '470 days']

#%% Import and organize XRD data 

# This function extracts just the 2theta and intensity data
# fram_index is the index of the postion of the frame you want inside
# the "dataframe_of_frames" 
def my_data_extract(fram_index): 
    tempArray = dataframe_of_frames[fram_index]
    a = np.array(tempArray.loc[:,'Angle'])
    b = np.array(tempArray.loc[:,' Intensity'])
    tempMatrix = np.vstack((a,b))
    return  tempMatrix

# Import data unactivated RGP
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/PC' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
print('List of unactivated RGP', pd.DataFrame(f_name))
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
P_free.append(my_data_extract(9))

# Import data 1mL NaOH to 1g PC aged 24 hours (1day)
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/Constant_NaOH_1mL10M_to_1gPC' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
print('List of 1-day files', pd.DataFrame(f_name))
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
P_free.append(my_data_extract(9))


# Import data 1mL NaOH to 1g PC aged 28 day
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
P_free.append(my_data_extract(6))

# Import data 1mL NaOH to 1g PC aged 470 day
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = 'Files_organized_for_plots/470_day' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))#list of files in the directory of datpath
print('List of 470-day files', pd.DataFrame(f_name))
print('Check that index matches with data sotored to named array')
f_howmany = range(len(f_name))
dataframe_of_frames = []

for x in f_howmany:
    temp_df=pd.read_csv(os.path.join(datpath, f_name[x]),skiprows=(range(0, 25)))
    dataframe_of_frames.append(temp_df)

Al_axial.append(my_data_extract(0))
Al_corner.append(my_data_extract(3))
Centroid.append(my_data_extract(4))
Mg_axial.append(my_data_extract(1))
Mg_corner.append(my_data_extract(2))
P_free.append(my_data_extract(5))
#%% print maximum value for each scan
def maxcount(xrd_data):
    for n in range(len(xrd_data)):
        print(Data_lable[n], np.max(Al_axial[n]))

print('Al-corner')      
maxcount(Al_corner)

print('Al-axial')      
maxcount(Al_axial)

print('Mg-axial')      
maxcount(Mg_axial)

print('Mg-corner')      
maxcount(Mg_corner)

print('PO4-Free')      
maxcount(P_free)

print('Centroid')      
maxcount(Centroid)

#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 16000 #used to shift graphs up or down
lnthikness= 1
xlimits = [ 5, 65]
ylimits = [-500, 6.2e4]
legspot = 'upper right' # Determines where legend is placed

font = FontProperties()
font.set_family('sans-serf')
font.set_name('Arial')
font.set_size(9)

ColorB = ['#777eb6', '#5560a2', '#313f8b', '#0e0e77'] # Blue
ColorG = ['#77b684','#58a265', '#388e46','#0e7723' ] # Green
ColorO = [ '#c76f0a', '#a15d11', '#7a4a12','#53330e'] # Orange/ brown
ColorK = [ '#8a8a8a','#626161', '#343433', '#000000'] # Gray
ColorPalet_1 = ["#4db758","#145092","#000000"]

#%% Ploting Function

def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name, plt_title, off_set):
    num_of_scans = range(len(np.array(xrd_data)))
    fig, ax = plt.subplots() 
    fig.set_figwidth(3.24) #size is in inches
    fig.set_figheight(2.5) #size is in inches
    # fig.tight_layout(pad=0.0)
    for n in num_of_scans:
        ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])

    # ax.set_xlabel("2θ (degrees)", fontsize=9)
    # ax.set_ylabel("Intensity", fontsize=9)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(xlimits)
    # ax.set_ylim(ylimits)
    ax.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax.yaxis.set_ticklabels([])
    ax.tick_params(axis='y',length=0)
    # ax.axes.xaxis.set_ticklabels([])
    ax.spines[['right', 'top']].set_visible(False)
    plt.title(plt_title, loc='right', fontsize=10)
    
    #Revers order of legend lables
    handles, labels = ax.get_legend_handles_labels()
    # ax.legend(handles[::-1], labels[::-1])

    svg_name_path = 'Plots/1_to_740days/XRD_Paper/' + svg_file_name + '.svg'
    # Uncomment next line to save the figure.
    # fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

# #%% Al-axial plot

# # order of inputs for xrd_quad_plot
# # xrd_data, plot_names, ColorPalet, svg_file_name, plt_title
# xrd_quad_plot(Al_axial, Data_lable , ColorB,\
#               'Al_axial_1to470day_forpaper2','Moderate-Aluminum', off_set)

# #%% Al-corner plot

# xrd_quad_plot(Al_corner , Data_lable , ColorB,\
#               'Al_corner_1to470day_forpaper2', 'High-Aluminum', 13500)

# #%% Mg-Axial

# xrd_quad_plot(Mg_axial , Data_lable , ColorG, 'Mg_Axial_1to470day_forpaper2',\
#               'Moderate-Magnesium', off_set)

# #%% Mg-Corner plot

# xrd_quad_plot(Mg_corner , Data_lable , ColorG, 'Mg_corner_1to470day_forpape2r',\
#               'High-Magnesium', off_set)

# #%% PO4-Free plot

# xrd_quad_plot(P_free , Data_lable , ColorO, 'PO4_free_1and28_day_forpaper2',\
#               'No-Phosphate', 7000)

# #%% Centroid plot

# xrd_quad_plot(Centroid , Data_lable , ColorK, 'Centroid_1to_510day_forpaper2',\
#               'High-Phosphate', 7000)

#%% multy plot function

# You need to have already defined a fig ans axis for this function to work
def plot_loop(ax, xrd_data, plot_names, ColorPalet, off_set):
    num_of_scans = range(len(np.array(xrd_data)))    
    for n in num_of_scans:
     ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
     linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n])
     
     # ax.set_xlabel("2θ (degrees)", fontsize=9)
     # ax.set_ylabel("Intensity", fontsize=9)
     ax.tick_params(axis='x', labelsize=12)
     ax.tick_params(axis='y', labelsize=12)
     ax.set_xlim(xlimits)
     ax.set_ylim(ylimits)
     ax.xaxis.set_minor_locator(MultipleLocator(2.5))
     ax.yaxis.set_ticklabels([])
     ax.tick_params(axis='y',length=0)
     # ax.axes.xaxis.set_ticklabels([])
     ax.spines[['right', 'top']].set_visible(False)
     
     #Revers order of legend lables
     # handles, labels = ax.get_legend_handles_labels()
     # ax.legend(handles[::-1], labels[::-1])
     
def subplot_title(ax, text, set_color):
    ax.set_title(text, loc='right', fontsize=9, fontstyle='normal', color=set_color)

    
#%% Grid of plots

fig = plt.figure(figsize=(8.5, 10)) # , layout="constrained", , layout="constrained"
spec = fig.add_gridspec(ncols=2, nrows=3)
plt.subplots_adjust(hspace=0.2, wspace=0.05)

ax0 = fig.add_subplot(spec[0, 0])
plot_loop(ax0, Al_axial, Data_lable , ColorB, off_set)
subplot_title(ax0,'Moderate-Aluminum',ColorB[3])
ax0.axes.xaxis.set_ticklabels([])

ax1 = fig.add_subplot(spec[0, 1])
n=0
H_Al_off = off_set #1400
n1 = .6
n2 = .55
ax1.plot(Al_corner[n][0,:], Al_corner[n][1,:] + n*H_Al_off, 
         linewidth=lnthikness, color=ColorB[n], label=Data_lable)
n=1
ax1.plot(Al_corner[n][0,:], Al_corner[n][1,:] + ((n - 1) + n1)*H_Al_off, 
         linewidth=lnthikness, color=ColorB[n], label=Data_lable)
n=2
ax1.plot(Al_corner[n][0,:], Al_corner[n][1,:] + ((n - 1) + n2)*H_Al_off, 
         linewidth=lnthikness, color=ColorB[n], label=Data_lable)
n=3
ax1.plot(Al_corner[n][0,:], Al_corner[n][1,:] + ((n - 1) + n1)*H_Al_off, 
         linewidth=lnthikness, color=ColorB[n], label=Data_lable)


# ax.set_xlabel("2θ (degrees)", fontsize=9)
# ax.set_ylabel("Intensity", fontsize=9)
ax1.tick_params(axis='x', labelsize=10)
ax1.tick_params(axis='y', labelsize=10)
ax1.set_xlim(xlimits)
ax1.set_ylim(ylimits)
ax1.xaxis.set_minor_locator(MultipleLocator(2.5))
ax1.yaxis.set_ticklabels([])
ax1.tick_params(axis='y',length=0)
# ax.axes.xaxis.set_ticklabels([])
ax1.spines[['right', 'top']].set_visible(False)
subplot_title(ax1,'High-Aluminum', ColorB[3])
ax1.axes.xaxis.set_ticklabels([])

ax2 = fig.add_subplot(spec[1, 0])
plot_loop(ax2, Mg_axial, Data_lable , ColorG, off_set)
subplot_title(ax2,'Moderate-Magnesium',ColorG[3])
ax2.axes.xaxis.set_ticklabels([])
ax2.set_ylabel("Intensity", fontsize=14)

ax3 = fig.add_subplot(spec[1, 1])
plot_loop(ax3, Mg_corner, Data_lable , ColorG, off_set) #11000
subplot_title(ax3,'High-Magnesium',ColorG[3])
ax3.axes.xaxis.set_ticklabels([])

ax4 = fig.add_subplot(spec[2, 0])
plot_loop(ax4, P_free, Data_lable , ColorO, off_set) #7000
subplot_title(ax4,'No-Phosphate',ColorO[3])

ax5 = fig.add_subplot(spec[2, 1])
plot_loop(ax5, Centroid, Data_lable , ColorK, off_set) #7000
subplot_title(ax5,'High-Phosphate',ColorK[3])


# This section added a big frame around the set of plots so you can make lables for shared axis
fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)
plt.xlabel("2θ (degrees)", fontsize=14)
# plt.ylabel("Intensity")

fig.savefig("Plots/1_to_740days/XRD_Paper/time_series_V5.svg", transparent=False, bbox_inches="tight")

# plt.close('all')

#%%

# fig, axes = plt.subplots(4, 2, sharex=True, sharey=True, figsize=(6,15))
# # add a big axis, hide frame
# fig.add_subplot(111, frameon=False)
# # hide tick and tick label of the big axis
# plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)
# plt.xlabel("common X")
# plt.ylabel("common Y")


