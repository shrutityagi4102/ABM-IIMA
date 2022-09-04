import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Individual
import sim

"""TO GENERATE REPORTS"""

answhole = pd.read_excel("ans.xlsx", sheet_name='Individual') #READS THE ANSWER EXCELSHEET

#LOCATION GRAPH
xaxis = list(answhole['IndiId']) #declaring x-AXIS
yaxis = list(answhole['Assigned Location']) #declaring y-AXIS
labels = Individual.simtimeid #declaring legend labels
fig = plt.figure()
ax = fig.add_subplot(111)
#PLOTTING
c,c1 =0,0
for j in range(Individual.no_of_sim):
    c1 = c
    c += Individual.no_of_indi
    x = xaxis[c1:c]
    y = yaxis[c1:c]
    ax.scatter(x, y,label=labels[j],marker="o")   #to plot the scattered points                 
#To set colors
colormap = plt.cm.gist_ncar  
colorst = [colormap(i) for i in np.linspace(0, 0.9,len(ax.collections))]       
for t,j1 in enumerate(ax.collections):
    j1.set_color(colorst[t])
#LABELING
ax.legend(fontsize='small',title='SimTime')
plt.xlabel("Individual ID's")
plt.ylabel("Locations")
plt.title("Location of Different Individuals in Different Time Periods")
plt.show()
#REPORTS
report = pd.read_excel("codeupdated.xlsx", sheet_name='Report') #READING THE REPORT SHEET
reportstobemade = sim.report().split(',') #FROM SIM GETTING THE REPORTS TO BE MADE
for i in reportstobemade:
    if i in list(report["ReportId"]):
        j = list(report["ReportId"]).index(i)
        target = list(report.iloc[j])
        yaxis = list(answhole[target[-3]]) #declaring Y-AXIS
        xaxis = list(answhole[target[-2]]) #declaring X-AXIS
        labels = Individual.simtimeid #declaring legend labels
        fig = plt.figure()
        ax = fig.add_subplot(111)
        #PLOTTING
        c,c1 =0,0
        for j in range(Individual.no_of_sim):
            c1 = c
            c += Individual.no_of_indi
            x = xaxis[c1:c]
            y = yaxis[c1:c]
            if target[-1] == "Scatter":
                ax.scatter(x, y,label=labels[j],marker="o")
                plt.ylabel(target[-3])
                plt.xlabel(target[-2])
            if target[-1] == "Line":
                ax.scatter(x, y,label=labels[j],marker="o")
                ax.plot(x,y,linestyle='--') #to connect points with lines
                plt.ylabel(target[-3])
                plt.xlabel(target[-2])
            if target[-1] == "Histogram":
                ax.hist(y, orientation = 'vertical', alpha=0.4,label=labels[j])
                plt.xlabel(target[-3])    
        #To set colors
        colormap = plt.cm.gist_ncar  
        colorst = [colormap(i) for i in np.linspace(0, 0.9,len(ax.collections))]       
        for t,j1 in enumerate(ax.collections):
            j1.set_color(colorst[t])
        #LABELING
        ax.legend(fontsize='small',title='SimTime')
        plt.title(target[1])
        plt.show()