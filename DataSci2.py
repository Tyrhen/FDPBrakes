import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import table


data_path = (
    "/Users/Ty/Desktop/FDP_brakes_proj_local/FDPBrakes/Datasets/FDP X 19 DATA.xlsx"
)
df1 = pd.read_excel(data_path, sheet_name="Three Sections")
df1 = df1[df1["Final Temp"] > 0]
df2 = pd.read_excel(data_path, sheet_name="Three Sections #2")

sns.set_style("darkgrid")
sns.set_palette("bright")


def figure1():
    figure1 = sns.lineplot(
        x="Stop Number",
        y="Friction Level",
        data=df1,
        hue="Test Section",
    )
    return figure1.figure.savefig(
        "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure1.svg"
    )


def figure2():
    figure2 = sns.lineplot(
        x="Stop Number",
        y="Friction Level",
        hue="Test Section",
        palette="bright",
        data=df2,
    )
    return figure2.figure.savefig(
        "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure2.svg"
    )


def figure3():
    figure3 = sns.relplot(
        x="Friction Level",
        y="Final Temp",
        col="Test Section",
        palette="bright",
        kind="line",
        data=df1,
    )
    return figure3.savefig(
        "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure3.svg"
    )


def figure4():
    figure4 = sns.relplot(
        x="Friction Level",
        y="Final Temp",
        col="Test Section",
        palette="bright",
        kind="scatter",
        data=df2,
    )
    return figure4.savefig(
        "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure4.svg"
    )


def figure5():
    figure5 = sns.catplot(x="Test Section", y="Friction Level", data=df1)
    return figure5.savefig(
        "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure5.svg"
    )


def figure6():
    fig6 = sns.catplot(x="Test Section", y="Friction Level", kind="violin", data=df2)
    return fig6.savefig("/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure6.svg")


def figure7():
    fig7 = sns.boxplot(x="Test Section", y="Friction Level", data=df1, whis=np.inf)
    fig7 = sns.stripplot(x="Test Section", y="Friction Level", data=df1, color=".3")
    return fig7.figure.savefig(
        "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure7.svg"
    )


def figure8():
    y = df1.groupby(["Test Section"]).mean()
    fig8 = sns.barplot(x="Test Section", y="Friction Level", data=y.reset_index())
    return fig8.figure.savefig(
        "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure8.svg"
    )


plt.clf()
figure1()
plt.clf()
figure2()
plt.clf()
figure3()
plt.clf()
figure4()
plt.clf()
figure6()
plt.clf()
figure5()
plt.clf()
figure7()
plt.clf()
figure8()


figure1 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure1.svg"
figure2 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure2.svg"
figure3 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure3.svg"
figure4 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure4.svg"
figure5 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure5.svg"
figure6 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure6.svg"
figure7 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure7.svg"
figure8 = "/Users/Ty/Desktop/FDP_brakes_proj_local/Figures/figure8.svg"
