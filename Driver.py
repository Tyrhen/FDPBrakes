
#Tools to covert HTML to PDF
from weasyprint import HTML, CSS
HTML('base.html').write_pdf('report.pdf')

#Successful test of importing variables from another py file
#can now separate the Datascience from the HTML formatting
import Datasci



"""
#Tools to implement variables into HTML File
from jinja2 import Environment, FileSystemLoader
file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)
template = env.get_template('base.html')
template_vars = {}
html_out = template.render(template_vars)
"""