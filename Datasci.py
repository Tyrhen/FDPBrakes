#Tools for Data Science/Data Analysis
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

SAE_path = "/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Test Protocols w Tire Calculator.xlsx"
SAE_data = pd.read_excel(SAE_path, sheet_name=4, index_col='Test Section')
SAE_data.drop(["Description"], axis = 1, inplace = True) 
plt.figure(figsize=(3,3), dpi =100, facecolor= 'blue')
xr = sns.regplot(x = SAE_data['Initial Disc Brake Temperature (C)'], y = SAE_data['Final Speed (mph)'])
graph = plt.savefig("graph1.png")
graph1 = "/Users/Ty/Desktop/FDP_brakes_proj_local/graph1.png"