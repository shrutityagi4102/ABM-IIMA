# ABM-IIMA

As part of my summer research internship at IIM Ahmedabad, I performed agent based modeling using Python

A Zip file containing all my work can be downloaded from here : https://drive.google.com/file/d/1gqCTdGS2Yt1Q7dlELrEgdsIUKcFoOnJX/view?usp=sharing

ABM.ipynb : This Python notebook has a LSTM Neural Network whose features,outputs and activation function are taken from the excel sheet

codeupdated.xlsx : This is the main excel sheet which contains information regarding individuals, world and location and their different parameters. In some sheets it also has information about neural networks and reports to be created as per which data is red from the excel sheet and created by the python files

ans.xlsx : This is the autogenersted excel sheet which is generated using Python code as per the information in the codeupdated.xlsx

sim.py  : This Python file is responsible for reading Paramteres from the excel sheet and sending it to other Python files ahead

Individual.py, World.py, Location.py : In these Python files as per paramtetes in the excel sheet, I have performed agent based modeling and returned a nested dictionary containing all details to be stored in the excel sheet
