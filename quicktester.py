import Datasci
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from xlsx2html import xlsx2html


def PDFconverter():

    """
    convert HTML into PDF dyanamically
    """
    # tools for creating variable template environment converting HTML to PDF
    from jinja2 import Environment, FileSystemLoader
    from weasyprint import HTML, CSS

    # loading the HTML file into an environment to pass variables to it
    file_loader = FileSystemLoader(".")
    env = Environment(loader=file_loader)
    template = env.get_template("FDPBrakes/base.html")

    # list of variables to pass
    template_vars = {}
    # Rendering the variables in and then converting the HTML to PDF
    html_out = template.render(template_vars)
    HTML(string=html_out, base_url=".").write_pdf(
        "testerreport.pdf",
        stylesheets=[
            "/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Static/basic.css"
        ],
    )


def excel_to_html(path):
    xlsx2html(
        path,
        "/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Datasets/TestExcel2HTML.html",
    )


PDFconverter()
