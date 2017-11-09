import os, sys
import numpy as np
import traci
import traci.constants as tc
import re
import sumolib
import time
import SUMO_PYTHON.General_TraciSUMO



class condition:
    PavePath = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Pavement_Condition_fileV0.npy'
    OutPath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Traci_Output-V2.1_file.npy'
    StreetPath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Belmont-Ave-EdgeList.npy'
    StreetDICPath = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Belmont-Ave-EdgeDIC.npy'

    pavementConditionarrary_T0 = np.array([["Edge_ID","Condition_RT","Tot_Trucks","Trucks_Pi","Trucks_Pi-1","Trucks_Pi-2","Trucks_Pi-3","MaxSpeed_i_m/s"],["-12150712#3",100,0,0,0,0,0,29],["-12150712#4",100,0,0,0,0,0,29],["-12150712#6",100,0,0,0,0,0,29],["-12327906#0",100,0,0,0,0,0,29],["-196358954#0",100,0,0,0,0,0,29],["-196358954#3",100,0,0,0,0,0,29],["-196358956#2",100,0,0,0,0,0,29],["-387423966",100,0,0,0,0,0,29],["-423956981",100,0,0,0,0,0,29],["-423956982",100,0,0,0,0,0,29],["-423965484",100,0,0,0,0,0,29],["-423967058#0",100,0,0,0,0,0,29],["-423967058#1",100,0,0,0,0,0,29],["-423967352",100,0,0,0,0,0,29],["-423967353",100,0,0,0,0,0,29],["-423967354",100,0,0,0,0,0,29],["-423967355",100,0,0,0,0,0,29],["-423967356",100,0,0,0,0,0,29],["-423967357",100,0,0,0,0,0,29],["-423967358#1",100,0,0,0,0,0,29],["-423967358#2",100,0,0,0,0,0,29],["-423967359#0",100,0,0,0,0,0,29],["-423967359#1",100,0,0,0,0,0,29],["-424803245",100,0,0,0,0,0,29],["-424803247#1",100,0,0,0,0,0,29],["-424824619",100,0,0,0,0,0,29],["-424824620",100,0,0,0,0,0,29],["-424824621",100,0,0,0,0,0,29],["-424978161",100,0,0,0,0,0,29],["-424978642.0",100,0,0,0,0,0,29],["-424978642.170",100,0,0,0,0,0,29],["-424978643",100,0,0,0,0,0,29],["-424978647#1",100,0,0,0,0,0,29],["-448887867",100,0,0,0,0,0,29],["-448887868",100,0,0,0,0,0,29],["-448887869",100,0,0,0,0,0,29],["-448887870#1",100,0,0,0,0,0,29],["-448887871#0",100,0,0,0,0,0,29],["-448887871#2",100,0,0,0,0,0,29],["-49940170#0",100,0,0,0,0,0,29],["12150712#3",100,0,0,0,0,0,29],["12150712#4",100,0,0,0,0,0,29],["12150712#5",100,0,0,0,0,0,29],["12327906#0",100,0,0,0,0,0,29],["12327906#1",100,0,0,0,0,0,29],["196358954#0",100,0,0,0,0,0,29],["196358954#1",100,0,0,0,0,0,29],["196358956#0",100,0,0,0,0,0,29],["387423966",100,0,0,0,0,0,29],["423956978",100,0,0,0,0,0,29],["423956979",100,0,0,0,0,0,29],["423956980",100,0,0,0,0,0,29],["423965484",100,0,0,0,0,0,29],["423967058#1",100,0,0,0,0,0,29],["423967352",100,0,0,0,0,0,29],["423967353",100,0,0,0,0,0,29],["423967354",100,0,0,0,0,0,29],["423967355",100,0,0,0,0,0,29],["423967356",100,0,0,0,0,0,29],["423967358#0",100,0,0,0,0,0,29],["423967358#2",100,0,0,0,0,0,29],["423967359#0",100,0,0,0,0,0,29],["423967359#1",100,0,0,0,0,0,29],["424803245",100,0,0,0,0,0,29],["424803247#0",100,0,0,0,0,0,29],["424824619",100,0,0,0,0,0,29],["424824620",100,0,0,0,0,0,29],["424824621",100,0,0,0,0,0,29],["424978639.0",100,0,0,0,0,0,29],["424978639.102",100,0,0,0,0,0,29],["424978640",100,0,0,0,0,0,29],["424978643",100,0,0,0,0,0,29],["424978644",100,0,0,0,0,0,29],["424978646",100,0,0,0,0,0,29],["448887867",100,0,0,0,0,0,29],["448887868",100,0,0,0,0,0,29],["448887869",100,0,0,0,0,0,29],["448887870#0",100,0,0,0,0,0,29],["448887871#0",100,0,0,0,0,0,29],["448887871#1",100,0,0,0,0,0,29]])
    Belmont_AVEDic ={'Headers' : 0, '-12150712#3': 1, '-12150712#4': 2, '-12150712#6': 3, '-12327906#0': 4, '-196358954#0': 5, '-196358954#3': 6, '-196358956#2': 7, '-387423966': 8, '-423956981': 9, '-423956982': 10, '-423965484': 11, '-423967058#0': 12, '-423967058#1': 13, '-423967352': 14, '-423967353': 15, '-423967354': 16, '-423967355': 17, '-423967356': 18, '-423967357': 19, '-423967358#1': 20, '-423967358#2': 21, '-423967359#0': 22, '-423967359#1': 23, '-424803245': 24, '-424803247#1': 25, '-424824619': 26, '-424824620': 27, '-424824621': 28, '-424978161': 29, '-424978642.0': 30, '-424978642.170': 31, '-424978643': 32, '-424978647#1': 33, '-448887867': 34, '-448887868': 35, '-448887869': 36, '-448887870#1': 37, '-448887871#0': 38, '-448887871#2': 39, '-49940170#0': 40, '12150712#3': 41, '12150712#4': 42, '12150712#5': 43, '12327906#0': 44, '12327906#1': 45, '196358954#0': 46, '196358954#1': 47, '196358956#0': 48, '387423966': 49, '423956978': 50, '423956979': 51, '423956980': 52, '423965484': 53, '423967058#1': 54, '423967352': 55, '423967353': 56, '423967354': 57, '423967355': 58, '423967356': 59, '423967358#0': 60, '423967358#2': 61, '423967359#0': 62, '423967359#1': 63, '424803245': 64, '424803247#0': 65, '424824619': 66, '424824620': 67, '424824621': 68, '424978639.0': 69, '424978639.102': 70, '424978640': 71, '424978643': 72, '424978644': 73, '424978646': 74, '448887867': 75, '448887868': 76, '448887869': 77, '448887870#0': 78, '448887871#0': 79, '448887871#1': 80}
    Condition_RT_T0 = ([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    
    Belmont_AVE = np.load(StreetPath)
    
    def DetFunc(edgez_i, Edge_TOT_Trucks,Edge_TOT_Trucks_Current_Period):
        pavementConditionarrary = np.load(condition.PavePath)
            ### print("edgez_i = ",str(edgez_i),"\n", str(pavementConditionarrary[0,1]),"\n condition.Belmont_AVEDic[edgez_i] = ",str(condition.Belmont_AVEDic[edgez_i]),"\t pavementConditionarrary[int(edgez_i,1] should be the condition RT", str(pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),1]),"<>\n")
         # 0.01339 = (7040 trucks per 10 years)/(5,256,000 hours per 10 years)*10 #Slightly arbitrary but just a function
        Condition_RT = 100.00 - float(Edge_TOT_Trucks) * 0.01339
        maxSpeedo = 30.54 #traci.edge.getParameter(edgez_i, "MAXSPEED") <- Still does not work
        #print("maxSpeedo = ",maxSpeedo)
        maxSpeed_i = 0.44704 *  (maxSpeedo - (maxSpeedo**((100-Condition_RT)/96))+4.5675) #0.44704(km/mph)
        maxSpeed_i2 = 0.44704 * ((-0.0000005*int(Condition_RT))**4+0.0001*int(Condition_RT)**3-0.0184*int(Condition_RT)**2+1.1929*int(Condition_RT)-4.5675)
        #print("Max Speed Now", str(maxSpeed_i),"\t\tAlternative function found by excel =",str(maxSpeed_i2))
        #traci.edge.setMaxSpeed(str(edgez_i),maxSpeed_i)
        pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),7] = maxSpeed_i
        pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),1] = Condition_RT
        pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),2] = Edge_TOT_Trucks
        pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),6] = pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),5]
        pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),5] = pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),4]
        pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),4] = pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),3]
        pavementConditionarrary[int(condition.Belmont_AVEDic[edgez_i]),3] = Edge_TOT_Trucks_Current_Period
        np.save(condition.PavePath,pavementConditionarrary)
        return
        
    def resetPaveCondition():
        pavementConditionarrary = condition.pavementConditionarrary_T0
        np.save(condition.PavePath,pavementConditionarrary)
        
    def printCondition_RT():
        pavementConditionarrary = np.load(condition.PavePath)
        return print(pavementConditionarrary)

    
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
pavementConditionarrary = np.load(condition.PavePath)
# condition.DetFunc(edgez_i, Edge_TOT_Trucks,Edge_TOT_Trucks_Current_Period)
# pavementConditionarrary = np.load(condition.PavePath)
print("pavementConditionarrary>>\n",str(pavementConditionarrary))
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