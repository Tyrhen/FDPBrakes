#Tools for Data Science/Data Analysis
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from pandas.plotting import table

#function to only pull in every 7th row of data (too many data points currently)
def logic(index):
    if index % 7 == 0:
        return False
    return True

#import data
SAE_path = "/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Test_Data_Filtered.csv"
SAE_data = pd.read_csv(SAE_path, skiprows= lambda x: logic(x) )

#Break data into the test sections 
Section_1 = SAE_data[(SAE_data['Next Test Section'] == 1)]
Section_2 = SAE_data[SAE_data['Next Test Section'] == 2]
Section_3 = SAE_data[SAE_data['Next Test Section'] == 3]


"""
#def OutputDescribeTable():
    desc = SAE_data.describe()
    #create a subplot without frame
    plot = plt.subplot(111, frame_on=False)
    #remove axis
    plot.xaxis.set_visible(False) 
    plot.yaxis.set_visible(False) 
    #create the table plot and position it in the upper left corner
    table(plot, desc,loc='upper right')
    #save the plot as a png file
    plt.savefig('desc_plot.png')

    #set the style of the graphs 
    sns.set_style("darkgrid")

"""

corr = Section_2.corr()
x= sns.heatmap(corr)
y = sns.lineplot(x = 'Mu' , y = 'Temp 3 Inboard (F)', data = Section_1)
plt.show()

"""
plt.figure(figsize=(3,3), dpi =100, facecolor= 'blue')
xr = sns.regplot(x = SAE_data['Initial Disc Brake Temperature (C)'], y = SAE_data['Final Speed (mph)'])
graph = plt.savefig("graph1.png")
graph1 = "/Users/Ty/Desktop/FDP_brakes_proj_local/graph1.png"
"""