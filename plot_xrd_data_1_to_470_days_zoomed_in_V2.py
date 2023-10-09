# This imports xrd data from multiple files and organizes data to plot
# one graph with diferent age samples
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties

#%% Make list to hold XRD data for each PC composition

Al_axial = []
Al_corner = []
Centroid = []
Mg_axial = []
Mg_corner = []
P_free = []


Data_lable = ['1 day', '28 days', '470 days']

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

# # This function takes the string that is the XRD file name and returns the
# # the section of the string that has the NaOH molarty data and formats it.
# def concentration_lable(name_index):
#     molar_tag = f_name[name_index].find('M_',25)
#     molar_value=(f_name[name_index][molar_tag-4:molar_tag-2]) + '.'\
#         + (f_name[name_index][molar_tag-2:molar_tag]) + ' M'
#     #removes leading zero from molarity value
#     if molar_value[0]=='0': molar_value = molar_value.replace('0', '',1)
#     return molar_value

# Use "f_name" to know what file is in what
# position. The index of "f_name" matches the index of "dataframe_of_frames"

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

#%% Settings for batch of graphs
#Values for setting that are used multple places
off_set = 0 #used to shift graphs up or down
# lnthikness= 1.5
xlimits = [ 10, 13]
ylimits = [600, 1.5e4]
legspot = 'upper right' # Determines where legend is placed

# font = FontProperties()
# font.set_family('sans-serf')
# font.set_name('Arial')
# font.set_size(9)

#%% Ploting Function

# Working on ploting in a grid
#Use this file to set style
plt.style.use('Input/publish2.mplstyle')

ColorPalet_1 = ["#ffb14e","#008e00","#000000"]
lnstyle = ['dotted', 'dashed', 'solid']

def plot_loop(ax,xrd_data, plot_names, ColorPalet, plt_title):
    num_of_scans = reversed( range(len(np.array(xrd_data))))

    for n in num_of_scans:
        ax.plot(xrd_data[n][0,:], xrd_data[n][1,:],
                color=ColorPalet[n], label=plot_names[n]) #linestyle=lnstyle[n], 

    ax.set_xlim(xlimits)
    # ax.set_ylim(ylimits)
    ax.xaxis.set_minor_locator(MultipleLocator(.5))
    ax.yaxis.set_ticklabels([])
    ax.tick_params(axis='y',length=0)
    # ax.spines[['right', 'top']].set_visible(False)
    # plt.title(plt_title,fontsize = 14)

    
    #Revers order of legend lables
    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(handles[::-1], labels[::-1])

    # svg_name_path = 'Plots/1_to_740days/XRD_Paper/zoomed_on_003/' + svg_file_name + '.svg'
    # Uncomment next line to save the figure.
    # fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig


#%% Plot on a grid

fig = plt.figure(figsize=(3.5, 4.1)) #, layout="constrained" 8.5, 10
spec = fig.add_gridspec(ncols=3, nrows=3)
plt.subplots_adjust(hspace=0.2, wspace=0.05)
y1a = 1.5e3
y1b = 14.5e3
y1 = [y1a, y1b]

y2r = (y1b - y1a) * 0.9104  / 3.0955   #4.3 / 14.6
y3r = (y1b - y1a) * 2.003 / 3.0955 
y2 = [y1a, y1a + y2r]
y3 = [y1a, y1a + y3r]
# H-Al
ax0 = fig.add_subplot(spec[:, 1])
# xrd_data, plot_names, ColorPalet, svg_file_name, plt_title
plot_loop(ax0, Mg_corner , Data_lable , ColorPalet_1,\
          'High-magnesium')
ax0.set_ylim(y1)
   
# H-Al
ax1 = fig.add_subplot(spec[1:, 2])
plot_loop(ax1, Al_corner , Data_lable , ColorPalet_1,\
          'High-aluminum')
ax1.set_ylim(y3)

ax2 = fig.add_subplot(spec[0, 0])
plot_loop(ax2, Al_axial, Data_lable , ColorPalet_1,\
              'Moderate-aluminum')
ax2.axes.xaxis.set_ticklabels([])
ax2.set_ylim(y2)

ax3 = fig.add_subplot(spec[1, 0])
plot_loop(ax3, Mg_axial , Data_lable , ColorPalet_1,\
              'Moderate-magnesium')
ax3.axes.xaxis.set_ticklabels([])
ax3.set_ylim(y2)
ax3.set_ylabel("Intensity", fontsize=14)  

ax4 = fig.add_subplot(spec[2, 0])
plot_loop(ax4, P_free , Data_lable , ColorPalet_1,\
              'No-phosphate')
ax4.set_ylim(y2)

# This section added a big frame around the set of plots so you can make lables for shared axis
fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)
plt.xlabel("2θ (degrees)", fontsize=14)
# plt.ylabel("Intensity")

fig.savefig("Plots/1_to_740days/XRD_Paper/zoomed_on_003/003grid3.svg", transparent=False, bbox_inches="tight")

#%%   
fig = plt.figure()
ax = fig.add_subplot()
plot_loop(ax, Mg_corner , Data_lable , ColorPalet_1,\
          'High-magnesium')
ax.legend(handlelength=1)

fig.savefig("Plots/1_to_740days/XRD_Paper/zoomed_on_003/get_legend.svg", transparent=False, bbox_inches="tight")



