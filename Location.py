import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

"""KEPT THE SAME AS LAST VERSION"""
#range for all random mean and S.D. values considered 0.0 to 1.0 (Both inclusive)
# Setting the parameters
# Location has the following parameters : Oid, En, PrCst, errOid, errEn, errPrdCst
# Oid
oid = pd.read_excel("codeupdated.xlsx", sheet_name='Oid')
oidlist = list(oid['Oid']) 
# errOid
erroid = pd.read_excel("codeupdated.xlsx", sheet_name='errOid')
erroidlist = list(erroid['Oid']) 
#En
en = pd.read_excel("codeupdated.xlsx", sheet_name='En')
enlist = list(en['En']) 
#errEn
erren = pd.read_excel("codeupdated.xlsx", sheet_name='errEn')
errenlist = list(erren['En']) 
#PrCst
prcst = pd.read_excel("codeupdated.xlsx", sheet_name='PrCst')
prcstlist = list(prcst['PrCst']) 
prdidlist = list(prcst['PrdId'])
#errPrCst
errprcst = pd.read_excel("codeupdated.xlsx", sheet_name='errPrCst')
errprcstlist = list(errprcst['PrCst']) 
errprdidlist = list(errprcst['PrdId'])
#Parameters have been set

# Creating a Individual agent
def make_agent_individual(oidlist,erroidlist,enlist,errenlist,prcstlist,errprcstlist):
    agent = []
    o = []
    for i in range(len(oidlist)):
        p = list(oid.iloc[i])
        o.append([p[0],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(o)
    erro = []
    for i in range(len(erroidlist)):
        p = list(erroid.iloc[i])
        erro.append([p[0],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(erro)
    n = []
    for i in range(len(enlist)):
        p = list(en.iloc[i])
        n.append([p[0],p[1],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(n)
    errn = []
    for i in range(len(errenlist)):
        p = list(erren.iloc[i])
        errn.append([p[0],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(errn)
    pr = []
    for i in range(len(prcstlist)):
        p = list(prcst.iloc[i])
        pr.append([p[0],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(pr)
    errp = []
    for i in range(len(errprcstlist)):
        p = list(errprcst.iloc[i])
        errp.append([p[0],p[1],np.random.normal(p[-2],p[-1])]) #this will randomly pick a value from a normal distirbution having mean and sd as mentioned in the excel sheet 
    agent.append(errp)
    return agent
#Creating population
def make_population_individual(S):
    population = []
    for i in range(S):     
        agent = make_agent_individual(oidlist,erroidlist,enlist,errenlist,prcstlist,errprcstlist)
        population.append(agent)
    return population
size = int(input("Please enter the population size : "))
population = make_population_individual(size)
# print(population)  #whole population
#USER INPUTS
opt = int(input("Please enter the option number of parameter for which you want to see the normal distribution plot \n1. Oid \n2. errOid \n3. En \n4. errEn \n5. PrCst \n6. errPrCst  \nYour choice : "))
allvalues = []
d = {1:oidlist, 2:erroidlist, 3:enlist, 4:errenlist, 5:prcstlist, 6:errprcstlist}
d1 = {1:oid, 2:erroid, 3:en, 4:erren, 5:prcst, 6:errprcst}
if opt>6 or opt<1:    #for wrong choice
    print("Please enter a correct choice, Restart the program")
    quit()
else:
    for i in range(size):
        allvalues.append(population[i][opt-1])      #storing all values in the population for that paramter

print("Please select the value of parameter for which you want to see the normal distirbution : ")
jk = d1[opt]
if opt == 5:       # to print prcst and prid
    print("Just enter the PrCst value")
    for i in range(len(prcstlist)):
        print(prcstlist[i],prdidlist[i])
elif opt == 6:       # to print prcst and prid
    print("Just enter the PrCst value")
    for i in range(len(errprcstlist)):
        print(errprcstlist[i],errprdidlist[i])
else:
    for keys in d:
        if opt == keys:
            for i in d[keys]:
                print(i)

val = input("Your choice : ")
valwise = []
for i in range(len(jk)):
    p = list(jk.iloc[i])
    if p[0] == val:
        valwise.append(p) #the first value has the mean and sd
for i in allvalues:
    for j in i:
        if j[0] == val:
            valwise.append(j)                  #storing all values according to the user's choice
if len(valwise)<=1:                              #if valwise is yet empty it means the user has entered a wrong option
    print("Please enter a correct choice, Restart the program")
    quit()
#x = np.linspace(-3,3,100) 
m = valwise[0][-2]
s = valwise[0][-1]
x = np.linspace(m-(3*s),m+(3*s),100)
#Normal Distribution : PDF
plt.subplot(1, 2, 1)
#PLOTS
plt.plot(x, stats.norm.pdf(x,m,s), label=(f"μ: {m}, σ: {s}"))
plt.legend(title='Values')
plt.title('Normal Distribution : PDF', fontsize=10)
#Normal Distribution : CDF
plt.subplot(1, 2, 2)
cdf = np.cumsum(stats.norm.pdf(x,m,s))
plt.plot(cdf)
plt.title('Normal Distribution : CDF', fontsize=10)
# points = i[-2]-i[-1], i[-2]+i[-1]      # POINTS OF STANDARD DEVIATION IF NEEDED
# plt.plot(x, stats.norm.pdf(x, i[-2], i[-1]), label=(f"μ: {i[-2]}, σ: {i[-1]}, Points of SD : {(round(points[0],2),round(points[1],2))}"))
plt.subplots_adjust(wspace=0.25, hspace=0)
plt.show()
#Histogram of the values selected
para_val = []
for i in range(1,len(valwise)):
    para_val.append(valwise[i][-1])         
plt.hist(para_val,bins=50,alpha=0.5, histtype='bar', ec='black')
median_hour = np.median(para_val)
plt.axvline(median_hour, color="black", ls="--", label="Median")
plt.legend(title='Values')
plt.title('Histogram of Values', fontsize=10)
plt.show()