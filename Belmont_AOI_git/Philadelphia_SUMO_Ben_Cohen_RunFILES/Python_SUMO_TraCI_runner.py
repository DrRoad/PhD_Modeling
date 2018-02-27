## Last worked on 2/23/2018

## This script was created by Ben Cohen for work toward the completion of his PhD in Civil Engineering.
## The primary purpose of this script is to set up a scenario variables, start up SUMO.exe or SUMOGUI.exe, and then use
## .\SUMO_sim_modding.py to handle all data collection and reporting.

## To use this file. I have been using Jupyter Notebook to directly run this script and iPyhton:
## $ run ./Python_SUMO_TraCI_runner.py


import numpy as np
import traci
import traci.constants as tc
import re
import time
import sumolib
import pandas as pd
import SUMO_sim_modding as SP
import openpyxl as OPENxlsx
# pd.set_option('display.max_rows', 5)


PERIOD_VARRIABLE = SP.Initializer.inputPeriod_asNumber(new=1)
fileINFO = SP.RunFileInfo.GetSimulationRunPrefix(display=0)
SUMO_outPUT_PREFIX = SP.RunFileInfo.GetSimulationRunPrefix(display=0)[0]
SUMO_Traci_PORT = int(SP.RunFileInfo.GetSimulationRunPrefix(display=0)[1])
SP.Initializer.startSUMO(SUMO_Traci_PORT,useCase=str(1))
# Ask for Steps to take or Time to run until
typeRun = SP.Runner.runtypeAsker()
Start_Time = int(traci.simulation.getCurrentTime()/1000) 
print("======",SUMO_outPUT_PREFIX,"======")
estimated_Run_Time = 90000
    # print("You did not specify how long you wanted to run until so the default value = ", estimated_Run_Time)
steps_TT = int(estimated_Run_Time)
# Initalize Files
edgeLISTa = SP.Edge.create_Edge_Instances()
wb = SP.Network_Period.load_n_create_Excel_NetworkFile(SUMO_outPUT_PREFIX,PERIOD_VARRIABLE,steps_TT,PATH=None)[0]
periodNamesLISTa = SP.Network_Period.load_n_create_Excel_NetworkFile(SUMO_outPUT_PREFIX,PERIOD_VARRIABLE,steps_TT,display=0)[1]

# Take a step(s)
SP.Runner.releaseTraci(Start_Time,typeRun,edgeLISTa,PERIOD_VARRIABLE,SUMO_outPUT_PREFIX,periodNamesLISTa,steps_TT)

continue01 = 0
continue01 = str(input("Press x to exit"))
while continue01 != "x":
    SP.Runner.releaseTraci(Start_Time,typeRun,edgeLISTa,PERIOD_VARRIABLE,SUMO_outPUT_PREFIX,periodNamesLISTa,steps_TT)
    continue01 = str(input("Press x to exit"))
    break
    
### I am up to here ###
class Edge():
    # import sumolib
    
    # edge_list = []
    def fillOutworksheet(SUMO_outPUT_PREFIX,periodCounter,edgeLISTa):#,periodNamesLISTa):
        #https://chrisalbon.com/python/data_wrangling/pandas_dataframe_load_xls/
        #### BIG CONTRIBUTION PART
        if periodCounter == 0:
            return
        # PATH_Network_DF_Period_0t00_TEMPLATExlsx = '/GitHub/PhD_Modeling/Belmont_AOI_git/Belmont_AOI-runFILES/Network_DF_Period_0t00_TEMPLATE.xlsx'
        print("\n\n<><><periodCounter = ",int(round(periodCounter)))
        periodCounter = int(round(periodCounter))#periodCounter = int(round(periodCounter)-1) # "-1" because we want to fill in the sheet from the perivious period.
        logger_TEMPDF =pd.read_excel(PATH_Network_DF_Period_0t00_TEMPLATExlsx) #creates a template
        # logger_TEMPDF =pd.read_excel(SP.PATH_Network_DF_Period_0t00_TEMPLATExlsx)
        counter = 0
        #for edge_i in Belmont_Ave[:]:
        for n in range(len(edgeLISTa)): ## I need Belmont_AVEDic[n] == edgeLISTa[n].edgeID == logger_TEMPDF.loc[n,'Belmont_AVEDic_ID']. 1-8-18 saved over tempalte with for loop range(len(edgeLISTa)): newTemplate.loc[i,'Belmont_AVEDic_ID'] = edgeLISTa[i].edgeID 
            logger_TEMPDF.loc[n,'Total_Vehicles'] = (edgeLISTa[n].truckCount + edgeLISTa[n].carCount)
            logger_TEMPDF.loc[n,'Total_Trucks'] = edgeLISTa[n].truckCount
            ## logger_TEMPDF.loc[logger_TEMPDF['Belmont_AVEDic_ID'].str.contains(Belmont_AVEDic[n]),'Total_Trucks'] = edgeLISTa[n].truckCount
            logger_TEMPDF.loc[n,'ESAL'] = edgeLISTa[n].ESAL_TOT
            Condition_RTi = 100.00 - (edgeLISTa[n].ESAL_TOT) * 0.01339
            logger_TEMPDF.loc[n,'Condition_Index'] = Condition_RTi
            # maxSpeedo = logger_TEMPDF.loc[logger_TEMPDF['Belmont_AVEDic_ID'].str.contains(Belmont_AVEDic[n]),'Original_Max_Speed']
            maxSpeedo = edgeLISTa[n].originalMAXSPEED
            maxSpeed_i =(maxSpeedo - (maxSpeedo**((100-Condition_RTi)/96))+4.5675) #Units m/s
            logger_TEMPDF.loc[n,'Dynamic_Max_Speed'] = maxSpeed_i
            # ##Validating writing below here
            # if n == 4:
                # print("\n[<<[<[<>]>]>>]\nedgeLISTa[4].truckCount = ",edgeLISTa[4].truckCount,"<><>\nlogger_TEMPDF.loc[logger_TEMPDF['Belmont_AVEDic_ID'].str.contains(edgeLISTa[n].edgeID),'Total_Trucks']= ",logger_TEMPDF.loc[logger_TEMPDF['Belmont_AVEDic_ID'].str.contains(edgeLISTa[n].edgeID),'Total_Trucks'],"\n[<<[<[<>]>]>>]\n")
            ## Do I need to reset the logger? Will it slow things down towards the end? 
            if len(edgeLISTa[n].vehidLIST) > 100:
                if n == 48:
                    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
                    print('memory use:', memoryUse)
                    edgeLISTa[n]._resetLOGGER(edgeLISTa)
                    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
                    print('memory use:', memoryUse)
                edgeLISTa[n]._resetLOGGER(edgeLISTa)
                ## Needed for metrics
        self.meanSpeed = int(traci.edge.getLastStepMeanSpeed(self.edgeID))
        self.PCR = 0
        self.IRI = 0
        self.AVE_QLTH = 0
        self.ADDT_rand = 0
        self.ADDT_Calc = 0
        self.AGE_0 = 0
        self.SNC = 0
        self.layer_1_dpth_in = 0
        self.layer1_6in_35_50 = 0
        self.layer2_6in_10_25 = 0
        self.layer3_12in_5_17 = 0
        self.ASS_CALI = 0
        ### NOW SAVE THIS DATAFRAME [[logger_TEMPDF]] TO THE SHEET THAT IT CAME FROM IN THE WORKBOOKER
        Network_Period.myWrite_to_excel(logger_TEMPDF,periodCounter,SUMO_outPUT_PREFIX,edgeLISTa)
        ### Change max speed of edge based on roadway damage
        Edge.setNewMaxSpeed(edgeLISTa,logger_TEMPDF)
        Edge.getMaxSpeed(edgeLISTa)
        print("Testing edgeLISTa[48].__dict__ ...\n",edgeLISTa[48].__dict__,"\n")