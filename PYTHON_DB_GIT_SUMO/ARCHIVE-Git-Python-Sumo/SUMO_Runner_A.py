import os, sys
import numpy as np
import traci
import traci.constants as tc
import re
import time
import sumolib
import General_TraciSUMO_Git as GTS
import Pavement_Condition_GIT as PC
import cProfile, pstats , io



#run /GitHub/PhD_Modeling/PYTHON_GIT_SUMO/SUMO_Runner.py
# https://stackoverflow.com/questions/582336/how-can-you-profile-a-script

# pr = cProfile.Profile()
# pr.enable()
GTS.general.releaseTraci(None)
# cProfile.run('GTS.general.releaseTraci(None)','/Sumo/BelmontC_AOI-outPUT-dropBOX')
# p = pstats.Stats('/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-profileFILES/7200b-restats.txt')
# p.strip_dirs().sort_stats('cumulative').print_stats()
# pr.disable()
# s = io.StringIO()
# sortby = 'cumulative'
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()
# print(s.getvalue())
#import SUMO_PYTHON.Pavement_Condition

