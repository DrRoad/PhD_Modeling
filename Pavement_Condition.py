import os, sys
import numpy as np
import traci
import traci.constants as tc
import re
import sumolib
import time
import General_TraciSUMO_Git
import pandas as pd



class condition:
    PavePath = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Pavement_Condition_fileV0.npy'
    OutPath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Traci_Output-V2.1_file.npy'
    StreetPath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Belmont-Ave-EdgeList.npy'
    StreetDICPath = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Belmont-Ave-EdgeDIC.npy'
    resetEdgeHistoryPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_VehIDhistoryNP_RESET.npy'  
    EdgeHistoryPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_VehIDhistoryNP.csv'
    resetEdgeHistoryPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_VehIDhistoryNPreset.csv'    
    EdgeParamPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_ParamNP.csv'
    resetEdgeParamPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_ParamNPreset.csv'
    PATH_Network_DF_Period_0t00_TEMPLATE = '/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-DataFrames/Network_DF_Period_0t00_TEMPLATE.csv'
    PATH_edge_i_cashe_TEMPLATE = '/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-DataFrames/Edge_i_cashe_TEMPLATE.csv' #index=['Belmont_AVEDic_ID',]'Edge_ID', 'Veh_ID', 'Type', 'Car_Count', 'Truck_Count', 'ESAL_contrib', 'Emergancy_Stop', 'Accident']
    PATH_BMAOI_edgeCasheFILES = '/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-DataFrames/BMAOI_edgeCasheFILES'
    
    #edge_parametersDF = {'1': [100,0,0,0,0,0,29,30], '2': [100,0,0,0,0,0,29,30], '3': [100,0,0,0,0,0,29,30], '4': [100,0,0,0,0,0,29,30], '5': [100,0,0,0,0,0,29,30], '6': [100,0,0,0,0,0,29,30], '7': [100,0,0,0,0,0,29,30], '8': [100,0,0,0,0,0,29,30], '9': [100,0,0,0,0,0,29,30], '10': [100,0,0,0,0,0,29,30], '11': [100,0,0,0,0,0,29,30], '12': [100,0,0,0,0,0,29,30], '13': [100,0,0,0,0,0,29,30], '14': [100,0,0,0,0,0,29,30], '15': [100,0,0,0,0,0,29,30], '16': [100,0,0,0,0,0,29,30], '17': [100,0,0,0,0,0,29,30], '18': [100,0,0,0,0,0,29,30], '19': [100,0,0,0,0,0,29,30], '20': [100,0,0,0,0,0,29,30], '21': [100,0,0,0,0,0,29,30], '22': [100,0,0,0,0,0,29,30], '23': [100,0,0,0,0,0,29,30], '24': [100,0,0,0,0,0,29,30], '25': [100,0,0,0,0,0,29,30], '26': [100,0,0,0,0,0,29,30], '27': [100,0,0,0,0,0,29,30], '28': [100,0,0,0,0,0,29,30], '29': [100,0,0,0,0,0,29,30], '30': [100,0,0,0,0,0,29,30], '31': [100,0,0,0,0,0,29,30], '32': [100,0,0,0,0,0,29,30], '33': [100,0,0,0,0,0,29,30], '34': [100,0,0,0,0,0,29,30], '35': [100,0,0,0,0,0,29,30], '36': [100,0,0,0,0,0,29,30], '37': [100,0,0,0,0,0,29,30], '38': [100,0,0,0,0,0,29,30], '39': [100,0,0,0,0,0,29,30], '40': [100,0,0,0,0,0,29,30], '41': [100,0,0,0,0,0,29,30], '42': [100,0,0,0,0,0,29,30], '43': [100,0,0,0,0,0,29,30], '44': [100,0,0,0,0,0,29,30], '45': [100,0,0,0,0,0,29,30], '46': [100,0,0,0,0,0,29,30], '47': [100,0,0,0,0,0,29,30], '48': [100,0,0,0,0,0,29,30], '49': [100,0,0,0,0,0,29,30], '50': [100,0,0,0,0,0,29,30], '51': [100,0,0,0,0,0,29,30], '52': [100,0,0,0,0,0,29,30], '53': [100,0,0,0,0,0,29,30], '54': [100,0,0,0,0,0,29,30], '55': [100,0,0,0,0,0,29,30], '56': [100,0,0,0,0,0,29,30], '57': [100,0,0,0,0,0,29,30], '58': [100,0,0,0,0,0,29,30], '59': [100,0,0,0,0,0,29,30], '60': [100,0,0,0,0,0,29,30], '61': [100,0,0,0,0,0,29,30], '62': [100,0,0,0,0,0,29,30], '63': [100,0,0,0,0,0,29,30], '64': [100,0,0,0,0,0,29,30], '65': [100,0,0,0,0,0,29,30], '66': [100,0,0,0,0,0,29,30], '67': [100,0,0,0,0,0,29,30], '68': [100,0,0,0,0,0,29,30], '69': [100,0,0,0,0,0,29,30], '70': [100,0,0,0,0,0,29,30], '71': [100,0,0,0,0,0,29,30], '72': [100,0,0,0,0,0,29,30], '73': [100,0,0,0,0,0,29,30], '74': [100,0,0,0,0,0,29,30], '75': [100,0,0,0,0,0,29,30], '76': [100,0,0,0,0,0,29,30], '77': [100,0,0,0,0,0,29,30], '78': [100,0,0,0,0,0,29,30], '79': [100,0,0,0,0,0,29,30], '80': [100,0,0,0,0,0,29,30]}     
     #edge_parametersDF = pd.DataFrame(edge_parametersDF,index=['Condition_RT','Tot_Trucks','Trucks_Pi','Trucks_Pi-1','Trucks_Pi-2','Trucks_Pi-3','MaxSpeed_i_m/s','O_max_mph'])
    #edge_parametersDF.to_csv(resetEdgeParamPANDAPATH)
    
    pavementConditionarrary_T0 = np.array([["Edge_ID","Condition_RT","Tot_Trucks","Trucks_Pi","Trucks_Pi-1","Trucks_Pi-2","Trucks_Pi-3","MaxSpeed_i_m/s"],["-12150712#3",100,0,0,0,0,0,29],["-12150712#4",100,0,0,0,0,0,29],["-12150712#6",100,0,0,0,0,0,29],["-12327906#0",100,0,0,0,0,0,29],["-196358954#0",100,0,0,0,0,0,29],["-196358954#3",100,0,0,0,0,0,29],["-196358956#2",100,0,0,0,0,0,29],["-387423966",100,0,0,0,0,0,29],["-423956981",100,0,0,0,0,0,29],["-423956982",100,0,0,0,0,0,29],["-423965484",100,0,0,0,0,0,29],["-423967058#0",100,0,0,0,0,0,29],["-423967058#1",100,0,0,0,0,0,29],["-423967352",100,0,0,0,0,0,29],["-423967353",100,0,0,0,0,0,29],["-423967354",100,0,0,0,0,0,29],["-423967355",100,0,0,0,0,0,29],["-423967356",100,0,0,0,0,0,29],["-423967357",100,0,0,0,0,0,29],["-423967358#1",100,0,0,0,0,0,29],["-423967358#2",100,0,0,0,0,0,29],["-423967359#0",100,0,0,0,0,0,29],["-423967359#1",100,0,0,0,0,0,29],["-424803245",100,0,0,0,0,0,29],["-424803247#1",100,0,0,0,0,0,29],["-424824619",100,0,0,0,0,0,29],["-424824620",100,0,0,0,0,0,29],["-424824621",100,0,0,0,0,0,29],["-424978161",100,0,0,0,0,0,29],["-424978642.0",100,0,0,0,0,0,29],["-424978642.170",100,0,0,0,0,0,29],["-424978643",100,0,0,0,0,0,29],["-424978647#1",100,0,0,0,0,0,29],["-448887867",100,0,0,0,0,0,29],["-448887868",100,0,0,0,0,0,29],["-448887869",100,0,0,0,0,0,29],["-448887870#1",100,0,0,0,0,0,29],["-448887871#0",100,0,0,0,0,0,29],["-448887871#2",100,0,0,0,0,0,29],["-49940170#0",100,0,0,0,0,0,29],["12150712#3",100,0,0,0,0,0,29],["12150712#4",100,0,0,0,0,0,29],["12150712#5",100,0,0,0,0,0,29],["12327906#0",100,0,0,0,0,0,29],["12327906#1",100,0,0,0,0,0,29],["196358954#0",100,0,0,0,0,0,29],["196358954#1",100,0,0,0,0,0,29],["196358956#0",100,0,0,0,0,0,29],["387423966",100,0,0,0,0,0,29],["423956978",100,0,0,0,0,0,29],["423956979",100,0,0,0,0,0,29],["423956980",100,0,0,0,0,0,29],["423965484",100,0,0,0,0,0,29],["423967058#1",100,0,0,0,0,0,29],["423967352",100,0,0,0,0,0,29],["423967353",100,0,0,0,0,0,29],["423967354",100,0,0,0,0,0,29],["423967355",100,0,0,0,0,0,29],["423967356",100,0,0,0,0,0,29],["423967358#0",100,0,0,0,0,0,29],["423967358#2",100,0,0,0,0,0,29],["423967359#0",100,0,0,0,0,0,29],["423967359#1",100,0,0,0,0,0,29],["424803245",100,0,0,0,0,0,29],["424803247#0",100,0,0,0,0,0,29],["424824619",100,0,0,0,0,0,29],["424824620",100,0,0,0,0,0,29],["424824621",100,0,0,0,0,0,29],["424978639.0",100,0,0,0,0,0,29],["424978639.102",100,0,0,0,0,0,29],["424978640",100,0,0,0,0,0,29],["424978643",100,0,0,0,0,0,29],["424978644",100,0,0,0,0,0,29],["424978646",100,0,0,0,0,0,29],["448887867",100,0,0,0,0,0,29],["448887868",100,0,0,0,0,0,29],["448887869",100,0,0,0,0,0,29],["448887870#0",100,0,0,0,0,0,29],["448887871#0",100,0,0,0,0,0,29],["448887871#1",100,0,0,0,0,0,29]],dtype=object)
    
    Condition_RT_T0 = ([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    
    Belmont_Ave=("-12150712#3", "-12150712#4", "-12150712#6", "-12327906#0", "-196358954#0", "-196358954#3", "-196358956#2", "-387423966", "-423956981", "-423956982", "-423965484", "-423967058#0", "-423967058#1", "-423967352", "-423967353", "-423967354", "-423967355", "-423967356", "-423967357", "-423967358#1", "-423967358#2", "-423967359#0", "-423967359#1", "-424803245", "-424803247#1", "-424824619", "-424824620", "-424824621", "-424978161", "-424978642.0", "-424978642.170", "-424978643", "-424978647#1", "-448887867", "-448887868", "-448887869", "-448887870#1", "-448887871#0", "-448887871#2", "-49940170#0", "12150712#3", "12150712#4", "12150712#5", "12327906#0", "12327906#1", "196358954#0", "196358954#1", "196358956#0", "387423966", "423956978", "423956979", "423956980", "423965484", "423967058#1", "423967352", "423967353", "423967354", "423967355", "423967356", "423967358#0", "423967358#2", "423967359#0", "423967359#1", "424803245", "424803247#0", "424824619", "424824620", "424824621", "424978639.0", "424978639.102", "424978640", "424978643", "424978644", "424978646", "448887867", "448887868", "448887869", "448887870#0", "448887871#0", "448887871#1")
    
    Belmont_AVEDic ={'-12150712#3' : '0e', '-12150712#4' : '1e', '-12150712#6' : '2e', '-12327906#0' : '3e', '-196358954#0' : '4e', '-196358954#3' : '5e', '-196358956#2' : '6e', '-387423966' : '7e', '-423956981' : '8e', '-423956982' : '9e', '-423965484' : '10e', '-423967058#0' : '11e', '-423967058#1' : '12e', '-423967352' : '13e', '-423967353' : '14e', '-423967354' : '15e', '-423967355' : '16e', '-423967356' : '17e', '-423967357' : '18e', '-423967358#1' : '19e', '-423967358#2' : '20e', '-423967359#0' : '21e', '-423967359#1' : '22e', '-424803245' : '23e', '-424803247#1' : '24e', '-424824619' : '25e', '-424824620' : '26e', '-424824621' : '27e', '-424978161' : '28e', '-424978642.0' : '29e', '-424978642.170' : '30e', '-424978643' : '31e', '-424978647#1' : '32e', '-448887867' : '33e', '-448887868' : '34e', '-448887869' : '35e', '-448887870#1' : '36e', '-448887871#0' : '37e', '-448887871#2' : '38e', '-49940170#0' : '39e', '12150712#3' : '40e', '12150712#4' : '41e', '12150712#5' : '42e', '12327906#0' : '43e', '12327906#1' : '44e', '196358954#0' : '45e', '196358954#1' : '46e', '196358956#0' : '47e', '387423966' : '48e', '423956978' : '49e', '423956979' : '50e', '423956980' : '51e', '423965484' : '52e', '423967058#1' : '53e', '423967352' : '54e', '423967353' : '55e', '423967354' : '56e', '423967355' : '57e', '423967356' : '58e', '423967358#0' : '59e', '423967358#2' : '60e', '423967359#0' : '61e', '423967359#1' : '62e', '424803245' : '63e', '424803247#0' : '64e', '424824619' : '65e', '424824620' : '66e', '424824621' : '67e', '424978639.0' : '68e', '424978639.102' : '69e', '424978640' : '70e', '424978643' : '71e', '424978644' : '72e', '424978646' : '73e', '448887867' : '74e', '448887868' : '75e', '448887869' : '76e', '448887870#0' : '77e', '448887871#0' : '78e', '448887871#1' : '79e'}
    #{'-12150712#3': '''', '-12150712#4': '2e', '-12150712#6': '3e', '-12327906#0': '4e', '-196358954#0': '5e', '-196358954#3': '6e', '-196358956#2': '7e', '-387423966': '8e', '-423956981': '9e', '-423956982': '10e', '-423965484': '11e', '-423967058#0': '12e', '-423967058#1': '13e', '-423967352': '14e', '-423967353': '15e', '-423967354': '16e', '-423967355': '17e', '-423967356': '18e', '-423967357': '19e', '-423967358#1': '20e', '-423967358#2': '21e', '-423967359#0': '22e', '-423967359#1': '23e', '-424803245': '24e', '-424803247#1': '25e', '-424824619': '26e', '-424824620': '27e', '-424824621': '28e', '-424978161': '29e', '-424978642.0': '30e', '-424978642.170': '31e', '-424978643': '32e', '-424978647#1': '33e', '-448887867': '34e', '-448887868': '35e', '-448887869': '36e', '-448887870#1': '37e', '-448887871#0': '38e', '-448887871#2': '39e', '-49940170#0': '40e', '12150712#3': '41e', '12150712#4': '42e', '12150712#5': '43e', '12327906#0': '44e', '12327906#1': '45e', '196358954#0': '46e', '196358954#1': '47e', '196358956#0': '48e', '387423966': '49e', '423956978': '50e', '423956979': '51e', '423956980': '52e', '423965484': '53e', '423967058#1': '54e', '423967352': '55e', '423967353': '56e', '423967354': '57e', '423967355': '58e', '423967356': '59e', '423967358#0': '60e', '423967358#2': '61e', '423967359#0': '62e', '423967359#1': '63e', '424803245': '64e', '424803247#0': '65e', '424824619': '66e', '424824620': '67e', '424824621': '68e', '424978639.0': '69e', '424978639.102': '70e', '424978640': '71e', '424978643': '72e', '424978644': '73e', '424978646': '74e', '448887867': '75e', '448887868': '76e', '448887869': '77e', '448887870#0': '78e', '448887871#0': '79e', '448887871#1': '80e'}
       
    equiv_ESAL = {'Car' : 0.0007, 'Truck' : 0.10, 'Semi' : 1.35, '40ftBus' : 1.85}
    Network_DF_Period_0t00DF_colDIC = {'Belmont_AVEDic_ID' : 0, 'Edge_ID' : 1, 'Condition_Index' : 2, 'State_of_Condition' : 3, 'Dynamic_Max_Speed' : 4, 'Total_Vehicles' : 5, 'ESAL' : 6, 'Total_Emergancy_Stops' : 7, 'Total_Accidents' : 8, 'Area' : 9, 'Roadway_Designation' : 10, 'Prority' : 11, 'Original_Max_Speed' : 12, 'Flood_Plain' : 13, 'Physical_Parameters_Others' : 14, 'Environmental_Parameters_Others' : 15}
    # Belmont_AVE = np.load(StreetPath)
    
    # def DetFunc_V0(edgez_i, Edge_TOT_Trucks,Edge_TOT_Trucks_Current_Period):
        # pavementConditionarrary = np.load(condition.PavePath)
            # ### print("edgez_i = ",str(edgez_i),"\n", str(pavementConditionarrary[0,1]),"\n condition.Belmont_AVEDic[edgez_i] = ",str(condition.Belmont_AVEDic[edgez_i]),"\t pavementConditionarrary[int(edgez_i,1] should be the condition RT", str(pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),1]),"<>\n")
         # # 0.01339 = (7040 trucks per 10 years)/(5,256,000 hours per 10 years)*10 #Slightly arbitrary but just a function
        # Condition_RT = 100.00 - float(Edge_TOT_Trucks) * 0.01339
        # maxSpeedo = 30.54 #traci.edge.getParameter(edgez_i, "MAXSPEED") <- Still does not work
        # #print("maxSpeedo = ",maxSpeedo)
        # maxSpeed_i = 0.44704 *  (maxSpeedo - (maxSpeedo**((100-Condition_RT)/96))+4.5675) #0.44704(km/mph)
        # maxSpeed_i2 = 0.44704 * ((-0.0000005*int(Condition_RT))**4+0.0001*int(Condition_RT)**3-0.0184*int(Condition_RT)**2+1.1929*int(Condition_RT)-4.5675)
        # #print("Max Speed Now", str(maxSpeed_i),"\t\tAlternative function found by excel =",str(maxSpeed_i2))
        # #traci.edge.setMaxSpeed(str(edgez_i),maxSpeed_i)
        # pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),7] = maxSpeed_i
        # pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),1] = Condition_RT
        # pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),2] = Edge_TOT_Trucks
        # pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),6] = pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),5]
        # pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),5] = pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),4]
        # pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),4] = pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),3]
        # pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),3] = Edge_TOT_Trucks_Current_Period
        # np.save(condition.PavePath,pavementConditionarrary)
        # return
        
    Network_DF_Period_0t00DF=pd.read_csv(PATH_Network_DF_Period_0t00_TEMPLATE)
    # Network_DF_Period_0t00DF.to_csv(Network_DF_Period_PATH)
    PATH_edge_1_cashe_DF=pd.read_csv(PATH_edge_i_cashe_TEMPLATE)

    def DetFuncII():#recreated 12.15.17   http://www.pavementinteractive.org/equivalent-single-axle-load/   http://www.pavementinteractive.org/loads/
        edge_ParametersDF = pd.DataFrame(edge_ParametersDF,index=['Condition_RT','Tot_Trucks','Trucks_Pi','Trucks_Pi-1','Trucks_Pi-2','Trucks_Pi-3','MaxSpeed_i_m/s','O_max_mph'])
        edge_ParametersDF.to_csv(EdgeHistoryPANDAPATH)
        edge_ParametersDF = pd.read_csv(condition.EdgeParamPANDAPATH)
        # # 0.01339 = (7040 trucks per 10 years)/(5,256,000 hours per 10 years)*10 #Slightly arbitrary but just a function
        # # Condition_RT = 100.00 - edge_ESAL_TEMP * 0.01339 used to be Tot_Trucks * 0.01339
        ##New File based on Periodhttps://www.fhwa.dot.gov/publications/research/infrastructure/pavements/13038/13038.pdf
        PERIOD_VARRIABLE = 28801
        Network_DF_Period_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + "Network_DF_Period-" + str(PERIOD_VARRIABLE) +".csv" #initalizes path address for new period piece
        Network_DF_Period_0t00DF=pd.read_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE)
        Network_DF_Period_DF = Network_DF_Period_0t00DF #0800 = 28801 seconds ##New File based on Period
        for edge_i in condition.Belmont_Ave:
            #Change Max Speed Based on ESAL_Tot
            Network_DF_Period_DF.loc[Network_DF_Period_DF['Belmont_AVEDic_ID'].str.contains(edge_i),'Total_Trucks_FutureESAL'] = edge_ESAL_TEMP
            #populate roadway parameters!!!
        
        
        
        
        
        for rd in Belmont_Ave:
            maxSpeedo = edge_ParametersDF.at['O_max_mph',str(Belmont_AVEDic[rd])]
            #print("maxSpeedo = ",maxSpeedo)
            #Condition_RTi = randint(25,100)
            Condition_RTi = edge_ParametersDF.at['Condition_RT',str(Belmont_AVEDic[rd])] #= Condition_RTi
            maxSpeed_i = 0.44704 *  (maxSpeedo - (maxSpeedo**((100-Condition_RTi)/96))+4.5675) #0.44704(km/mph)
            edge_ParametersDF.at['MaxSpeed_i_m/s',str(Belmont_AVEDic[rd])] = maxSpeed_i
    
    
    def Truck_Count_III(PERIOD_VARRIABLE): #works manually not working 
        equiv_ESAL = {'Car' : 0.0007, 'Truck' : 0.10, 'Semi' : 1.35, '40ftBus' : 1.85}
        ##New File based on Period
        #Network_DF_Period_DF = Network_DF_Period_0t00DF #0800 = 28801 seconds ##New File based on Period
        PERIOD_VARRIABLE = PERIOD_VARRIABLE
        Network_DF_Period_0t00csv=pd.read_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE)
        Network_DF_Period_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + "Network_DF_Period_" + str(PERIOD_VARRIABLE) +".csv"
        Network_DF_Period_0t00csv.to_csv(Network_DF_Period_PATH)
        Network_DF_Period_DF = pd.read_csv(Network_DF_Period_PATH)
        for edge_i in condition.Belmont_Ave[:]: ## test edge_i = "424978646" .. 73e
            while Network_DF_Period_DF.columns[0] != 'Belmont_AVEDic_ID':
                COLNAME = Network_DF_Period_DF.columns[0]
                del Network_DF_Period_DF[COLNAME]#delete the column
            #edge_i = "424978646"
            edge_cashe_LOAD_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + condition.Belmont_AVEDic[edge_i] +".csv" #initalizes path address for cashe file
            edge_i_cashe_csv = pd.read_csv(edge_cashe_LOAD_PATH) #loads cashe file in
            while edge_i_cashe_csv.columns[0] != 'Belmont_AVEDic_ID':
                COLNAME = edge_i_cashe_csv.columns[0]
                del edge_i_cashe_csv[COLNAME]#delete the column
            Car_Count_TEMP = max(edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,4],0)
            Truck_Count_TEMP = max(edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,5],0)
            Tota_TRUCKl_Count_TEMP = max(edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,5],0)
            print("Loaded Edge CasheFile...",condition.Belmont_AVEDic[edge_i],".csv","Car_Count_TEMP = ", Car_Count_TEMP, "Truck_Count_TEMP = ", Truck_Count_TEMP, "Tota_TRUCKl_Count_TEMP = ", Tota_TRUCKl_Count_TEMP)
            Edge_i_VehIDs_lastStep_j = traci.edge.getLastStepVehicleIDs(edge_i) #gets the list of vehicles on edge for the last step
            #examine list
            for vehID_k in Edge_i_VehIDs_lastStep_j: #TEST FOR NEXT STEP, DOUBLE COUNTING, REMOVE FROM LIST PROB NOT NEEDED, BUT FILE COULD GET LONG
                #print(vehID_k)
                if vehID_k in edge_i_cashe_csv['Veh_ID']:
                    print("vehID_k is already in here\tvehID_k = ",str(vehID_k))
                    continue #?
                else:
                    print("Onward")
             # ##testing vehID_k = Edge_i_VehIDs_lastStep_j[0]
                if re.search('(.*?)Car(.*?)',traci.vehicle.getTypeID(vehID_k),re.IGNORECASE) != None:
                    print("CAR!")
                    Car_Count_TEMP = Car_Count_TEMP +1
                    # print("Car_Count_TEMP = ",Car_Count_TEMP)
                    #Put Veh_ID in Column 'Veh_ID' [2], Veh_Type in column 'Type' [3], fill in 'Car_Count' [4] how do I find the next available row? 
                    edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,2] = vehID_k
                    edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,3] = traci.vehicle.getTypeID(vehID_k)
                    edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,4] = Car_Count_TEMP
                    edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,5] = Truck_Count_TEMP
                    edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,6] = max(-1, Car_Count_TEMP*equiv_ESAL['Car'])
                    #print("Car\r\n") #+ edge_i_cashe_csv)
                else:   #Update counts and ESAL Contribution based on type of trcuk ESAL equivalant loads found here http://www.pavementinteractive.org/loads/  
                ##BUT OUTDATED METHOD## New Methods http://www.pavementinteractive.org/equivalent-single-axle-load/
                # https://www.dot.state.pa.us/public/PubsForms/Publications/PUB%20242.pdf - try this out
                    Truck_Count_TEMP = Truck_Count_TEMP +1
                    # print("Truck_Count_TEMP = ",Truck_Count_TEMP)
                    #Put Veh_ID in Column 'Veh_ID' [2], Veh_Type in column 'Type' [3], fill in 'Truck_Count' [[[5]]] how do I find the next available row? 
                    edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,2] = vehID_k
                    edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,3] = traci.vehicle.getTypeID(vehID_k)
                    edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,4] = Car_Count_TEMP
                    edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,5] = Truck_Count_TEMP
                    if re.search('(.*?)Panel(.*)',traci.vehicle.getTypeID(vehID_k),re.IGNORECASE) != None:
                        edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,6] = edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,6] + equiv_ESAL['Truck']
                    elif re.search('(.*?)Single_Rear_Truck(.*)',traci.vehicle.getTypeID(vehID_k),re.IGNORECASE) != None:
                        edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,6] = edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,6] + equiv_ESAL['Truck']
                    elif re.search('(.*?)Double_Rear_Truck(.*)',traci.vehicle.getTypeID(vehID_k),re.IGNORECASE) != None:
                        edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,6] = edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,6] + equiv_ESAL['Semi']
                    elif re.search('(.*?)bus(.*)',traci.vehicle.getTypeID(vehID_k),re.IGNORECASE) != None:
                        edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,6] = edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,6] + equiv_ESAL['40ftBus']
                    else:
                        print("I Don't Know What you Are")
                    edge_ESAL_TEMP = edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,6]
                    print("edge_ESAL_TEMP = ", edge_ESAL_TEMP, "Truck_Count_TEMP = ", Truck_Count_TEMP,"Car_Count_TEMP = ", Car_Count_TEMP,"\r\nedge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1] = ",edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1])
                    # What is each truck's ESAL? ESAL is "An 18,000 pound load on a single axle with dual tires" https://www.dot.state.mn.us/stateaid/projectdelivery/pdp/pavement/esal-overview.pdf
                    # Load || Number of ESALs || 18,000 lb. single axle 1.000 || 2,000 lb. single axle 0.0003 || 30,000 lb. single axle 7.9 || 18,000 lb. tandem axle 0.109 || 40,000 lb. tandem axle 2.06 http://www.pavementinteractive.org/loads/
                Network_DF_Period_DF.loc[Network_DF_Period_DF['Belmont_AVEDic_ID'].str.contains(edge_i),'Total_Vehicles'] = Truck_Count_TEMP + Car_Count_TEMP
                Network_DF_Period_DF.loc[Network_DF_Period_DF['Belmont_AVEDic_ID'].str.contains(edge_i),'ESAL'] = edge_ESAL_TEMP
                Condition_RTi = 100.00 - edge_ESAL_TEMP * 0.01339
                Network_DF_Period_DF.loc[Network_DF_Period_DF['Belmont_AVEDic_ID'].str.contains(edge_i),'Condition_Index'] = Condition_RTi
                ### !!!!!!!!!!WHAt units are needed for this? currently Original_Max_Speed is in m/s!!!!!!!
                maxSpeedo = Network_DF_Period_DF.loc[Network_DF_Period_DF['Belmont_AVEDic_ID'].str.contains(edge_i),'Original_Max_Speed']
                maxSpeed_i = 0.44704 *  (maxSpeedo - (maxSpeedo**((100-Condition_RTi)/96))+4.5675) #0.44704(km/mph)
                Network_DF_Period_DF.to_csv(Network_DF_Period_PATH)
                New_Row_Data = pd.DataFrame([condition.Belmont_AVEDic[edge_i],edge_i,0,0,0,0,0,0,0],index=['Belmont_AVEDic_ID', 'Edge_ID', 'Veh_ID', 'Type', 'Car_Count','Truck_Count', 'ESAL_contrib', 'Emergancy_Stop', 'Accident'])
                New_Row_Data = pd.DataFrame.transpose(New_Row_Data)
                edge_i_cashe_csv = edge_i_cashe_csv.append(New_Row_Data)
            edge_i_cashe_csv.to_csv(edge_cashe_LOAD_PATH)

                
    def Make_Edge_CasheFiles():
    ## Test to make sure PATH_edge_i_cashe_TEMPLATE [C:\Sumo\runs\BelmontC_AOI_main\BelmontC_AOI-outPUT\BMAOI_C-DataFrames\Edge_i_cashe_TEMPLATE.csv] is saved as a CVS UT-8 (Comma delimited)(*.csv)
        Network_DF_Period_0t00csv=pd.read_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE)
        Network_DF_Period_0t00DF = pd.DataFrame(Network_DF_Period_0t00csv)
        edge_i_cashe_csv = pd.read_csv(condition.PATH_edge_i_cashe_TEMPLATE)
        edge_i_cashe_DF = pd.DataFrame(edge_i_cashe_csv)
        for edge_i in condition.Belmont_Ave[:]:
            #read in edge's cashe file
            edge_cashe_DF_NAME = "PATH_edge_"+condition.Belmont_AVEDic[edge_i]+"_cashe_DF" #make a new file for each edge
            print(edge_cashe_DF_NAME)
            edge_i_cashe_DF.iloc[0,0] = condition.Belmont_AVEDic[edge_i]
            edge_i_cashe_DF.iloc[0,1] = edge_i
            #Edge_i_VehIDs_lastStep_j = traci.edge.getLastStepVehicleIDs(edge_i)
            PATH_save_to_edgeCasheFILES = condition.PATH_BMAOI_edgeCasheFILES +"/"+condition.Belmont_AVEDic[edge_i]+".csv"
            edge_i_cashe_DF.to_csv(PATH_save_to_edgeCasheFILES)# Save cashe file
            
        # for edge_i in condition.Belmont_Ave[:]: #this code gives the index column a label, but it keeps creating a new column then
            # edge_cashe_LOAD_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + Belmont_AVEDic[edge_i] +".csv" #initalizes path address for cashe file
            # edge_i_cashe_csv = pd.read_csv(edge_cashe_LOAD_PATH) #loads cashe file in
            # pd.DataFrame(edge_i_cashe_csv, columns=['Index Column', 'Belmont_AVEDic_ID', 'Edge_ID', 'Veh_ID', 'Type','Car_Count', 'Truck_Count', 'ESAL_contrib', 'Emergancy_Stop', 'Accident'])
            # edge_i_cashe_csv.to_csv(edge_cashe_LOAD_PATH)
            
        # # traci.vehicle.addFull("Ben_Tracker_1","U_Tracker_Ben","TRACKER_TRUCK")
        # # traci.vehicle.addFull("Ben_Tracker_2","U_Tracker_Ben","TRACKER_TRUCK")
        # # traci.vehicle.addFull("Ben_Tracker_3","U_Tracker_Ben","TRACKER_TRUCK")
        # # traci.vehicle.addFull("Ben_Tracker_4","U_Tracker_Ben","TRACKER_TRUCK")
        # # traci.vehicle.addFull("Ben_Tracker_5","U_Tracker_Ben","TRACKER_TRUCK")
        
    def ParameterGetter():
        net = sumolib.net.readNet('C:\GitHub\PhD_Modeling\Belmont_AOI_git\Belmont_AOI-runFILES\Belmount_AOI-V5.net.xml')
        Network_DF_Period_0t00csv=pd.read_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE)
        Network_DF_Period_0t00DF = pd.DataFrame(Network_DF_Period_0t00csv)
        print(condition.Network_DF_Period_0t00DF_colDIC)
        Network_DF_Period_0t00DF_colDIC = {'Belmont_AVEDic_ID' : 0, 'Edge_ID' : 1, 'Condition_Index' : 2, 'State_of_Condition' : 3, 'Dynamic_Max_Speed' : 4, 'Total_Vehicles' : 5, 'ESAL' : 6, 'Total_Emergancy_Stops' : 7, 'Total_Accidents' : 8, 'Area' : 9, 'Roadway_Designation' : 10, 'Prority' : 11, 'Original_Max_Speed' : 12, 'Flood_Plain' : 13, 'Physical_Parameters_Others' : 14, 'Environmental_Parameters_Others' : 15}
        #edge_i = "424978646"
        edge_counter = 0
        for edge_i in condition.Belmont_Ave[:]:
            print("Edge_i = ", edge_i, "Network_DF_Period_0t00DF['Belmont_AVEDic_ID'].str.contains(edge_i).iloc[edge_counter] = ", Network_DF_Period_0t00DF['Belmont_AVEDic_ID'].str.contains(edge_i).iloc[edge_counter], "edge_counter = ",edge_counter)
            if Network_DF_Period_0t00DF['Belmont_AVEDic_ID'].str.contains(edge_i).iloc[edge_counter] == True:#.iloc[edge_counter]:
                Initial_Max_Speed = net.getEdge(edge_i).getSpeed()# 1 m/s = 2.23694 mph 
                Network_DF_Period_0t00DF.loc[Network_DF_Period_0t00DF['Belmont_AVEDic_ID'].str.contains(edge_i),'Original_Max_Speed'] = Initial_Max_Speed
                edge_i_area = 0 #calculate Area
                for lane_numb in range(len(net.getEdge(edge_i).getLanes())): # http://www.sumo.dlr.de/daily/pydoc/traci._lane.html & http://www.sumo.dlr.de/pydoc/sumolib.net.lane.html
                    lane_i = str(edge_i+"_"+str(int(lane_numb)))
                    edge_i_area = edge_i_area + traci.lane.getWidth(lane_i)*net.getEdge(edge_i).getLength() 
                Network_DF_Period_0t00DF.loc[Network_DF_Period_0t00DF['Belmont_AVEDic_ID'].str.contains(edge_i),'Area'] = edge_i_area
                Network_Prority = net.getEdge(edge_i).getPriority()
                Network_DF_Period_0t00DF.loc[Network_DF_Period_0t00DF['Belmont_AVEDic_ID'].str.contains(edge_i),'Prority'] = Network_Prority
                print("Edge: ", edge_i,"Has been parameterized")
            else:
                print("SHIT!!!!!")
            edge_counter = edge_counter + 1
            Network_DF_Period_0t00DF.to_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE)
        
        
    def DetFunc():#Clearly needs help but works in isolation 11.2
        edge_ParametersDF = pd.DataFrame(edge_ParametersDF,index=['Condition_RT','Tot_Trucks','Trucks_Pi','Trucks_Pi-1','Trucks_Pi-2','Trucks_Pi-3','MaxSpeed_i_m/s','O_max_mph'])
        edge_ParametersDF.to_csv(EdgeHistoryPANDAPATH)
        edge_ParametersDF = pd.read_csv(condition.EdgeParamPANDAPATH)
        # for rd in Belmont_Ave:
             # edge_ParametersDF[rd]['Condition_RT']=100
        for rd in Belmont_Ave:
            maxSpeedo = edge_ParametersDF.at['O_max_mph',str(Belmont_AVEDic[rd])]
            #print("maxSpeedo = ",maxSpeedo)
            #Condition_RTi = randint(25,100)
            Condition_RTi = edge_ParametersDF.at['Condition_RT',str(Belmont_AVEDic[rd])] #= Condition_RTi
            maxSpeed_i = 0.44704 *  (maxSpeedo - (maxSpeedo**((100-Condition_RTi)/96))+4.5675) #0.44704(km/mph)
            edge_ParametersDF.at['MaxSpeed_i_m/s',str(Belmont_AVEDic[rd])] = maxSpeed_i
        
    def resetPaveCondition():
        #edge_VehIDhistoryPD = pd.read_csv(condition.resetEdgeHistoryPANDAPATH)
        edge_ParametersDF = pd.read_csv(condition.resetEdgeParamPANDAPATH)

        
    def printCondition_RT():
        # Belmont_AVE = np.load(condition.StreetPath)
        # Belmont_AVE = condition.Belmont_AVE
        edge_ParametersDF = pd.read_csv(condition.EdgeParamPANDAPATH)
        # for edge_i in condition.Belmont_Ave[:]:
            # edge_i_INDEX = int(condition.Belmont_AVEDic[edge_i])
        Conditions_RT9 = edge_ParametersDF.loc[0]
        return print("Conditions_RT9 = ",Conditions_RT9)

    
    def BreakingThingZ(Edge_TOT_Trucks, edgez_i,Edge_TOT_Trucks_Current_Period):
        if int(Edge_TOT_Trucks) == 150:
            print("At Step <><"+str(traci.simulation.getCurrentTime()/1000)+"><>"+"\n\t"+"<<Edge "+str(edgez_i)+">>"+"\t"+"Total Trucks Have Reached 50. With "+str(Edge_TOT_Trucks_Current_Period)+" new trucks this step"+"\n\t"+"Changing Max Speed to 10 m/s")
            traci.edge.setMaxSpeed(str(edgez_i),10.00)
            #input("Press Enter to continue...")
        elif int(Edge_TOT_Trucks) == 250:
            print("Edge "+str(edgez_i)+"Total Trucks Have Reached 150. With "+str(Edge_TOT_Trucks_Current_Period)+" new trucks this step"+"\n\t"+"Changing Max Speed to 7 m/s")
            traci.edge.setMaxSpeed(str(edgez_i),7.00)
            #input("Press Enter to continue...")
        elif int(Edge_TOT_Trucks) == 600:
            print("Edge "+str(edgez_i)+"Total Trucks Have Reached 500. With "+str(Edge_TOT_Trucks_Current_Period)+" new trucks this step"+"\n\t"+"Changing Max Speed to 1 m/s")
            traci.edge.setMaxSpeed(str(edgez_i),1.00)
            #input("Press Enter to continue...")
        # else:
            # continue
# traci.edge.getParameter("387423966", "MAXSPEED")

print("!\n!\t!\t!Pavement Condition Controls Activated!")
# edgez_i = "-12150712#3"
# Edge_TOT_Trucks = 3000
# Edge_TOT_Trucks_Current_Period = 30
#pavementConditionarrary = np.load(condition.PavePath)
# condition.DetFunc(edgez_i, Edge_TOT_Trucks,Edge_TOT_Trucks_Current_Period)
# pavementConditionarrary = np.load(condition.PavePath)
#print("pavementConditionarrary>>\n",str(pavementConditionarrary))
#print("resetPaveCondition>>\n",condition.resetPaveCondition(),"pavementConditionarrary>>\n",str(pavementConditionarrary))

# run C:\Sumo\tools\SUMO_PYTHON\Pavement_Condition.py
### Graveyard of maybe useful things
# =-4e-07*A2^4 + 0.0001*A2^3 - 0.0181*A2^2 + 1.1821*A2 - 4.4797
# = 4E-19*$A2^4 + 5E-05*$A2^3 - 0.0128*$A2^2 + 1.079*$A2 - 4.1265
# -4E-07$A2^4 + 0.0001$A2^3 - 0.0182$A2^2 + 1.1872$A2 - 4.5214

# Belmont_AVEDic ={'-12150712#3' : 2, '-12150712#4' : 3, '-12150712#6' : 4, '-12327906#0' : 5, '-196358954#0' : 6, '-196358954#3' : 7, '-196358956#2' : 8, '-387423966' : 9, '-423956981' : 10, '-423956982' : 11, '-423965484' : 12, '-423967058#0' : 13, '-423967058#1' : 14, '-423967352' : 15, '-423967353' : 16, '-423967354' : 17, '-423967355' : 18, '-423967356' : 19, '-423967357' : 20, '-423967358#1' : 21, '-423967358#2' : 22, '-423967359#0' : 23, '-423967359#1' : 24, '-424803245' : 25, '-424803247#1' : 26, '-424824619' : 27, '-424824620' : 28, '-424824621' : 29, '-424978161' : 30, '-424978642.0' : 31, '-424978642.170' : 32, '-424978643' : 33, '-424978647#1' : 34, '-448887867' : 35, '-448887868' : 36, '-448887869' : 37, '-448887870#1' : 38, '-448887871#0' : 39, '-448887871#2' : 40, '-49940170#0' : 41, '12150712#3' : 42, '12150712#4' : 43, '12150712#5' : 44, '12327906#0' : 45, '12327906#1' : 46, '196358954#0' : 47, '196358954#1' : 48, '196358956#0' : 49, '387423966' : 50, '423956978' : 51, '423956979' : 52, '423956980' : 53, '423965484' : 54, '423967058#1' : 55, '423967352' : 56, '423967353' : 57, '423967354' : 58, '423967355' : 59, '423967356' : 60, '423967358#0' : 61, '423967358#2' : 62, '423967359#0' : 63, '423967359#1' : 64, '424803245' : 65, '424803247#0' : 66, '424824619' : 67, '424824620' : 68, '424824621' : 69, '424978639.0' : 70, '424978639.102' : 71, '424978640' : 72, '424978643' : 73, '424978644' : 74, '424978646' : 75, '448887867' : 76, '448887868' : 77, '448887869' : 78, '448887870#0' : 79, '448887871#0' : 80, '448887871#1' : 81 }

    # def DetFunc(edgez_i, Edge_TOT_Trucks,Edge_TOT_Trucks_Current_Period):
        # pavementConditionarrary = np.load(condition.PavePath)
        # #Edge_TOT_Trucks = general.Edge_TOT_Trucks
        # #edgez_i = general.edgez_i
        # #Edge_TOT_Trucks_Current_Period = general.Edge_TOT_Trucks_Current_Period
        # # Calculate ESAL per vehtype
        # #for edgez_i in condition.Belmont_AVE[:]:#check condition and change max speed
            # ### print("edgez_i = ",str(edgez_i),"\n", str(pavementConditionarrary[0,1]),"\n condition.Belmont_AVEDic[edgez_i] = ",str(condition.Belmont_AVEDic[edgez_i]),"\t pavementConditionarrary[int(edgez_i,1] should be the condition RT", str(pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),1]),"<>\n")
            # Condition_RT = 100 - Edge_TOT_Trucks * 0.01339 # 0.01339 = (7040 trucks per 10 years)/(5,256,000 hours per 10 years)*10 #Slightly arbitrary but just a function
            # pavementConditionarrary[int(edgez_i,1] = Condition_RT
            # maxSpeed_i = 0.44704 *  (maxSpeedo - (maxSpeedo^((100-Condition_RT)/96))+4.5675) #0.44704(km/mph)
            # maxSpeed_i2 = =0.44704 * ((-0.0000005*Condition_RT)^4+0.0001*Condition_RT^3-0.0184*Condition_RT^2+1.1929*Condition_RT-4.5675)
            # print("Max Speed Now", str(maxSpeed_i),"\t\tAlternative function found by excel =",str(maxSpeed_i2))
            # traci.edge.setMaxSpeed(str(edgez_i),maxSpeed_i)
            # np.save(condition.PavePath,pavementConditionarrary)
            
    
    # def linkmaxSpeed(Condition_RT, maxSpeedo):
        # pavementConditionarrary = np.load(condition.PavePath)
        # for edgez_i in Belmont_AVE[:]:#check condition and change max speed
            # ### print("edgez_i = ",str(edgez_i),"\n", str(pavementConditionarrary[0,1]),"\n condition.Belmont_AVEDic[edgez_i] = ",str(condition.Belmont_AVEDic[edgez_i]),"\t pavementConditionarrary[int(edgez_i,1] should be the condition RT", str(pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),1]),"<>\n")
            # Condition_RT = pavementConditionarrary[int(edgez_i,1]
            # maxSpeed_i = 0.44704 *  (maxSpeedo - (maxSpeedo^((100-Condition_RT)/96))+4.5675) #0.44704(km/mph)
            # maxSpeed_i2 = =0.44704 * ((-0.0000005*Condition_RT)^4+0.0001*Condition_RT^3-0.0184*Condition_RT^2+1.1929*Condition_RT-4.5675)
            # print("Max Speed Now", str(maxSpeed_i),"\t\tAlternative function found by excel =",str(maxSpeed_i2))
            # traci.edge.setMaxSpeed(str(edgez_i),maxSpeed_i)