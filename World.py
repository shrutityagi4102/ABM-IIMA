import pandas as pd 
import numpy as np
import sim
#range for all random mean and S.D. values considered 0.0 to 1.0 (Both inclusive)
# Setting the parameters
# World has the following parameters : Indiv ,Loc, EndwToId, PrdToTns, PFs, errEndwToId, errPFs, errEndwVal, EndwVal
#PFs 
PFs = pd.read_excel("codeupdated.xlsx", sheet_name='PFs')
pfslist = list(PFs['PFId'])
#errPFs
errPFs = pd.read_excel("codeupdated.xlsx", sheet_name='errPfs')
errpfslist = list(errPFs['PFId'])
#EndwToId
EndwToId = pd.read_excel("codeupdated.xlsx", sheet_name='EndwToId')
endwtoidlist = list(EndwToId['IdnsEndw']) 
#errEndwToId
errEndwToId = pd.read_excel("codeupdated.xlsx", sheet_name='errEndwToId')
errendwtoidlist = list(errEndwToId['IdEndw']) 
#PrdToTns
PrdToTns = pd.read_excel("codeupdated.xlsx", sheet_name='PrdToTns')
prdtotnslist = list(PrdToTns['PrdT']) 
#EndwVal
EndwValId = pd.read_excel("codeupdated.xlsx", sheet_name='EndwValId')
endwvalidlist = list(EndwValId['IdIdPFIdEndwId'])
#errEndwVal
errEndwValId = pd.read_excel("codeupdated.xlsx", sheet_name='errEndwValId')
errendwvalidlist = list(errEndwValId['IdIdPFIdEndwId'])
#Parameters have been set

#Creating a world agent
def make_agent_world(pfslist,errpfslist,endwtoidlist,errendwtoidlist,prdtotnslist,endwvalidlist,errendwvalidlist):
    agent = []
    toid = []
    for i in range(len(endwtoidlist)):
        p = list(EndwToId.iloc[i])
        toid.append([p[0],np.random.normal(p[-2],p[-1])]) 
    agent.append(toid)
    errtoid = []
    for i in range(len(errendwtoidlist)):
        p = list(errEndwToId.iloc[i])
        errtoid.append([p[0],np.random.normal(p[-2],p[-1])]) 
    agent.append(errtoid)
    prd = []
    for i in range(len(prdtotnslist)):
        p = list(PrdToTns.iloc[i])
        prd.append([p[0],np.random.normal(p[-2],p[-1])]) 
    agent.append(prd)
    vali = []
    for i in range(len(endwvalidlist)):
        p = list(EndwValId.iloc[i])
        vali.append([p[0],np.random.normal(p[-2],p[-1])]) 
    agent.append(vali)
    errvali = []
    for i in range(len(errendwvalidlist)):
        p = list(errEndwValId.iloc[i])
        errvali.append([p[0],np.random.normal(p[-2],p[-1])]) 
    agent.append(errvali)
    pf = []
    for i in range(len(pfslist)):
        p = list(PFs.iloc[i])
        pf.append(p) 
    agent.append(pf)
    errpf = []
    for i in range(len(errpfslist)):
        p = list(errPFs.iloc[i])
        errpf.append(p) 
    agent.append(errpf)
    return agent
#Creating population
def make_population_world(S):
    population = {}
    for i in worldids:     
        population[i] = make_agent_world(pfslist,errpfslist,endwtoidlist,errendwtoidlist,prdtotnslist,endwvalidlist,errendwvalidlist)
    return population

size = sim.world() #SIZE COMES FROM SIM FILE
worldids = ["WID"+str(i) for i in range(1,size+1)]
population = make_population_world(size) #THIS FUNCTION CALLS THE MAKE_AGENT_WORLD NUMBER OF SPECIFIED TIMES
# print(population)
"""STRUCTRE : A dictionary with key as world ID having value as a list """