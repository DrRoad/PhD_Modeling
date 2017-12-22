run /Sumo/SUMO-0.31.0/sumo-0.31.0/tools/visualization/plot_net_selection.py --net /GitHub/PhD_Modeling/Belmont_AOI_git/Belmont_AOI-runFILES/Belmount_AOI-V5.net.xml \
--selection /GitHub/PhD_Modeling/Belmont_AOI_git/Belmont_AOI_toolBOX/Plotting/BMAIO-Cali_3.4-EDGES \
 --xlabel [m] --ylabel [m] \
 --xticks 960,5100,1000,16 --yticks 1100,5990,1000,16 \
--selected-width 2 \
--selected-color #de0000 \
--edge-width .2 \


	
run /Sumo/SUMO-0.31.0/sumo-0.31.0/tools/visualization/plot_net_dump.py --net /GitHub/PhD_Modeling/Belmont_AOI_git/Belmont_AOI-runFILES/Belmount_AOI-V5.net.xml \
 --verbose \
 --xticks 960,5100,1000,16 --yticks 1100,5990,1000,16 \
 --measures speed,speed --xlabel [m] --ylabel [m] \
 --default-width 1 \
 --dump-inputs /Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-edgeFILES/BM_test-num_7-BM_test-num_13-30-min.xml,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-edgeFILES/BM_test-num_7-BM_test-num_13-30-min.xml \
 --output /Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-Images/BM_test-num_13-30-min-percent_DIFF.png \
 --colormap RdYlGn_r \
 --min-color-value -100 --max-color-value 101 \
 --max-width 3 --min-width -1 \
 -w .5 -c .5 \
 

 run /Sumo/SUMO-0.31.0/sumo-0.31.0/tools/visualization/plot_net_dump.py --net /GitHub/PhD_Modeling/Belmont_AOI_git/Belmont_AOI-runFILES/Belmount_AOI-V5.net.xml \
 --verbose \
 --xticks 960,5100,1000,16 --yticks 1100,5990,1000,16 \
 --measures speed,speed --xlabel [m] --ylabel [m] \
 --default-width 1 \
 --dump-inputs ,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-edgeFILES/BM_test-num_7-BM_test-num_13-30-min-MODELED-63000.xml,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-edgeFILES/BM_test-num_7-BM_test-num_13-30-min-MODELED-63000.xml \
 --output /Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-Images/BM_test-num_13-30-min-percent_DIFF.png \
  --min-color-value 29 --max-color-value 560 \
 --max-width 5 --min-width 1 \
 -w .5 -c .5 
 
 --colormap RdYlGn \
 --max-width-vaule 3 --min-width-value .5 \
 
 --colormap matplotlib.cm.RdYlGn_r \
 --colormap #0:#00c000,.25:#408040,.5:#808080,.75:#804040,1:#c00000 \
 --defaultwidth .5 --default-color #606060 \
 


--xlim 7000,14000 --ylim 9000,16000 -\


run /Sumo/SUMO-0.31.0/sumo-0.31.0/tools/visualization/plot_summary.py \
	-i /Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-summaryFILES/BM_test-num_4-newTLSallCAR-Summary_output.xml,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-summaryFILES/BM_test-num_5-Summary_output.xml,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-summaryFILES/BM_test-num_6-Summary_output.xml,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-summaryFILES/BM_test-num_13-15min_test_cars-Yroutes-Summary_output.xml,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-summaryFILES/BM_test-num_13-30min_test_cars-Yroutes-Summary_output.xml,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-summaryFILES/BM_test-num_13-60min_test_cars-Yroutes-Summary_output.xml \
	-l num_4,num_5,num_6_Short_Intervals,num_13-15min_test_cars-Yroutes,num_13-30min_test_cars-Yroutes,num_13-60min_test_cars-Yroutes --xlim 0,88400 --ylim 0,2100 \
	-o /Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-Images/Num_13_summary_running.png --yticks 0,2100,100,10 \
	--xticks 0,88401,14400,14 --xtime1 --ygrid \
	--ylabel "running vehicles [#]" --xlabel "time" \
	--title "Calibrators Pulsing running vehicles over time" --adjust .25,.2
	
	run /Sumo/SUMO-0.31.0/sumo-0.31.0/tools/visualization/plot_summary.py \
	-i /Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-summaryFILES/BM_test-num_4-newTLSallCAR-Summary_output.xml,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-summaryFILES/BM_test-num_5-Summary_output.xml,/Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-summaryFILES/BM_test-num_6-Summary_output.xml \
	-l num_4,num_5,num_6_Short_Intervals --xlim 0,88400 --ylim 0,2000 \
	-o /Sumo/runs/BelmontC_AOI_main/BelmontC_AOI-outPUT/BMAOI_C-Images/Num_13_summary_running.png --yticks 0,2001,100,10 \
	--xticks 0,88401,14400,14 --xtime1 --ygrid \
	--ylabel "running vehicles [#]" --xlabel "time" \
	--title "Running vehicles over time" --adjust .20,.2