
import Datasci
import DataSci2

""" creates PDF file from HTML """

def PDFconverter():
        #tools for creating variable template environment converting HTML to PDF
    from jinja2 import Environment, FileSystemLoader
    from weasyprint import HTML, CSS
          
        #loading the HTML file into an environment to pass variables to it
    file_loader = FileSystemLoader('.')
    env = Environment(loader = file_loader)
    template = env.get_template('FDPBrakes/base.html')

        #list of variables to pass 
    template_vars = {
            "Report_Standard":2,
            "Make_And_Model": 1,
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






