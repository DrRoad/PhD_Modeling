
# coding: utf-8

# ## Lasted Worked on 2/25/2018

# In[1]:

import numpy as np
import traci
import traci.constants as tc
import re
import time
import sumolib
# import cProfile, pstats , io
import pandas as pd
import openpyxl as OPENxlsx


pd.set_option('display.max_rows', 5)


# In[2]:

loading_FROM = input("\n\t\t<><><> press d to run from Drexel location <><><>")
print("loading_FROM = ",loading_FROM)
if loading_FROM == str("d"):
	configPATH = "C:/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/Belmont_AOI_git/Belmont_AOI-runFILES/BMAOI_TRACI_DXL.sumocfg"
else:
	configPATH = "C:/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/Belmont_AOI_git/Belmont_AOI-runFILES/BMAOI_TRACI_DB.sumocfg"
print("configPATH = ",configPATH)


# In[3]:

import sumoPython_git_A as SP


# In[ ]:


PERIOD_VARRIABLE = SP.Initializer.inputPeriod_asNumber(new=1)
fileINFO = SP.RunFileInfo.GetSimulationRunPrefix(loading_FROM=loading_FROM,display=0)
SUMO_outPUT_PREFIX = SP.RunFileInfo.GetSimulationRunPrefix(loading_FROM=loading_FROM,display=0)[0]
SUMO_Traci_PORT = int(SP.RunFileInfo.GetSimulationRunPrefix(loading_FROM=loading_FROM,display=0)[1])
SP.Initializer.startSUMO(SUMO_Traci_PORT,useCase=str(1))
    # Ask for Steps to take or Time to run until
typeRun = SP.Runner.runtypeAsker()
Start_Time = int(traci.simulation.getCurrentTime()/1000) #SP.Initializer.runSUMO(SUMO_Traci_PORT,useCase="Continue")[0]
# estimated_Run_Time = input("...\n\n\nHow long will you run this file for... ")
# if estimated_Run_Time == '':
estimated_Run_Time = 90000
    # print("You did not specify how long you wanted to run until so the default value = ", estimated_Run_Time)
steps_TT = int(estimated_Run_Time)
# Initalize Files
print("======",SUMO_outPUT_PREFIX,"======")
edgeLISTa = SP.Edge.create_Edge_Instances()
wb = SP.Network_Period.load_n_create_Excel_NetworkFile(SUMO_outPUT_PREFIX,PERIOD_VARRIABLE,steps_TT,PATH=None)[0]
periodNamesLISTa = SP.Network_Period.load_n_create_Excel_NetworkFile(SUMO_outPUT_PREFIX,PERIOD_VARRIABLE,steps_TT,display=0)[1]



# In[ ]:

# Take a step(s)
SP.Runner.releaseTraci(Start_Time,typeRun,edgeLISTa,PERIOD_VARRIABLE,SUMO_outPUT_PREFIX,periodNamesLISTa,steps_TT)

continue01 = 0
continue01 = str(input("Press x to exit"))
while continue01 != "x":
    SP.Runner.releaseTraci(Start_Time,typeRun,edgeLISTa,PERIOD_VARRIABLE,SUMO_outPUT_PREFIX,periodNamesLISTa,steps_TT)
    continue01 = str(input("Press x to exit"))
    break

# In[ ]:

# # typeRun = 'T'


# In[ ]:

# # traci.close()


# Look for 
# Storage(a
# C:\Sumo\runs\BelmontC_AOI_main\BelmontC_AOI-outPUT\BMAOI_C-EmissionFILES\Emissions_output.xml

# In[ ]:

# # edgeLISTa[1].Dynamic_Max_Speed



# In[ ]:

# # logger_TEMPDF.loc[1,'ESAL'] = edgeLISTa[1].ESAL_TOT
# # Condition_RTi = 100.00 - (edgeLISTa[1].ESAL_TOT) * 0.01339
# # logger_TEMPDF.loc[1,'Condition_Index'] = Condition_RTi
# maxSpeedo = logger_TEMPDF.loc[logger_TEMPDF['Belmont_AVEDic_ID'].str.contains(Belmont_AVEDic[n]),'Original_Max_Speed']
# # maxSpeedo = edgeLISTa[1].originalMAXSPEED
# # maxSpeed_i =(maxSpeedo - (maxSpeedo**((100-Condition_RTi)/96))+4.5675)
# # edgeLISTa[1].Dynamic_Max_Speed = maxSpeed_i


# In[ ]:

# # maxSpeed_i


# In[ ]:

# # edgeLISTa[1].__dict__


# In[ ]:

# # PATH_to_Save_to = "/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-DataFrames/BMAOI_edgeCasheFILES/Network_" +SUMO_outPUT_PREFIX + "_PeriodBook.xlsx"
# # logger_TEMPDF =pd.read_excel(PATH_to_Save_to)
# # logger_TEMPDF.PCR[1]


# In[ ]:

# # http://onlinepubs.trb.org/Onlinepubs/trr/1989/1215/1215-001.pdf
      # PCR(t) = 90 - a * [exp(Age^b)-1] * log(ESAL/SNC^c) a = 0.6349; b = 0.4203; and c = 2.7062


# In[ ]:

# PATH_Network_DF_Period_0t00_TEMPLATExlsx = '/GitHub/PhD_Modeling/Belmont_AOI_git/Belmont_AOI-runFILES/Network_DF_Period_0t00_TEMPLATE.xlsx'
# # PATH_Network_DF_Period_0t00_TEMPLATExlsx = PATH_Network_DF_Period_0t00_TEMPLATExlsx = '/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/Belmont_AOI_git/Belmont_AOI-runFILES/Network_DF_Period_0t00_TEMPLATE.xlsx'
# # PATH_Network_DF_Period_0t00_TEMPLATExlsx
# # logger_TEMPDF =pd.read_excel(PATH_Network_DF_Period_0t00_TEMPLATExlsx)
# # print(logger_TEMPDF.columns,"\nlogger_TEMPDF.AGE_0 = ",logger_TEMPDF.AGE_0)


# In[ ]:

# # import sumoPython_git_A as SP


# In[ ]:

# # logger_TEMPDF.loc[1,'AGE_0']


# In[ ]:

# # edgeLISTa[1].Dynamic_Max_Speed


# In[ ]:

# # logger_TEMPDF.loc[logger_TEMPDF['Belmont_AVEDic_ID'].str.contains(edgeLISTa[1].edgeID),'Dynamic_Max_Speed'] #== edgeLISTa[1].Dynamic_Max_Speed



# In[ ]:

# # age_t = 4
# # ESAL = 2
# # SNC=2


# In[ ]:

# # PCCR = 90-0.6349 * (np.exp(age_t**0.4203)-1) * np.log(ESAL/(SNC**2.7062))
# # IRRI = 52 + 8.1 * ()


# In[ ]:

# # age_now = (self.AGE_0+self.AGE_t/31556926)


# In[ ]:




# In[ ]:

# # def set_some_more_try_to_integrate(edgeLISTa,logger_TEMPDF):
    # # for n in range(len(edgeLISTa)):
        # # edgeLISTa[n].AGE_0 = logger_TEMPDF.loc[n,'AGE_0']
        # # edgeLISTa[n].ADDT_rand = logger_TEMPDF.loc[n,'ADTT_rand']
        # # edgeLISTa[n].ASS_CALI = logger_TEMPDF.loc[n,'ASS_CALI']
        # # edgeLISTa[n].SNC = logger_TEMPDF.loc[n,'SNC']
        # # edgeLISTa[n].layer_1_dpth_in = logger_TEMPDF.loc[n,'layer_1_dpth_in']
        # # edgeLISTa[n].layer1_6in_35_50 = logger_TEMPDF.loc[n,'layer1_6in_35_50']
        # # edgeLISTa[n].layer2_6in_10_25 = logger_TEMPDF.loc[n,'layer2_6in_10_25']
        # # edgeLISTa[n].layer3_12in_5_17 = logger_TEMPDF.loc[n,'layer3_12in_5_17']
        # # edgeLISTa[n].AADT_Calc = logger_TEMPDF.loc[n,'ADTT_rand']

# # set_some_more_try_to_integrate(edgeLISTa,logger_TEMPDF)
# # self.meanSpeed = int(traci.edge.getLastStepMeanSpeed(self.edgeID))
# # self.PCR = 90-0.6349 * (np.exp((self.AGE_0+self.AGE_t/31556926)**0.4203)-1) * np.log(self.ESAL_TOT/((self.SNC)**2.7062)

# # self.IRI = 52+8.1*((self.AGE_0+self.AGE_t/31556926))+0.0009*self.ADDT_Calc

# # edgeLISTa[1].__dict__

