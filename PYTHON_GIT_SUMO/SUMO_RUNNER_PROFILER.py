<<<<<<< HEAD


#run /GitHub/PhD_Modeling/PYTHON_GIT_SUMO/SUMO_Runner.py
# https://stackoverflow.com/questions/582336/how-can-you-profile-a-script

# pr = cProfile.Profile()
# pr.enable()
cProfile.run('GTS.general.releaseTraci(None)','TEST12restats')
p = pstats.Stats('TEST12restats')
p.strip_dirs().sort_stats(-1).print_stats()
# pr.disable()
# s = StringIO.StringIO()
# sortby = 'cumulative'
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()
# print(s.getvalue())
=======


#run /GitHub/PhD_Modeling/PYTHON_GIT_SUMO/SUMO_Runner.py
# https://stackoverflow.com/questions/582336/how-can-you-profile-a-script

# pr = cProfile.Profile()
# pr.enable()
cProfile.run('GTS.general.releaseTraci(None)','TEST12restats')
p = pstats.Stats('TEST12restats')
p.strip_dirs().sort_stats(-1).print_stats()
# pr.disable()
# s = StringIO.StringIO()
# sortby = 'cumulative'
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()
# print(s.getvalue())
>>>>>>> 5384f079850537bd07bf47a379f46fbae5d078e0
#import SUMO_PYTHON.Pavement_Condition