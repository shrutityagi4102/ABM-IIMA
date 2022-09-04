import pandas as pd 
import numpy as np
import sim
#range for all random mean and S.D. values considered 0.0 to 1.0 (Both inclusive)
# Setting the parameters
no_of_indi,no_of_sim = sim.individual()  #getting the number of individuals and time period from the sim file
indids = ["ID"+str(i) for i in range(1,no_of_indi+1)] #setting individual ids
simtimeid = ["T"+str(i) for i in range(1,no_of_sim+1)] #setting simtime ids
# Individual has the following parameters : NgProp, errNgProp, Locations,Loc,TnsCst,TnsInst,EndwCst,EndwAvail,errTnsCst,errTnsInst,errEndwAvail,errEndwCst
# NgProp
ngprop = pd.read_excel("codeupdated.xlsx", sheet_name='NgProp')
ngproplist = list(ngprop['NgProp'])
# errNgProp
errngprop = pd.read_excel("codeupdated.xlsx", sheet_name='errNgProp')
errngproplist = list(errngprop['errNgProp']) 
# locations
locations = pd.read_excel("codeupdated.xlsx", sheet_name='Location')
locidlist = list(locations['LocId']) 
locnamelist = list(locations['LocName'])
# TnsCst
tnscst = pd.read_excel("codeupdated.xlsx", sheet_name='TnsCst')
tnscstlist = list(tnscst['TnsCst']) 
# errTnsCst
errtnscst = pd.read_excel("codeupdated.xlsx", sheet_name='errTnsCst')
errtnscstlist = list(errtnscst['TnsCst']) 
# TnsInst
tnsinst = pd.read_excel("codeupdated.xlsx", sheet_name='TnsInst')
tnsinstlist = list(tnsinst['Tns']) 
# errTnsInst
errtnsinst = pd.read_excel("codeupdated.xlsx", sheet_name='errTnsInst')
errtnsinstlist = list(errtnsinst['Tns']) 
# EndwCst
endwcst = pd.read_excel("codeupdated.xlsx", sheet_name='EndwCst')
endwcstlist = list(endwcst['EndwCst']) 
# errEndwCst
errendwcst = pd.read_excel("codeupdated.xlsx", sheet_name='errEndwCst')
errendwcstlist = list(errendwcst['EndwCst']) 
# EndwAvail
endwavail = pd.read_excel("codeupdated.xlsx", sheet_name='EndwAvail')
endwavaillist = list(endwavail['EndwAvail']) 
# errEndwAvail
errendwavail = pd.read_excel("codeupdated.xlsx", sheet_name='errEndwAvail')
errendwavaillist = list(errendwavail['EndwAvail']) 
# Parameters have been set
# Creating a Individual agent
def make_agent_individual(ngproplist, errngproplist,locidlist,tnscstlist, errtnscstlist, tnsinstlist, errtnsinstlist, endwcstlist, errendwcstlist, endwavaillist, errendwavaillist):
    agent = []
    global ng
    ng = []
    for i in range(len(ngproplist)):
        p = list(ngprop.iloc[i])
        ng.append([p[0],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(ng)
    global errng
    errng = []
    for i in range(len(errngproplist)):
        p = list(errngprop.iloc[i])
        errng.append([p[0],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(errng)
    global loc
    loc = []
    for i in range(len(locidlist)):
        p = list(locations.iloc[i])
        loc.append([p[0],p[1],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(loc)
    global cst
    cst = []
    for i in range(len(tnscstlist)):
        p = list(tnscst.iloc[i])
        cst.append([p[0],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(cst)
    global errcst
    errcst = []
    for i in range(len(errtnscstlist)):
        p = list(errtnscst.iloc[i])
        errcst.append([p[0],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(errcst)
    global inst
    inst = []
    for i in range(len(tnsinstlist)):
        p = list(tnsinst.iloc[i])
        inst.append([p[0],p[1],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(inst)
    global errinst
    errinst = []
    for i in range(len(errtnsinstlist)):
        p = list(errtnsinst.iloc[i])
        errinst.append([p[0],p[1],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(errinst)
    global endw
    endw = []
    for i in range(len(endwcstlist)):
        p = list(endwcst.iloc[i])
        endw.append([p[0],p[1],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(endw)
    global errendw
    errendw = []
    for i in range(len(errendwcstlist)):
        p = list(errendwcst.iloc[i])
        errendw.append([p[0],p[1],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(errendw)
    global avail
    avail = []
    for i in range(len(endwavaillist)):
        p = list(endwavail.iloc[i])
        avail.append([p[0],p[1],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(avail)
    global erravail
    erravail = []
    for i in range(len(errendwavaillist)):
        p = list(errendwavail.iloc[i])
        erravail.append([p[0],p[1],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(erravail)
    return agent
# probability is weight/sum of all weights, WEIGHT IN OUR CASE WILL BE mean*10
weights = [i*10 for i in list(locations['Mean'])]
probability = [i/sum(weights) for i in weights] #calulcating the probability of a location

def assign_loc(): # assigning a location as per the probability
    loc = np.random.choice(locnamelist, p=probability)
    return loc
#for each individual
def indi(): 
    population = {}
    for i in indids:     
        population[i] = [assign_loc(),make_agent_individual(ngproplist, errngproplist,locidlist,tnscstlist, errtnscstlist, tnsinstlist, errtnsinstlist, endwcstlist, errendwcstlist, endwavaillist, errendwavaillist)]
    return population
#for each simulation
def sim(): 
    alltimeindi = {}
    for i in simtimeid:
        alltimeindi[i] = indi()
    return alltimeindi
# print(sim())
"""STRUCTRE : DICTIONARY WITH A KEY AS SIMTIME -> VALUE AS A DICTIONARY HAVING ALL INDIVIDUALS CREATED IN THAT TIME PERIOD, THEY KEY OF THAT DICTIONARY IS INDIVIDUAL ID -> VALUE OF THAT IDCITONARY IS A LIST HAVING THE ASSIGNED LOCATION AND ALL THE PARAMETERS ASSIGNED TO AN INDIVIDUAL -> THE LIST FOR ALL PARAMETERS HAS A LIST FOR EACH PARAMETER I.E. A LIST FOR NGPROP HAVING LISTS FOR EACH VALUE OF NGPROP"""