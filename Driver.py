
import Datasci

if __name__ == "__main__":
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
        template_vars = {"test": "testing" ,
            "Report_Standard":"SAE J2707 Report Example",
            "Make_And_Model": "2019 Ford F-150",
            "fig_1": Datasci.fig1,
            "fig_2": Datasci.fig2,
            "fig_3": Datasci.fig3,
            "fig_4": Datasci.fig4,
            "fig_5": Datasci.fig5,
            "fig_6": Datasci.fig6,
            "fig_7": Datasci.fig7,
            }
        
        #Rendering the variables in and then converting the HTML to PDF
        html_out = template.render(template_vars)
        HTML(string = html_out, base_url='.').write_pdf('report.pdf', stylesheets=["/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Static/basic.css"])
   
    PDFconverter()






