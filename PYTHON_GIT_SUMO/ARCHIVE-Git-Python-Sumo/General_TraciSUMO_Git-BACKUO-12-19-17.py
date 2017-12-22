import os, sys
from random import *
import numpy as np
import traci
import traci.constants as tc
import re
import sumolib
import time
import Pavement_Condition as PC
import pandas as pd
#import SUMO_PYTHON._Belmont_Street
# File modified from C:\Users\Biko\Dropbox\PhD\Research\Models\SUMO\SUMO_DropBox\Belmont_Ave-Run\SUMO_Python-Belmont_OLD\Traci_Sim_Continue_V1.2.py
# C:\Sumo\tools\SUMO_PYTHON <-- folder location

class general:
    sumoBinary = "C:/Sumo/SUMO-0.31.0/sumo-0.31.0/bin/sumo-gui"
    configPATH = "C:\GitHub\PhD_Modeling\Belmont_AOI_git\Belmont_AOI-runFILES\BMAOI-TRACI.sumocfg"
    sumoCmd = [sumoBinary, "-c", configPATH, "--start"]
    path='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Traci_Output-V2_file.txt'
    NPpath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Traci_Output-V2.1_file.npy'
    Streetpath ='/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Belmont-Ave-EdgeList.npy'
    StreetDICpath = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Belmont-Ave-EdgeDIC.npy'
    EdgeVehIDHistoryPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_VehIDhistoryNP.csv'
    resetEdgeVehIDHistoryPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_VehIDhistoryNPreset.csv'
    EdgeParamPANDAPATH = '/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/edge_ParamNP.csv'
    #def __init__(self):
    Trucks_this_time_around = 0
    Edge_TOT_Trucks = 0
    Edge_TOT_Trucks_Current_Period = 0
    #If you want to reset edge_VehIDhistoryPD enter 1
    # edge_VehIDhistoryPD=np.load(NPpath)
    # Belmont_Ave = np.load(Streetpath)
    headerZ = []
    Period_Time = ()
    Period_Break_Point = 0
    Belmont_Ave=("-12150712#3","-12150712#4","-12150712#6","-12327906#0","-196358954#0","-196358954#3","-196358956#2","-387423966","-423956981","-423956982","-423965484","-423967058#0","-423967058#1","-423967352","-423967353","-423967354","-423967355","-423967356","-423967357","-423967358#1","-423967358#2","-423967359#0","-423967359#1","-424803245","-424803247#1","-424824619","-424824620","-424824621","-424978161","-424978642.0","-424978642.170","-424978643","-424978647#1","-448887867","-448887868","-448887869","-448887870#1","-448887871#0","-448887871#2","-49940170#0","12150712#3","12150712#4","12150712#5","12327906#0","12327906#1","196358954#0","196358954#1","196358956#0","387423966","423956978","423956979","423956980","423965484","423967058#1","423967352","423967353","423967354","423967355","423967356","423967358#0","423967358#2","423967359#0","423967359#1","424803245","424803247#0","424824619","424824620","424824621","424978639.0","424978639.102","424978640","424978643","424978644","424978646","448887867","448887868","448887869","448887870#0","448887871#0","448887871#1")
    
    Belmont_AVEDic ={'-12150712#3': 1, '-12150712#4': 2, '-12150712#6': 3, '-12327906#0': 4, '-196358954#0': 5, '-196358954#3': 6, '-196358956#2': 7, '-387423966': 8, '-423956981': 9, '-423956982': 10, '-423965484': 11, '-423967058#0': 12, '-423967058#1': 13, '-423967352': 14, '-423967353': 15, '-423967354': 16, '-423967355': 17, '-423967356': 18, '-423967357': 19, '-423967358#1': 20, '-423967358#2': 21, '-423967359#0': 22, '-423967359#1': 23, '-424803245': 24, '-424803247#1': 25, '-424824619': 26, '-424824620': 27, '-424824621': 28, '-424978161': 29, '-424978642.0': 30, '-424978642.170': 31, '-424978643': 32, '-424978647#1': 33, '-448887867': 34, '-448887868': 35, '-448887869': 36, '-448887870#1': 37, '-448887871#0': 38, '-448887871#2': 39, '-49940170#0': 40, '12150712#3': 41, '12150712#4': 42, '12150712#5': 43, '12327906#0': 44, '12327906#1': 45, '196358954#0': 46, '196358954#1': 47, '196358956#0': 48, '387423966': 49, '423956978': 50, '423956979': 51, '423956980': 52, '423965484': 53, '423967058#1': 54, '423967352': 55, '423967353': 56, '423967354': 57, '423967355': 58, '423967356': 59, '423967358#0': 60, '423967358#2': 61, '423967359#0': 62, '423967359#1': 63, '424803245': 64, '424803247#0': 65, '424824619': 66, '424824620': 67, '424824621': 68, '424978639.0': 69, '424978639.102': 70, '424978640': 71, '424978643': 72, '424978644': 73, '424978646': 74, '448887867': 75, '448887868': 76, '448887869': 77, '448887870#0': 78, '448887871#0': 79, '448887871#1': 80}
    
    # EdgeHistoryDIC ={'-12150712#3' : 0, '-12150712#4' : 1, '-12150712#6' : 2, '-12327906#0' : 3, '-196358954#0' : 4, '-196358954#3' : 5, '-196358956#2' : 6, '-387423966' : 7, '-423956981' : 8, '-423956982' : 9, '-423965484' : 10, '-423967058#0' : 11, '-423967058#1' : 12, '-423967352' : 13, '-423967353' : 14, '-423967354' : 15, '-423967355' : 16, '-423967356' : 17, '-423967357' : 18, '-423967358#1' : 19, '-423967358#2' : 20, '-423967359#0' : 21, '-423967359#1' : 22, '-424803245' : 23, '-424803247#1' : 24, '-424824619' : 25, '-424824620' : 26, '-424824621' : 27, '-424978161' : 28, '-424978642.0' : 29, '-424978642.170' : 30, '-424978643' : 31, '-424978647#1' : 32, '-448887867' : 33, '-448887868' : 34, '-448887869' : 35, '-448887870#1' : 36, '-448887871#0' : 37, '-448887871#2' : 38, '-49940170#0' : 39, '12150712#3' : 40, '12150712#4' : 41, '12150712#5' : 42, '12327906#0' : 43, '12327906#1' : 44, '196358954#0' : 45, '196358954#1' : 46, '196358956#0' : 47, '387423966' : 48, '423956978' : 49, '423956979' : 50, '423956980' : 51, '423965484' : 52, '423967058#1' : 53, '423967352' : 54, '423967353' : 55, '423967354' : 56, '423967355' : 57, '423967356' : 58, '423967358#0' : 59, '423967358#2' : 60, '423967359#0' : 61, '423967359#1' : 62, '424803245' : 63, '424803247#0' : 64, '424824619' : 65, '424824620' : 66, '424824621' : 67, '424978639.0' : 68, '424978639.102' : 69, '424978640' : 70, '424978643' : 71, '424978644' : 72, '424978646' : 73, '448887867' : 74, '448887868' : 75, '448887869' : 76, '448887870#0' : 77, '448887871#0' : 78, '448887871#1' : 79}
    
    
    def resetEdgeArray(): #If you want to reset edge_VehIDhistoryPD enter "1"
        #import numpy as np
        print("\n\n\t\t\tRunning resetEdgeArray Function...")
        edge_VehIDhistoryPD = pd.read_csv(general.EdgeVehIDHistoryPANDAPATH)
        print("EdgeVehIDHistoryPANDAPATH = ",general.EdgeVehIDHistoryPANDAPATH,"\nCurrent Edge Arrary has a shape of ><",edge_VehIDhistoryPD.shape,"><\n")
        newRunQ = input("\n\nPress 1 to reset Edge Array for a new run...  ")
        print("\t\tYou pressed - ",newRunQ,"\n")
        ## Now what you pressed....
        if newRunQ == "1":
            PC.condition.resetPaveCondition()
            edge_VehIDhistoryPD = pd.read_csv(general.resetEdgeVehIDHistoryPANDAPATH)
            print("\t\t\t\tThanks for resetting, new shape",edge_VehIDhistoryPD.shape,"\n\n")
            print("\t\t\tPC.condition.printCondition_RT() = ",PC.condition.printCondition_RT())
        else:
            print("\t\t\t\tOK Nothing! Righty-O! Shape still",edge_VehIDhistoryPD.shape,"\n\n")
        
        ###need to just move one down to the other
    def addNewColumn(Period_Time,Start_Time,steps_TT,NPpathgiven=None):#ADD CASES
        print("\n\n\t\t\tRunning addNewColumn Function...\nPeriod Time: ",str(Period_Time))
        general.Timez(Start_Time,steps_TT)
        if NPpathgiven == None: 
            NPpath = general.NPpath #'/Users/Biko/Dropbox/PhD/Research/Models/SUMO/SUMO_DropBox/Belmont_Ave-Run/SUMO_Python-Belmont_OLD/Traci_Output-V2_file.npy'
            edge_VehIDhistoryPD = np.load(NPpath)
            print("NPpath = ",NPpath,"\nCurrent Edge Arrary has a shape of ><",edge_VehIDhistoryPD.shape,"><\n")
        else:
            NPpathgiven = NPpath
            edge_VehIDhistoryPD = np.load(NPpath)
        #Array Not Changed
        old_shapeSize = edge_VehIDhistoryPD.shape # general.edge_VehIDhistoryPD.shape
        print("Checking Array Shape..\nName=...general.edge_VehIDhistoryPD.shape\n\t...Status...",general.edge_VehIDhistoryPD.shape[1],"\n\t\t>>>ADDING Truck Column<<")
        
        edge_VehIDhistoryPD=np.insert(edge_VehIDhistoryPD,edge_VehIDhistoryPD.shape[1],str(Period_Time),axis=1)
        #print("\n <><>CHECKING<><>\nedge_VehIDhistoryPD...\n", edge_VehIDhistoryPD)
        print("Checking Array Shape..\nName=...general.edge_VehIDhistoryPD.shape\t...Status...",edge_VehIDhistoryPD.shape[1],"\n\t\t>>>ADDING Period Time Column<<\nPeriod Time: ",str(Period_Time)) # removed general. from general.edge_VehIDhistoryPD.shape
        
        edge_VehIDhistoryPD=np.insert(edge_VehIDhistoryPD,edge_VehIDhistoryPD.shape[1],"00",axis=1)
        general.edge_VehIDhistoryPD = edge_VehIDhistoryPD
        print("Checking Array Shape..\nName=...general.edge_VehIDhistoryPD.shape\t...Status...",edge_VehIDhistoryPD.shape[1])
        print("\nNew Shape size: ",edge_VehIDhistoryPD.shape,"\nOld shape Size: ",str(old_shapeSize))
        np.save(general.NPpath,edge_VehIDhistoryPD)
        
    
    def Timez(Start_Time,steps_TT):
        print("Getting new Timez...")
        if steps_TT == None:
           steps_TT = 54
        No_next_steps = int(steps_TT) #4402
        #Start_Time = str(traci.simulation.getCurrentTime()/1000)
        Period_Time=str(Start_Time) + " - " + str(int(traci.simulation.getCurrentTime()/1000+No_next_steps))
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
    def outPUT(useCase,steps_TT,Start_Time,Trucks_this_time_around):
        general.Timez(Start_Time,steps_TT,)
        #steps_TT = int(steps_TT)
        End_Time=int(traci.simulation.getCurrentTime()/1000)
        #Start_Time = int(steps_TT) + End_Time
        Elsapse_Time = End_Time - Start_Time
        print(Start_Time)
        Period_Time = str(Start_Time) + str(" - P_i")
        general.HeaderZ(useCase,Period_Time)
        headerZ = general.headerZ
        np.save(general.NPpath, edge_VehIDhistoryPD)
        print("Printing headerZ...\n",headerZ)
        np.savetxt(general.path,edge_VehIDhistoryPD,fmt='%s',header='[',newline='"]\n["',delimiter='";"',footer=']') #,header=headerZ
        #np.load(NPpath)
        print("\nThere were this many trucks on the edges, Trucks_this_time_around: ",Trucks_this_time_around,"\n"+"Total steps taken<>< ",Elsapse_Time)
        goAgain = input("\n\n >>>>>>> This part of the journey has ended. Press anything to contine?\n>>>>>>>>>Or x to EXIT\n\n>  >\t> >\t>> ")
        PC.condition.printCondition_RT()
        if goAgain == "x":
#            traci.close()
            print("\n\n^^---Journey has ended---^^\n\n") #,edge_VehIDhistoryPD,"
        else:
            #general.addNewColumn(2,Period_Time)
            general.releaseTraci(useCase="Continue")

###Run the Code####
    def releaseTraci(useCase,typeRun=None,steps_TT=None,TotTruckLevel=None,NextTimeToStop=None):
        #global edge_VehIDhistoryPD
        #global edge_VehIDhistoryNP
        global Start_Time
        edge_VehIDhistoryPD = pd.read_csv(general.EdgeVehIDHistoryPANDAPATH)
        #edge_VehIDhistoryPD = pd.DataFrame(general.EdgeVehIDHistoryPANDAPATH)
        edge_ConditionPD = pd.read_csv(general.EdgeParamPANDAPATH)
        #edge_ConditionPD = pd.DataFrame(general.EdgeParamPANDAPATH)
        Belmont_Ave = general.Belmont_Ave #np.load(general.Streetpath) <- fine don't want array
        #print("useCase =",useCase)
        if useCase == None:
           print("\t\t\t\t\t\t###STARTING####")
           useCase = input("\n\tPress 1 for a new Run:  \n") #\nPress Anything to continue...
        if useCase == "1":
            traci.start(general.sumoCmd,5454)
            traci.simulationStep()
            Start_Time = int(traci.simulation.getCurrentTime()/1000)
            general.resetEdgeArray()
            Period_Time="00"
            steps_TT="000"
            #general.addNewColumn(Period_Time,Start_Time,steps_TT)
            #addNewColumn(Period_Time,Start_Time,steps_TT,NPpathgiven=None)
            
            #global edge_VehIDhistoryPD Moved to top #does this even work
            #edge_VehIDhistoryPD = edge_VehIDhistoryPD #does this even work
            Start_Time = int(traci.simulation.getCurrentTime()/1000)
            edge_VehIDhistoryNP = pd.read_csv(general.resetEdgeVehIDHistoryPANDAPATH)
            ## checking code Broken now###
            #check12 = np.insert(edge_VehIDhistoryPD,check12.shape[1],general.edge_VehIDhistoryPD,axis=1)
            #check12 = str(edge_VehIDhistoryPD) + str(general.edge_VehIDhistoryPD)
            #print("Checking Array.....\ncheck12=... \t",check12[1])
            ### End Checking Code ###
        elif useCase == "Continue":
            print("\t\t\t\t\t!!!!!!!!!!!!!!CONTINUING!!!!!!!!!!!!!!\t\t\t")
            typeRun = "2"
            Start_Time = int(traci.simulation.getCurrentTime()/1000)
            #general.addNewColumn(Period_Time,Start_Time,steps_TT,NPpathgiven=None)
        elif useCase == "x":
            np.save(general.NPpath, general.edge_VehIDhistoryPD)
            np.save(general.EdgeHistoryPATH, edge_VehIDhistoryNP)
            #np.load(general.NPpath)
            traci.close()
        
        
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
        general.Timez(Start_Time,steps_TT,)
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
                #PC.condition.TruckCountIII()()
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
                #PC.condition.TruckCountIII()
        elif str(typeRun) == "3": # run until set truck accomulation level Var -> TotTruckLevel
            while int(general.Edge_TOT_Trucks) < 600: #runs until you find the 1st (max) total trucks that equal a number, what if it was the last (min)
                #print("step No. = ", step," out of ",No_next_steps) #Showing the steps boggy downy machiny
                traci.simulationStep()
                #step += 1 #Use with while statement
                #edge_VehIDhistoryPD = np.load(NPpath)
                ### Make this a function ####
                #PC.condition.TruckCountIII()
                steps_TT = steps_TT +1
        elif str(typeRun) == "4": #run until input time VAR -> NextTimeToStop
            print("\nCurrent Time is: ",str(traci.simulation.getCurrentTime()/1000))
            NextTimeToStop = input("\nWhen would you like to run until? ... ")
            NextTimeToStop = int(NextTimeToStop)
            while traci.simulation.getCurrentTime()/1000 < NextTimeToStop:
                traci.simulationStep()
                #PC.condition.TruckCountIII()()
                steps_TT = NextTimeToStop - Start_Time
                
        ## General Output and things after each run has done its things
        general.Timez(Start_Time,steps_TT)
        general.HeaderZ(useCase,general.Period_Time)
        print("Current Adventure run has ended.\ngeneral.headerZ = ",str(general.headerZ),"\nedge_VehIDhistoryPD =\n", edge_VehIDhistoryPD) #or upper case H in headerz for general function call
        #np.save(general.NPpath, edge_VehIDhistoryPD)
        np.save(general.EdgeVehIDHistoryPANDAPATH, edge_VehIDhistoryNP)
        #np.load(general.NPpath)
        print("Going to general.outPUT:\nuseCase: ",str(useCase),"\nedge_VehIDhistoryPD\nsteps_TT = NextTimeToStop - Start_Time = ",str(steps_TT),"\nNextTimeToStop",str(NextTimeToStop))
        general.outPUT(useCase,steps_TT,Start_Time,Trucks_this_time_around) #general.outPUT(useCase,edge_VehIDhistoryPD,steps_TT)

print("\n\n\t\t\t\tGeneral_TraciSUMO has been imported\n")
