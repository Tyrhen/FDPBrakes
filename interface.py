import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import matplotlib
matplotlib.use("TkAgg")
import DataSci2
import Datasci

#Functions for the buttons of the GUI
def givedata():
	"""
	Take input from user about the details of the vehicle being tested
	"""
	listed = []
	answer1 = simpledialog.askstring("Input", "What is the Make of the Test Vehicle", parent=root)
	if answer1 is not None:
		print(answer1)
		listed.append(answer1)
	
	
	answer2 = simpledialog.askstring("Input", "What is the Model of the Test Vehicle", parent=root)
	if answer2 is not None:
		print(answer2)
		listed.append(answer2)
		

	answer3 = simpledialog.askstring("Input", "What is the date? (format: xx/xx/xx)", parent=root)
	if answer3 is not None:
		print(answer3)
		listed.append(answer3)
		

	answer4 = simpledialog.askinteger("Input", "What is year of the model?", parent=root, minvalue=0, maxvalue=2020)
	if answer4 is not None:
		print(answer4)
		listed.append(answer4)
	print(listed)
	return answer1,answer2 
def PDFconverter():
    """
	convert HTML into PDF dyanamically
	"""
	#tools for creating variable template environment converting HTML to PDF
    from jinja2 import Environment, FileSystemLoader
    from weasyprint import HTML, CSS

    #loading the HTML file into an environment to pass variables to it
    file_loader = FileSystemLoader('.')
    env = Environment(loader = file_loader)
    template = env.get_template('FDPBrakes/base.html')

    #list of variables to pass 
    answer1,answer2 = givedata()
    template_vars = {
            "Report_Standard":answer1,
            "Make_And_Model": answer2,
            "fig2_1": DataSci2.figure1,
            "fig2_2": DataSci2.figure2,
            "fig2_3": DataSci2.figure3,
            "fig2_4": DataSci2.figure4,
            "fig2_5": DataSci2.figure5,
            "fig2_6": DataSci2.figure6,
            "fig2_7": DataSci2.figure7,
            "fig2_8": DataSci2.figure8,
            "fig_1": Datasci.fig1,
            "fig_2": Datasci.fig2,
            "fig_3": Datasci.fig3,
            "fig_4": Datasci.fig4,
            "fig_5": Datasci.fig5,
            "fig_7": Datasci.fig7,
           }
        
        #Rendering the variables in and then converting the HTML to PDF
    html_out = template.render(template_vars)
    HTML(string = html_out, base_url='.').write_pdf('report.pdf', stylesheets=["/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Static/basic.css"])
def getdata():
	"""
	prompt user for path of the excel file that contains all the test data
	"""
	file_path = filedialog.askopenfilename(title = 'Select File',filetypes=[("Excel files", ".xlsx .xls")])
	l1 = tk.Label(root, text = "File path: " + file_path)
	l1.place(relx =0, rely = 0.9)	

if __name__ == "__main__":
	root = tk.Tk()
	b1 = tk.Button(root, text = 'Choose Excel Data File', command = getdata)
	b1.pack()
	b2 = tk.Button(root, text = 'Input Variables and Run', command = PDFconverter)
	b2.pack()
	root.mainloop()
	

