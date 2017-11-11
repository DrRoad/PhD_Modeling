#run /Users/Biko/Documents/GitHub/PhD_Modeling/Calibrator_Test/SUMO_cTEST-Runner.py

#GTS.general.releaseTraci(None)

import os, sys
from random import *
import numpy as np
import traci
import traci.constants as tc
import re
import sumolib
import time
#import SUMO_PYTHON.Pavement_Condition as PC
import pandas as pd

sumoBinary = "C:/Sumo/SUMO-0.31.0/sumo-0.31.0/bin/sumo-gui"
configPATH = "C:/Users/Biko/Documents/GitHub/PhD_Modeling/Calibrator_Test/cali-TEST-Run_Files/Cali-Test.sumocfg"
sumoCmd = [sumoBinary, "-c", configPATH, "--start"]



print("\t\t\t\t\t\t###STARTING####")
useCase = input("\n\tPress 1 for a new Run:  \n") #\nPress Anything to continue...
if useCase == "1":
	traci.start(sumoCmd,5454)
	traci.simulationStep()
	Start_Time = int(traci.simulation.getCurrentTime()/1000)
	Period_Time="00"
	steps_TT="000"
	#general.addNewColumn(Period_Time,Start_Time,steps_TT)
	#addNewColumn(Period_Time,Start_Time,steps_TT,NPpathgiven=None)

	#global edge_VehIDhistoryPD Moved to top #does this even work
	#edge_VehIDhistoryPD = edge_VehIDhistoryPD #does this even work
	Start_Time = int(traci.simulation.getCurrentTime()/1000)
	steps_TT = input("How many steps would you like to take? ")
	for step in range(int(steps_TT)):
		traci.simulationStep()
elif useCase=="x":
	traci.close()
else:
	print("\t\t\t\t\t!!!!!!!!!!!!!!CONTINUING!!!!!!!!!!!!!!\t\t\t")
	steps_TT = input("How many steps would you like to take? ")
	for step in range(int(steps_TT)):
		traci.simulationStep()



#run /Users/Biko/Documents/GitHub/PhD_Modeling/Calibrator_Test/SUMO_cTEST-Runner.py