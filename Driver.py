from jinja2 import Environment, FileSystemLoader
file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)
template = env.get_template('test.html')
output = template.render(title = 'tyrhen')


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#twelve_path = "/Users/Ty/Desktop/FDP Brakes/fatal_police_shootings_data.csv"
#twelve_data = pd.read_csv(twelve_path, index_col = 'id')
#print(list(twelve_data.columns))
#x = sns.barplot(x = twelve_data['age'], y = twelve_data['race'])
#plt.show(x)