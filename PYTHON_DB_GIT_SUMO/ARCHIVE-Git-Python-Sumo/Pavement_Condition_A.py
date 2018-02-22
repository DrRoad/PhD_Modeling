import os, sys
import numpy as np
import traci
import traci.constants as tc
import re
import sumolib
import time
import General_TraciSUMO_A as GTS
import pandas as pd
from pandas import ExcelWriter



class condition:
    PATH_Network_DF_Period_0t00_TEMPLATE = '/Sumo/BelmontC_AOI-outPUT-dropBOX/BMAOI_C-DataFrames/Network_DF_Period_0t00_TEMPLATE.csv'
    PATH_edge_i_cashe_TEMPLATE = '/Sumo/BelmontC_AOI-outPUT-dropBOX/BMAOI_C-DataFrames/Edge_i_cashe_TEMPLATE.csv' 
    PATH_BMAOI_edgeCasheFILES = '/Sumo/BelmontC_AOI-outPUT-dropBOX/BMAOI_C-DataFrames/BMAOI_edgeCasheFILES'
    PATH_Network_DF_Period_0t00_DF = '/Sumo/BelmontC_AOI-outPUT-dropBOX/BMAOI_C-DataFrames/Network_DF_Period_0t00_DF.csv'
    
  
    Belmont_Ave=("-12150712#3", "-12150712#4", "-12150712#6", "-12327906#0", "-196358954#0", "-196358954#3", "-196358956#2", "-387423966", "-423956981", "-423956982", "-423965484", "-423967058#0", "-423967058#1", "-423967352", "-423967353", "-423967354", "-423967355", "-423967356", "-423967357", "-423967358#1", "-423967358#2", "-423967359#0", "-423967359#1", "-424803245", "-424803247#1", "-424824619", "-424824620", "-424824621", "-424978161", "-424978642.0", "-424978642.170", "-424978643", "-424978647#1", "-448887867", "-448887868", "-448887869", "-448887870#1", "-448887871#0", "-448887871#2", "-49940170#0", "12150712#3", "12150712#4", "12150712#5", "12327906#0", "12327906#1", "196358954#0", "196358954#1", "196358956#0", "387423966", "423956978", "423956979", "423956980", "423965484", "423967058#1", "423967352", "423967353", "423967354", "423967355", "423967356", "423967358#0", "423967358#2", "423967359#0", "423967359#1", "424803245", "424803247#0", "424824619", "424824620", "424824621", "424978639.0", "424978639.102", "424978640", "424978643", "424978644", "424978646", "448887867", "448887868", "448887869", "448887870#0", "448887871#0", "448887871#1")
    
    Belmont_AVEDic ={'-12150712#3' : '0e', '-12150712#4' : '1e', '-12150712#6' : '2e', '-12327906#0' : '3e', '-196358954#0' : '4e', '-196358954#3' : '5e', '-196358956#2' : '6e', '-387423966' : '7e', '-423956981' : '8e', '-423956982' : '9e', '-423965484' : '10e', '-423967058#0' : '11e', '-423967058#1' : '12e', '-423967352' : '13e', '-423967353' : '14e', '-423967354' : '15e', '-423967355' : '16e', '-423967356' : '17e', '-423967357' : '18e', '-423967358#1' : '19e', '-423967358#2' : '20e', '-423967359#0' : '21e', '-423967359#1' : '22e', '-424803245' : '23e', '-424803247#1' : '24e', '-424824619' : '25e', '-424824620' : '26e', '-424824621' : '27e', '-424978161' : '28e', '-424978642.0' : '29e', '-424978642.170' : '30e', '-424978643' : '31e', '-424978647#1' : '32e', '-448887867' : '33e', '-448887868' : '34e', '-448887869' : '35e', '-448887870#1' : '36e', '-448887871#0' : '37e', '-448887871#2' : '38e', '-49940170#0' : '39e', '12150712#3' : '40e', '12150712#4' : '41e', '12150712#5' : '42e', '12327906#0' : '43e', '12327906#1' : '44e', '196358954#0' : '45e', '196358954#1' : '46e', '196358956#0' : '47e', '387423966' : '48e', '423956978' : '49e', '423956979' : '50e', '423956980' : '51e', '423965484' : '52e', '423967058#1' : '53e', '423967352' : '54e', '423967353' : '55e', '423967354' : '56e', '423967355' : '57e', '423967356' : '58e', '423967358#0' : '59e', '423967358#2' : '60e', '423967359#0' : '61e', '423967359#1' : '62e', '424803245' : '63e', '424803247#0' : '64e', '424824619' : '65e', '424824620' : '66e', '424824621' : '67e', '424978639.0' : '68e', '424978639.102' : '69e', '424978640' : '70e', '424978643' : '71e', '424978644' : '72e', '424978646' : '73e', '448887867' : '74e', '448887868' : '75e', '448887869' : '76e', '448887870#0' : '77e', '448887871#0' : '78e', '448887871#1' : '79e'}
          
    equiv_ESAL = {'Car' : 0.0007, 'Truck' : 0.10, 'Semi' : 1.35, '40ftBus' : 1.85}
    Network_DF_Period_0t00DF_colDIC = {'Belmont_AVEDic_ID' : 0, 'Edge_ID' : 1, 'Condition_Index' : 2, 'State_of_Condition' : 3, 'Dynamic_Max_Speed' : 4, 'Total_Vehicles' : 5, 'ESAL' : 6, 'Total_Emergancy_Stops' : 7, 'Total_Accidents' : 8, 'Area' : 9, 'Roadway_Designation' : 10, 'Prority' : 11, 'Original_Max_Speed' : 12, 'Flood_Plain' : 13, 'Physical_Parameters_Others' : 14, 'Environmental_Parameters_Others' : 15}
       
    # Network_DF_Period_0t00DF=pd.read_csv(PATH_Network_DF_Period_0t00_TEMPLATE)
    # Network_DF_Period_0t00DF.to_csv(currentNetwork_DF_Period_PATH)
    # PATH_edge_1_cashe_DF=pd.read_csv(PATH_edge_i_cashe_TEMPLATE)
    global currentNetwork_DF_FILE
    global currentNetwork_DF_Period_PATH
    global currentPeriodSheetname
    global SUMO_outPUT_PREFIX
    
    
    
    def DetFuncII(PERIOD_VARRIABLE = '28801a'):#recreated 12.15.17   http://www.pavementinteractive.org/equivalent-single-axle-load/   http://www.pavementinteractive.org/loads/

        # # 0.01339 = (7040 trucks per 10 years)/(5,256,000 hours per 10 years)*10 #Slightly arbitrary but just a function
        # # Condition_RT = 100.00 - edge_ESAL_TEMP * 0.01339 used to be Tot_Trucks * 0.01339
        ##New File based on Periodhttps://www.fhwa.dot.gov/publications/research/infrastructure/pavements/13038/13038.pdf
        PERIOD_VARRIABLE = 28801
        #currentNetwork_DF_Period_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + "Network_DF_Period-" + str(PERIOD_VARRIABLE) +"_" + SUMO_outPUT_PREFIX + ".csv" #initalizes path address for new period piece
        Network_DF_Period_0t00DF=pd.read_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE)
        currentNetwork_DF_FILE = Network_DF_Period_0t00DF #0800 = 28801 seconds ##New File based on Period
        for edge_i in condition.Belmont_Ave:
            #Change Max Speed Based on ESAL_Tot
            currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'Total_Trucks_FutureESAL'] = edge_ESAL_TEMP
            Condition_RTi = 100.00 - edge_ESAL_TEMP * 0.01339 
            #populate roadway parameters!!!

        for rd in Belmont_Ave:
            maxSpeed_i = currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'Dynamic_Max_Speed']
            traci.edge.setMaxSpeed(maxSpeed_i)
            #print("maxSpeedo = ",maxSpeedo)
            #Condition_RTi = randint(25,100)
            # Condition_RTi = edge_ParametersDF.at['Condition_RT',str(Belmont_AVEDic[rd])] #= Condition_RTi
            # maxSpeed_i = 0.44704 *  (maxSpeedo - (maxSpeedo**((100-Condition_RTi)/96))+4.5675) #0.44704(km/mph)
            

    def Truck_Count_III(useCase, Sim_Step_Count, PERIOD_VARRIABLE): #works manually not working 
        global currentNetwork_DF_FILE
        global currentNetwork_DF_Period_PATH
        global currentPeriodSheetname
        condition.Network_DF_Period_Maker(PERIOD_VARRIABLE,useCase,justDisplay=1) # Does this work to initalize currentNetwork_DF_FILE & currentNetwork_DF_Period_PATH? "
        # print("Does this work to initalize currentNetwork_DF_Period_PATH?\l\n....... ", currentNetwork_DF_Period_PATH)
        equiv_ESAL = {'Car' : 0.0007, 'Truck' : 0.10, 'Semi' : 1.35, '40ftBus' : 1.85}
        #New File based on Period
        if (int(traci.simulation.getCurrentTime()/1000)/PERIOD_VARRIABLE).is_integer():
            condition.Network_DF_Period_Maker(PERIOD_VARRIABLE,useCase,justDisplay=0) ##  GENERATE NEW NETWORK_DFs PER PERIOD 
            condition.DisplayFiles(PERIOD_VARRIABLE)
            print("\r\n<>check<>currentNetwork_DF_Period_PATH = ",currentNetwork_DF_Period_PATH)
        elif str(useCase) == "1":
            # print("This is a check\r\n ... currentNetwork_DF_FILE.iloc[7]: ",currentNetwork_DF_FILE.iloc[7], "\r\n<><>currentNetwork_DF_Period_PATH = ",currentNetwork_DF_Period_PATH,"\n\n\n\n!!!<><><L><O><O><K><><A><B><O><V><E><><>!!!")
            useCase = "Continue"
        currentNetwork_DF_FILE = pd.read_excel(currentNetwork_DF_Period_PATH,currentPeriodSheetname)
        
        # if (int(traci.simulation.getCurrentTime()/1000)/10).is_integer():
            # print("\n\n\t\t<<<<Loading - Network_DF>>>>>\n currentNetwork_DF_FILE from...",currentNetwork_DF_Period_PATH,"   ",traci.simulation.getCurrentTime()/1000,"\n")
        while currentNetwork_DF_FILE.columns[0] != 'Belmont_AVEDic_ID':
            COLNAME = currentNetwork_DF_FILE.columns[0]
            del currentNetwork_DF_FILE[COLNAME]#delete the column
        for edge_i in condition.Belmont_Ave[:]: ## test edge_i = '-387423966' ... 7e || "424978646" .. 73e
            #edge_i = "424978646"
            edge_cashe_LOAD_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + condition.Belmont_AVEDic[edge_i] +".csv" #initalizes path address for cashe file
            edge_i_cashe_csv = pd.read_csv(edge_cashe_LOAD_PATH) #loads cashe file in
            # if (int(traci.simulation.getCurrentTime()/1000)/10).is_integer():
                # if condition.Belmont_AVEDic[edge_i] == "7e":
                    # print("\n\n\t\t<<<<Loading - 7e_CSV>>>>>\n 7e's edge_i_cashe_csv to...",edge_cashe_LOAD_PATH,"   ",traci.simulation.getCurrentTime()/1000,"\n")
            while edge_i_cashe_csv.columns[0] != 'Belmont_AVEDic_ID':
                COLNAME = edge_i_cashe_csv.columns[0]
                del edge_i_cashe_csv[COLNAME]#delete the column
            Car_Count_TEMP = max(edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,4],0)
            Truck_Count_TEMP = max(edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,5],0)
            Tota_TRUCKl_Count_TEMP = max(edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,5],0)
            edge_ESAL_TEMP = max(edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,6],0)
            #print("Loaded Edge CasheFile...",condition.Belmont_AVEDic[edge_i],".csv","Car_Count_TEMP = ", Car_Count_TEMP, "Truck_Count_TEMP = ", Truck_Count_TEMP, "Tota_TRUCKl_Count_TEMP = ", Tota_TRUCKl_Count_TEMP)
            Edge_i_VehIDs_lastStep_j = traci.edge.getLastStepVehicleIDs(edge_i) #gets the list of vehicles on edge for the last step
            #examine list
            for vehID_k in Edge_i_VehIDs_lastStep_j: #TEST FOR NEXT STEP, DOUBLE COUNTING, REMOVE FROM LIST PROB NOT NEEDED, BUT FILE COULD GET LONG
                # print("vehID_k = ", vehID_k, "\nedge_i_cashe_csv.Veh_ID[:] = ",edge_i_cashe_csv.Veh_ID[:]) #edge_i_cashe_csv.loc['Veh_ID'])
                #if re.search('%s',edge_i_cashe_csv['Veh_ID'],re.IGNORECASE) != None:
                if edge_i_cashe_csv['Veh_ID'].str.contains(str(vehID_k)).any() == True:
                    # print("\nvehID_k is already in here\tvehID_k = ",str(vehID_k))
                    continue #?
                else:
                    # print("Onward")
                    # ##testing vehID_k = Edge_i_VehIDs_lastStep_j[0]
                    if re.search('(.*?)Car(.*?)',traci.vehicle.getTypeID(vehID_k),re.IGNORECASE) != None:
                        #print("CAR!")
                        Car_Count_TEMP = Car_Count_TEMP +1
                        # print("Car_Count_TEMP = ",Car_Count_TEMP)
                        #Put Veh_ID in Column 'Veh_ID' [2], Veh_Type in column 'Type' [3], fill in 'Car_Count' [4] how do I find the next available row? 
                        edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,2] = vehID_k
                        edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,3] = traci.vehicle.getTypeID(vehID_k)
                        edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,4] = Car_Count_TEMP
                        edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,5] = Truck_Count_TEMP
                        edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,6] = edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-2,6] + Car_Count_TEMP*equiv_ESAL['Car']
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
                        # edge_ESAL_TEMP = edge_i_cashe_csv.iloc[edge_i_cashe_csv.shape[0]-1,6]
                        
                        # What is each truck's ESAL? ESAL is "An 18,000 pound load on a single axle with dual tires" https://www.dot.state.mn.us/stateaid/projectdelivery/pdp/pavement/esal-overview.pdf
                        # Load || Number of ESALs || 18,000 lb. single axle 1.000 || 2,000 lb. single axle 0.0003 || 30,000 lb. single axle 7.9 || 18,000 lb. tandem axle 0.109 || 40,000 lb. tandem axle 2.06 http://www.pavementinteractive.org/loads/
                        #print("\n\n<><><THIS SHOULD BE WHERE YOU UPDATE AND SAVE><><>\n\n<>")
                        currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'Total_Vehicles'] = Truck_Count_TEMP + Car_Count_TEMP
                        currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'Total_Trucks'] = Truck_Count_TEMP
                        currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'ESAL'] = edge_ESAL_TEMP
                        Condition_RTi = 100.00 - edge_ESAL_TEMP * 0.01339
                        currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'Condition_Index'] = Condition_RTi
                        maxSpeedo = currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'Original_Max_Speed']
                        maxSpeed_i =(maxSpeedo - (maxSpeedo**((100-Condition_RTi)/96))+4.5675) #Units m/s
                        currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'Dynamic_Max_Speed'] = maxSpeed_i
                        condition.excelSAVER(currentNetwork_DF_FILE,currentPeriodSheetname,)
                        # currentNetwork_DF_FILE.to_csv(currentNetwork_DF_Period_PATH)
                        # writer = ExcelWriter(str(currentNetwork_DF_Period_PATH))
                        # currentNetwork_DF_FILE.to_excel(writer, currentPeriodSheetname)
                        # writer.saver()
                    # if (int(traci.simulation.getCurrentTime()/1000)/10).is_integer():
                        # print("\n\n\t\t<<<<Saving - Network_DF>>>>>\n currentNetwork_DF_FILE to...",currentNetwork_DF_Period_PATH,"   ",traci.simulation.getCurrentTime()/1000,"\n")
                    New_Row_Data = pd.DataFrame([condition.Belmont_AVEDic[edge_i],edge_i,0,0,0,0,0,0,0],index=['Belmont_AVEDic_ID', 'Edge_ID', 'Veh_ID', 'Type', 'Car_Count','Truck_Count', 'ESAL_contrib', 'Emergancy_Stop', 'Accident'])
                    New_Row_Data = pd.DataFrame.transpose(New_Row_Data)
                    edge_i_cashe_csv = edge_i_cashe_csv.append(New_Row_Data)
                    edge_i_cashe_csv.to_csv(edge_cashe_LOAD_PATH)
                    # if (int(traci.simulation.getCurrentTime()/1000)/10).is_integer():
                        # if condition.Belmont_AVEDic[edge_i] == "7e":
                            # print("\n\n\t\t<<<<Saving - 7e_CSV>>>>>\n 7e's edge_i_cashe_csv to...",edge_cashe_LOAD_PATH,"   ",traci.simulation.getCurrentTime()/1000,"\n")
        return #currentNetwork_DF_Period_PATH, currentNetwork_DF_FILE #, print("currentNetwork_DF_Period_PATH = ", currentNetwork_DF_Period_PATH) # "\r\ncurrentNetwork_DF_FILE = ", currentNetwork_DF_FILE.iloc[0:4])
        
        
    
        
    def Network_DF_Period_Maker(PERIOD_VARRIABLE,useCase,justDisplay): # = 3600): 12.20 Added justDisplay as a potentail for using this function to control all Network_Period_DF_Files and Paths
    # make just one workbook each run and new sheets per period https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html https://stackoverflow.com/questions/29459461/pandas-dataframe-to-excel-sheet http://xlsxwriter.readthedocs.io/example_pandas_header_format.html
        #edge_i = "424978646"
        global currentNetwork_DF_Period_PATH 
        global currentNetwork_DF_FILE
        global currentPeriodSheetname 
        global startPeriodTime
        global endPeriodTime
        condition.GetSimulationRunPrefix(display = 0)
        GTS.general.Timez(Start_Time=1,steps_TT=0,display=0)
        ### currentNetwork_DF_FILE = pd.read_excel(open(currentNetwork_DF_Period_PATH,'rb'), currentPeriodSheetname=currentPeriodSheetname)

        if justDisplay != 1:
            print("\n\n!!!!Network_DF_Period_Maker() running!!!\n\nuseCase = ",useCase, "int(traci.simulation.getCurrentTime()/1000)/3600) = ", int((traci.simulation.getCurrentTime()/1000)/3600))
            if (int(traci.simulation.getCurrentTime()/1000)/3600).is_integer(): #test to see if it is a whole number which would require a new periodFILE
                print("\n\n....\t...\t..\t.\t<<!>><<>>OLD Period<<>><<!>>\r\nperiodFILE = ",currentNetwork_DF_Period_PATH,"\n",currentNetwork_DF_FILE.iloc[7],"\n")
                startPeriodTime = int(traci.simulation.getCurrentTime()/1000)
                endPeriodTime = startPeriodTime + PERIOD_VARRIABLE
                condition.GetSimulationRunPrefix(display = 0)
                print("startPeriodTime = ",startPeriodTime, "endPeriodTime = ",endPeriodTime)
                # currentNetwork_DF_Period_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + "Network_DF_" + SUMO_outPUT_PREFIX + "_periodFILE_" + str(startPeriodTime) + "_to_" + str(endPeriodTime) + ".csv"
                currentNetwork_DF_Period_PATH = str(condition.PATH_BMAOI_edgeCasheFILES + "/" +"Network_DF_" + str(SUMO_outPUT_PREFIX) + "_periodFILEs.xls")
                Network_DF_Period_0t00csv=pd.read_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE) #initalizing new periodFILE
                currentNetwork_DF_FILE = pd.DataFrame(Network_DF_Period_0t00csv) # initalizing new file
                # currentNetwork_DF_FILE.to_csv(currentNetwork_DF_Period_PATH) # saving new periodFILE
                currentPeriodSheetname = str(str(SUMO_outPUT_PREFIX)+"_Period_"+str(startPeriodTime)+"_to_"+str(endPeriodTime))
                condition.excelSAVER(currentNetwork_DF_Period_PATH,currentPeriodSheetname)
                # writer = ExcelWriter(str(currentNetwork_DF_Period_PATH))
                # currentNetwork_DF_FILE.to_excel(writer, currentPeriodSheetname)
                # writer.saver()# saving new periodFILE
                print("\n\n....\t...\t..\t.\t<<!>><<>>New Period<<>><<!>>\n\n","currentPeriodSheetname = ",currentPeriodSheetname, "\ncurrentNetwork_DF_Period_PATH = ",currentNetwork_DF_Period_PATH,"\n")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!This is a check\r\n ... currentNetwork_DF_FILE.iloc[7]: ",currentNetwork_DF_FILE.iloc[7], "\r\n<><>currentNetwork_DF_Period_PATH = ",currentNetwork_DF_Period_PATH)
            elif str(useCase) == "1":
                startPeriodTime = int(traci.simulation.getCurrentTime()/1000)
                endPeriodTime = startPeriodTime + PERIOD_VARRIABLE
                condition.GetSimulationRunPrefix(display = 0)
                print("startPeriodTime = ",startPeriodTime, "endPeriodTime = ",endPeriodTime)
                #currentNetwork_DF_Period_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + "Network_DF_" + SUMO_outPUT_PREFIX + "_periodFILE_" + str(startPeriodTime) + "_to_" + str(endPeriodTime) + ".csv"
                currentNetwork_DF_Period_PATH = str(condition.PATH_BMAOI_edgeCasheFILES + "/" +"Network_DF_" + str(SUMO_outPUT_PREFIX) + "_periodFILEs.xls")
                Network_DF_Period_0t00csv=pd.read_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE) #initalizing new periodFILE
                currentNetwork_DF_FILE = pd.DataFrame(Network_DF_Period_0t00csv) # initalizing new file
                #currentNetwork_DF_FILE.to_csv(currentNetwork_DF_Period_PATH) # saving new periodFILE
                currentPeriodSheetname = str(str(SUMO_outPUT_PREFIX)+"_Period_"+str(startPeriodTime)+"_to_"+str(endPeriodTime))
                condition.excelSAVER(currentNetwork_DF_Period_PATH,currentPeriodSheetname)
                # writer = ExcelWriter(currentNetwork_DF_Period_PATH)
                # currentNetwork_DF_FILE.to_excel(writer, currentPeriodSheetname)
                # writer.saver()
                print("\n\n....\t...\t..\t.\t<<!>><<>>New Run<<>><<!>>\n\n","currentPeriodSheetname = ",currentPeriodSheetname, "\ncurrentNetwork_DF_Period_PATH = ",currentNetwork_DF_Period_PATH,"\n")
                # print("!!!!!!!!!!!!!!!!!!!!!!!!This is a check\r\n ... currentNetwork_DF_FILE.iloc[7]: ",currentNetwork_DF_FILE.iloc[7], "\r\n<><>currentNetwork_DF_Period_PATH = ",currentNetwork_DF_Period_PATH)
                print("\n\n!!!!Network_DF_Period_Maker() FINISHED !!!")
            else:
                print("<><>Just Getting Network_DF FilePATH... I think<><>\n\n","currentPeriodSheetname = ",currentPeriodSheetname, "\ncurrentNetwork_DF_Period_PATH = ",currentNetwork_DF_Period_PATH,"\n")
        return currentNetwork_DF_Period_PATH, currentPeriodSheetname, startPeriodTime, endPeriodTime

    def excelSAVER(currentNetwork_DF_Period_PATH,currentPeriodSheetname):
        currentNetwork_DF_FILE = pd.read_csv(currentNetwork_DF_Period_PATH)
        writer = ExcelWriter(currentNetwork_DF_FILE)
        currentNetwork_DF_FILE.to_excel(writer, currentPeriodSheetname)
        writer.save()
        return
        
    def DisplayFiles(PERIOD_VARRIABLE):
        print("\n\nStarting DisplayFiles Function\n")
        global currentNetwork_DF_Period_PATH #= condition.PATH_BMAOI_edgeCasheFILES + "/" + "Network_DF_Period_" + str(PERIOD_VARRIABLE) +"_" + SUMO_outPUT_PREFIX + ".csv"
        currentNetwork_DF_FILE = pd.read_excel(currentNetwork_DF_Period_PATH,currentPeriodSheetname)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!This is a check\r\n ... currentNetwork_DF_FILE.iloc[7]: ",currentNetwork_DF_FILE.iloc[7], "\n\n<><>currentNetwork_DF_Period_PATH = '",currentNetwork_DF_Period_PATH,"'\n")
        print("Period = ", PERIOD_VARRIABLE, "currentNetwork_DF_FILE = ......\/..............\/.........\/......\r\n",currentNetwork_DF_FILE.iloc[7])
        print("DisplayFiles Function Completed\n\n")
        edge_i = '-387423966'
        edge_cashe_LOAD_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + condition.Belmont_AVEDic[edge_i] +".csv" #initalizes path address for cashe file
        edge_i_cashe_csv = pd.read_csv(edge_cashe_LOAD_PATH) #loads cashe file in
        while edge_i_cashe_csv.columns[0] != 'Belmont_AVEDic_ID':
            COLNAME = edge_i_cashe_csv.columns[0]
            del edge_i_cashe_csv[COLNAME]#delete the column
        print("Do these match? ", edge_i_cashe_csv.Truck_Count.iloc[edge_i_cashe_csv.shape[0]-1], "\n&\n",currentNetwork_DF_FILE.loc[currentNetwork_DF_FILE['Belmont_AVEDic_ID'].str.contains(edge_i),'Total_Trucks'],"\n?????????????\n\nedge_cashe_LOAD_PATH ='",edge_cashe_LOAD_PATH, "'\ncurrentNetwork_DF_Period_PATH='",currentNetwork_DF_Period_PATH,"'") #currentNetwork_DF_FILE.Total_Trucks[7] 
        print("\n$ run /GitHub/PhD_Modeling/PYTHON_GIT_SUMO/SUMO_Runner.py\n")
        ##NO...Why currentNetwork_DF_FILE not working properly?
        
    def ParameterGetter():
        print("\n\nParameterGetter is Starting")
        net = sumolib.net.readNet('C:\GitHub\PhD_Modeling\Belmont_AOI_git\Belmont_AOI-runFILES\Belmount_AOI-V5.net.xml')
        Network_DF_Period_0t00csv=pd.read_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE)
        Network_DF_Period_0t00DF = pd.DataFrame(Network_DF_Period_0t00csv)
        print(condition.Network_DF_Period_0t00DF_colDIC)
        Network_DF_Period_0t00DF_colDIC = {'Belmont_AVEDic_ID' : 0, 'Edge_ID' : 1, 'Condition_Index' : 2, 'State_of_Condition' : 3, 'Dynamic_Max_Speed' : 4, 'Total_Vehicles' : 5, 'Total_Trucks' : 6, 'ESAL' : 7, 'Total_Emergancy_Stops' : 8, 'Total_Accidents' : 9, 'Area' : 10, 'Roadway_Designation' : 11, 'Prority' : 12, 'Original_Max_Speed' : 13, 'Flood_Plain' : 14, 'Physical_Parameters_Others' : 15, 'Environmental_Parameters_Others' : 16}
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
            reallyrestTemplate = input("Do you really want to reset the Template? (y) ")
            if reallyrestTemplate == "y":
                Network_DF_Period_0t00DF.to_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE)
            else:
                print("I should take this part out if I use it in the greater scheme of things")
            print("\n\nParameterGetter is Complete\n\n")
            

    def Reset_Edge_CasheFiles():
        print("\n\nReset_Edge_CasheFiles has started")
    ## Test to make sure PATH_edge_i_cashe_TEMPLATE [C:\Users\BikoDOT\Dropbox\PhD\Research\Models\SUMO\SUMO_DropBox\Belmont_Ave-Run\BelmontC_AOI-outPUT-dropBOX\BMAOI_C-DataFrames\Edge_i_cashe_TEMPLATE.csv] is saved as a CVS UT-8 (Comma delimited)(*.csv)
    ## 12.21 Try to make this save to one excel workbook with many sheets https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html - maybe not csv better for large dataframes
    #edge_i = "424978646"
        edge_i_cashe_csv = pd.read_csv(condition.PATH_edge_i_cashe_TEMPLATE)
        edge_i_cashe_DF = pd.DataFrame(edge_i_cashe_csv)
        for edge_i in condition.Belmont_Ave[:]:
            #read in edge's cashe file
            edge_cashe_LOAD_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + condition.Belmont_AVEDic[edge_i] +".csv" #initalizes path address for cashe file
            edge_i_cashe_DF.to_csv(edge_cashe_LOAD_PATH)
            while edge_i_cashe_DF.columns[0] != 'Belmont_AVEDic_ID':
                COLNAME = edge_i_cashe_DF.columns[0]
                del edge_i_cashe_DF[COLNAME]#delete the column
            # print(edge_i_cashe_DF)
            edge_i_cashe_DF.iloc[0,0] = condition.Belmont_AVEDic[edge_i]
            edge_i_cashe_DF.iloc[0,1] = edge_i
            #Edge_i_VehIDs_lastStep_j = traci.edge.getLastStepVehicleIDs(edge_i)
            #PATH_save_to_edgeCasheFILES = condition.PATH_BMAOI_edgeCasheFILES +"/"+condition.Belmont_AVEDic[edge_i]+".csv"
            edge_i_cashe_DF.to_csv(edge_cashe_LOAD_PATH)# Save cashe file
        return print("Reset_Edge_CasheFiles has completed\n\n")
        
    def GetSimulationRunPrefix(display):
        global SUMO_outPUT_PREFIX
        global SUMO_Traci_PORT
        with open('/GitHub/PhD_Modeling/Belmont_AOI_git/Belmont_AOI-runFILES/BMAOI-TRACI.sumocfg') as f:
            for line in f:
                if '<output-prefix value="BM_test-TRACI-' in line:
                    #print(line)
                    SUMO_outPUT_PREFIX_LINE = line
                    SUMO_outPUT_PREFIX = re.search('<output-prefix value="BM_test-TRACI-(.*)-"/>',SUMO_outPUT_PREFIX_LINE, re.IGNORECASE).group(1)
                if '<remote-port value=' in line:
                    SUMO_outPUT_Port_LINE = line
                    SUMO_Traci_PORT = re.search('<remote-port value="(.*)"/>',SUMO_outPUT_Port_LINE, re.IGNORECASE).group(1)
        if display == 1:
            print("\nSUMO_outPUT_PREFIX = ", SUMO_outPUT_PREFIX,"\n\SUMO_Traci_PORT = ", SUMO_Traci_PORT)
        return SUMO_outPUT_PREFIX, SUMO_Traci_PORT#, print("\nSUMO_outPUT_PREFIX = ", SUMO_outPUT_PREFIX,"\nSUMO_Traci_PORT = ", SUMO_Traci_PORT)
        
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
        
      
    # def BreakingThingZ(Edge_TOT_Trucks, edgez_i,Edge_TOT_Trucks_Current_Period):
        # if int(Edge_TOT_Trucks) == 150:
            # print("At Step <><"+str(traci.simulation.getCurrentTime()/1000)+"><>"+"\n\t"+"<<Edge "+str(edgez_i)+">>"+"\t"+"Total Trucks Have Reached 50. With "+str(Edge_TOT_Trucks_Current_Period)+" new trucks this step"+"\n\t"+"Changing Max Speed to 10 m/s")
            # traci.edge.setMaxSpeed(str(edgez_i),10.00)
            # #input("Press Enter to continue...")
        # elif int(Edge_TOT_Trucks) == 250:
            # print("Edge "+str(edgez_i)+"Total Trucks Have Reached 150. With "+str(Edge_TOT_Trucks_Current_Period)+" new trucks this step"+"\n\t"+"Changing Max Speed to 7 m/s")
            # traci.edge.setMaxSpeed(str(edgez_i),7.00)
            # #input("Press Enter to continue...")
        # elif int(Edge_TOT_Trucks) == 600:
            # print("Edge "+str(edgez_i)+"Total Trucks Have Reached 500. With "+str(Edge_TOT_Trucks_Current_Period)+" new trucks this step"+"\n\t"+"Changing Max Speed to 1 m/s")
            # traci.edge.setMaxSpeed(str(edgez_i),1.00)
            #input("Press Enter to continue...")
        # else:
            # continue
# traci.edge.getParameter("387423966", "MAXSPEED")

print("!\n!\t!\t!Pavement Condition Controls Activated!")
# Testing
# while len(Edge_i_VehIDs_lastStep_j) <1:
    # traci.simulationStep()
    # Edge_i_VehIDs_lastStep_j = traci.edge.getLastStepVehicleIDs(edge_i)
# print(Edge_i_VehIDs_lastStep_j)

        # condition.GetSimulationRunPrefix()
        # currentNetwork_DF_Period_PATH = str(condition.PATH_BMAOI_edgeCasheFILES + "/" +"Network_DF_" + str(SUMO_outPUT_PREFIX) + "_periodFILEs.xls")
        # currentPeriodSheetname = str(str(SUMO_outPUT_PREFIX)+"_Period_"+str(startPeriodTime)+"_to_"+str(endPeriodTime))
        # writer = ExcelWriter(currentNetwork_DF_Period_PATH,currentPeriodSheetname=currentPeriodSheetname)


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

# ##New File based on Period
# if int(traci.simulation.getCurrentTime()/1000) == 2:
    # n = 0
    # Start_Time = str(traci.simulation.getCurrentTime()/1000)

# if int(traci.simulation.getCurrentTime()/1000) == max(3600*(n/3600),2): # int(traci.simulation.getCurrentTime()/1000) used to be PERIOD_VARRIABLE 
    # try:
        # currentNetwork_DF_Period_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + "Network_DF_Period_" + "Start_Time" + "_" + str(PERIOD_VARRIABLE) +"_" + SUMO_outPUT_PREFIX + ".csv"
        # currentNetwork_DF_FILE = pd.read_excel(currentNetwork_DF_Period_PATH,currentPeriodSheetname)

        # print(n)
    # except OSError as err: #https://docs.python.org/3/library/exceptions.html#BaseException 
        # print("File Not Found", err," Making a new file for period = ", PERIOD_VARRIABLE) 
        # Network_DF_Period_0t00csv=pd.read_csv(condition.PATH_Network_DF_Period_0t00_TEMPLATE)
        # Period_Start_Time = max(3600*(n/3600),2)
        # # PERIOD_VARRIABLE = PERIOD_VARRIABLE
        # currentNetwork_DF_Period_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + "Network_DF_Period_" + Period_Start_Time + "_" + str(PERIOD_VARRIABLE) +"_" + SUMO_outPUT_PREFIX + ".csv"
        # Network_DF_Period_0t00csv.to_csv(currentNetwork_DF_Period_PATH)
        # currentNetwork_DF_FILE = pd.read_excel(currentNetwork_DF_Period_PATH,currentPeriodSheetname)
        # n =  n + 1
        # print("....\t...\t..\t.\t<<!>><<>>New Period<<>><<!>>\r\nn = ",n)
# currentNetwork_DF_Period_PATH = condition.PATH_BMAOI_edgeCasheFILES + "/" + "Network_DF_Period_" + "Start_Time" + "_" + str(PERIOD_VARRIABLE) +"_" + SUMO_outPUT_PREFIX + ".csv"
# currentNetwork_DF_FILE = pd.read_excel(currentNetwork_DF_Period_PATH,currentPeriodSheetname)

# Belmont_AVEDic ={'-12150712#3' : 2, '-12150712#4' : 3, '-12150712#6' : 4, '-12327906#0' : 5, '-196358954#0' : 6, '-196358954#3' : 7, '-196358956#2' : 8, '-387423966' : 9, '-423956981' : 10, '-423956982' : 11, '-423965484' : 12, '-423967058#0' : 13, '-423967058#1' : 14, '-423967352' : 15, '-423967353' : 16, '-423967354' : 17, '-423967355' : 18, '-423967356' : 19, '-423967357' : 20, '-423967358#1' : 21, '-423967358#2' : 22, '-423967359#0' : 23, '-423967359#1' : 24, '-424803245' : 25, '-424803247#1' : 26, '-424824619' : 27, '-424824620' : 28, '-424824621' : 29, '-424978161' : 30, '-424978642.0' : 31, '-424978642.170' : 32, '-424978643' : 33, '-424978647#1' : 34, '-448887867' : 35, '-448887868' : 36, '-448887869' : 37, '-448887870#1' : 38, '-448887871#0' : 39, '-448887871#2' : 40, '-49940170#0' : 41, '12150712#3' : 42, '12150712#4' : 43, '12150712#5' : 44, '12327906#0' : 45, '12327906#1' : 46, '196358954#0' : 47, '196358954#1' : 48, '196358956#0' : 49, '387423966' : 50, '423956978' : 51, '423956979' : 52, '423956980' : 53, '423965484' : 54, '423967058#1' : 55, '423967352' : 56, '423967353' : 57, '423967354' : 58, '423967355' : 59, '423967356' : 60, '423967358#0' : 61, '423967358#2' : 62, '423967359#0' : 63, '423967359#1' : 64, '424803245' : 65, '424803247#0' : 66, '424824619' : 67, '424824620' : 68, '424824621' : 69, '424978639.0' : 70, '424978639.102' : 71, '424978640' : 72, '424978643' : 73, '424978644' : 74, '424978646' : 75, '448887867' : 76, '448887868' : 77, '448887869' : 78, '448887870#0' : 79, '448887871#0' : 80, '448887871#1' : 81 }

    # def DetFunc(edgez_i, Edge_TOT_Trucks,Edge_TOT_Trucks_Current_Period):
        # pavementConditionarrary = np.load(condition.PavePath)
        # #Edge_TOT_Trucks = GTS.general.Edge_TOT_Trucks
        # #edgez_i = GTS.general.edgez_i
        # #Edge_TOT_Trucks_Current_Period = GTS.general.Edge_TOT_Trucks_Current_Period
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
            
                
        # # traci.vehicle.addFull("Ben_Tracker_1","U_Tracker_Ben","TRACKER_TRUCK")
        # # traci.vehicle.addFull("Ben_Tracker_2","U_Tracker_Ben","TRACKER_TRUCK")
        # # traci.vehicle.addFull("Ben_Tracker_3","U_Tracker_Ben","TRACKER_TRUCK")
        # # traci.vehicle.addFull("Ben_Tracker_4","U_Tracker_Ben","TRACKER_TRUCK")
        # # traci.vehicle.addFull("Ben_Tracker_5","U_Tracker_Ben","TRACKER_TRUCK")