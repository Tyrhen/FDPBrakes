#Tools for Data Science/Data Analysis
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from pandas.plotting import table
import matplotlib.ticker as mticker


#function to only pull in every 7th row of data (too many data points currently)
def logic(index):
    if index % 7 == 0:
        return False
    return True

#import data
SAE_path = "/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Test_Data_Filter.csv"
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
    
"""


"""
def Multiplot():
    fig1, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(13,4.5))
    sns.swarmplot(x="Dyno Speed (RPM)", y = 'Temp 3 Inboard (F)', data = Section_1 , ax = ax2)
    ax2.set_xticklabels([])

    sns.regplot(x = 'Mu' , y = 'Temp 3 Inboard (F)', data = Section_1, x_bins = 4, ax =ax1)
    ax2.set_ylabel("")
    ax2.set_yticklabels([])
    ax2.set_xticklabels([])


    sns.lineplot(x = "Temp 4 Outboard (F)", y = 'Temp 3 Inboard (F)', data = Section_1,  ax =ax3 )
    ax3.set_ylabel("")
    ax3.set_yticklabels([])
    return fig1.savefig("fig1.svg")
"""
sns.set_style("whitegrid")
def facetplot1():
    for item in SAE_data["Next Test Section"]:
        str(item)
    fig1 = sns.FacetGrid(SAE_data, col = "Next Test Section")
    fig1 = fig1.map(plt.scatter, "Mu", "Hydraulic Pressure", edgecolor = "w",)
    return fig1.savefig("fig1.svg")

def facetplot2():
    for item in SAE_data["Next Test Section"]:
        str(item)
    for item in SAE_data["Cycle_Count_Value"]:
        float(item)

    fig2 = sns.FacetGrid(SAE_data, col = "Next Test Section")
    fig2 = fig2.map(plt.scatter, "Mu", "Temp 3 Inboard (F)", edgecolor = "w",)
    return fig2.savefig("fig2.svg")

def facetplot3():
    for item in SAE_data["Next Test Section"]:
        str(item)
    for item in SAE_data["Cycle_Count_Value"]:
        float(item)
    fig5 = sns.FacetGrid(SAE_data, col = "Next Test Section")
    fig5 = fig5.map(plt.bar, "Cycle_Count_Value", "Mu",)
    return fig5.savefig("fig5.svg")

def relplot():
    for item in SAE_data["Next Test Section"]:
        str(item)
    for item in SAE_data["Cycle_Count_Value"]:
        float(item)
    fig4 = sns.relplot(x="Mu", y="Temp 4 Outboard (F)", col="Next Test Section", 
    hue="Cycle_Count_Value", kind="scatter", data=SAE_data)
    return fig4.savefig("fig4.svg")

def heatmap():
    s2 = Section_2.drop('Next Test Section',axis =1)
    corr = s2.corr()
    heat = sns.heatmap(corr)
    fig3 = heat.get_figure()
    fig3.tight_layout()
    return fig3.savefig("fig3.svg")
    
heatmap()
facetplot1()
facetplot2()
facetplot3()
relplot()


#paths
fig1 = "/Users/Ty/Desktop/FDP_brakes_proj_local/fig1.svg"
fig2 =  "/Users/Ty/Desktop/FDP_brakes_proj_local/fig2.svg"
fig3 = "/Users/Ty/Desktop/FDP_brakes_proj_local/fig3.svg"
fig4 = "/Users/Ty/Desktop/FDP_brakes_proj_local/fig4.svg"
fig5 = "/Users/Ty/Desktop/FDP_brakes_proj_local/fig5.svg"



