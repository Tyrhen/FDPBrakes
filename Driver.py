from jinja2 import Environment, FileSystemLoader
import weasyprint
file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)



import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

SAE_path = "Test Protocols w Tire Calculator.xlsx"
SAE_data = pd.read_excel(SAE_path, sheet_name=4, index_col='Test Section')
SAE_data.drop(["Description"], axis = 1, inplace = True) 
xr = sns.lineplot(x = SAE_data['Initial Disc Brake Temperature (C)'], y = SAE_data['Final Speed (mph)'])


template = env.get_template('base.html')
template_vars = {"graph1": xr, "name": "FDP Brake"}
html_out = template.render(template_vars)
