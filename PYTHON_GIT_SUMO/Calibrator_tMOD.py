<<<<<<< HEAD
# Trying to replecate this function to see why calibrators are not adding vehicles 
# to the simulation.
  http://www.sumo.dlr.de/daily/doxygen/d0/db7/_m_s_calibrator_8cpp_source.html#l00479
  479 MSCalibrator::remainingVehicleCapacity(int laneIndex) const {
  480     if (laneIndex < 0) {
  481         const int numLanes = (int)myEdge->getLanes().size();
  482         int result = 0;
  483         for (int i = 0; i < numLanes; ++i) {
  484             result = MAX2(result, remainingVehicleCapacity(i));
  485         }
  486         return result;
  487     }
  488     assert(laneIndex < (int)myEdge->getLanes().size());
  489     MSLane* lane = myEdge->getLanes()[laneIndex];
  490     MSVehicle* last = lane->getLastFullVehicle();
  491     const SUMOVehicleParameter* pars = myCurrentStateInterval->vehicleParameter;
  492     const MSVehicleType* vtype = MSNet::getInstance()->getVehicleControl().getVType(pars->vtypeid);
  493     const double spacePerVehicle = vtype->getLengthWithGap() + myEdge->getSpeedLimit() * vtype->getCarFollowModel().getHeadwayTime();
  494     if (last == 0) {
  495         // ensure vehicles can be inserted on short edges
  496         return MAX2(1, (int)(myEdge->getLength() / spacePerVehicle));
  497     } else {
  498         return (int)(last->getPositionOnLane() / spacePerVehicle);
  499     }
  500 }
  
import os, sys
import numpy as np
import traci
import traci.constants as tc
import re
import sumolib
## sys.path.append('/GitHub/PhD_Modeling/PYTHON_GIT_SUMO')
## import General_TraciSUMO as GTS

def remainingVehicleCapacity():
	edgeLIST =  traci.edge.getIDList()
	for myEdge in edgeLIST():
		numLanes = 4
		vehLISTLANE_i = 0
		for vehLISTLANE_i in range(3):
			
		
		/ProgramData/Anaconda3/Lib/seasnake
		/GitHub/SUMO_SCR/src/netedit/GNECalibrator.cpp
## Trainings http://sumo.dlr.de/wiki/Tools/Sumolib
 import sumolib
 # parse the net
 net = sumolib.net.readNet('/GitHub/PhD_Modeling/Calibrator_Test/cali-TEST-Run_Files/Calibrator_Test-Track_V0.FAT.net.xml')
net.getEdges() ## T_Edge = '1_2_to_2_2'
T_Edge = '1_2_to_2_2'
edge_parINFO = np.empty([30,6],dtype=object)
edge_parINFOPD = pd.DataFrame(edge_parINFO,index=['1_2_to_2_2_0','1_2_to_2_2_1','1_2_to_2_2_2','1_2_to_2_2_3','MaxSpeed_i_m/s','Current_Speed')
for i in range(4):
	if i == 3:
		T_Edge = '1_2_to_2_2'
		lane_i=str(i)
		T_Edge_Lane = str(T_Edge+"_"+lane_i)
		laneSpeed_0 = 13.41
		edge_parINFOPD.iloc[0,i] = laneSpeed_0
		laneSpeed_c = traci.lane.getLastStepMeanSpeed(T_Edge_Lane)
		edge_parINFO[0,i+1] = laneSpeed_c
	else:
		T_Edge = '1_2_to_2_2'
		lane_i=str(i)
		T_Edge_Lane = str(T_Edge+"_"+lane_i)
		laneLength = traci.lane.getLength(T_Edge_Lane)
		edge_parINFOPD.iloc[0,i] = laneLength
	print("T_Edge_Lane = ",T_Edge_Lane, "Length =",traci.lane.getLength(T_Edge_Lane),"\nThis should be the same =",edge_parINFOPD.iloc[0,i],traci.lane.getLength(T_Edge_Lane))
print(edge_parINFOPD[0])
	
	traci.lane.getLength('1_2_to_2_2_1')
	
	
	
	
	
	
	
	
	
	
	
	
=======
# Trying to replecate this function to see why calibrators are not adding vehicles 
# to the simulation.
  http://www.sumo.dlr.de/daily/doxygen/d0/db7/_m_s_calibrator_8cpp_source.html#l00479
  479 MSCalibrator::remainingVehicleCapacity(int laneIndex) const {
  480     if (laneIndex < 0) {
  481         const int numLanes = (int)myEdge->getLanes().size();
  482         int result = 0;
  483         for (int i = 0; i < numLanes; ++i) {
  484             result = MAX2(result, remainingVehicleCapacity(i));
  485         }
  486         return result;
  487     }
  488     assert(laneIndex < (int)myEdge->getLanes().size());
  489     MSLane* lane = myEdge->getLanes()[laneIndex];
  490     MSVehicle* last = lane->getLastFullVehicle();
  491     const SUMOVehicleParameter* pars = myCurrentStateInterval->vehicleParameter;
  492     const MSVehicleType* vtype = MSNet::getInstance()->getVehicleControl().getVType(pars->vtypeid);
  493     const double spacePerVehicle = vtype->getLengthWithGap() + myEdge->getSpeedLimit() * vtype->getCarFollowModel().getHeadwayTime();
  494     if (last == 0) {
  495         // ensure vehicles can be inserted on short edges
  496         return MAX2(1, (int)(myEdge->getLength() / spacePerVehicle));
  497     } else {
  498         return (int)(last->getPositionOnLane() / spacePerVehicle);
  499     }
  500 }
  
import os, sys
import numpy as np
import traci
import traci.constants as tc
import re
import sumolib
## sys.path.append('/GitHub/PhD_Modeling/PYTHON_GIT_SUMO')
## import General_TraciSUMO as GTS

def remainingVehicleCapacity():
	edgeLIST =  traci.edge.getIDList()
	for myEdge in edgeLIST():
		numLanes = 4
		vehLISTLANE_i = 0
		for vehLISTLANE_i in range(3):
			
		
		/ProgramData/Anaconda3/Lib/seasnake
		/GitHub/SUMO_SCR/src/netedit/GNECalibrator.cpp
## Trainings http://sumo.dlr.de/wiki/Tools/Sumolib
 import sumolib
 # parse the net
 net = sumolib.net.readNet('/GitHub/PhD_Modeling/Calibrator_Test/cali-TEST-Run_Files/Calibrator_Test-Track_V0.FAT.net.xml')
net.getEdges() ## T_Edge = '1_2_to_2_2'
T_Edge = '1_2_to_2_2'
edge_parINFO = np.empty([30,6],dtype=object)
edge_parINFOPD = pd.DataFrame(edge_parINFO,index=['1_2_to_2_2_0','1_2_to_2_2_1','1_2_to_2_2_2','1_2_to_2_2_3','MaxSpeed_i_m/s','Current_Speed')
for i in range(4):
	if i == 3:
		T_Edge = '1_2_to_2_2'
		lane_i=str(i)
		T_Edge_Lane = str(T_Edge+"_"+lane_i)
		laneSpeed_0 = 13.41
		edge_parINFOPD.iloc[0,i] = laneSpeed_0
		laneSpeed_c = traci.lane.getLastStepMeanSpeed(T_Edge_Lane)
		edge_parINFO[0,i+1] = laneSpeed_c
	else:
		T_Edge = '1_2_to_2_2'
		lane_i=str(i)
		T_Edge_Lane = str(T_Edge+"_"+lane_i)
		laneLength = traci.lane.getLength(T_Edge_Lane)
		edge_parINFOPD.iloc[0,i] = laneLength
	print("T_Edge_Lane = ",T_Edge_Lane, "Length =",traci.lane.getLength(T_Edge_Lane),"\nThis should be the same =",edge_parINFOPD.iloc[0,i],traci.lane.getLength(T_Edge_Lane))
print(edge_parINFOPD[0])
	
	traci.lane.getLength('1_2_to_2_2_1')
	
	
	
	
	
	
	
	
	
	
	
	
>>>>>>> 5384f079850537bd07bf47a379f46fbae5d078e0
	