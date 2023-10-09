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
lnthikness= 1.5
xlimits = [ 8.5, 13]
ylimits = [600, 0.50e4]
legspot = 'upper right' # Determines where legend is placed

# font = FontProperties()
# font.set_family('sans-serf')
# font.set_name('Arial')
# font.set_size(9)

#%% Ploting Function

ColorPalet_1 = ["#ffb14e","#008e00","#000000"]
lnstyle = ['dotted', 'dashed', 'solid']
def xrd_quad_plot(xrd_data, plot_names, ColorPalet, svg_file_name, plt_title, off_set):
    num_of_scans = range(len(np.array(xrd_data)))
    plt.style.use('Input/publish.mplstyle')
    fig, ax = plt.subplots(figsize=(1.75, 3.5)) #size is in inches 
    plt.axvline(11.65, color='gray')
    for n in num_of_scans:
        ax.plot(xrd_data[n][0,:], xrd_data[n][1,:] + n*off_set, 
        linewidth=lnthikness, color=ColorPalet[n], label=plot_names[n]) #linestyle=lnstyle[n],

    ax.set_xlabel("2θ") #, fontsize=9)
    ax.set_ylabel("Intensity") #, fontsize=9)
    # ax.tick_params(axis='x', labelsize=8)
    # ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(xlimits)
    ax.set_ylim(ylimits)
    ax.xaxis.set_minor_locator(MultipleLocator(.5))
    ax.yaxis.set_ticklabels([])
    ax.tick_params(axis='y',length=0)
    ax.spines[['right', 'top']].set_visible(False)
    plt.title(plt_title,fontsize = 14)
    
    
    #Revers order of legend lables
    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(handles[::-1], labels[::-1])

    svg_name_path = 'Plots/1_to_740days/XRD_Paper/zoomed_on_003/' + svg_file_name + '.svg'
    # Uncomment next line to save the figure.
    fig.savefig(svg_name_path, transparent=False, bbox_inches="tight")
    return fig

#%% Al-axial plot

# order of inputs for xrd_quad_plot
# xrd_data, plot_names, ColorPalet, svg_file_name, plt_title
xrd_quad_plot(Al_axial, Data_lable , ColorPalet_1,\
              'M-Al_2','Moderate-aluminum', off_set)
# Uncomment this line to save the figure.
# fig.savefig('Plots/ledgend.svg', transparent=False, bbox_inches="tight")

#%% Al-corner plot

xrd_quad_plot(Al_corner , Data_lable , ColorPalet_1,\
              'H-Al_2', 'High-aluminum', off_set)
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")


#%% Mg-Axial

xrd_quad_plot(Mg_axial , Data_lable , ColorPalet_1, 'M-Mg_3',\
              'Moderate-magnesium', off_set)
plt.axvline(11.65, color='gray')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Mg-corner

xrd_quad_plot(Mg_corner , Data_lable , ColorPalet_1, 'H-Mg_2',\
              'High-magnesium', off_set)
plt.axvline(11.65, color='gray')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% Centroid plot

xrd_quad_plot(Centroid , Data_lable , ColorPalet_1, 'H-P_2',\
              'High-phosphate', off_set)
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")

#%% PO4-Free plot

xrd_quad_plot(P_free , Data_lable , ColorPalet_1, 'N-P_3',\
              'No-phosphate', off_set)
# plt.axvline(11.65, color='gray')
# Uncomment this line to save the figure.
# fig.savefig('Plots/AL_halfmL_to_1g.svg', transparent=False, bbox_inches="tight")



