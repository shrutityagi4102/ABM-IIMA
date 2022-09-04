import pandas as pd 
# STORING THE SIM DATA FROM EXCEELSHEET
sim = pd.read_excel("codeupdated.xlsx", sheet_name='NUMBERS') 

#TO SEND THE NUMBER OF WORLDS
def world(row_num=3):
    return list(sim['NoOfWorld'])[row_num]

#TO SEND THE NUMBER OF INDIVIDUALS AND SIMULATION TIME
def individual(row_num=4):
    return list(sim['NoOfIndivPerWorld'])[row_num],list(sim['SimTime'])[row_num]

#TO SEND THE REPORTS TO BE CREATED
def report(row_num=3):
    return list(sim['Reports created'])[row_num]

