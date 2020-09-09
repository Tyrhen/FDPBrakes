import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from pandas.plotting import table


data_path = "/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Datasets/FDP X 19 DATA.xlsx"
df1 = pd.read_excel(data_path, sheet_name="Three Sections")
df1 = df1[df1["Final Temp"] > 0] 
df2 = pd.read_excel(data_path, sheet_name="Three Sections #2")

y = df1.groupby(['Test Section']).mean()

sns.barplot(x = 'Test Section', y = 'Friction Level', data = y.reset_index())
plt.show()
