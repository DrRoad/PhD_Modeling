import os, sys
from random import *
import numpy as np
import traci
import traci.constants as tc
import re
import sumolib
import time
import SUMO_PYTHON.Pavement_Condition as PC
import pandas as pd
#import SUMO_PYTHON._Belmont_Street
# File modified from C:\Users\Biko\Dropbox\PhD\Research\Models\SUMO\SUMO_DropBox\Belmont_Ave-Run\SUMO_Python-Belmont\Traci_Sim_Continue_V1.2.py


class general:
    sumoBinary = "C:/Sumo/SUMO-0.31.0/sumo-0.31.0/bin/sumo-gui"
    configPATH = "C:/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/Belmont_Output/BM-TRACI.sumocfg"
    sumoCmd = [sumoBinary, "-c", configPATH, "--start"]
    path='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Traci_Output-V2_file.txt'
    NPpath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Traci_Output-V2.1_file.npy'
    Streetpath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Belmont-Ave-EdgeList.npy'
    StreetDICpath = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Belmont-Ave-EdgeDIC.npy'
    EdgeHistoryPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/edge_VehIDhistoryNP.npy'
    resetEdgeHistoryPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/edge_VehIDhistoryNP_RESET.npy'
    #def __init__(self):
    Trucks_this_time_around = 0
    Edge_TOT_Trucks = 0
    Edge_TOT_Trucks_Current_Period = 0
    #If you want to reset edge_based_truck_count enter 1
    # edge_based_truck_count=np.load(NPpath)
    # Belmont_Ave = np.load(Streetpath)
    headerZ = []
    Period_Time = ()
    Period_Break_Point = 0
    Belmont_Ave=("-12150712#3","-12150712#4","-12150712#6","-12327906#0","-196358954#0","-196358954#3","-196358956#2","-387423966","-423956981","-423956982","-423965484","-423967058#0","-423967058#1","-423967352","-423967353","-423967354","-423967355","-423967356","-423967357","-423967358#1","-423967358#2","-423967359#0","-423967359#1","-424803245","-424803247#1","-424824619","-424824620","-424824621","-424978161","-424978642.0","-424978642.170","-424978643","-424978647#1","-448887867","-448887868","-448887869","-448887870#1","-448887871#0","-448887871#2","-49940170#0","12150712#3","12150712#4","12150712#5","12327906#0","12327906#1","196358954#0","196358954#1","196358956#0","387423966","423956978","423956979","423956980","423965484","423967058#1","423967352","423967353","423967354","423967355","423967356","423967358#0","423967358#2","423967359#0","423967359#1","424803245","424803247#0","424824619","424824620","424824621","424978639.0","424978639.102","424978640","424978643","424978644","424978646","448887867","448887868","448887869","448887870#0","448887871#0","448887871#1")
    
    Belmont_AVEDic ={'-12150712#3': 1, '-12150712#4': 2, '-12150712#6': 3, '-12327906#0': 4, '-196358954#0': 5, '-196358954#3': 6, '-196358956#2': 7, '-387423966': 8, '-423956981': 9, '-423956982': 10, '-423965484': 11, '-423967058#0': 12, '-423967058#1': 13, '-423967352': 14, '-423967353': 15, '-423967354': 16, '-423967355': 17, '-423967356': 18, '-423967357': 19, '-423967358#1': 20, '-423967358#2': 21, '-423967359#0': 22, '-423967359#1': 23, '-424803245': 24, '-424803247#1': 25, '-424824619': 26, '-424824620': 27, '-424824621': 28, '-424978161': 29, '-424978642.0': 30, '-424978642.170': 31, '-424978643': 32, '-424978647#1': 33, '-448887867': 34, '-448887868': 35, '-448887869': 36, '-448887870#1': 37, '-448887871#0': 38, '-448887871#2': 39, '-49940170#0': 40, '12150712#3': 41, '12150712#4': 42, '12150712#5': 43, '12327906#0': 44, '12327906#1': 45, '196358954#0': 46, '196358954#1': 47, '196358956#0': 48, '387423966': 49, '423956978': 50, '423956979': 51, '423956980': 52, '423965484': 53, '423967058#1': 54, '423967352': 55, '423967353': 56, '423967354': 57, '423967355': 58, '423967356': 59, '423967358#0': 60, '423967358#2': 61, '423967359#0': 62, '423967359#1': 63, '424803245': 64, '424803247#0': 65, '424824619': 66, '424824620': 67, '424824621': 68, '424978639.0': 69, '424978639.102': 70, '424978640': 71, '424978643': 72, '424978644': 73, '424978646': 74, '448887867': 75, '448887868': 76, '448887869': 77, '448887870#0': 78, '448887871#0': 79, '448887871#1': 80}
    
    EdgeHistoryDIC ={'-12150712#3' : 0, '-12150712#4' : 1, '-12150712#6' : 2, '-12327906#0' : 3, '-196358954#0' : 4, '-196358954#3' : 5, '-196358956#2' : 6, '-387423966' : 7, '-423956981' : 8, '-423956982' : 9, '-423965484' : 10, '-423967058#0' : 11, '-423967058#1' : 12, '-423967352' : 13, '-423967353' : 14, '-423967354' : 15, '-423967355' : 16, '-423967356' : 17, '-423967357' : 18, '-423967358#1' : 19, '-423967358#2' : 20, '-423967359#0' : 21, '-423967359#1' : 22, '-424803245' : 23, '-424803247#1' : 24, '-424824619' : 25, '-424824620' : 26, '-424824621' : 27, '-424978161' : 28, '-424978642.0' : 29, '-424978642.170' : 30, '-424978643' : 31, '-424978647#1' : 32, '-448887867' : 33, '-448887868' : 34, '-448887869' : 35, '-448887870#1' : 36, '-448887871#0' : 37, '-448887871#2' : 38, '-49940170#0' : 39, '12150712#3' : 40, '12150712#4' : 41, '12150712#5' : 42, '12327906#0' : 43, '12327906#1' : 44, '196358954#0' : 45, '196358954#1' : 46, '196358956#0' : 47, '387423966' : 48, '423956978' : 49, '423956979' : 50, '423956980' : 51, '423965484' : 52, '423967058#1' : 53, '423967352' : 54, '423967353' : 55, '423967354' : 56, '423967355' : 57, '423967356' : 58, '423967358#0' : 59, '423967358#2' : 60, '423967359#0' : 61, '423967359#1' : 62, '424803245' : 63, '424803247#0' : 64, '424824619' : 65, '424824620' : 66, '424824621' : 67, '424978639.0' : 68, '424978639.102' : 69, '424978640' : 70, '424978643' : 71, '424978644' : 72, '424978646' : 73, '448887867' : 74, '448887868' : 75, '448887869' : 76, '448887870#0' : 77, '448887871#0' : 78, '448887871#1' : 79}
    
    edge_based_truck_count=np.array([["-12150712#3",0], ["-12150712#4",0], ["-12150712#6",0], ["-12327906#0",0], ["-196358954#0",0], ["-196358954#3",0], ["-196358956#2",0], ["-387423966",0], ["-423956981",0], ["-423956982",0], ["-423965484",0], ["-423967058#0",0], ["-423967058#1",0], ["-423967352",0], ["-423967353",0], ["-423967354",0], ["-423967355",0], ["-423967356",0], ["-423967357",0], ["-423967358#1",0], ["-423967358#2",0], ["-423967359#0",0], ["-423967359#1",0], ["-424803245",0], ["-424803247#1",0], ["-424824619",0], ["-424824620",0], ["-424824621",0], ["-424978161",0], ["-424978642.0",0], ["-424978642.170",0], ["-424978643",0], ["-424978647#1",0], ["-448887867",0], ["-448887868",0], ["-448887869",0], ["-448887870#1",0], ["-448887871#0",0], ["-448887871#2",0], ["-49940170#0",0], ["12150712#3",0], ["12150712#4",0], ["12150712#5",0], ["12327906#0",0], ["12327906#1",0], ["196358954#0",0], ["196358954#1",0], ["196358956#0",0], ["387423966",0], ["423956978",0], ["423956979",0], ["423956980",0], ["423965484",0], ["423967058#1",0], ["423967352",0], ["423967353",0], ["423967354",0], ["423967355",0], ["423967356",0], ["423967358#0",0], ["423967358#2",0], ["423967359#0",0], ["423967359#1",0], ["424803245",0], ["424803247#0",0], ["424824619",0], ["424824620",0], ["424824621",0], ["424978639.0",0], ["424978639.102",0], ["424978640",0], ["424978643",0], ["424978644",0], ["424978646",0], ["448887867",0], ["448887868",0], ["448887869",0], ["448887870#0",0], ["448887871#0",0], ["448887871#1",0]])
    
    edge_based_truck_count_T0=np.array([["-12150712#3",0], ["-12150712#4",0], ["-12150712#6",0], ["-12327906#0",0], ["-196358954#0",0], ["-196358954#3",0], ["-196358956#2",0], ["-387423966",0], ["-423956981",0], ["-423956982",0], ["-423965484",0], ["-423967058#0",0], ["-423967058#1",0], ["-423967352",0], ["-423967353",0], ["-423967354",0], ["-423967355",0], ["-423967356",0], ["-423967357",0], ["-423967358#1",0], ["-423967358#2",0], ["-423967359#0",0], ["-423967359#1",0], ["-424803245",0], ["-424803247#1",0], ["-424824619",0], ["-424824620",0], ["-424824621",0], ["-424978161",0], ["-424978642.0",0], ["-424978642.170",0], ["-424978643",0], ["-424978647#1",0], ["-448887867",0], ["-448887868",0], ["-448887869",0], ["-448887870#1",0], ["-448887871#0",0], ["-448887871#2",0], ["-49940170#0",0], ["12150712#3",0], ["12150712#4",0], ["12150712#5",0], ["12327906#0",0], ["12327906#1",0], ["196358954#0",0], ["196358954#1",0], ["196358956#0",0], ["387423966",0], ["423956978",0], ["423956979",0], ["423956980",0], ["423965484",0], ["423967058#1",0], ["423967352",0], ["423967353",0], ["423967354",0], ["423967355",0], ["423967356",0], ["423967358#0",0], ["423967358#2",0], ["423967359#0",0], ["423967359#1",0], ["424803245",0], ["424803247#0",0], ["424824619",0], ["424824620",0], ["424824621",0], ["424978639.0",0], ["424978639.102",0], ["424978640",0], ["424978643",0], ["424978644",0], ["424978646",0], ["448887867",0], ["448887868",0], ["448887869",0], ["448887870#0",0], ["448887871#0",0], ["448887871#1",0]])
    
    def resetEdgeArray(NPpathgiven=None): #If you want to reset edge_based_truck_count enter "1"
        #import numpy as np
        print("\n\n\t\t\tRunning resetEdgeArray Function...")
        if NPpathgiven == None:
            NPpath = general.NPpath #'/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Traci_Output-V2_file.npy'
        else:
            NPpath = NPpathgiven
        edge_based_truck_count=np.load(NPpath)
        print("NPpath = ",NPpath,"\nCurrent Edge Arrary has a shape of ><",edge_based_truck_count.shape,"><\n")
        newRunQ = input("\n\nPress 1 to reset Edge Array for a new run...  ")
        print("\t\tYou pressed - ",newRunQ,"\n")
        ## Now what you pressed....
        if newRunQ == "1":
            PC.condition.resetPaveCondition()
            edge_based_truck_count = general.edge_based_truck_count_T0
            # NPpath='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Traci_Output-V2_file.npy'
            np.save(NPpath, edge_based_truck_count)
            #print(np.load(NPpath))
            print("\t\t\t\tThanks for resetting, new shape",edge_based_truck_count.shape,"\n\n")
            print("\t\t\tPC.condition.printCondition_RT() = ",PC.condition.printCondition_RT())
        else:
            print("\t\t\t\tOK Nothing! Righty-O! Shape still",edge_based_truck_count.shape,"\n\n")
        
        
    def addNewColumn(case,Period_Time,NPpathgiven=None):#ADD CASES
        print("Running addNewColumn Function...\nPeriod Time: ",str(Period_Time))
        general.Timez()
        case = str(case)
        print("case= ", case)
        if NPpathgiven == None: 
            NPpath = general.NPpath #'/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont/Traci_Output-V2_file.npy'
            edge_based_truck_count = np.load(NPpath)
            print("NPpath = ",NPpath,"\nCurrent Edge Arrary has a shape of ><",edge_based_truck_count.shape,"><\n")
        else:
            NPpathgiven = NPpath
            edge_based_truck_count = np.load(NPpath)
        #Array Not Changed
        old_shapeSize = general.edge_based_truck_count.shape
        print("Checking Array Shape..\nName=...general.edge_based_truck_count.shape\n\t...Status...",general.edge_based_truck_count.shape[1],"\n\t\t>>>ADDING Truck Column<<")
        
        edge_based_truck_count=np.insert(edge_based_truck_count,edge_based_truck_count.shape[1],str(Period_Time),axis=1)
        #print("\n <><>CHECKING<><>\nedge_based_truck_count...\n", edge_based_truck_count)
        print("Checking Array Shape..\nName=...general.edge_based_truck_count.shape\t...Status...",general.edge_based_truck_count.shape[1],"\n\t\t>>>ADDING Period Time Column<<\nPeriod Time: ",str(Period_Time))
        
        edge_based_truck_count=np.insert(edge_based_truck_count,edge_based_truck_count.shape[1],"00",axis=1)
        general.edge_based_truck_count = edge_based_truck_count
        print("Checking Array Shape..\nName=...general.edge_based_truck_count.shape\t...Status...",general.edge_based_truck_count.shape[1])
        print("\nNew Shape size: ",general.edge_based_truck_count.shape,"\nOld shape Size: ",str(old_shapeSize))
        np.save(general.NPpath, general.edge_based_truck_count)
        
    
    def Timez(steps_TT=None):
        print("Getting new Timez...")
        if steps_TT == None:
           steps_TT = 54
        No_next_steps = steps_TT #4402
        Start_Time = str(traci.simulation.getCurrentTime()/1000)
        Period_Time=str(str(traci.simulation.getCurrentTime()/1000) + " - " + str(traci.simulation.getCurrentTime()/1000+No_next_steps))
        timeZ=(Start_Time,Period_Time,No_next_steps)
        timeZDIC={'Starting time =':Start_Time,'Ending Time=':Period_Time,'Steps Take:':No_next_steps}
        general.Period_Time = Period_Time
        return print("Starting time =",str(Start_Time)," Ending Time=",str(Period_Time)," Steps Take: ",str(No_next_steps))# + Start_Time + timeZDIC + Period_Time
        
    def HeaderZ(useCase,Period_Time):
       # headerZ=[]
        #print("Running HeaderZ Function... Use Case = ",useCase)
        #useCase = input("Press 1 for a new run")
        if useCase == 1:
            headerZ=["edge;", "TOT_Trucks"]
            #print("A New Run, A New Array!!!\n Your new headerZ >>", headerZ)
            headerZ = general.headerZ
            return print(headerZ)
        else:
            NewRunHeaders = ['Trucks_4_P_i',str(Period_Time)]
            #print("New headers being added", NewRunHeaders)
            general.headerZ.append(NewRunHeaders)
            headerZ = general.headerZ
            return print(headerZ)
            
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
            

    def CountingTrucks():
        edge_VehIDhistoryNP = np.load(general.EdgeHistoryPATH)
        Period_Break_Point = general.Period_Break_Point
        for edgez_i in general.Belmont_Ave[:]:
            edge_based_truck_count = general.edge_based_truck_count
            general.Edge_TOT_Trucks = edge_based_truck_count[int(general.Belmont_AVEDic[edgez_i])-1,1]
            general.Edge_TOT_Trucks_Current_Period = 0
            notcar=0#edge_based_truck_count[int(general.Belmont_AVEDic[edgez_i])-1,int(edge_based_truck_count.shape[1]-2)]
            for veh_id in traci.edge.getLastStepVehicleIDs(str(edgez_i))[:]:
### I want to be able to store the veh_id per edge and make sure it only counts unique ids onces
                if re.search('Car_(.*?)',str(traci.vehicle.getTypeID(str(veh_id)))) == None:
                    notcar = int(notcar) + 1
                    #print("Step Time is",str(traci.simulation.getCurrentTime()/1000),"On Edge_<><",str(edgez_i),"><> Found a truck! A duck?! No a ",str(traci.vehicle.getTypeID(str(veh_id))),"!! VAR_notcar = ",str(notcar))
                    general.Edge_TOT_Trucks = int(edge_based_truck_count[general.Belmont_AVEDic[edgez_i]-1,1])+int(notcar)
                    general.Edge_TOT_Trucks_Current_Period = notcar
                    ##Adding back to array## - !!!!!!!!
                    edge_based_truck_count[int(general.Belmont_AVEDic[edgez_i])-1,int(edge_based_truck_count.shape[1]-1)] = general.Edge_TOT_Trucks_Current_Period
                    edge_based_truck_count[int(general.Belmont_AVEDic[edgez_i])-1,1]=general.Edge_TOT_Trucks
            ##Really good level to check the count of trucks per edge per step
        # print("New Step Time is",str(traci.simulation.getCurrentTime()/1000),"Edge-><><",edgez_i," Tot-Trucks-=-",general.Edge_TOT_Trucks," Tot-Trucks-This-Period-=",general.Edge_TOT_Trucks_Current_Period)
                general.Trucks_this_time_around = int(general.Trucks_this_time_around) + int(general.Edge_TOT_Trucks_Current_Period)
            ##Simulating the breaking down of the 
            #general.BreakingThingZ(general.Edge_TOT_Trucks, edgez_i, general.Edge_TOT_Trucks_Current_Period) roads and reducing speed
            #print(traci.edge.getParameter(edgez_i, "MAXSPEED"))
            #Every Period check and update edges every 60 seconds
        Period_Break_Point = Period_Break_Point + (1/60)
        general.Period_Break_Point = Period_Break_Point
        #print("\n\tPeriod_Break_Point = ",str(Period_Break_Point))
        if int(Period_Break_Point) > 1:
            #print("\n\tPeriod_Break_Point = ",str(Period_Break_Point))
            for edgez_i in general.Belmont_Ave[:]:
                PC.condition.DetFunc(edgez_i, general.Edge_TOT_Trucks,general.Edge_TOT_Trucks_Current_Period)
            general.Period_Break_Point = 0

### CODEING IN PROGRESS
    def newTruckCount():
        Period_Break_Point = general.Period_Break_Point
        edge_VehIDhistoryNP = np.sort(np.load(general.EdgeHistoryPATH)) ## I want a reset path as well

        #print("edge_VehIDhistoryNP = ",edge_VehIDhistoryNP,"\nvehIDsinList = ",str(NOofvehIDsinList),"\n\n")
        #for edge_i in The big array that doesn't exist yet
        for edge_i in general.Belmont_Ave[:]:
            edge_based_truck_count = np.load(general.NPpath)
            Edge_i_VehIDs_lastStep_j = traci.edge.getLastStepVehicleIDs(edge_i)
            Edge_TOT_Trucks = int(edge_based_truck_count[general.Belmont_AVEDic[edge_i]-1,1])
            Edge_TOT_Trucks_Current_Period = 0
            #print(Edge_i_VehIDs_lastStep_j)
            #print("Edge_i_VehIDs_lastStep_j = ",Edge_i_VehIDs_lastStep_j)
            for vehID_k in Edge_i_VehIDs_lastStep_j:
                #print("\nvehID_k = ",str(vehID_k))
                NOofvehIDsinList = 0
                freeSpots = 0
                notcar = 0
                ##Testing below
                for spot_L in range(edge_VehIDhistoryNP.shape[1]): ## Calculating the number of IDs in the list
                    #print(spot_L)
                    #print("edge_VehIDhistoryNP[int(general.EdgeHistoryDIC[edge_i])] = ",edge_VehIDhistoryNP[int(general.EdgeHistoryDIC[edge_i])])
                    if "zblank" in edge_VehIDhistoryNP[int(general.EdgeHistoryDIC[edge_i]),spot_L]: #zblank                    
                        freeSpots = freeSpots + 1 
                        NOofvehIDsinList = int(edge_VehIDhistoryNP.shape[1]-1) - freeSpots # fristOpenSpot = NOofvehIDsinList
                         #print("freeSpots = ",freeSpots,"NOofvehIDsinList =",NOofvehIDsinList)
                        ## Call this first open spot
                    #print("\n#NOofvehIDsinList =",NOofvehIDsinList,"\n")
                ### if ID in departed list = an ID in the edge_VehIDhistoryNP, then remove the ID from edge_VehIDhistoryNP
                departedIDlist = traci.simulation.getDepartedIDList()
                for dptIDs in departedIDlist:
                    if dptIDs in edge_VehIDhistoryNP[:]:
                        np.core.defchararray.replace(edge_VehIDhistoryNP,dptIDs,"zblank")
                        edge_VehIDhistoryNP = np.sort(edge_VehIDhistoryNP)
                    #print("\ndptIDs = ",dptIDs,"\nedge_VehIDhistoryNP = \n",edge_VehIDhistoryNP)
                ### Adding vehicles to list
                if vehID_k in edge_VehIDhistoryNP[int(general.EdgeHistoryDIC[edge_i])]:
                    continue #? #print("vehID_k is already in here\tvehID_k = ",str(vehID_k))
                elif re.search('Car_(.*?)',str(traci.vehicle.getTypeID(str(vehID_k)))) == None:
                    # print("\nNew vehicle to the list...\nvehIDsinList = ",str(NOofvehIDsinList),"\nedge_VehIDhistoryNP[(NOofvehIDsinList+1)] = ",str(edge_VehIDhistoryNP[NOofvehIDsinList]))
                    # print("\vehID_k = ",str(vehID_k),"\nedge_VehIDhistoryNP[(NOofvehIDsinList+1)] = \n",str(edge_VehIDhistoryNP[(NOofvehIDsinList+1)]),"\n")
                    NOofvehIDsinList = NOofvehIDsinList +1 ## Updating the 
                    notcar = int(notcar) + 1
                    edge_VehIDhistoryNP[int(general.EdgeHistoryDIC[edge_i]),NOofvehIDsinList]= str(vehID_k) # fristOpenSpot = NOofvehIDsinList
                    Edge_TOT_Trucks = int(edge_based_truck_count[general.Belmont_AVEDic[edge_i]-1,1])+int(notcar)
                    Edge_TOT_Trucks_Current_Period = notcar
                    ##Adding back to array## - !!!!!!!!
                    edge_based_truck_count[int(general.Belmont_AVEDic[edge_i])-1,int(edge_based_truck_count.shape[1]-1)] = Edge_TOT_Trucks_Current_Period
                    edge_based_truck_count[int(general.Belmont_AVEDic[edge_i])-1,1] = Edge_TOT_Trucks
                    np.save(general.EdgeHistoryPATH,np.sort(edge_VehIDhistoryNP))
                    np.save(general.NPpath,edge_based_truck_count)
            ##Really good level to check the count of trucks per edge per step
        # print("New Step Time is",str(traci.simulation.getCurrentTime()/1000),"Edge-><><",edge_i," Tot-Trucks-=-",general.Edge_TOT_Trucks," Tot-Trucks-This-Period-=",general.Edge_TOT_Trucks_Current_Period)
                general.Trucks_this_time_around = int(general.Trucks_this_time_around) + int(general.Edge_TOT_Trucks_Current_Period)
       # print("edge_VehIDhistoryNP = ",edge_VehIDhistoryNP,"\n")
        Period_Break_Point = general.Period_Break_Point
        Period_Break_Point = Period_Break_Point + (1/60)
        general.Period_Break_Point = Period_Break_Point
        #print("\n\tPeriod_Break_Point = ",str(Period_Break_Point))
        if int(Period_Break_Point) >= 1:
            #print("\n\tPeriod_Break_Point = ",str(Period_Break_Point))
            for edgez_i in general.Belmont_Ave[:]:
                PC.condition.DetFunc(edgez_i, general.Edge_TOT_Trucks,general.Edge_TOT_Trucks_Current_Period)
            general.Period_Break_Point = 0

        # traci.vehicle.addFull("Ben_Tracker_1","U_Tracker_Ben","TRACKER_TRUCK")
        # traci.vehicle.addFull("Ben_Tracker_2","U_Tracker_Ben","TRACKER_TRUCK")
        # traci.vehicle.addFull("Ben_Tracker_3","U_Tracker_Ben","TRACKER_TRUCK")
        # traci.vehicle.addFull("Ben_Tracker_4","U_Tracker_Ben","TRACKER_TRUCK")
        # traci.vehicle.addFull("Ben_Tracker_5","U_Tracker_Ben","TRACKER_TRUCK")

   
###    ###OUTPUT####  #https://docs.scipy.org/doc/numpy/reference/generated/numpy.save.html#numpy.save
    def outPUT(useCase,edge_based_truck_count,steps_TT):
        general.Timez()
        #steps_TT = int(steps_TT)
        End_Time=int(traci.simulation.getCurrentTime()/1000)
        Start_Time = int(steps_TT) + End_Time
        Elsapse_Time = End_Time - Start_Time
        print(Start_Time)
        Period_Time = str(Start_Time) + str(" - P_i")
        #print("There were this many trucks on the edges, ",general.Trucks_this_time_around,"\n"+"Total steps taken<>< ",Elsapse_Time)
        general.HeaderZ(useCase,Period_Time)
        headerZ = general.headerZ
        np.save(general.NPpath, edge_based_truck_count)
        print("Printing headerZ...\n",headerZ)
        np.savetxt(general.path,edge_based_truck_count,fmt='%s',header='[',newline='"]\n["',delimiter='";"',footer=']') #,header=headerZ
        #np.load(NPpath)
        print("\nThere were this many trucks on the edges, general.Trucks_this_time_around: ",general.Trucks_this_time_around,"\n"+"Total steps taken<>< ",Elsapse_Time)
        goAgain = input("\n\n >>>>>>> This part of the journey has ended. Press anything to contine?\n>>>>>>>>>Or x to EXIT\n\n>  >\t> >\t>> ")
        PC.condition.printCondition_RT()
        if goAgain == "x":
#            traci.close()
            print("\n\n^^---Journey has ended---^^\n\n") #,edge_based_truck_count,"
        else:
            #general.addNewColumn(2,Period_Time)
            general.releaseTraci(useCase="Continue")

###Run the Code####
    def releaseTraci(useCase,typeRun=None,steps_TT=None,TotTruckLevel=None,NextTimeToStop=None):
        check12 = np.array([])
        edge_based_truck_count=np.load(general.NPpath)
        Belmont_Ave = general.Belmont_Ave #np.load(general.Streetpath) <- fine don't want array
        print("useCase =",useCase)
        if useCase == None:
           print("\t\t\t\t\t\t###STARTING####")
           useCase = input("\n\tPress 1 for a new Run:  \n") #\nPress Anything to continue...
        if useCase == "1":
            traci.start(general.sumoCmd,5454)
            traci.simulationStep()
            general.resetEdgeArray()
            general.addNewColumn(2,Period_Time="00")
            edge_based_truck_count=general.edge_based_truck_count
            ## checking code ###
            #check12 = np.insert(edge_based_truck_count,check12.shape[1],general.edge_based_truck_count,axis=1)
            check12 = str(edge_based_truck_count) + str(general.edge_based_truck_count)
            print("Checking Array.....\ncheck12=... \t",check12[1])
            ### End Checking Code ###
        elif useCase == "Continue":
            print("\t\t\t\t\t!!!!!!!!!!!!!!CONTINUING!!!!!!!!!!!!!!\t\t\t")
            general.addNewColumn(2,general.Period_Time)
            typeRun = "2"
        elif useCase == "x":
            np.save(general.NPpath, general.edge_based_truck_count)
            #np.load(general.NPpath)
            traci.close()
        
        Start_Time = int(traci.simulation.getCurrentTime()/1000)
        print("\nBeginning Journey Now\n\tPlease See Gui for Show\n")
        typeRun = input("\n\nPush T to Run Simulation until the end\nPush 2 to run for XXX Steps\nPush 3 to run until set truck accomulation level\nPush 4 to run until input time\nCurrent Step_Time : "+str(traci.simulation.getCurrentTime()/1000)+"\n\n\tEnter Run Type Here: ")
        print("You pressed", str(typeRun),"= typeRun")
        #Defining the Constants
        # if str(typeRun) != "T" or str(typeRun) != "2" or str(typeRun) != "3" or str(typeRun) != "4":
            # typeRun = "2"
        # if steps_TT == None:
            # steps_TT = 54
        # if TotTruckLevel == None:
            # TotTruckLevel = "666"
        # if NextTimeToStop == None:
            # NextTimeToStop = int(traci.simulation.getCurrentTime()/1000) + steps_TT
        steps_TT = 0
        stepCounter = 0
        notcar=0
        general.Timez()
        Period_Break_Point=('50','1000','2500')
        periodCounter = 0
        if str(typeRun) == "T": #Run Simulation unti the end
            while traci.simulation.getMinExpectedNumber() > 0:
                #print("step No. = ", step," out of ",No_next_steps) #Showing the steps boggy downy machiny
                traci.simulationStep()
                stepCounter = stepCounter +1
                steps_TT = steps_TT +1
                # if stepCounter == Period_Break_Point(int(periodCounter)):
                    # goOn = input("\n\t\t\t>>> Press X to exit...")
                    # if goOn == "X":
                        # break
### Make this a function ####
                ### Make this a function ####
                general.newTruckCount()
                periodCounter = periodCounter + 1
        elif str(typeRun) == "2": #run for XXX Steps VAR -> steps_TT
            #print("\nCheck Check... typeRun is: ",typeRun,"=2(?)")
            steps_TT = input("How many steps would you like to take? ")
            #No_next_steps = int(steps_TT)
            for step in range(int(steps_TT)):
                traci.simulationStep()
                ### Make this a function ####
                general.newTruckCount()
        elif str(typeRun) == "3": # run until set truck accomulation level Var -> TotTruckLevel
            while int(general.Edge_TOT_Trucks) < 600: #runs until you find the 1st (max) total trucks that equal a number, what if it was the last (min)
                #print("step No. = ", step," out of ",No_next_steps) #Showing the steps boggy downy machiny
                traci.simulationStep()
                #step += 1 #Use with while statement
                #edge_based_truck_count = np.load(NPpath)
                ### Make this a function ####
                general.newTruckCount()
                steps_TT = steps_TT +1
        elif str(typeRun) == "4": #run until input time VAR -> NextTimeToStop
            print("\nCurrent Time is: ",str(traci.simulation.getCurrentTime()/1000))
            NextTimeToStop = input("\nWhen would you like to run until? ... ")
            NextTimeToStop = int(NextTimeToStop)
            while traci.simulation.getCurrentTime()/1000 < NextTimeToStop:
                traci.simulationStep()
                general.newTruckCount()
                steps_TT = NextTimeToStop - Start_Time
                
        ## General Output and things after each run has done its things
        general.Timez()
        general.HeaderZ(useCase,general.Period_Time)
        print("Current Adventure run has ended.\ngeneral.headerZ = ",str(general.headerZ),"\nedge_based_truck_count =\n", str(edge_based_truck_count)) #or upper case H in headerz for general function call
        np.save(general.NPpath, edge_based_truck_count)
        np.load(general.NPpath)
        print("Going to general.outPUT:\nuseCase: ",str(useCase),"\nedge_based_truck_count\nsteps_TT = NextTimeToStop - Start_Time = ",str(steps_TT),"\nNextTimeToStop",str(NextTimeToStop))
        general.outPUT(useCase,edge_based_truck_count,steps_TT)
print("\n\n\t\t\t\tGeneral_TraciSUMO has been imported\n")
### For testing Purposes while running from file.
### CODEING IN PROGRESS
# traci.simulationStep()
# edge_i = "424978639.0"
# edge_i = "424978646"
# print("\nGetting the last Step's VehIDs from Edge ",edge_i,str(traci.edge.getLastStepVehicleIDs(edge_i)))

# edge_VehIDhistoryNP = np.array(["424978639.0","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank","blank"])
# edge_VehIDhistoryNP.astype('U64')
# vehIDsinList = 0
# for steps in range(60):
    # traci.simulationStep()
    # print("edge_VehIDhistoryNP = ",edge_VehIDhistoryNP,"\nvehIDsinList = ",str(vehIDsinList),"\n\n")
    # #for edge_i in The big array that doesn't exist yet
    # Edge_i_VehIDs_j = traci.edge.getLastStepVehicleIDs(edge_i)
    # print("Edge_i_VehIDs_j = ",Edge_i_VehIDs_j)
    # for vehID_j in Edge_i_VehIDs_j:
        # print("\nvehID_j = ",str(vehID_j))
        # if vehID_j in edge_VehIDhistoryNP:
            # print("vehID_j is already in here\tvehID_j = ",str(vehID_j))
        # else:
            # vehIDsinList = vehIDsinList +1
            # print("\nvehIDsinList = ",str(vehIDsinList),"\nedge_VehIDhistoryNP[0,(vehIDsinList+1)] = ",str(edge_VehIDhistoryNP[0,vehIDsinList]))
            # edge_VehIDhistoryNP[0,vehIDsinList]= str(vehIDi)
            # print("\vehIDi = ",str(vehIDi),"\nedge_VehIDhistoryNP[0,(vehIDsinList+1)] = \n",str(edge_VehIDhistoryNP[0,(vehIDsinList+1)]))
    # print("edge_VehIDhistoryNP = ",edge_VehIDhistoryNP)

# traci.vehicle.addFull("Ben_Tracker_1","U_Tracker_Ben","TRACKER_TRUCK")
# traci.vehicle.addFull("Ben_Tracker_2","U_Tracker_Ben","TRACKER_TRUCK")
# traci.vehicle.addFull("Ben_Tracker_3","U_Tracker_Ben","TRACKER_TRUCK")
# traci.vehicle.addFull("Ben_Tracker_4","U_Tracker_Ben","TRACKER_TRUCK")
# traci.vehicle.addFull("Ben_Tracker_5","U_Tracker_Ben","TRACKER_TRUCK")
    
    # addFull(self, vehID, routeID, typeID='DEFAULT_VEHTYPE', depart=None, departLane='first', departPos='base', departSpeed='0', arrivalLane='current', arrivalPos='max', arrivalSpeed='current', fromTaz='', toTaz='', line='', personCapacity=0, personNumber=0) - http://www.sumo.dlr.de/daily/pydoc/traci._vehicle.html

### End of Detour

# edgez_i='196358954#1'
# notcar = 2
# #edge_based_truck_count[int(Belmont_RDaryDic[edgez_i])-1,1]
# print("edgez_i='196358954#1' --> general.Belmont_AVEDic[edgez_i] = ",str(general.Belmont_AVEDic[edgez_i]),"\nNotcar = ",str(notcar))
# print("\ngeneral.edge_based_truck_count[general.Belmont_AVEDic[edgez_i]-1,1] = ", str(general.edge_based_truck_count[general.Belmont_AVEDic[edgez_i]-1,1]))
# print("int(notcar) = ",str(notcar))

# general.releaseTraci(None)
# print(general.edge_based_truck_count)