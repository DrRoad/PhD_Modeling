import os, sys
import numpy as np
import traci
import traci.constants as tc
import re
import SUMO_PYTHON.General_TraciSUMO as GTS



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
import SUMO_PYTHON.Pavement_Condition as PC
import pandas as pd

sumoBinary = "C:/Sumo/SUMO-0.31.0/sumo-0.31.0/bin/sumo-gui"
configPATH = "C:/Users/Biko/Documents/GitHub/SUMO/Calibrator_Test/Cali-Test.sumocfg"
sumoCmd = [sumoBinary, "-c", configPATH, "--start"]

traci.start(sumoCmd,5454)
traci.simulationStep()


