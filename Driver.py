
#Tools to implement variables into HTML File
from jinja2 import Environment, FileSystemLoader
file_loader = FileSystemLoader('.')
env = Environment(loader = file_loader)
template = env.get_template('base.html')

template_vars = {"test": "testing" ,
"Report_Standard":"SAE J2707 Report Examplllle"}
html_out = template.render(template_vars)

#Tools to covert HTML to PDF
from weasyprint import HTML, CSS
HTML(string = html_out).write_pdf('report.pdf', stylesheets=["Static/basic.css"])

#Successful test of importing variables from another py file
#can now separate the Datascience from the HTML formatting
import Datasci





