#Tools for Data Science/Data Analysis
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

#function to only pull in every 7th row of information
def logic(index):
    if index % 7 == 0:
        return False
    return True

SAE_path = "/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/07-15-2020 0.csv"
SAE_data = pd.read_csv(SAE_path, skiprows= lambda x: logic(x) )

#To have just rows of the actual braking process
SAE_data = SAE_data[SAE_data['Mu'] != '#DIV/0!']
Section_1 = SAE_data[(SAE_data['Next Test Section'] == 1) & SAE_data['Mu'] > 0]
Section_2 = SAE_data[SAE_data['Next Test Section'] == 2]
Section_3 = SAE_data[SAE_data['Next Test Section'] == 3]
#to drop all categorical data and get rid of Air pressure
#SAE_data.drop(["Air Pressure (PSI)","Load Cell Value (lbs)","Step_Value","Next Test Section"], axis =1, inplace = True)



#set the style of the graphs 
sns.set_style("darkgrid")

#Plots
corr = Section_1.corr()
x= sns.heatmap(corr)
y = sns.lineplot(x = 'Mu' , y = 'Temp 3 Inboard (F)', data = Section_1)
plt.xticks(np.arange(0,1))
#print(SAE_data.head())
plt.show(y)

"""
plt.figure(figsize=(3,3), dpi =100, facecolor= 'blue')
xr = sns.regplot(x = SAE_data['Initial Disc Brake Temperature (C)'], y = SAE_data['Final Speed (mph)'])
graph = plt.savefig("graph1.png")
graph1 = "/Users/Ty/Desktop/FDP_brakes_proj_local/graph1.png"
"""