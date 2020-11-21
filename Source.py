import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import matplotlib
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import Datasci

def givedata():
	Make = simpledialog.askstring("Input", "What is the Make of the Test Vehicle", parent=root)
	if Make is not None:
		print(Make)
	Model = simpledialog.askstring("Input", "What is the Model of the Test Vehicle", parent=root)
	if Model is not None:
		print(Model)	
	Year = simpledialog.askinteger("Input", "What is year of the model?", parent=root, minvalue=0, maxvalue=2025)
	if Year is not None:
		print(Year)
	Dateformat = simpledialog.askstring("Input", "What is the date? (format: xx/xx/xx)", parent=root)
	if Dateformat is not None:
		print(Dateformat)
	Submodel = simpledialog.askstring("Input", "What is the submodel of the vehicle?", parent=root,)
	if Submodel is not None:
		print(Submodel)
	tire_size = simpledialog.askstring("Input", "What is the tire size? (Front/Rear) [cm]", parent=root,)
	if tire_size is not None:
		print(tire_size)
	rolling_radius = simpledialog.askstring("Input", "What is the rolling radius size? (Front/Rear) [cm]", parent=root,)
	if rolling_radius is not None:
		print(rolling_radius)
	vehicle_weight = simpledialog.askinteger("Input", "What is gross vehicle weight of the vehicle? [kgf],[N]", parent=root, minvalue=0, maxvalue = 10000)
	if vehicle_weight is not None:
		print(vehicle_weight)
	cg_height = simpledialog.askinteger("Input", "What is the height of the center of gravity? [m]", parent=root, minvalue=0, maxvalue=2025)
	if cg_height is not None:
		print(cg_height)
	wheelbase = simpledialog.askinteger("Input", "What is length  of the wheelbase? [m]", parent=root, minvalue=0, maxvalue=2025)
	if wheelbase is not None:
		print(wheelbase)
	brake_brand = simpledialog.askstring("Input", "What is the name/brand of the brake?", parent=root,)
	if brake_brand is not None:
		print(brake_brand)
	brake_size = simpledialog.askstring("Input", "What is the brake size? (eff.radius/outside diam./thickness)[mm]", parent=root,)
	if brake_size is not None:
		print(brake_size)
	caliper_size = simpledialog.askstring("Input", "What is the caliper size? (piston diameter/number of pistons)[mm]", parent=root,)
	if caliper_size is not None:
		print(caliper_size)
	length_pad = simpledialog.askinteger("Input", "What is the length of the Lining (pad) in the sliding direction? [mm]", parent=root, minvalue = 0 , maxvalue = 500)
	if length_pad is not None:
		print(length_pad)
	width_pad = simpledialog.askinteger("Input", "What is the width of the Lining (pad) in the perpendicular direction? [mm]", parent=root, minvalue = 0 , maxvalue = 500)
	if width_pad is not None:
		print(width_pad)
	thickness_pad = simpledialog.askinteger("Input", "What is the thickness of the Lining (pad)? [mm]", parent=root, minvalue = 0 , maxvalue = 500)
	if thickness_pad is not None:
		print(thickness_pad)
	area_pad = simpledialog.askinteger("Input", "What is the area of the Lining (pad)? [mm^2]", parent=root, minvalue = 0 , maxvalue = 5000)
	if area_pad is not None:
		print(area_pad)
	wheel_drive = simpledialog.askstring("Input", "What kind of drive system does the vehicle have? (FX2/RX2,AWD,4WD)", parent=root,)
	if wheel_drive is not None:
		print(wheel_drive)
	inertia = simpledialog.askinteger("Input", "What is the calculated Inertia? [kgm^2]", parent=root, minvalue = 0 , maxvalue = 5000)
	if inertia is not None:
		print(inertia)
	shaft_speed = simpledialog.askinteger("Input", "What is the shaft speed at 50 km/h? [km/h]", parent=root, minvalue = 0 , maxvalue = 5000)
	if shaft_speed is not None:
		print(shaft_speed)
	braking_torque = simpledialog.askinteger("Input", "What is the braking torque at 0.3g? [N*m]", parent=root, minvalue = 0 , maxvalue = 5000)
	if braking_torque is not None:
		print(braking_torque)
	friction_material = simpledialog.askstring("Input", "What is the friction material on the pad?", parent=root,)
	if friction_material is not None:
		print(friction_material)
	return [Make, Model, Dateformat, Year, Submodel, vehicle_weight, cg_height, wheelbase, rolling_radius, tire_size, brake_brand, brake_size, 
	thickness_pad, caliper_size, length_pad, width_pad, wheel_drive, inertia, shaft_speed, braking_torque, friction_material, area_pad]
def PDFconverter():
    from jinja2 import Environment, FileSystemLoader
    from weasyprint import HTML, CSS
    file_loader = FileSystemLoader('.')
    env = Environment(loader = file_loader)
    template = env.get_template('FDPBrakes/base.html')
    [Make, Model, Dateformat, Year, Submodel, vehicle_weight, cg_height, wheelbase, rolling_radius, tire_size, brake_brand, brake_size, 
	thickness_pad, caliper_size, length_pad, width_pad, wheel_drive, inertia, shaft_speed, braking_torque, friction_material, area_pad] = givedata()
    [figure1,figure2,figure3,figure4, figure5, figure6,figure7, figure8] = DataSci2()
    template_vars = {
            "Report_Standard":Make,
            "Make_And_Model": Model,
            "Dateformat": Dateformat,
            'Year': Year,
	    'Submodel': Submodel, 
	    'vehicle_weight':vehicle_weight,
	    'cg_height': cg_height,
	    'wheelbase': wheelbase,
	    'rolling_radius': rolling_radius,
            'tire_size': tire_size,
	    'brake_brand': brake_brand,
			'brake_size': brake_size,
			'thickness_pad':thickness_pad,
			'caliper_size': caliper_size,
			'length_pad': length_pad,
			'width_pad': width_pad,
			'wheel_drive': wheel_drive,
			'shaft_speed': shaft_speed,
			'braking_torque': braking_torque,
			'friction_material': friction_material,
			'area_pad': area_pad,
			'inertia': inertia,
			"fig2_1": figure1,
            "fig2_2": figure2,
            "fig2_3": figure3,
            "fig2_4": figure4,
            "fig2_5": figure5,
            "fig2_6": figure6,
            "fig2_7": figure7,
            "fig2_8": figure8,
            "fig_1": Datasci.fig1,
            "fig_2": Datasci.fig2,
            "fig_3": Datasci.fig3,
            "fig_4": Datasci.fig4,
            "fig_5": Datasci.fig5,
            "fig_7": Datasci.fig7,
           }
    html_out = template.render(template_vars)
    HTML(string = html_out, base_url='.').write_pdf('mockreport.pdf', stylesheets=["/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Static/basic.css"])
def getdata():
	file_path = filedialog.askopenfilename(title = 'Select File',filetypes=[("Excel files", ".xlsx .xls")])
	return file_path	
def DataSci2():
	data_path = getdata()
	df1 = pd.read_excel(data_path, sheet_name="Three Sections")
	df1 = df1[df1["Final Temp"] > 0] 
	df2 = pd.read_excel(data_path, sheet_name="Three Sections #2")
<<<<<<< HEAD:interface.py

	
=======
>>>>>>> 50eb1f4144bd67bc41a4ad320710a8f46b79907c:Source.py
	sns.set_palette("bright")
	def figure1():
		figure1 = sns.lineplot(x= 'Stop Number', y = 'Friction Level', data=df1, hue = "Test Section",)
	def figure2():
		figure2 = sns.lineplot(x="Stop Number", y="Friction Level", hue="Test Section", palette= "bright",  data= df2)
	def figure3():
		figure3 = sns.relplot(x="Friction Level", y="Final Temp", col="Test Section", palette= "bright", kind="line", data= df1)
	def figure4():
		figure4 = sns.relplot(x="Friction Level", y="Final Temp", col="Test Section", palette= "bright", kind="scatter", data= df2)
	def figure5():
		figure5 = sns.catplot(x="Test Section", y="Friction Level", data=df1)
	def figure6():
		fig6 = sns.catplot(x="Test Section", y="Friction Level", kind = "violin", data=df2)
	def figure7():
		fig7 = sns.boxplot(x="Test Section", y="Friction Level", data=df1, whis=np.inf)
		fig7 = sns.stripplot(x="Test Section", y="Friction Level", data=df1, color=".3") 	
	def figure8():
		y = df1.groupby(['Test Section']).mean()
		fig8 = sns.barplot(x = 'Test Section', y = 'Friction Level', data = y.reset_index())
		
	return [figure1,figure2,figure3,figure4,figure5,figure6,figure7,figure8]

if __name__ == "__main__":
	root = tk.Tk()
	b1 = tk.Button(root, text = 'Input Variables, Select Excel Sheet, and Run', command = PDFconverter)
	b1.pack()
	root.mainloop()
	

