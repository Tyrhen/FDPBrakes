#Tools for Data Science/Data Analysis

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


#function to only pull in every 7th row of data (too many data points currently)
def logic(index):
    if index % 7 == 0:
        return False
    return True

#import data
SAE_path = "/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Datasets/Test_Data_Filter.csv"
SAE_data = pd.read_csv(SAE_path, skiprows= lambda x: logic(x) )


#Break data into the test sections 
Section_1 = SAE_data[(SAE_data['Next Test Section'] == 1)]
Section_2 = SAE_data[SAE_data['Next Test Section'] == 2]
Section_3 = SAE_data[SAE_data['Next Test Section'] == 3]




"""Below are all the functions that produce graphs"""
#general styling for plots
sns.set_style("whitegrid")
def FIG1():
    sns.set_style("whitegrid")
    for item in SAE_data["Next Test Section"]:
        str(item)
    fig1 = sns.FacetGrid(SAE_data, col = "Next Test Section")
    fig1 = fig1.map(plt.scatter, "Mu", "Hydraulic Pressure", edgecolor = "w",)
    return fig1.savefig("/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig1.svg")

def FIG2():
    sns.set_style("darkgrid")
    for item in SAE_data["Next Test Section"]:
        str(item)
    for item in SAE_data["Cycle_Count_Value"]:
        float(item)

    fig2 = sns.FacetGrid(SAE_data, col = "Next Test Section")
    fig2 = fig2.map(plt.scatter, "Mu", "Temp 3 Inboard (F)", edgecolor = "w",)
    
    return fig2.savefig("/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig2.svg")

def FIG5():
    sns.set_style("white")
    for item in SAE_data["Next Test Section"]:
        str(item)
    for item in SAE_data["Cycle_Count_Value"]:
        float(item)
    fig5 = sns.FacetGrid(SAE_data, col = "Next Test Section")
    fig5 = fig5.map(plt.bar, "Cycle_Count_Value", "Mu", color = 'red', ecolor = 'black')
    return fig5.savefig("/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig5.svg")

def FIG4():
    sns.set_style("darkgrid")
    for item in SAE_data["Next Test Section"]:
        str(item)
    for item in SAE_data["Cycle_Count_Value"]:
        float(item)
    fig4 = sns.relplot(x="Mu", y="Temp 4 Outboard (F)", col="Next Test Section",  kind="scatter", data=SAE_data)
    return fig4.savefig("/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig4.svg")

def FIG7():
    fig7 = sns.lmplot(x="Mu", y="Temp 4 Outboard (F)", col="Next Test Section", hue="Next Test Section", data =SAE_data, fit_reg = True, col_wrap = 3, height = 3)
    return fig7.savefig("/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig7.svg")

def FIG3():
    s2 = Section_2.drop('Next Test Section',axis =1)
    corr = s2.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
     fig3, heat = plt.subplots(figsize=(7, 5))
     heat = sns.heatmap(corr, mask=mask, vmax=.3, square=True)
    
    fig3 = heat.get_figure()
    fig3.tight_layout()
    return fig3.savefig("/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig3.svg")


"""function calls to produce graphs"""
plt.clf()
FIG3()
plt.clf()
FIG1()
plt.clf()
FIG2()
plt.clf()
FIG5()
plt.clf()
FIG4()
plt.clf()
FIG7()



"""paths for figures"""
fig1 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig1.svg"
fig2 =  "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig2.svg"
fig3 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig3.svg"
fig4 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig4.svg"
fig5 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig5.svg"
fig6 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig6.svg"
fig7 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/fig7.svg"

"""EXCEL to HTML"""
#wb = pd.read_excel('D:\eclipse\test.xlsx') # This reads in your excel doc as a pandas DataFrame

#wb.to_html('C:\test.html') # Export the DataFrame (Excel doc) to an html file 


