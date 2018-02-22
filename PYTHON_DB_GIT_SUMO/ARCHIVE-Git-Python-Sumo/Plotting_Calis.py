<<<<<<< HEAD
# 11.29.2017 - I'm not sure if this works or not
### This one does C:\GitHub\PhD_Modeling\PYTHON_GIT_SUMO\pyplot_simple-V2.py


import numpy as np
import traci
import traci.constants as tc
import matplotlib.pyplot as plt
import pandas as pd
import sumolib

# parse the net
FATnet = sumolib.net.readNet('/GitHub/PhD_Modeling/Calibrator_Test/cali-TEST-Run_Files/Calibrator_Test-Track_V0.net.xml')

FATnetjunctionsPATH = '/Sumo/runs/caliTEST-C/caliTEST-OUTPUT-C/FATnetjunctionsDATAFRAME.cvs'

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)



# retrieve the coordinate of a node based on its ID
edgeLIST =  traci.edge.getIDList()
edgeLIST = np.array([edgeLIST])


edge_ParametersDF = pd.DataFrame(edge_ParametersDF,index=['Condition_RT','Tot_Trucks','Trucks_Pi','Trucks_Pi-1','Trucks_Pi-2','Trucks_Pi-3','MaxSpeed_i_m/s','O_max_mph'])

juncNAMES=('0_0', '0_1', '0_2', '1_0', '1_1', '1_2', '2_0', '2_1', '2_2', '3_0', '3_1', '3_2', 'FIN', 'STRT')
juncINFO=np.empty([14,31],dtype=object)
for myJuntion in range(14):
	#print("myJuntion = ",myJuntion,"-",str(juncNAMES[myJuntion]),";",FATnet.getNode(str(juncNAMES[myJuntion])).getCoord())
	print(str(juncNAMES[myJuntion]),";",FATnet.getNode(str(juncNAMES[myJuntion])).getCoord())
	juncTEMP = FATnet.getNode(str(juncNAMES[myJuntion])).getCoord()
	juncINFO[myJuntion,0] = juncNAMES[myJuntion]
	juncINFO[myJuntion,1] = juncTEMP[0]
	juncINFO[myJuntion,2] = juncTEMP[1]
	
	
	
	
	FATnet.getEdge(myEdge).getToNode().getID())
	FATnet.getNode('0_0').getCoord()
	
	
	
	
	
juncList=('0_0', '0_1', '0_2', '1_0', '1_1', '1_2', '2_0', '2_1', '2_2', '3_0', '3_1', '3_2', 'FIN', 'STRT')

FATnetjunctions = {'junction:0_0' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:0_1' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:0_2' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:1_0' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:1_1' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:1_2' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:2_0' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:2_1' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:2_2' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:3_0' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:3_1' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:3_2' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:FIN' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:STRT' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average_ Percent_Diff']}
FATnetjunctionDF = pd.DataFrame(FATnetjunctions,index=['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average_Percent_Diff'])
=======
# 11.29.2017 - I'm not sure if this works or not
### This one does C:\GitHub\PhD_Modeling\PYTHON_GIT_SUMO\pyplot_simple-V2.py


import numpy as np
import traci
import traci.constants as tc
import matplotlib.pyplot as plt
import pandas as pd
import sumolib

# parse the net
FATnet = sumolib.net.readNet('/GitHub/PhD_Modeling/Calibrator_Test/cali-TEST-Run_Files/Calibrator_Test-Track_V0.net.xml')

FATnetjunctionsPATH = '/Sumo/runs/caliTEST-C/caliTEST-OUTPUT-C/FATnetjunctionsDATAFRAME.cvs'

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)



# retrieve the coordinate of a node based on its ID
edgeLIST =  traci.edge.getIDList()
edgeLIST = np.array([edgeLIST])


edge_ParametersDF = pd.DataFrame(edge_ParametersDF,index=['Condition_RT','Tot_Trucks','Trucks_Pi','Trucks_Pi-1','Trucks_Pi-2','Trucks_Pi-3','MaxSpeed_i_m/s','O_max_mph'])

juncNAMES=('0_0', '0_1', '0_2', '1_0', '1_1', '1_2', '2_0', '2_1', '2_2', '3_0', '3_1', '3_2', 'FIN', 'STRT')
juncINFO=np.empty([14,31],dtype=object)
for myJuntion in range(14):
	#print("myJuntion = ",myJuntion,"-",str(juncNAMES[myJuntion]),";",FATnet.getNode(str(juncNAMES[myJuntion])).getCoord())
	print(str(juncNAMES[myJuntion]),";",FATnet.getNode(str(juncNAMES[myJuntion])).getCoord())
	juncTEMP = FATnet.getNode(str(juncNAMES[myJuntion])).getCoord()
	juncINFO[myJuntion,0] = juncNAMES[myJuntion]
	juncINFO[myJuntion,1] = juncTEMP[0]
	juncINFO[myJuntion,2] = juncTEMP[1]
	
	
	
	
	FATnet.getEdge(myEdge).getToNode().getID())
	FATnet.getNode('0_0').getCoord()
	
	
	
	
	
juncList=('0_0', '0_1', '0_2', '1_0', '1_1', '1_2', '2_0', '2_1', '2_2', '3_0', '3_1', '3_2', 'FIN', 'STRT')

FATnetjunctions = {'junction:0_0' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:0_1' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:0_2' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:1_0' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:1_1' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:1_2' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:2_0' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:2_1' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:2_2' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:3_0' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:3_1' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:3_2' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:FIN' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average, Percent, Diff'], 'junction:STRT' : ['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average_ Percent_Diff']}
FATnetjunctionDF = pd.DataFrame(FATnetjunctions,index=['%Diff-1800', '%Diff-3600', '%Diff-5400', '%Diff-7200', '%Diff-9000', '%Diff-10800', '%Diff-12600', '%Diff-14400', '%Diff-16200', '%Diff-18000', '%Diff-19800', '%Diff-21600', '%Diff-23400', '%Diff-25200', '%Diff-27000', '%Diff-28800', '%Diff-30600', '%Diff-32400', '%Diff-34200', '%Diff-36000', '%Diff-37800', '%Diff-39600', '%Diff-41400', '%Diff-43200', '%Diff-45000', '%Diff-46800', '%Diff-48600', '%Diff-50400', 'Average_Percent_Diff'])
>>>>>>> 5384f079850537bd07bf47a379f46fbae5d078e0
FATnetjunctionDF.to_csv(FATnetjunctionsPATH)