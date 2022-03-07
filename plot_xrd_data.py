import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%% Import data
#This section will read only the diffraction data of the  csv  files in the folder
# at the path "datapath" into a data frame.
datpath = '../Cement/Scans/Files_organized_for_plots/Constant_NaOH_1mL10M_to_1gPC' # directory where data is stored relative to py script location
f_name = (os.listdir(datpath))
dataframe_of_frames = []

for x in f_name:
    temp_df=pd.read_csv(os.path.join(datpath, f_name[0]),skiprows=(range(0, 25)))
    dataframe_of_frames.append(temp_df)
    # print(os.path.join(datpath, x))
header=['Angle',' TimePerStep',' Intensity',' ESD'],
#%% Name imported data
#Use this section to give your data a useful name manually

#fram_index is the index of the postion of the frame you whant
#inside the "dataframe_of_frames"
def my_data_extract(fram_index): 
    tempArray = dataframe_of_frames[fram_index]
    a = np.array(tempArray.loc[:,'Angle'])
    b = np.array(tempArray.loc[:,' Intensity'])
    tempMatrix = np.vstack((a,b))
    return  tempMatrix
#takes extracts the angle and intesity data from one xrd file into a array
Alax = my_data_extract(0)
Alco = my_data_extract(1)
Cent = my_data_extract(2)
Mgax = my_data_extract(3)
Mgco = my_data_extract(4)
Pax = my_data_extract(5)
Pco = my_data_extract(6)
Siax = my_data_extract(7)
Sico = my_data_extract(8)
#%% Ploting XRD data
#fig, ax = plt.subplot()
# lnWidth = 0.5
# plt.plot( Cent[0,:], Cent[1,:], linewidth = lnWidth )
# plt.xlabel("two theta")
# plt.ylabel("Intensity (counts)")

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(Cent[0,:], Cent[1,:])
ax.set_xlabel("two theta")
ax.setyxlabel("Intensity (counts)")