#Tools for Data Science/Data Analysis
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

SAE_path = "Test Protocols w Tire Calculator.xlsx"
SAE_data = pd.read_excel(SAE_path, sheet_name=4, index_col='Test Section')
SAE_data.drop(["Description"], axis = 1, inplace = True) 
xr = sns.lineplot(x = SAE_data['Initial Disc Brake Temperature (C)'], y = SAE_data['Final Speed (mph)'])