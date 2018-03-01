import numpy as np
import pandas as pd

Calibrator_Dict ={1:'ConcrseDR_Belmont_MemHll_EB_02_33083', 2:'Wynn_GeogresLA_53rd_EB_05_37100', 3:'Belmont_Conshi_US1_NB_08_47340', 4:'Wynn_54th_PrkSD_BTH_EB_02_47475', 5:'Montgm_BelMan_76_ramps_EB_14_110747', 6:'Montgm_76_ramp_MLK_EB_14_110749', 7:'Wynn_PrkSD_Belmont_BTH_EB_15_118680', 8:'Girard_38th_34th_WB_2017_135477', 9:'ParkSide_52nd_Belmont_EB_2017_135473', 10:'Wynn_PrkSD_Belmont_BTH/2_EB_15_118680', 11:'Belmont_Wynn_PrkSD_NB_05_37671', 12:'Belmont_PennGRV_WYALUSING_NB_09_53494', 13:'Belmont_PrkSD_Monument_NB_09_53497', 14:'Belmont_BmontMansn_PrkSD_NB_09_53723', 15:'Belmont_Wynn_GrgHill_NB_10_67303', 16:'Belmont_Monmnt_Conshi_NB_12_87722', 17:'Belmont_PrkSD_GrgHill_NB_16_127934', 18:'Belmont_Stiles_Viola_NB_17_135471', 19:'Belmont_Wynn_PrkSD_SB_05_37672', 20:'Belmont_Conshi_US1_SB_08_47341', 21:'Belmont_PrkSD_Monument_SB_09_53496', 22:'Belmont_BmontMansn_PrkSD_SB_09_53723', 23:'Belmont_Wynn_GrgHill_SB_10_67304', 24:'Belmont_Lansdwn_States_SB_11_78089', 25:'Belmont_Monmnt_Conshi_SB_12_87723', 26:'Belmont_GrgHill_Monmnt_SB_16_127937', 27:'Belmont_Stiles_Viola_SB_17_135472', 28:'Parkside_limiter_SB_49940321#1', 29:'Parkside_limiter_1_SB_12184200#0', 30:'ConcrseDR_Belmont_MemHll_WB_02_33084', 31:'GrgeHill_Wynn_BTH_02_WB_33087', 32:'Wynn_GeogresLA_53rd_WB_05_37101', 33:'Montgm_BelMan_76_ramps_WB_14_110748', 34:'Montgm_76_ramp_MLK_WB_14_110750', 35:'ParkSide_52nd_Belmont_WB_2017_135473'}

Cali_copies_needed_Dict ={1:7, 2:14, 3:4, 4:14, 5:4, 6:2, 7:4, 8:8, 9:10, 10:9, 11:5, 12:11, 13:4, 14:4, 15:7, 16:4, 17:9, 18:8, 19:7, 20:6, 21:0, 22:5, 23:0, 24:3, 25:7, 26:8, 27:4, 28:3, 29:4, 30:5, 31:3, 32:1, 33:6, 34:10, 35:4} #needed 204

From_Where_Dict = {1:'-106455704#9' , 2:'-196358983#7' , 3:'196358956#0' , 4:'-196358983#4' , 5:'12180067#4' , 6:'43117623' , 7:'12180460#0' , 8:'134558408#1' , 9:'-388756837#2' , 10:'-12180460#1' , 11:'387423966' , 12:'12150712#4' , 13:'196358954#0' , 14:'424978644' , 15:'424978639.102' , 16:'196358954#1' , 17:'423967359#0' , 18:'423956980' , 19:'-387423966' , 20:'-196358956#2' , 21:'-196358954#3' , 22:'-423965484' , 23:'-49940170#0' , 24:'-423967359#1' , 25:'-448887868' , 26:'-424978642.170' , 27:'-423956982' , 28:'49940321#1' , 29:'12184200#0' , 30:'106455704#4' , 31:'49940069' , 32:'196358983#7' , 33:'-12180067#5' , 34:'-43117624#1' , 35:'62105282#0'}

sink_dict={1 :'-43117599',2 :'485212847#0',3 :'49887339.0',4 :'43357850#14.0',5 :'49321305',6 :'-43357850#4',7 :'196358965',8 :'-12150712#3',9 :'12327906#1',10:'12319898#1',11:'104526256-AddedOnRampEdge',12:'-448845166',13:'-43119842',14:'-42706763#2',15:'32121248#14',16:'196358983#8'}

cali_dict_II={}
for cali in range(35):
    cali_list=list()
    cali_dict_UDer ={}
    print("Calibrator_Dict[cali] = ",Calibrator_Dict[cali+1])
    if str(Calibrator_Dict[cali+1]) in list_Sink_1:
        cali_list.append('sink_dict[1]')
    if Calibrator_Dict[cali+1] in list_Sink_2:
            cali_list.append('sink_dict[2]')
    if Calibrator_Dict[cali+1] in list_Sink_3:
            cali_list.append('sink_dict[3]')
    if Calibrator_Dict[cali+1] in list_Sink_4:
            cali_list.append('sink_dict[4]')
    if Calibrator_Dict[cali+1] in list_Sink_5:
            cali_list.append('sink_dict[5]')
    if Calibrator_Dict[cali+1] in list_Sink_6:
            cali_list.append('sink_dict[6]')
    if Calibrator_Dict[cali+1] in list_Sink_7:
            cali_list.append('sink_dict[7]')
    if Calibrator_Dict[cali+1] in list_Sink_8:
            cali_list.append('sink_dict[8]')
    if Calibrator_Dict[cali+1] in list_Sink_9:
            cali_list.append('sink_dict[9]')
    if Calibrator_Dict[cali+1] in list_Sink_10:
            cali_list.append('sink_dict[10]')
    if Calibrator_Dict[cali+1] in list_Sink_11:
            cali_list.append('sink_dict[11]')
    if Calibrator_Dict[cali+1] in list_Sink_12:
            cali_list.append('sink_dict[12]')
    if Calibrator_Dict[cali+1] in list_Sink_13:
            cali_list.append('sink_dict[13]')
    if Calibrator_Dict[cali+1] in list_Sink_14:
            cali_list.append('sink_dict[14]')
    if Calibrator_Dict[cali+1] in list_Sink_15:
            cali_list.append('sink_dict[15]')
    if Calibrator_Dict[cali+1] in list_Sink_16:
            cali_list.append('sink_dict[16]')
    cali_dict_UDer = {Calibrator_Dict[cali+1]:cali_list}
    print(cali_dict_UDer)
    cali_dict_II.update(cali_dict_UDer)
