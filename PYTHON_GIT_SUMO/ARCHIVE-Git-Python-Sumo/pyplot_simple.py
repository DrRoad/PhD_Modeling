# run /GitHub/PhD_Modeling/PYTHON_GIT_SUMO/pyplot_simple.py

# # Have a look at the colormaps here and decide which one you'd like:
# # http://matplotlib.org/1.2.1/examples/pylab_examples/show_colormaps.html

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

junc_ID_X_Y = np.array([[0_0, 0.0, 0.0], ['0_1', 0.0, 100.0], ['0_2', 0.0, 200.0], ['1_0', 100.0, 0.0], ['1_1', 100.0, 100.0], ['1_2', 100.0, 200.0], ['2_0', 200.0, 0.0], ['2_1', 200.0, 100.0], ['2_2', 200.0, 200.0], ['3_0', 300.0, 0.0], ['3_1', 300.0, 100.0], ['3_2', 300.0, 200.0], ['FIN', 400.0, 300.0], ['STRT', -100.0, -100.0]])

#f, axarr = plt.subplots(2, sharex=True)
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot([279.32,221.85], [210.2,210.2])
# ax1.set_title('Sharing Y axis')
# ax2.plot([10.2,10.2], [20.83,78.15])
# plt.show()

# fig1 = plt.figure()
# fig1.set_size_inches(9.5,8)
# ax1 = fig1.add_subplot(111)


# ax1.plot([279.32,221.85], [210.2,210.2], linewidth=28.37)
# ax1.plot([10.2,10.2], [20.83,78.15], linewidth=26.77)
# ax1.plot([-10.2,-10.2], [179.505,121.85], linewidth=26.07)
# ax1.plot([189.8,189.8], [178.15,121.85], linewidth=25.22)
# ax1.plot([100,20.52], [210.2,210.2], linewidth=24.05)
# ax1.plot([78.15,20.015], [10.2,10.2], linewidth=23.26)
# ax1.plot([21.85,78.15], [89.8,89.8], linewidth=20.23)
# ax1.plot([200,121.85], [10.2,10.2], linewidth=19.29)
# ax1.plot([110.2,110.2], [21.85,78.15], linewidth=18.81)
# ax1.plot([178.15,100], [210.2,210.2], linewidth=17.57)
# ax1.plot([100,178.15], [189.8,189.8], linewidth=15.35)
# ax1.plot([-10.2,-10.2], [78.15,20.83], linewidth=15.17)
# ax1.plot([178.15,121.85], [110.2,110.2], linewidth=13.92)
# ax1.plot([-100,-13.27], [-100,-13.275], linewidth=11.68)
# ax1.plot([20.055,78.15], [-10.2,-10.2], linewidth=10.94)
# ax1.plot([310.2,310.2], [20.48,78.15], linewidth=10.42)
# ax1.plot([121.85,178.15], [89.8,89.8], linewidth=9.63)
# ax1.plot([78.15,21.85], [110.2,110.2], linewidth=9.54)
# ax1.plot([279.4,200], [10.2,10.2], linewidth=9.21)
# ax1.plot([89.8,89.8], [78.15,21.85], linewidth=5.39)
# ax1.plot([221.85,278.15], [89.8,89.8], linewidth=5.15)
# ax1.plot([289.8,289.8], [179.28,121.85], linewidth=4.98)
# ax1.plot([210.2,210.2], [121.85,178.15], linewidth=4.06)
# ax1.plot([278.15,221.85], [110.2,110.2], linewidth=4.05)
# ax1.plot([221.85,279.32], [189.8,189.8], linewidth=2.69)
# ax1.plot([310.2,310.2], [121.85,179.28], linewidth=2.67)
# ax1.plot([289.8,289.8], [78.15,20.48], linewidth=2.03)
# ax1.plot([20.52,100], [189.8,189.8], linewidth=1.24)
# ax1.plot([10.2,10.2], [121.85,179.565], linewidth=1.1)
# ax1.plot([200,279.34], [-10.2,-10.2], linewidth=0.41)
# ax1.plot([121.85,200], [-10.2,-10.2], linewidth=0.19)
# ax1.plot([309.84,400], [209.84,300], linewidth=0.19)

#Now Plotting Junctions
xI = junc_ID_X_Y[:,1]
yI = junc_ID_X_Y[:,2]
ax1.scatter(xI,yI,s=200,c='r',alpha=0.5)



colormap = plt.cm.RdYlGn
# not sure if this goes here or not   for i in range(num_plots):
#colormap = plt.cm.gist_ncar #nipy_spectral, Set1,Paired   
colors = [colormap(i) for i in np.linspace(0, 1,len(ax1.lines))]
for i,j in enumerate(ax1.lines):
    j.set_color(colors[i])

# plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
# plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, num_plots))))
plt.xlabel('Longitude\n Thickness of Lines indicates larger AVE_%Diff of simulated_FLOW on edge vs input_FLOW')
plt.ylabel('Latitude')
plt.title('Super_Highway_4_Lane_Cali_Percent_Diff')
#plt.grid(True)
imageFILENAME_1 = 'Super_Highway_4_Lane_Cali_Percent_Diff-2'
imagePATH_1 = str('/Sumo/runs/caliTEST-C/caliTEST-OUTPUT-C/Image_Files/'+imageFILENAME_1+'.png')
#plt.savefig(imagePATH_1,dpi=120)

#plt.show()


#ax2 = fig1.add_subplot(111)

ax2.plot([279.32,221.85], [210.2,210.2], linewidth=15.44)
ax2.plot([10.2,10.2], [20.83,78.15], linewidth=15.05)
ax2.plot([-10.2,-10.2], [179.505,121.85], linewidth=13.56)
ax2.plot([189.8,189.8], [178.15,121.85], linewidth=13.39)
ax2.plot([100,20.52], [210.2,210.2], linewidth=12.55)
ax2.plot([78.15,20.015], [10.2,10.2], linewidth=11.79)
ax2.plot([21.85,78.15], [89.8,89.8], linewidth=11.51)
ax2.plot([200,121.85], [10.2,10.2], linewidth=11.38)
ax2.plot([110.2,110.2], [21.85,78.15], linewidth=9.88)
ax2.plot([178.15,100], [210.2,210.2], linewidth=9.74)
ax2.plot([100,178.15], [189.8,189.8], linewidth=9.18)
ax2.plot([-10.2,-10.2], [78.15,20.83], linewidth=9.1)
ax2.plot([178.15,121.85], [110.2,110.2], linewidth=8.9)
ax2.plot([-100,-13.27], [-100,-13.275], linewidth=8.47)
ax2.plot([20.055,78.15], [-10.2,-10.2], linewidth=8.33)
ax2.plot([310.2,310.2], [20.48,78.15], linewidth=8.13)
ax2.plot([121.85,178.15], [89.8,89.8], linewidth=7.92)
ax2.plot([78.15,21.85], [110.2,110.2], linewidth=7.57)
ax2.plot([279.4,200], [10.2,10.2], linewidth=7.56)
ax2.plot([89.8,89.8], [78.15,21.85], linewidth=6.8)
ax2.plot([221.85,278.15], [89.8,89.8], linewidth=6.67)
ax2.plot([289.8,289.8], [179.28,121.85], linewidth=6.46)
ax2.plot([210.2,210.2], [121.85,178.15], linewidth=6.24)
ax2.plot([278.15,221.85], [110.2,110.2], linewidth=5.38)
ax2.plot([221.85,279.32], [189.8,189.8], linewidth=4.36)
ax2.plot([310.2,310.2], [121.85,179.28], linewidth=3.59)
ax2.plot([289.8,289.8], [78.15,20.48], linewidth=3.06)
ax2.plot([20.52,100], [189.8,189.8], linewidth=2.92)
ax2.plot([10.2,10.2], [121.85,179.565], linewidth=2.53)
ax2.plot([200,279.34], [-10.2,-10.2], linewidth=2.53)
ax2.plot([121.85,200], [-10.2,-10.2], linewidth=2.27)
ax2.plot([309.84,400], [209.84,300], linewidth=1.94)


#Now Plotting Junctions
xI = junc_ID_X_Y[:,1]
yI = junc_ID_X_Y[:,2]
ax2.scatter(xI,yI,s=200,c='r',alpha=0.5)

num_plots = 32

colormap = plt.cm.RdYlGn
# not sure if this goes here or not   for i in range(num_plots):
#colormap = plt.cm.gist_ncar #nipy_spectral, Set1,Paired   
colors = [colormap(i) for i in np.linspace(0, 1,len(ax2.lines))]
for i,j in enumerate(ax2.lines):
    j.set_color(colors[i])

# plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
# plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, num_plots))))
plt.xlabel('Longitude\n Thickness of Lines indicates larger AVE_%Diff of simulated_FLOW on edge vs input_FLOW')
plt.ylabel('Latitude')
plt.title('Super_Highway_4_Lane_Cali_AVE_Percent_Occupied')
#plt.grid(True)
imageFILENAME_2 = 'V0.0.14.T_FATnet-AVE_Percent_Occupancy-2'
imagePATH_2 = str('/Sumo/runs/caliTEST-C/caliTEST-OUTPUT-C/Image_Files/'+imageFILENAME_2+'.png')
# plt.set_size_inches(9.5,8)
plt.savefig(imagePATH_2,dpi=120)

# Two subplots, the axes array is 1-d

plt.show()
# https://matplotlib.org/examples/pylab_examples/subplots_demo.html - How to have multi-plots

### WORKS ###
# Edge_0_0_to_0_1 = plt.plot([10.2,10.2], [20.83,78.15], linewidth=26.77)
# Edge_0_0_to_1_0 = plt.plot([20.055,78.15], [-10.2,-10.2], linewidth=10.94)
# Edge_0_1_to_0_0 = plt.plot([-10.2,-10.2], [78.15,20.83], linewidth=15.17)
# Edge_0_1_to_0_2 = plt.plot([10.2,10.2], [121.85,179.565], linewidth=1.1)
# Edge_0_1_to_1_1 = plt.plot([21.85,78.15], [89.8,89.8], linewidth=20.23)
# Edge_0_2_to_0_1 = plt.plot([-10.2,-10.2], [179.505,121.85], linewidth=26.07)
# Edge_0_2_to_1_2 = plt.plot([20.52,100], [189.8,189.8], linewidth=1.24)
# Edge_1_0_to_0_0 = plt.plot([78.15,20.015], [10.2,10.2], linewidth=23.26)
# Edge_1_0_to_1_1 = plt.plot([110.2,110.2], [21.85,78.15], linewidth=18.81)
# Edge_1_0_to_2_0 = plt.plot([121.85,200], [-10.2,-10.2], linewidth=0.19)
# Edge_1_1_to_0_1 = plt.plot([78.15,21.85], [110.2,110.2], linewidth=9.54)
# Edge_1_1_to_1_0 = plt.plot([89.8,89.8], [78.15,21.85], linewidth=5.39)
# Edge_1_1_to_2_1 = plt.plot([121.85,178.15], [89.8,89.8], linewidth=9.63)
# Edge_1_2_to_0_2 = plt.plot([100,20.52], [210.2,210.2], linewidth=24.05)
# Edge_1_2_to_2_2 = plt.plot([100,178.15], [189.8,189.8], linewidth=15.35)
# Edge_2_0_to_1_0 = plt.plot([200,121.85], [10.2,10.2], linewidth=19.29)
# Edge_2_0_to_3_0 = plt.plot([200,279.34], [-10.2,-10.2], linewidth=0.41)
# Edge_2_1_to_1_1 = plt.plot([178.15,121.85], [110.2,110.2], linewidth=13.92)
# Edge_2_1_to_2_2 = plt.plot([210.2,210.2], [121.85,178.15], linewidth=4.06)
# Edge_2_1_to_3_1 = plt.plot([221.85,278.15], [89.8,89.8], linewidth=5.15)
# Edge_2_2_to_1_2 = plt.plot([178.15,100], [210.2,210.2], linewidth=17.57)
# Edge_2_2_to_2_1 = plt.plot([189.8,189.8], [178.15,121.85], linewidth=25.22)
# Edge_2_2_to_3_2 = plt.plot([221.85,279.32], [189.8,189.8], linewidth=2.69)
# Edge_3_0_to_2_0 = plt.plot([279.4,200], [10.2,10.2], linewidth=9.21)
# Edge_3_0_to_3_1 = plt.plot([310.2,310.2], [20.48,78.15], linewidth=10.42)
# Edge_3_1_to_2_1 = plt.plot([278.15,221.85], [110.2,110.2], linewidth=4.05)
# Edge_3_1_to_3_0 = plt.plot([289.8,289.8], [78.15,20.48], linewidth=2.03)
# Edge_3_1_to_3_2 = plt.plot([310.2,310.2], [121.85,179.28], linewidth=2.67)
# Edge_3_2_to_2_2 = plt.plot([279.32,221.85], [210.2,210.2], linewidth=28.37)
# Edge_3_2_to_3_1 = plt.plot([289.8,289.8], [179.28,121.85], linewidth=4.98)
# Edge_FINISH = plt.plot([309.84,400], [209.84,300], linewidth=0.19)
# Edge_START = plt.plot([-100,-13.27], [-100,-13.275], linewidth=11.68)


# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')


# plt.plot([20.83,78.15],[10.2,10.2], linewidth=1.0, [-10.2,-10.2],[20.055,78.15], linewidth=1.0, [78.15,20.83],[-10.2,-10.2], linewidth=1.0, [121.85,179.565],[10.2,10.2], linewidth=1.0, [89.8,89.8],[21.85,78.15], linewidth=1.0, [179.505,121.85],[-10.2,-10.2], linewidth=1.0, [189.8,189.8],[20.52,100], linewidth=1.0, [10.2,10.2],[78.15,20.015], linewidth=1.0, [21.85,78.15],[110.2,110.2], linewidth=1.0, [-10.2,-10.2],[121.85,200], linewidth=1.0, [110.2,110.2],[78.15,21.85], linewidth=1.0, [78.15,21.85],[89.8,89.8], linewidth=1.0, [89.8,89.8],[121.85,178.15], linewidth=1.0, [210.2,210.2],[100,20.52], linewidth=1.0, [189.8,189.8],[100,178.15], linewidth=1.0, [10.2,10.2],[200,121.85], linewidth=1.0, [-10.2,-10.2],[200,279.34], linewidth=1.0, [110.2,110.2],[178.15,121.85], linewidth=1.0, [121.85,178.15],[210.2,210.2], linewidth=1.0, [89.8,89.8],[221.85,278.15], linewidth=1.0, [210.2,210.2],[178.15,100], linewidth=1.0, [178.15,121.85],[189.8,189.8], linewidth=1.0, [189.8,189.8],[221.85,279.32], linewidth=1.0, [10.2,10.2],[279.4,200], linewidth=1.0, [20.48,78.15],[310.2,310.2], linewidth=1.0, [110.2,110.2],[278.15,221.85], linewidth=1.0, [78.15,20.48],[289.8,289.8], linewidth=1.0, [121.85,179.28],[310.2,310.2], linewidth=1.0, [210.2,210.2],[279.32,221.85], linewidth=1.0, [179.28,121.85],[289.8,289.8], linewidth=1.0, [209.84,300],[309.84,400], linewidth=1.0, [-100,-13.275],[-100,-13.27], linewidth=1.0)
# plt.show()

# lines = plt.plot([20.83,78.15],[10.2,10.2], [-10.2,-10.2],[20.055,78.15], [78.15,20.83],[-10.2,-10.2], [121.85,179.565],[10.2,10.2], [89.8,89.8],[21.85,78.15], [179.505,121.85],[-10.2,-10.2], [189.8,189.8],[20.52,100], [10.2,10.2],[78.15,20.015], [21.85,78.15],[110.2,110.2], [-10.2,-10.2],[121.85,200], [110.2,110.2],[78.15,21.85], [78.15,21.85],[89.8,89.8], [89.8,89.8],[121.85,178.15], [210.2,210.2],[100,20.52], [189.8,189.8],[100,178.15], [10.2,10.2],[200,121.85], [-10.2,-10.2],[200,279.34], [110.2,110.2],[178.15,121.85], [121.85,178.15],[210.2,210.2], [89.8,89.8],[221.85,278.15], [210.2,210.2],[178.15,100], [178.15,121.85],[189.8,189.8], [189.8,189.8],[221.85,279.32], [10.2,10.2],[279.4,200], [20.48,78.15],[310.2,310.2], [110.2,110.2],[278.15,221.85], [78.15,20.48],[289.8,289.8], [121.85,179.28],[310.2,310.2], [210.2,210.2],[279.32,221.85], [179.28,121.85],[289.8,289.8], [209.84,300],[309.84,400], [-13.27,plt.plot([-100,-100,-13.27,-13.275])],[-100,-13.275])

# y1 = np.array([10.2, 20.055, -10.2, 10.2, 21.85, -10.2, 20.52, 78.15, 110.2, 121.85, 78.15, 89.8, 121.85, 100, 100, 200, 200, 178.15, 210.2, 221.85, 178.15, 189.8, 221.85, 279.4, 310.2, 278.15, 289.8, 310.2, 279.32, 289.8, 309.84, -100])
# x1 = np.array([20.83, -10.2, 78.15, 121.85, 89.8, 179.505, 189.8, 10.2, 21.85, -10.2, 110.2, 78.15, 89.8, 210.2, 189.8, 10.2, -10.2, 110.2, 121.85, 89.8, 210.2, 178.15, 189.8, 10.2, 20.48, 110.2, 78.15, 121.85, 210.2, 179.28, 209.84, -100])
# y2 = np.array([10.2, 78.15, -10.2, 10.2, 78.15, -10.2, 100, 20.015, 110.2, 200, 21.85, 89.8, 178.15, 20.52, 178.15, 121.85, 279.34, 121.85, 210.2, 278.15, 100, 189.8, 279.32, 200, 310.2, 221.85, 289.8, 310.2, 221.85, 289.8, 400, -13.27])
# x2 = np.array([78.15, -10.2, 20.83, 179.565, 89.8, 121.85, 189.8, 10.2, 78.15, -10.2, 110.2, 21.85, 89.8, 210.2, 189.8, 10.2, -10.2, 110.2, 178.15, 89.8, 210.2, 121.85, 189.8, 10.2, 78.15, 110.2, 20.48, 179.28, 210.2, 121.85, 300, -13.275])
# lines = plt.plot(x1, y1, x2, y2)
# # use keyword args
# #plt.setp(lines, color='b', linewidth=2.0)
# plt.show()


# ### From https://stackoverflow.com/questions/4805048/how-to-get-different-colored-lines-for-different-plots-in-a-single-figure
# import matplotlib.pyplot as plt
# import numpy as np




# fig1 = plt.figure()
# ax1 = fig1.add_subplot(111)
# for i in range(1,33):
    # ax1.plot(np.array([1,5])*i,label=i)
# colormap = plt.cm.gist_ncar #nipy_spectral, Set1,Paired   
# colors = [colormap(i) for i in np.linspace(0, 1,len(ax1.lines))]
# for i,j in enumerate(ax1.lines):
    # j.set_color(colors[i])
# ax1.legend(loc=2)

# #########################

# import matplotlib.pyplot as plt
# import numpy as np

# yPAIR = np.array([[10.2,10.2],[20.055,78.15],[-10.2,-10.2],[10.2,10.2],[21.85,78.15],[-10.2,-10.2],[20.52,100],[78.15,20.015],[110.2,110.2],[121.85,200],[78.15,21.85],[89.8,89.8],[121.85,178.15],[100,20.52],[100,178.15],[200,121.85],[200,279.34],[178.15,121.85],[210.2,210.2],[221.85,278.15],[178.15,100],[189.8,189.8],[221.85,279.32],[279.4,200],[310.2,310.2],[278.15,221.85],[289.8,289.8],[310.2,310.2],[279.32,221.85],[289.8,289.8],[309.84,400],[-100,-13.27]],dtype='int')

# xPAIR = np.array([[20.83,78.15],[-10.2,-10.2],[78.15,20.83],[121.85,179.565],[89.8,89.8],[179.505,121.85],[189.8,189.8],[10.2,10.2],[21.85,78.15],[-10.2,-10.2],[110.2,110.2],[78.15,21.85],[89.8,89.8],[210.2,210.2],[189.8,189.8],[10.2,10.2],[-10.2,-10.2],[110.2,110.2],[121.85,178.15],[89.8,89.8],[210.2,210.2],[178.15,121.85],[189.8,189.8],[10.2,10.2],[20.48,78.15],[110.2,110.2],[78.15,20.48],[121.85,179.28],[210.2,210.2],[179.28,121.85],[209.84,300],[-100,-13.275]],dtype='int')
# edgeLIST=('0_0-0_1', '0_0-1_0', '0_1-0_0', '0_1-0_2', '0_1-1_1', '0_2-0_1', '0_2-1_2', '1_0-0_0', '1_0-1_1', '1_0-2_0', '1_1-0_1', '1_1-1_0', '1_1-2_1', '1_2-0_2', '1_2-2_2', '2_0-1_0', '2_0-3_0', '2_1-1_1', '2_1-2_2', '2_1-3_1', '2_2-1_2', '2_2-2_1', '2_2-3_2', '3_0-2_0', '3_0-3_1', '3_1-2_1', '3_1-3_0', '3_1-3_2', '3_2-2_2', '3_2-3_1', 'FINISH', 'START')
# plt.plot(xPAIR[:,0], yPAIR[:,1])
# plt.show()

# num_plots = 32

# # Have a look at the colormaps here and decide which one you'd like:
# # http://matplotlib.org/1.2.1/examples/pylab_examples/show_colormaps.html
# colormap = plt.cm.gist_ncar
# #plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
# #plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, num_plots))))

# # Plot several different functions...
# x = np.arange(10)
# labels = []
# for i in range(1, 32):
    # plt.plot(xPAIR[:,0], yPAIR[:,1])
	# plt.plot(xPAIR[1,0], yPAIR[1,1])
	# plt.plot(xPAIR[2,0], yPAIR[2,1])
	# plt.plot(xPAIR[0,0], yPAIR[0,1])
# #    labels.append(r'$%edgeLIST[i]$' % (i, 5*i))
# plt.plot(xPAIR[:,0], yPAIR[:,1])
# plt.show()
# # I'm basically just demonstrating several different legend options here...
# plt.legend(labels, ncol=4, loc='upper center', 
           # bbox_to_anchor=[0.5, 1.1], 
           # columnspacing=1.0, labelspacing=0.0,
           # handletextpad=0.0, handlelength=1.5,
           # fancybox=True, shadow=True)

# plt.show()
# x1, y1, x2, y2
# plt.plot(int(xPAIR[1,0]), int(yPAIR[1,0]), int(xPAIR[1,1]), int(yPAIR[1,1]))
# plt.plot(int(xPAIR[2,0]), int(yPAIR[2,0]), int(xPAIR[2,1]), int(yPAIR[2,1]))
# plt.plot(int(xPAIR[0,0]), int(yPAIR[0,0]), int(xPAIR[0,1]), int(yPAIR[0,1]))
# plt.show()
# ####
# x = np.arange(10)
# labels = []
# for i in range(1, num_plots + 1):
    # plt.plot(x, i * x + 5 * i)
    # labels.append(r'$y = %ix + %i$' % (i, 5*i))

# # I'm basically just demonstrating several different legend options here...
# plt.legend(labels, ncol=4, loc='upper center', 
           # bbox_to_anchor=[0.5, 1.1], 
           # columnspacing=1.0, labelspacing=0.0,
           # handletextpad=0.0, handlelength=1.5,
           # fancybox=True, shadow=True)

# plt.show()

#junc_ID_X_Y = np.array([[0_0, 0.0, 0.0], ['0_1', 0.0, 100.0], ['0_2', 0.0, 200.0], ['1_0', 100.0, 0.0], ['1_1', 100.0, 100.0], ['1_2', 100.0, 200.0], ['2_0', 200.0, 0.0], ['2_1', 200.0, 100.0], ['2_2', 200.0, 200.0], ['3_0', 300.0, 0.0], ['3_1', 300.0, 100.0], ['3_2', 300.0, 200.0], ['FIN', 400.0, 300.0], ['STRT', -100.0, -100.0]])

# plt.plot([20.83,78.15], [10.2,10.2])
# plt.plot([-10.2,-10.2], [20.055,78.15])
# plt.plot([78.15,20.83], [-10.2,-10.2])
# plt.plot([121.85,179.565], [10.2,10.2])
# plt.plot([89.8,89.8], [21.85,78.15])
# plt.plot([179.505,121.85], [-10.2,-10.2])
# plt.plot([189.8,189.8], [20.52,100])
# plt.plot([10.2,10.2], [78.15,20.015])
# plt.plot([21.85,78.15], [110.2,110.2])
# plt.plot([-10.2,-10.2], [121.85,200])
# plt.plot([110.2,110.2], [78.15,21.85])
# plt.plot([78.15,21.85], [89.8,89.8])
# plt.plot([89.8,89.8], [121.85,178.15])
# plt.plot([210.2,210.2], [100,20.52])
# plt.plot([189.8,189.8], [100,178.15])
# plt.plot([10.2,10.2], [200,121.85])
# plt.plot([-10.2,-10.2], [200,279.34])
# plt.plot([110.2,110.2], [178.15,121.85])
# plt.plot([121.85,178.15], [210.2,210.2])
# plt.plot([89.8,89.8], [221.85,278.15])
# plt.plot([210.2,210.2], [178.15,100])
# plt.plot([178.15,121.85], [189.8,189.8])
# plt.plot([189.8,189.8], [221.85,279.32])
# plt.plot([10.2,10.2], [279.4,200])
# plt.plot([20.48,78.15], [310.2,310.2])
# plt.plot([110.2,110.2], [278.15,221.85])
# plt.plot([78.15,20.48], [289.8,289.8])
# plt.plot([121.85,179.28], [310.2,310.2])
# plt.plot([210.2,210.2], [279.32,221.85])
# plt.plot([179.28,121.85], [289.8,289.8])
# plt.plot([209.84,300], [309.84,400])
# plt.plot([-100,-13.275], [-100,-13.27])

# Edge_0_0_to_0_1 = plt.plot([10.2,10.2], [20.83,78.15], linewidth=1.0)
# Edge_0_0_to_1_0 = plt.plot([20.055,78.15], [-10.2,-10.2], linewidth=1.0)
# Edge_0_1_to_0_0 = plt.plot([-10.2,-10.2], [78.15,20.83], linewidth=1.0)
# Edge_0_1_to_0_2 = plt.plot([10.2,10.2], [121.85,179.565], linewidth=1.0)
# Edge_0_1_to_1_1 = plt.plot([21.85,78.15], [89.8,89.8], linewidth=1.0)
# Edge_0_2_to_0_1 = plt.plot([-10.2,-10.2], [179.505,121.85], linewidth=1.0)
# Edge_0_2_to_1_2 = plt.plot([20.52,100], [189.8,189.8], linewidth=1.0)
# Edge_1_0_to_0_0 = plt.plot([78.15,20.015], [10.2,10.2], linewidth=1.0)
# Edge_1_0_to_1_1 = plt.plot([110.2,110.2], [21.85,78.15], linewidth=1.0)
# Edge_1_0_to_2_0 = plt.plot([121.85,200], [-10.2,-10.2], linewidth=1.0)
# Edge_1_1_to_0_1 = plt.plot([78.15,21.85], [110.2,110.2], linewidth=1.0)
# Edge_1_1_to_1_0 = plt.plot([89.8,89.8], [78.15,21.85], linewidth=1.0)
# Edge_1_1_to_2_1 = plt.plot([121.85,178.15], [89.8,89.8], linewidth=1.0)
# Edge_1_2_to_0_2 = plt.plot([100,20.52], [210.2,210.2], linewidth=1.0)
# Edge_1_2_to_2_2 = plt.plot([100,178.15], [189.8,189.8], linewidth=1.0)
# Edge_2_0_to_1_0 = plt.plot([200,121.85], [10.2,10.2], linewidth=1.0)
# Edge_2_0_to_3_0 = plt.plot([200,279.34], [-10.2,-10.2], linewidth=1.0)
# Edge_2_1_to_1_1 = plt.plot([178.15,121.85], [110.2,110.2], linewidth=1.0)
# Edge_2_1_to_2_2 = plt.plot([210.2,210.2], [121.85,178.15], linewidth=1.0)
# Edge_2_1_to_3_1 = plt.plot([221.85,278.15], [89.8,89.8], linewidth=1.0)
# Edge_2_2_to_1_2 = plt.plot([178.15,100], [210.2,210.2], linewidth=1.0)
# Edge_2_2_to_2_1 = plt.plot([189.8,189.8], [178.15,121.85], linewidth=1.0)
# Edge_2_2_to_3_2 = plt.plot([221.85,279.32], [189.8,189.8], linewidth=1.0)
# Edge_3_0_to_2_0 = plt.plot([279.4,200], [10.2,10.2], linewidth=1.0)
# Edge_3_0_to_3_1 = plt.plot([310.2,310.2], [20.48,78.15], linewidth=1.0)
# Edge_3_1_to_2_1 = plt.plot([278.15,221.85], [110.2,110.2], linewidth=1.0)
# Edge_3_1_to_3_0 = plt.plot([289.8,289.8], [78.15,20.48], linewidth=1.0)
# Edge_3_1_to_3_2 = plt.plot([310.2,310.2], [121.85,179.28], linewidth=1.0)
# Edge_3_2_to_2_2 = plt.plot([279.32,221.85], [210.2,210.2], linewidth=1.0)
# Edge_3_2_to_3_1 = plt.plot([289.8,289.8], [179.28,121.85], linewidth=1.0)
# Edge_FINISH = plt.plot([309.84,400], [209.84,300], linewidth=1.0)
# Edge_START = plt.plot([-100,-13.27], [-100,-13.275], linewidth=1.0)






# for i in range(14):
	# xI = junc_ID_X_Y[i,1]
	# yI = junc_ID_X_Y[i,2]
	# print("Edgei =",junc_ID_X_Y[i,0],"xI = ",xI,"yI = ",yI)


# plt.show()
	
	
	
	
	# fig1 = plt.figure()
# ax1 = fig1.add_subplot(111)


# for i in range(1,15):
    # ax1.plot(np.array([1,5])*i,label=i)
	# print(np.array([1,5])*i,edgeLIST[i])
			# [1 5] 0_0-1_0
			# [ 2 10] 0_1-0_0
			# [ 3 15] 0_1-0_2
			# [ 4 20] 0_1-1_1
			# [ 5 25] 0_2-0_1
			# [ 6 30] 0_2-1_2
			# [ 7 35] 1_0-0_0
			# [ 8 40] 1_0-1_1
			# [ 9 45] 1_0-2_0
			# [10 50] 1_1-0_1
			# [11 55] 1_1-1_0
			# [12 60] 1_1-2_1
			# [13 65] 1_2-0_2
			# [14 70] 1_2-2_2


