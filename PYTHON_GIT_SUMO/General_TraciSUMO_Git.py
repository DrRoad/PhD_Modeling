import os, sys
from random import *
import numpy as np
import traci
import traci.constants as tc
import re
import sumolib
import time
import Pavement_Condition_GIT as PC
import pandas as pd
import profile
from pandas import ExcelWriter


#import SUMO_PYTHON._Belmont_Street
# File modified from C:\Users\Biko\Dropbox\PhD\Research\Models\SUMO\SUMO_DropBox\Belmont_Ave-Run\SUMO_Python-Belmont_OLD\Traci_Sim_Continue_V1.2.py
# C:\Sumo\tools\SUMO_PYTHON <-- folder location

class general:
    sumoGUIBinary = "C:/Sumo/SUMO-0.31.0/sumo-0.31.0/bin/sumo-gui"
    sumoBinary = "C:/Sumo/SUMO-0.31.0/sumo-0.31.0/bin/sumo"
    configPATH = "C:\GitHub\PhD_Modeling\Belmont_AOI_git\Belmont_AOI-runFILES\BMAOI-TRACI.sumocfg"
    sumoCmd = [sumoBinary, "-c", configPATH, "--start"]
    sumoGUICmd = [sumoGUIBinary, "-c", configPATH, "--start"]
    path='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Traci_Output-V2_file.txt'
    NPpath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Traci_Output-V2.1_file.npy'
    Streetpath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Belmont-Ave-EdgeList.npy'
    StreetDICpath = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Belmont-Ave-EdgeDIC.npy'
    EdgeVehIDHistoryPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_VehIDhistoryNP.csv'
    resetEdgeVehIDHistoryPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_VehIDhistoryNPreset.csv'
    EdgeParamPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_ParamNP.csv'
    #def __init__(self):
    # Trucks_this_time_around = 0
    # Edge_TOT_Trucks = 0
    # Edge_TOT_Trucks_Current_Period = 0
    # headerZ = []
    # Period_Time = ()
    # Period_Break_Point = 0
    Belmont_Ave=("-12150712#3","-12150712#4","-12150712#6","-12327906#0","-196358954#0","-196358954#3","-196358956#2","-387423966","-423956981","-423956982","-423965484","-423967058#0","-423967058#1","-423967352","-423967353","-423967354","-423967355","-423967356","-423967357","-423967358#1","-423967358#2","-423967359#0","-423967359#1","-424803245","-424803247#1","-424824619","-424824620","-424824621","-424978161","-424978642.0","-424978642.170","-424978643","-424978647#1","-448887867","-448887868","-448887869","-448887870#1","-448887871#0","-448887871#2","-49940170#0","12150712#3","12150712#4","12150712#5","12327906#0","12327906#1","196358954#0","196358954#1","196358956#0","387423966","423956978","423956979","423956980","423965484","423967058#1","423967352","423967353","423967354","423967355","423967356","423967358#0","423967358#2","423967359#0","423967359#1","424803245","424803247#0","424824619","424824620","424824621","424978639.0","424978639.102","424978640","424978643","424978644","424978646","448887867","448887868","448887869","448887870#0","448887871#0","448887871#1")
    
    Belmont_AVEDic ={'-12150712#3': 1, '-12150712#4': 2, '-12150712#6': 3, '-12327906#0': 4, '-196358954#0': 5, '-196358954#3': 6, '-196358956#2': 7, '-387423966': 8, '-423956981': 9, '-423956982': 10, '-423965484': 11, '-423967058#0': 12, '-423967058#1': 13, '-423967352': 14, '-423967353': 15, '-423967354': 16, '-423967355': 17, '-423967356': 18, '-423967357': 19, '-423967358#1': 20, '-423967358#2': 21, '-423967359#0': 22, '-423967359#1': 23, '-424803245': 24, '-424803247#1': 25, '-424824619': 26, '-424824620': 27, '-424824621': 28, '-424978161': 29, '-424978642.0': 30, '-424978642.170': 31, '-424978643': 32, '-424978647#1': 33, '-448887867': 34, '-448887868': 35, '-448887869': 36, '-448887870#1': 37, '-448887871#0': 38, '-448887871#2': 39, '-49940170#0': 40, '12150712#3': 41, '12150712#4': 42, '12150712#5': 43, '12327906#0': 44, '12327906#1': 45, '196358954#0': 46, '196358954#1': 47, '196358956#0': 48, '387423966': 49, '423956978': 50, '423956979': 51, '423956980': 52, '423965484': 53, '423967058#1': 54, '423967352': 55, '423967353': 56, '423967354': 57, '423967355': 58, '423967356': 59, '423967358#0': 60, '423967358#2': 61, '423967359#0': 62, '423967359#1': 63, '424803245': 64, '424803247#0': 65, '424824619': 66, '424824620': 67, '424824621': 68, '424978639.0': 69, '424978639.102': 70, '424978640': 71, '424978643': 72, '424978644': 73, '424978646': 74, '448887867': 75, '448887868': 76, '448887869': 77, '448887870#0': 78, '448887871#0': 79, '448887871#1': 80}
        
    global Start_Time
    global steps_TT
    global currentNetwork_DF_Period_PATH
    global SUMO_outPUT_PREFIX

    
    def Timez(Start_Time,steps_TT,display=0):
        if display != 0:
            print("Getting new Timez...")
            if steps_TT == None:
               steps_TT = 54
            No_next_steps = int(steps_TT) #4402
            #Start_Time = str(traci.simulation.getCurrentTime()/1000)
            Period_Time=str(Start_Time) + " - " + str(int(traci.simulation.getCurrentTime()/1000+No_next_steps))
            timeZ=(Start_Time,Period_Time,No_next_steps)
            timeZDIC={'Starting time =':Start_Time,'Ending Time=':Period_Time,'Steps Take:':No_next_steps}
            general.Period_Time = Period_Time
        return #print("Starting time =",str(Start_Time)," Ending Time=",str(Period_Time)," Steps Take: ",str(No_next_steps))# + Start_Time + timeZDIC + Period_Time
            
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
            


        # traci.vehicle.addFull("Ben_Tracker_1","U_Tracker_Ben","TRACKER_TRUCK")
        # traci.vehicle.addFull("Ben_Tracker_2","U_Tracker_Ben","TRACKER_TRUCK")
        # traci.vehicle.addFull("Ben_Tracker_3","U_Tracker_Ben","TRACKER_TRUCK")
        # traci.vehicle.addFull("Ben_Tracker_4","U_Tracker_Ben","TRACKER_TRUCK")
        # traci.vehicle.addFull("Ben_Tracker_5","U_Tracker_Ben","TRACKER_TRUCK")
        
    def addBen_Trackers():
        traci.vehicle.addFull("Ben_Tracker_1","U_Tracker_Ben","TRACKER_TRUCK")
        traci.vehicle.addFull("Ben_Tracker_2","U_Tracker_Ben","TRACKER_TRUCK")
        traci.vehicle.addFull("Ben_Tracker_3","U_Tracker_Ben","TRACKER_TRUCK")
        traci.vehicle.addFull("Ben_Tracker_4","U_Tracker_Ben","TRACKER_TRUCK")
        traci.vehicle.addFull("Ben_Tracker_5","U_Tracker_Ben","TRACKER_TRUCK")
        # <route id="U_Tracker_Ben" edges="424978646 424978639.0 424978639.102"/> FROM: C:\Users\Biko\Dropbox\PhD\Research\Models\SUMO\SUMO_DropBox\Belmont_Ave-Run\Belmont-AOI-Run_Files\Belmount_AOI-caliborators-DB-V3.2.xml

###    ###OUTPUT####  #https://docs.scipy.org/doc/numpy/reference/generated/numpy.save.html#numpy.save
    def outPUT(useCase,Start_Time,PERIOD_VARRIABLE, steps_TT):
        PC.condition.GetSimulationRunPrefix(display = 0)
        SUMO_outPUT_PREFIX = PC.condition.GetSimulationRunPrefix(display=0)[0]
        startPeriodTime = PC.condition.Network_DF_Period_Maker(PERIOD_VARRIABLE,useCase,justDisplay=1)[2]
        endPeriodTime = PC.condition.Network_DF_Period_Maker(PERIOD_VARRIABLE,useCase,justDisplay=1)[3]
        currentPeriodSheetname = str(str(SUMO_outPUT_PREFIX)+"_Period_"+str(startPeriodTime)+"_to_"+str(endPeriodTime))
        currentNetwork_DF_Period_PATH = PC.condition.Network_DF_Period_Maker(PERIOD_VARRIABLE,useCase,justDisplay = 1)[0]
        
        currentNetwork_DF_FILE = pd.read_excel(currentNetwork_DF_Period_PATH,currentPeriodSheetname)
        Trucks_this_time_around = 0 #Summing Trucks
        for edge_i in general.Belmont_Ave[:]:
            Trucks_this_time_around = Trucks_this_time_around + currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'Total_Trucks'] 
        general.Timez(Start_Time,steps_TT,display=0)
        #steps_TT = int(steps_TT)
        End_Time=int(traci.simulation.getCurrentTime()/1000)
        #Start_Time = int(steps_TT) + End_Time
        Elsapse_Time = End_Time - Start_Time
        print("\nStart_Time = ",Start_Time, "End_Time = ",End_Time, "Elsapse_Time = ",Elsapse_Time,"\n")
        #np.load(NPpath)
        print("\nThere were this many trucks on the edges, Trucks_this_time_around: broken\n"+"Total steps taken<>< ",Elsapse_Time) #",Trucks_this_time_around,"
        goAgain = input("\n\n >>>>>>> This part of the journey has ended. Press anything to contine?\n>>>>>>>>>Or x to EXIT\n\n>  >\t> >\t>> ")
        
        if goAgain == "x":
#            traci.close()
            print("\n\n^^---Journey has ended---^^\n\n") #,edge_VehIDhistoryPD,"
        else:
            #general.addNewColumn(2,Period_Time)
            general.releaseTraci(useCase="Continue")
            
    def inputPeriod_asNumber():
        global PERIOD_VARRIABLE
        while True: #http://www.101computing.net/number-only/
                try:
                    userINPUT = input("\r\n\nPress [1] to enter a user defined Period_Interval.\r\nPress anything else to continue default is seconds 3600 or 1 hour? ... ") 
                    if  userINPUT != '1':
                        PERIOD_VARRIABLE = 3600 #Default to 1 hour
                        return PERIOD_VARRIABLE, print("\n\nPERIOD_VARRIABLE = ", PERIOD_VARRIABLE,"\n")
                        break
                    else:
                        PERIOD_VARRIABLE = int(input("\nWhat would you like the Period of Collection to be default is seconds 3600 or 1 hour? ... "))
                    # while PERIOD_VARRIABLE.is_integer == False:
                        # PERIOD_VARRIABLE = input("!!!!!!!!!!!!Type ERROR\t\tPlease Enter an Integer\n\t\t\t\tWhat would you like the Period of Collection to be default is seconds 3600 or 1 hour? ... ")
                except ValueError:# as err: #https://docs.python.org/3/library/exceptions.html#BaseException 
                    print("\n!!!!!!!!!!!!Type ERROR\n\t\tPlease Enter an Integer\n\tWhat would you like the Period of Collection to be default is seconds 3600 or 1 hour? ... ")
                    continue
                else:
                    return PERIOD_VARRIABLE, print("PERIOD_VARRIABLE = ", PERIOD_VARRIABLE)
                    break

###Run the Code####
    def releaseTraci(useCase,typeRun=None,steps_TT=None,TotTruckLevel=None,NextTimeToStop=None,rideAgain = 1):
        PC.condition.GetSimulationRunPrefix(display = 1)
        global Start_Time
        global SUMO_RUN_PREFIX
        global PERIOD_VARRIABLE
        SUMO_Traci_PORT = PC.condition.GetSimulationRunPrefix(display=0)[0]
        
        # while rideAgain == 1:
            #print("useCase =",useCase)
        if useCase == None:
           print("\t\t\t\t\t\t###STARTING####")
           useCase = input("\n\tPress 1 for a new Run:  \n") #\nPress Anything to continue...
        if useCase == "1":
            GUI_01 = input("Press Zero to use GUI? (0)\n")
            portTouse = input("Confirm with: BMAOI-TRACI.sumocfg .. port in File: .."+ str(SUMO_Traci_PORT)+"\nPlease select a port\t...") # 
            if portTouse == None:
                portTouse = int(SUMO_Traci_PORT)
            print("\n\t\tTrying port ..  ",portTouse,"\n\n")
            if str(GUI_01) != "0":
                traci.start(general.sumoCmd,int(portTouse))
            else:
                traci.start(general.sumoGUICmd,int(portTouse))
            traci.simulationStep()
            Start_Time = int(traci.simulation.getCurrentTime()/1000)
            general.inputPeriod_asNumber() #new function
            PC.condition.Reset_Edge_CasheFiles()
            PC.condition.Network_DF_Period_Maker(PERIOD_VARRIABLE,useCase,justDisplay = 0)
            Period_Time="00"
            steps_TT="000"
            #general.addNewColumn(Period_Time,Start_Time,steps_TT)
            #addNewColumn(Period_Time,Start_Time,steps_TT,NPpathgiven=None)
            #global edge_VehIDhistoryPD Moved to top #does this even work
            #edge_VehIDhistoryPD = edge_VehIDhistoryPD #does this even work
            Start_Time = int(traci.simulation.getCurrentTime()/1000)

        elif useCase == "Continue":
            print("\t\t\t\t\t!!!!!!!!!!!!!!CONTINUING!!!!!!!!!!!!!!\t\t\t")
            typeRun = "4"
            Start_Time = int(traci.simulation.getCurrentTime()/1000)
            #general.addNewColumn(Period_Time,Start_Time,steps_TT,NPpathgiven=None)
        elif useCase == "x":
            PC.condition.DisplayFiles()
            #np.load(general.NPpath)
            traci.close()
        
        
        print("\nBeginning Journey Now\n\tPlease See Gui for Show\n")
        typeRun = input("\n\nPush T to Run Simulation until the end\nPush 2 to run for XXX Steps\nPush 3 to run until set truck accomulation level\nPush 4 to run until input time\nCurrent Step_Time : "+str(traci.simulation.getCurrentTime()/1000)+"\n\n\tEnter Run Type Here: ")
        print("You pressed", str(typeRun),"= typeRun")
        #Defining the Constants
        steps_TT = 0
        stepCounter = 0
        notcar=0
        general.Timez(Start_Time,steps_TT,)
        Period_Break_Point=('50','1000','2500')
        periodCounter = 0
        Sim_Step_Count = 0
        if str(typeRun) == "T": #Run Simulation unti the end
            while traci.simulation.getMinExpectedNumber() > 0:
                #print("step No. = ", step," out of ",No_next_steps) #Showing the steps boggy downy machiny
                traci.simulationStep()
                stepCounter = stepCounter +1
                steps_TT = steps_TT +1
                PC.condition.Truck_Count_III(useCase, Sim_Step_Count, PERIOD_VARRIABLE = int(PERIOD_VARRIABLE))
                periodCounter = periodCounter + 1/60
        elif str(typeRun) == "2": #run for XXX Steps VAR -> steps_TT
            #print("\nCheck Check... typeRun is: ",typeRun,"=2(?)")
            addTesterTrucks = input("\nDO you want to add some test truckers (1/0)?")
            steps_TT = input("How many steps would you like to take? ")
            #No_next_steps = int(steps_TT)
            if addTesterTrucks == "1":
                traci.simulationStep()
                general.addBen_Trackers()
            for step in range(int(steps_TT)):
                traci.simulationStep()
                PC.condition.Truck_Count_III(useCase, Sim_Step_Count, PERIOD_VARRIABLE = int(PERIOD_VARRIABLE))
        elif str(typeRun) == "3": # run until set truck accomulation level Var -> TotTruckLevel
            while int(general.Edge_TOT_Trucks) < 600: #runs until you find the 1st (max) total trucks that equal a number, what if it was the last (min)
                #print("step No. = ", step," out of ",No_next_steps) #Showing the steps boggy downy machiny
                traci.simulationStep()
                ### Make this a function ####
                PC.condition.Truck_Count_III(useCase, Sim_Step_Count, PERIOD_VARRIABLE = int(PERIOD_VARRIABLE))
                steps_TT = steps_TT +1
        elif str(typeRun) == "4": #run until input time VAR -> NextTimeToStop
            print("\nCurrent Time is: ",str(traci.simulation.getCurrentTime()/1000))
            NextTimeToStop = input("\nWhen would you like to run until? ... ")
            NextTimeToStop = int(NextTimeToStop)
            #######PERIOD_VARRIABLE = input("\nWhat would you like the Period of Collection to be default is seconds 28801 or 8:00am? ... ")
            print("\t\t\t<><>Running until time: ",NextTimeToStop,"<><>")
            while traci.simulation.getCurrentTime()/1000 < NextTimeToStop:
                ##WHAT I NEED HERE IS A WAY TO GENERATE NEW NETWORK_DFs PER PERIOD
                traci.simulationStep()
                Sim_Step_Count = Sim_Step_Count + 1
                PC.condition.Truck_Count_III(useCase, Sim_Step_Count, PERIOD_VARRIABLE = int(PERIOD_VARRIABLE))
                steps_TT = NextTimeToStop - Start_Time
                # if (steps_TT/10).is_integer:
                    # print(" steps_TT = ",steps_TT, "Sim_Step_Count = ",Sim_Step_Count)
        ## General Output and things after each run has done its things
        #Show Network files
        #print("Network_DF_Period_PATH = ",Network_DF_Period_PATH, "Network_DF_Period_DF = ", Network_DF_Period_DF)
        PC.condition.DisplayFiles(PERIOD_VARRIABLE)
        # print("\n\nThanks for riding the SUMO Traci Train. Please come back again soon\r\n$ run /GitHub/PhD_Modeling/PYTHON_GIT_SUMO/SUMO_Runner.py\n")
        # goAgain = input("\n\n >>>>>>> This part of the journey has ended. Press anything to contine?\n>>>>>>>>>Or x to EXIT\n\n>  >\t> >\t>> ")
        # if goAgain == "x":
# #            traci.close()
            # print("\n\n^^---Journey has ended---^^\n\n") #,edge_VehIDhistoryPD,"
        # else:
            # #general.addNewColumn(2,Period_Time)
            # general.releaseTraci(useCase="Continue")
        general.outPUT(useCase,Start_Time,PERIOD_VARRIABLE, steps_TT)
print("\n\n\t\t\t\tGeneral_TraciSUMO has been imported\n")
