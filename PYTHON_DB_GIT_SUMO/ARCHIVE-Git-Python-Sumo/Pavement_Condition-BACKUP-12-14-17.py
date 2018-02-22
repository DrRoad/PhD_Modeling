<<<<<<< HEAD
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
	PATH_Network_DF_Period_0t00 = '/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-DataFrames/Network_DF_Period_0i00.csv'
	PATH_edge_i_cashe_TEMPLATE = '/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-DataFrames/Edge_i_cashe_TEMPLATE.csv'
    
    #edge_parametersDF = {'1': [100,0,0,0,0,0,29,30], '2': [100,0,0,0,0,0,29,30], '3': [100,0,0,0,0,0,29,30], '4': [100,0,0,0,0,0,29,30], '5': [100,0,0,0,0,0,29,30], '6': [100,0,0,0,0,0,29,30], '7': [100,0,0,0,0,0,29,30], '8': [100,0,0,0,0,0,29,30], '9': [100,0,0,0,0,0,29,30], '10': [100,0,0,0,0,0,29,30], '11': [100,0,0,0,0,0,29,30], '12': [100,0,0,0,0,0,29,30], '13': [100,0,0,0,0,0,29,30], '14': [100,0,0,0,0,0,29,30], '15': [100,0,0,0,0,0,29,30], '16': [100,0,0,0,0,0,29,30], '17': [100,0,0,0,0,0,29,30], '18': [100,0,0,0,0,0,29,30], '19': [100,0,0,0,0,0,29,30], '20': [100,0,0,0,0,0,29,30], '21': [100,0,0,0,0,0,29,30], '22': [100,0,0,0,0,0,29,30], '23': [100,0,0,0,0,0,29,30], '24': [100,0,0,0,0,0,29,30], '25': [100,0,0,0,0,0,29,30], '26': [100,0,0,0,0,0,29,30], '27': [100,0,0,0,0,0,29,30], '28': [100,0,0,0,0,0,29,30], '29': [100,0,0,0,0,0,29,30], '30': [100,0,0,0,0,0,29,30], '31': [100,0,0,0,0,0,29,30], '32': [100,0,0,0,0,0,29,30], '33': [100,0,0,0,0,0,29,30], '34': [100,0,0,0,0,0,29,30], '35': [100,0,0,0,0,0,29,30], '36': [100,0,0,0,0,0,29,30], '37': [100,0,0,0,0,0,29,30], '38': [100,0,0,0,0,0,29,30], '39': [100,0,0,0,0,0,29,30], '40': [100,0,0,0,0,0,29,30], '41': [100,0,0,0,0,0,29,30], '42': [100,0,0,0,0,0,29,30], '43': [100,0,0,0,0,0,29,30], '44': [100,0,0,0,0,0,29,30], '45': [100,0,0,0,0,0,29,30], '46': [100,0,0,0,0,0,29,30], '47': [100,0,0,0,0,0,29,30], '48': [100,0,0,0,0,0,29,30], '49': [100,0,0,0,0,0,29,30], '50': [100,0,0,0,0,0,29,30], '51': [100,0,0,0,0,0,29,30], '52': [100,0,0,0,0,0,29,30], '53': [100,0,0,0,0,0,29,30], '54': [100,0,0,0,0,0,29,30], '55': [100,0,0,0,0,0,29,30], '56': [100,0,0,0,0,0,29,30], '57': [100,0,0,0,0,0,29,30], '58': [100,0,0,0,0,0,29,30], '59': [100,0,0,0,0,0,29,30], '60': [100,0,0,0,0,0,29,30], '61': [100,0,0,0,0,0,29,30], '62': [100,0,0,0,0,0,29,30], '63': [100,0,0,0,0,0,29,30], '64': [100,0,0,0,0,0,29,30], '65': [100,0,0,0,0,0,29,30], '66': [100,0,0,0,0,0,29,30], '67': [100,0,0,0,0,0,29,30], '68': [100,0,0,0,0,0,29,30], '69': [100,0,0,0,0,0,29,30], '70': [100,0,0,0,0,0,29,30], '71': [100,0,0,0,0,0,29,30], '72': [100,0,0,0,0,0,29,30], '73': [100,0,0,0,0,0,29,30], '74': [100,0,0,0,0,0,29,30], '75': [100,0,0,0,0,0,29,30], '76': [100,0,0,0,0,0,29,30], '77': [100,0,0,0,0,0,29,30], '78': [100,0,0,0,0,0,29,30], '79': [100,0,0,0,0,0,29,30], '80': [100,0,0,0,0,0,29,30]}     
     #edge_parametersDF = pd.DataFrame(edge_parametersDF,index=['Condition_RT','Tot_Trucks','Trucks_Pi','Trucks_Pi-1','Trucks_Pi-2','Trucks_Pi-3','MaxSpeed_i_m/s','O_max_mph'])
    #edge_parametersDF.to_csv(resetEdgeParamPANDAPATH)
    
    pavementConditionarrary_T0 = np.array([["Edge_ID","Condition_RT","Tot_Trucks","Trucks_Pi","Trucks_Pi-1","Trucks_Pi-2","Trucks_Pi-3","MaxSpeed_i_m/s"],["-12150712#3",100,0,0,0,0,0,29],["-12150712#4",100,0,0,0,0,0,29],["-12150712#6",100,0,0,0,0,0,29],["-12327906#0",100,0,0,0,0,0,29],["-196358954#0",100,0,0,0,0,0,29],["-196358954#3",100,0,0,0,0,0,29],["-196358956#2",100,0,0,0,0,0,29],["-387423966",100,0,0,0,0,0,29],["-423956981",100,0,0,0,0,0,29],["-423956982",100,0,0,0,0,0,29],["-423965484",100,0,0,0,0,0,29],["-423967058#0",100,0,0,0,0,0,29],["-423967058#1",100,0,0,0,0,0,29],["-423967352",100,0,0,0,0,0,29],["-423967353",100,0,0,0,0,0,29],["-423967354",100,0,0,0,0,0,29],["-423967355",100,0,0,0,0,0,29],["-423967356",100,0,0,0,0,0,29],["-423967357",100,0,0,0,0,0,29],["-423967358#1",100,0,0,0,0,0,29],["-423967358#2",100,0,0,0,0,0,29],["-423967359#0",100,0,0,0,0,0,29],["-423967359#1",100,0,0,0,0,0,29],["-424803245",100,0,0,0,0,0,29],["-424803247#1",100,0,0,0,0,0,29],["-424824619",100,0,0,0,0,0,29],["-424824620",100,0,0,0,0,0,29],["-424824621",100,0,0,0,0,0,29],["-424978161",100,0,0,0,0,0,29],["-424978642.0",100,0,0,0,0,0,29],["-424978642.170",100,0,0,0,0,0,29],["-424978643",100,0,0,0,0,0,29],["-424978647#1",100,0,0,0,0,0,29],["-448887867",100,0,0,0,0,0,29],["-448887868",100,0,0,0,0,0,29],["-448887869",100,0,0,0,0,0,29],["-448887870#1",100,0,0,0,0,0,29],["-448887871#0",100,0,0,0,0,0,29],["-448887871#2",100,0,0,0,0,0,29],["-49940170#0",100,0,0,0,0,0,29],["12150712#3",100,0,0,0,0,0,29],["12150712#4",100,0,0,0,0,0,29],["12150712#5",100,0,0,0,0,0,29],["12327906#0",100,0,0,0,0,0,29],["12327906#1",100,0,0,0,0,0,29],["196358954#0",100,0,0,0,0,0,29],["196358954#1",100,0,0,0,0,0,29],["196358956#0",100,0,0,0,0,0,29],["387423966",100,0,0,0,0,0,29],["423956978",100,0,0,0,0,0,29],["423956979",100,0,0,0,0,0,29],["423956980",100,0,0,0,0,0,29],["423965484",100,0,0,0,0,0,29],["423967058#1",100,0,0,0,0,0,29],["423967352",100,0,0,0,0,0,29],["423967353",100,0,0,0,0,0,29],["423967354",100,0,0,0,0,0,29],["423967355",100,0,0,0,0,0,29],["423967356",100,0,0,0,0,0,29],["423967358#0",100,0,0,0,0,0,29],["423967358#2",100,0,0,0,0,0,29],["423967359#0",100,0,0,0,0,0,29],["423967359#1",100,0,0,0,0,0,29],["424803245",100,0,0,0,0,0,29],["424803247#0",100,0,0,0,0,0,29],["424824619",100,0,0,0,0,0,29],["424824620",100,0,0,0,0,0,29],["424824621",100,0,0,0,0,0,29],["424978639.0",100,0,0,0,0,0,29],["424978639.102",100,0,0,0,0,0,29],["424978640",100,0,0,0,0,0,29],["424978643",100,0,0,0,0,0,29],["424978644",100,0,0,0,0,0,29],["424978646",100,0,0,0,0,0,29],["448887867",100,0,0,0,0,0,29],["448887868",100,0,0,0,0,0,29],["448887869",100,0,0,0,0,0,29],["448887870#0",100,0,0,0,0,0,29],["448887871#0",100,0,0,0,0,0,29],["448887871#1",100,0,0,0,0,0,29]],dtype=object)
    
    Condition_RT_T0 = ([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    
    Belmont_Ave=("-12150712#3","-12150712#4","-12150712#6","-12327906#0","-196358954#0","-196358954#3","-196358956#2","-387423966","-423956981","-423956982","-423965484","-423967058#0","-423967058#1","-423967352","-423967353","-423967354","-423967355","-423967356","-423967357","-423967358#1","-423967358#2","-423967359#0","-423967359#1","-424803245","-424803247#1","-424824619","-424824620","-424824621","-424978161","-424978642.0","-424978642.170","-424978643","-424978647#1","-448887867","-448887868","-448887869","-448887870#1","-448887871#0","-448887871#2","-49940170#0","12150712#3","12150712#4","12150712#5","12327906#0","12327906#1","196358954#0","196358954#1","196358956#0","387423966","423956978","423956979","423956980","423965484","423967058#1","423967352","423967353","423967354","423967355","423967356","423967358#0","423967358#2","423967359#0","423967359#1","424803245","424803247#0","424824619","424824620","424824621","424978639.0","424978639.102","424978640","424978643","424978644","424978646","448887867","448887868","448887869","448887870#0","448887871#0","448887871#1")
    
    Belmont_AVEDic ={'-12150712#3': 1, '-12150712#4': 2, '-12150712#6': 3, '-12327906#0': 4, '-196358954#0': 5, '-196358954#3': 6, '-196358956#2': 7, '-387423966': 8, '-423956981': 9, '-423956982': 10, '-423965484': 11, '-423967058#0': 12, '-423967058#1': 13, '-423967352': 14, '-423967353': 15, '-423967354': 16, '-423967355': 17, '-423967356': 18, '-423967357': 19, '-423967358#1': 20, '-423967358#2': 21, '-423967359#0': 22, '-423967359#1': 23, '-424803245': 24, '-424803247#1': 25, '-424824619': 26, '-424824620': 27, '-424824621': 28, '-424978161': 29, '-424978642.0': 30, '-424978642.170': 31, '-424978643': 32, '-424978647#1': 33, '-448887867': 34, '-448887868': 35, '-448887869': 36, '-448887870#1': 37, '-448887871#0': 38, '-448887871#2': 39, '-49940170#0': 40, '12150712#3': 41, '12150712#4': 42, '12150712#5': 43, '12327906#0': 44, '12327906#1': 45, '196358954#0': 46, '196358954#1': 47, '196358956#0': 48, '387423966': 49, '423956978': 50, '423956979': 51, '423956980': 52, '423965484': 53, '423967058#1': 54, '423967352': 55, '423967353': 56, '423967354': 57, '423967355': 58, '423967356': 59, '423967358#0': 60, '423967358#2': 61, '423967359#0': 62, '423967359#1': 63, '424803245': 64, '424803247#0': 65, '424824619': 66, '424824620': 67, '424824621': 68, '424978639.0': 69, '424978639.102': 70, '424978640': 71, '424978643': 72, '424978644': 73, '424978646': 74, '448887867': 75, '448887868': 76, '448887869': 77, '448887870#0': 78, '448887871#0': 79, '448887871#1': 80}
       
    Belmont_AVE = np.load(StreetPath)
    
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
		
Network_DF_Period_0t00DF=pd.read_csv(PATH_Network_DF_Period_0t00)


        
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
=======
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
	PATH_Network_DF_Period_0t00 = '/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-DataFrames/Network_DF_Period_0i00.csv'
	PATH_edge_i_cashe_TEMPLATE = '/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-DataFrames/Edge_i_cashe_TEMPLATE.csv'
    
    #edge_parametersDF = {'1': [100,0,0,0,0,0,29,30], '2': [100,0,0,0,0,0,29,30], '3': [100,0,0,0,0,0,29,30], '4': [100,0,0,0,0,0,29,30], '5': [100,0,0,0,0,0,29,30], '6': [100,0,0,0,0,0,29,30], '7': [100,0,0,0,0,0,29,30], '8': [100,0,0,0,0,0,29,30], '9': [100,0,0,0,0,0,29,30], '10': [100,0,0,0,0,0,29,30], '11': [100,0,0,0,0,0,29,30], '12': [100,0,0,0,0,0,29,30], '13': [100,0,0,0,0,0,29,30], '14': [100,0,0,0,0,0,29,30], '15': [100,0,0,0,0,0,29,30], '16': [100,0,0,0,0,0,29,30], '17': [100,0,0,0,0,0,29,30], '18': [100,0,0,0,0,0,29,30], '19': [100,0,0,0,0,0,29,30], '20': [100,0,0,0,0,0,29,30], '21': [100,0,0,0,0,0,29,30], '22': [100,0,0,0,0,0,29,30], '23': [100,0,0,0,0,0,29,30], '24': [100,0,0,0,0,0,29,30], '25': [100,0,0,0,0,0,29,30], '26': [100,0,0,0,0,0,29,30], '27': [100,0,0,0,0,0,29,30], '28': [100,0,0,0,0,0,29,30], '29': [100,0,0,0,0,0,29,30], '30': [100,0,0,0,0,0,29,30], '31': [100,0,0,0,0,0,29,30], '32': [100,0,0,0,0,0,29,30], '33': [100,0,0,0,0,0,29,30], '34': [100,0,0,0,0,0,29,30], '35': [100,0,0,0,0,0,29,30], '36': [100,0,0,0,0,0,29,30], '37': [100,0,0,0,0,0,29,30], '38': [100,0,0,0,0,0,29,30], '39': [100,0,0,0,0,0,29,30], '40': [100,0,0,0,0,0,29,30], '41': [100,0,0,0,0,0,29,30], '42': [100,0,0,0,0,0,29,30], '43': [100,0,0,0,0,0,29,30], '44': [100,0,0,0,0,0,29,30], '45': [100,0,0,0,0,0,29,30], '46': [100,0,0,0,0,0,29,30], '47': [100,0,0,0,0,0,29,30], '48': [100,0,0,0,0,0,29,30], '49': [100,0,0,0,0,0,29,30], '50': [100,0,0,0,0,0,29,30], '51': [100,0,0,0,0,0,29,30], '52': [100,0,0,0,0,0,29,30], '53': [100,0,0,0,0,0,29,30], '54': [100,0,0,0,0,0,29,30], '55': [100,0,0,0,0,0,29,30], '56': [100,0,0,0,0,0,29,30], '57': [100,0,0,0,0,0,29,30], '58': [100,0,0,0,0,0,29,30], '59': [100,0,0,0,0,0,29,30], '60': [100,0,0,0,0,0,29,30], '61': [100,0,0,0,0,0,29,30], '62': [100,0,0,0,0,0,29,30], '63': [100,0,0,0,0,0,29,30], '64': [100,0,0,0,0,0,29,30], '65': [100,0,0,0,0,0,29,30], '66': [100,0,0,0,0,0,29,30], '67': [100,0,0,0,0,0,29,30], '68': [100,0,0,0,0,0,29,30], '69': [100,0,0,0,0,0,29,30], '70': [100,0,0,0,0,0,29,30], '71': [100,0,0,0,0,0,29,30], '72': [100,0,0,0,0,0,29,30], '73': [100,0,0,0,0,0,29,30], '74': [100,0,0,0,0,0,29,30], '75': [100,0,0,0,0,0,29,30], '76': [100,0,0,0,0,0,29,30], '77': [100,0,0,0,0,0,29,30], '78': [100,0,0,0,0,0,29,30], '79': [100,0,0,0,0,0,29,30], '80': [100,0,0,0,0,0,29,30]}     
     #edge_parametersDF = pd.DataFrame(edge_parametersDF,index=['Condition_RT','Tot_Trucks','Trucks_Pi','Trucks_Pi-1','Trucks_Pi-2','Trucks_Pi-3','MaxSpeed_i_m/s','O_max_mph'])
    #edge_parametersDF.to_csv(resetEdgeParamPANDAPATH)
    
    pavementConditionarrary_T0 = np.array([["Edge_ID","Condition_RT","Tot_Trucks","Trucks_Pi","Trucks_Pi-1","Trucks_Pi-2","Trucks_Pi-3","MaxSpeed_i_m/s"],["-12150712#3",100,0,0,0,0,0,29],["-12150712#4",100,0,0,0,0,0,29],["-12150712#6",100,0,0,0,0,0,29],["-12327906#0",100,0,0,0,0,0,29],["-196358954#0",100,0,0,0,0,0,29],["-196358954#3",100,0,0,0,0,0,29],["-196358956#2",100,0,0,0,0,0,29],["-387423966",100,0,0,0,0,0,29],["-423956981",100,0,0,0,0,0,29],["-423956982",100,0,0,0,0,0,29],["-423965484",100,0,0,0,0,0,29],["-423967058#0",100,0,0,0,0,0,29],["-423967058#1",100,0,0,0,0,0,29],["-423967352",100,0,0,0,0,0,29],["-423967353",100,0,0,0,0,0,29],["-423967354",100,0,0,0,0,0,29],["-423967355",100,0,0,0,0,0,29],["-423967356",100,0,0,0,0,0,29],["-423967357",100,0,0,0,0,0,29],["-423967358#1",100,0,0,0,0,0,29],["-423967358#2",100,0,0,0,0,0,29],["-423967359#0",100,0,0,0,0,0,29],["-423967359#1",100,0,0,0,0,0,29],["-424803245",100,0,0,0,0,0,29],["-424803247#1",100,0,0,0,0,0,29],["-424824619",100,0,0,0,0,0,29],["-424824620",100,0,0,0,0,0,29],["-424824621",100,0,0,0,0,0,29],["-424978161",100,0,0,0,0,0,29],["-424978642.0",100,0,0,0,0,0,29],["-424978642.170",100,0,0,0,0,0,29],["-424978643",100,0,0,0,0,0,29],["-424978647#1",100,0,0,0,0,0,29],["-448887867",100,0,0,0,0,0,29],["-448887868",100,0,0,0,0,0,29],["-448887869",100,0,0,0,0,0,29],["-448887870#1",100,0,0,0,0,0,29],["-448887871#0",100,0,0,0,0,0,29],["-448887871#2",100,0,0,0,0,0,29],["-49940170#0",100,0,0,0,0,0,29],["12150712#3",100,0,0,0,0,0,29],["12150712#4",100,0,0,0,0,0,29],["12150712#5",100,0,0,0,0,0,29],["12327906#0",100,0,0,0,0,0,29],["12327906#1",100,0,0,0,0,0,29],["196358954#0",100,0,0,0,0,0,29],["196358954#1",100,0,0,0,0,0,29],["196358956#0",100,0,0,0,0,0,29],["387423966",100,0,0,0,0,0,29],["423956978",100,0,0,0,0,0,29],["423956979",100,0,0,0,0,0,29],["423956980",100,0,0,0,0,0,29],["423965484",100,0,0,0,0,0,29],["423967058#1",100,0,0,0,0,0,29],["423967352",100,0,0,0,0,0,29],["423967353",100,0,0,0,0,0,29],["423967354",100,0,0,0,0,0,29],["423967355",100,0,0,0,0,0,29],["423967356",100,0,0,0,0,0,29],["423967358#0",100,0,0,0,0,0,29],["423967358#2",100,0,0,0,0,0,29],["423967359#0",100,0,0,0,0,0,29],["423967359#1",100,0,0,0,0,0,29],["424803245",100,0,0,0,0,0,29],["424803247#0",100,0,0,0,0,0,29],["424824619",100,0,0,0,0,0,29],["424824620",100,0,0,0,0,0,29],["424824621",100,0,0,0,0,0,29],["424978639.0",100,0,0,0,0,0,29],["424978639.102",100,0,0,0,0,0,29],["424978640",100,0,0,0,0,0,29],["424978643",100,0,0,0,0,0,29],["424978644",100,0,0,0,0,0,29],["424978646",100,0,0,0,0,0,29],["448887867",100,0,0,0,0,0,29],["448887868",100,0,0,0,0,0,29],["448887869",100,0,0,0,0,0,29],["448887870#0",100,0,0,0,0,0,29],["448887871#0",100,0,0,0,0,0,29],["448887871#1",100,0,0,0,0,0,29]],dtype=object)
    
    Condition_RT_T0 = ([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    
    Belmont_Ave=("-12150712#3","-12150712#4","-12150712#6","-12327906#0","-196358954#0","-196358954#3","-196358956#2","-387423966","-423956981","-423956982","-423965484","-423967058#0","-423967058#1","-423967352","-423967353","-423967354","-423967355","-423967356","-423967357","-423967358#1","-423967358#2","-423967359#0","-423967359#1","-424803245","-424803247#1","-424824619","-424824620","-424824621","-424978161","-424978642.0","-424978642.170","-424978643","-424978647#1","-448887867","-448887868","-448887869","-448887870#1","-448887871#0","-448887871#2","-49940170#0","12150712#3","12150712#4","12150712#5","12327906#0","12327906#1","196358954#0","196358954#1","196358956#0","387423966","423956978","423956979","423956980","423965484","423967058#1","423967352","423967353","423967354","423967355","423967356","423967358#0","423967358#2","423967359#0","423967359#1","424803245","424803247#0","424824619","424824620","424824621","424978639.0","424978639.102","424978640","424978643","424978644","424978646","448887867","448887868","448887869","448887870#0","448887871#0","448887871#1")
    
    Belmont_AVEDic ={'-12150712#3': 1, '-12150712#4': 2, '-12150712#6': 3, '-12327906#0': 4, '-196358954#0': 5, '-196358954#3': 6, '-196358956#2': 7, '-387423966': 8, '-423956981': 9, '-423956982': 10, '-423965484': 11, '-423967058#0': 12, '-423967058#1': 13, '-423967352': 14, '-423967353': 15, '-423967354': 16, '-423967355': 17, '-423967356': 18, '-423967357': 19, '-423967358#1': 20, '-423967358#2': 21, '-423967359#0': 22, '-423967359#1': 23, '-424803245': 24, '-424803247#1': 25, '-424824619': 26, '-424824620': 27, '-424824621': 28, '-424978161': 29, '-424978642.0': 30, '-424978642.170': 31, '-424978643': 32, '-424978647#1': 33, '-448887867': 34, '-448887868': 35, '-448887869': 36, '-448887870#1': 37, '-448887871#0': 38, '-448887871#2': 39, '-49940170#0': 40, '12150712#3': 41, '12150712#4': 42, '12150712#5': 43, '12327906#0': 44, '12327906#1': 45, '196358954#0': 46, '196358954#1': 47, '196358956#0': 48, '387423966': 49, '423956978': 50, '423956979': 51, '423956980': 52, '423965484': 53, '423967058#1': 54, '423967352': 55, '423967353': 56, '423967354': 57, '423967355': 58, '423967356': 59, '423967358#0': 60, '423967358#2': 61, '423967359#0': 62, '423967359#1': 63, '424803245': 64, '424803247#0': 65, '424824619': 66, '424824620': 67, '424824621': 68, '424978639.0': 69, '424978639.102': 70, '424978640': 71, '424978643': 72, '424978644': 73, '424978646': 74, '448887867': 75, '448887868': 76, '448887869': 77, '448887870#0': 78, '448887871#0': 79, '448887871#1': 80}
       
    Belmont_AVE = np.load(StreetPath)
    
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
		
Network_DF_Period_0t00DF=pd.read_csv(PATH_Network_DF_Period_0t00)


        
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
>>>>>>> 5384f079850537bd07bf47a379f46fbae5d078e0
            # traci.edge.setMaxSpeed(str(edgez_i),maxSpeed_i)