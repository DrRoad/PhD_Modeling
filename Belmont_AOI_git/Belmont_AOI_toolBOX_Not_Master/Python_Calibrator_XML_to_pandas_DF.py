
# coding: utf-8

# # Last worked on 2/28/2018
# # Save the DVRPC traffic count data as a PDF. Remove the bars with select
# # object. Save as a .txt file. Do some regrex magic to change variable names and make them on their own line. Then just run read_n_record_cali_vph_file(cali_raw_TXTPATH,recNUM_LIST):
# # read_n_save_Cali_runFILE(): can extract xml files and bring into a Python3 Pandas Dataframe object

# In[1]:

import numpy as np
import traci
import traci.constants as tc
import re
import time
import sumolib
# import cProfile, pstats , io
import pandas as pd
# import sumoPython_git_A as SP
import openpyxl as OPENxlsx
pd.set_option('display.max_columns', 99,'display.max_rows', 99)


# In[2]:

cali_TEMP = pd.read_excel("C:\Dropbox\Phd_R_Ms\PhD_Modeling_DB_GIT\BMAOI_Dbox-DataFrames\Calibrator_Master_V3.xlsx")
# recNUM_LIST_OLD = ['33083', '33084', '33087', '37100', '37101', '37671', '37672', '47340', '47341', '47475', '53494', '53497', '53496', '53723', '53723', '67303', '67304', '78089', '87722', '87723', '110747', '110748', '110749', '110750', '118680', '127934', '127937', '135472', '135471', '135477', '135473', '135473', '118680']
recNUM_LIST = ['33083', '33084', '33087', '37100', '37101', '37671', '37672', '47340', '47341', '47475', '53494', '53497', '53496', '53723a', '53723', '67303', '67304', '78089', '87722', '87723', '110747', '110748', '110749', '110750', '118680a', '127934', '127937', '135472', '135471', '135477', '33087a','33087b','135473a', '135473b', '118680']
cali_raw_TXTPATH = '/Dropbox/Phd_R_Ms/SUMO_DB_root/Belmont_Ave-Run/DVRPC-Traffic_Count_Data-Belmount-AOI/Selected_Small_Belmount_AOI_ALL-class-turn-volume_MOD.txt'


# In[3]:

cali_TEMP_DICT = dict()
for columns in cali_TEMP:
    if cali_TEMP.loc['RECORDNUM',columns] in recNUM_LIST:
        cali_TEMP_DICT.update({str(cali_TEMP.loc['RECORDNUM',columns]):str(columns)})
#         print(columns, cali_TEMP.loc['RECORDNUM',columns])
print(cali_TEMP_DICT)
print(cali_TEMP.columns)
recNum = '33083'
print(cali_TEMP_DICT[recNum])
# cali_TEMP.loc['RECORDNUM',30]# in recNUM_LIST
# cali_TEMP.iloc[cali_TEMP.index.get_loc('RECORDNUM'),int(cali_TEMP_DICT[recNum])] = 'pee'
# cali_TEMP
# cali_TEMP_DICT = {'37101': '4', '37672': '6', '53723': '14', '110748': '21', '47341': '8', '87723': '19', '33083': '0', '135471': '28', '110747': '20', '33087': '2', '53494': '10', '110749': '22', '53497': '11', '37100': '3', '33084': '1', '53496': '12', '78089': '17', '127934': '25', '110750': '23', '37671': '5', '47475': '9', '135472': '27', '127937': '26', '87722': '18', '47340': '7', '67304': '16', '118680': '34', '135473': '33', '67303': '15'}


# In[ ]:




# In[4]:

def read_n_record_cali_vph_file(cali_raw_TXTPATH,recNUM_LIST):
    cali_TEMP_DICT = dict()
    for columns in cali_TEMP:
        if cali_TEMP.loc['RECORDNUM',columns] in recNUM_LIST:
            cali_TEMP_DICT.update({str(cali_TEMP.loc['RECORDNUM',columns]):str(columns)})
    #         print(columns, cali_TEMP.loc['RECORDNUM',columns])
    for recNum in recNUM_LIST:
#         counter +=1
        last_char = recNUM_LIST[int(cali_TEMP_DICT[recNum])][len(recNUM_LIST[int(cali_TEMP_DICT[recNum])])-1:len(recNUM_LIST[int(cali_TEMP_DICT[recNum])])]
        if re.search('[a-z]',last_char):
            recNuma = recNUM_LIST[int(cali_TEMP_DICT[recNum])][1:len(recNUM_LIST[int(cali_TEMP_DICT[recNum])])-1]
            print("Rerouting ",recNum," is now ", recNuma)
#         if recNum == '135473a': #'135473a', '135473b',
#             recNuma = '135473' #recNUM_LIST[recNum][1:len(recNUM_LIST[recNum])-1]
#         elif recNum == '135473b':
#             recNuma = '135473'
        else:
            recNuma = recNum
        with open(cali_raw_TXTPATH) as f:
            print("Searching for ",recNum)
            capture = 0
            for line in f:
                if recNuma in line:
#                     print(line)
                    capture = 1
                    AM = 1
                    PM = 0
#                     counter += 1
                    print("\n<><> CAPTURING ", recNum, " and storing in column ", cali_TEMP_DICT[recNum])
                    RECORDNUM_LINE = line
                    RECORDNUM_ID = re.search("DVRPC_FILE_NUM: (.*)", RECORDNUM_LINE, re.IGNORECASE).group(1)
                    print("RECORDNUM_ID = ",RECORDNUM_ID, end="; ")
                    cali_TEMP.iloc[cali_TEMP.index.get_loc('rec_Check'),int(cali_TEMP_DICT[recNum])] = RECORDNUM_ID
#                     cali_TEMP.loc['rec_Check',cali_TEMP_DICT[recNum]] = RECORDNUM_ID
#                     cali_TEMP.loc['rec_Check',cali_TEMP['RECORDNUM'].str.contains(recNum)] = RECORDNUM_ID
#                     print("rec_Check = be true.. ", str(RECORDNUM_ID) == str(recNum),RECORDNUM_ID,"=?=",recNum)
#                 elif 'TO:' in line:
#                     TO_LINE = line
#                     TO_rd = re.search("TO: (.*)", TO_LINE, re.IGNORECASE).group(1)
#                     cali_TEMP.loc['TO',cali_TEMP_DICT[recNum]] = TO_rd
#                     print(TO_rd)
#                 elif 'FROM:' in line:
#                     FROM_LINE = line
#                     FROM_rd = re.search("FROM: (.*)", FROM_LINE, re.IGNORECASE).group(1)
#                     cali_TEMP.loc['FROM',cali_TEMP_DICT[recNum]] = FROM_rd   
#                     print(FROM_rd)
                if capture == 1:
                    if 'AXLE_CORR_FACTOR:' in line:
                        AXLE_CORR_FACTOR_LINE = line
                        AXLE_CORR_FACTOR_numb = re.search("AXLE_CORR_FACTOR: (.*)", AXLE_CORR_FACTOR_LINE, re.IGNORECASE).group(1)
#                         cali_TEMP.loc['AXLE_CORR_FACTOR',cali_TEMP_DICT[recNum]] = AXLE_CORR_FACTOR_numb
                        cali_TEMP.iloc[cali_TEMP.index.get_loc('AXLE_CORR_FACTOR'),int(cali_TEMP_DICT[recNum])] = AXLE_CORR_FACTOR_numb
                        print("AXLE_CORR_FACTOR_numb = ", AXLE_CORR_FACTOR_numb, end="; ")
                    elif 'AADT:' in line:
                        AADT_LINE = line
                        AADT_numb = re.search("AADT: (.*)", AADT_LINE, re.IGNORECASE).group(1)
#                         cali_TEMP.loc['AADT',cali_TEMP_DICT[recNum]] = AADT_numb
                        cali_TEMP.iloc[cali_TEMP.index.get_loc('AADT'),int(cali_TEMP_DICT[recNum])] = AADT_numb
                        print("AADT = ", AADT_numb, end="; ")
                    elif 'AM_Peak_prct:' in line:
                        AM_Peak_prct_LINE = line
                        AM_Peak_prct_numb = re.search("AM_Peak_prct: (.*)", AM_Peak_prct_LINE, re.IGNORECASE).group(1)
#                         cali_TEMP.loc['AM_Peak_prct',cali_TEMP_DICT[recNum]] = AM_Peak_prct_numb
                        cali_TEMP.iloc[cali_TEMP.index.get_loc('AM_Peak_prct'),int(cali_TEMP_DICT[recNum])] = AM_Peak_prct_numb
                        print("AM_Peak_prct_numb = ",AM_Peak_prct_numb, end="; ")
                    elif 'Hour_Beginning:' in line:
                            Hour_Beginning_LINE = line
                            Hour_Beginning_numb = re.search("Hour_Beginning: (.*)", Hour_Beginning_LINE, re.IGNORECASE).group(1)
                            if Hour_Beginning_numb[len(Hour_Beginning_numb)-2:len(Hour_Beginning_numb)] == 'AM':
                                cali_TEMP.iloc[cali_TEMP.index.get_loc('Hour_Beginning_AM'),int(cali_TEMP_DICT[recNum])] = Hour_Beginning_numb
                                print("Hour_Beginning...AM = ",Hour_Beginning_numb, end="; ")
                            else:
                                cali_TEMP.iloc[cali_TEMP.index.get_loc('Hour_Beginning_PM'),int(cali_TEMP_DICT[recNum])] = Hour_Beginning_numb
                                print("Hour_Beginning...PM = ",Hour_Beginning_numb, end="\n")
                    elif 'SEASONAL_FACTOR:' in line:
                        SEASONAL_FACTOR_LINE = line
                        SEASONAL_FACTOR_numb = re.search("SEASONAL_FACTOR: (.*)", SEASONAL_FACTOR_LINE, re.IGNORECASE).group(1)
#                         cali_TEMP.loc['SEASONAL_FACTOR',cali_TEMP_DICT[recNum]] = SEASONAL_FACTOR_numb
                        cali_TEMP.iloc[cali_TEMP.index.get_loc('SEASONAL_FACTOR'),int(cali_TEMP_DICT[recNum])] = SEASONAL_FACTOR_numb
                        print("SEASONAL_FACTOR_numb = ",SEASONAL_FACTOR_numb, end="; ")
                    elif 'PM_Peak_prct:' in line:
                        PM_Peak_prct_LINE = line
                        PM_Peak_prct_numb = re.search("PM_Peak_prct: (.*)", PM_Peak_prct_LINE, re.IGNORECASE).group(1)
#                         cali_TEMP.loc['PM_Peak_prct',cali_TEMP_DICT[recNum]] = PM_Peak_prct_numb
                        cali_TEMP.iloc[cali_TEMP.index.get_loc('PM_Peak_prct'),int(cali_TEMP_DICT[recNum])] = PM_Peak_prct_numb
                        print("PM_Peak_prct_numb = ",PM_Peak_prct_numb, end="; ")
#                     elif 'Hour_Beginning:' in line:
#                         if PM == 1:
#                             Hour_Beginning_LINE =line
#                             Hour_Beginning_numb = re.search("Hour_Beginning: (.*)", Hour_Beginning_LINE, re.IGNORECASE).group(1)
#     #                         cali_TEMP.loc['Hour_Beginning',cali_TEMP_DICT[recNum]] = Hour_Beginning_numb
#                             cali_TEMP.iloc[cali_TEMP.index.get_loc('Hour_Beginning'),int(cali_TEMP_DICT[recNum])] = Hour_Beginning_numb
#                             print("Hour_Beginning...PM = ",Hour_Beginning_numb, end="\n")
# 
                    elif 'TAKEN BY' in line:
                        capture = 0
#                     counter += 1
                        print("\n\t\t\tabove was\n\t\t\t<><>",recNum,"<><>\n")# counter = ",counter,"\n")
    return cali_TEMP


# In[ ]:

# bigstring = open(cali_raw_TXTPATH)
# # bigstring.readlines()


# In[5]:

cal_DF = read_n_record_cali_vph_file(cali_raw_TXTPATH,recNUM_LIST)


# In[7]:

pd.DataFrame.to_excel(cali_TEMP,'C:\Dropbox\Phd_R_Ms\PhD_Modeling_DB_GIT\BMAOI_Dbox-DataFrames\Calibrator_Master_V3.xlsx')
# 


# In[6]:

cali_TEMP


# In[ ]:

# print(int(cali_TEMP_DICT['118680a']))
# recc = '118680a'
# # recNUM_LIST[recc][1:len(recNUM_LIST[recc])-1]
# # len(int(recNUM_LIST[cali_TEMP_DICT[recc]]))-1
# # int(recNUM_LIST[int(cali_TEMP_DICT[recc])])
# # recNUM_LIST[int(recNUM_LIST[int(cali_TEMP_DICT[recc])])]
# last_char = recNUM_LIST[int(cali_TEMP_DICT[recc])][len(recNUM_LIST[int(cali_TEMP_DICT[recc])])-1:len(recNUM_LIST[int(cali_TEMP_DICT[recc])])]#[len(recNUM_LIST[recc])-1:len(recNUM_LIST[recc])]
# if re.search('[a-z]',last_char):
#     print("Rerouting", recNUM_LIST[int(cali_TEMP_DICT[recc])][1:len(recNUM_LIST[int(cali_TEMP_DICT[recc])])-1])
    
# # re.search('[a-z]',pp)
# with open(cali_raw_TXTPATH) as f:
#     print("Searching for ",recNum)
#     capture = 0
#     for line in f:
#         if 'Hour_Beginning:' in line:
#             Hour_Beginning_LINE = line
#             Hour_Beginning_numb = re.search("Hour_Beginning: (.*)", Hour_Beginning_LINE, re.IGNORECASE).group(1)
#             if Hour_Beginning_numb[len(Hour_Beginning_numb)-2:len(Hour_Beginning_numb)] == 'AM':
#                 print(line)
# print(cali_TEMP.loc['RECORDNUM',0])
# print(cali_TEMP.loc['RECORDNUM'].str.contains(recNUM_LIST[0]))
# cali_TEMP.iloc[:,cali_TEMP['RECORDNUM'].str.contains(recNUM_LIST[0])==True]
# # cali_TEMP.loc['rec_Check',cali_TEMP['RECORDNUM'].str.contains(recNum)] = RECORDNUM_ID
# cal_DF.loc['rec_Check',2]
# print(recNUM_LIST[0])
# # cali_TEMP.loc[cali_TEMP['RECORDNUM'].str.contains(recNum),'rec_Check'] = recNum
# print(cal_DF.loc['RECORDNUM',0]==recNUM_LIST[0])
# # cal_DF.loc['RECORDNUM',cal_DF.loc['RECORDNUM'].str.contains(recNum)]
# cal_DF.loc['RECORDNUM'].str.contains(recNUM_LIST[0])
# # cal_DF.loc['RECORDNUM',0] =str(cal_DF.loc['RECORDNUM',0])


# In[ ]:

def read_n_save_Cali_runFILE():
    SUMO_outPUT_PREFIX = "TESTii"
    PATH_cali_MASTER_TEMPLATExlsx = '/Dropbox/Phd_R_Ms/Asset_Use_N_Management_Complete_Model/DropBox_ToolBox__MASTER__refresh_with_GIT/Calibrator_Master_TEMPLATE.xlsx'
    PATH_to_Save_to = "/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/BMAOI_Dbox-DataFrames/Network_" + SUMO_outPUT_PREFIX + "_Calibrator_XML_extract.xlsx"
    logger_TEMPDF =pd.read_excel(PATH_cali_MASTER_TEMPLATExlsx)
#         global SUMO_outPUT_PREFIX
#         global SUMO_Traci_PORT
    counter = 0
    readfromPATH = '/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/Belmont_AOI_git/Belmont_AOI_toolBOX/Belmount_AOI-caliborators-DB-V6-SUMO31-15min_RAW.xml'
    with open(readfromPATH) as f:
    #open('/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/Belmont_AOI_git/Belmont_AOI-runFILES/BMAOI_TRACI_DB.sumocfg') as f:
        termLIST = list()
        termcounter = 0
        for line in f:
            # print("SUMO_outPUT_PREFIX = ",SUMO_outPUT_PREFIX)
            # if SUMO_outPUT_PREFIX =="":
#                 routeProbe id="ConcrseDR-Belmont-MemHll-EB-02-RouteProbe" edge="-106455704#9"
            if '<routeProbe id="' in line:
                counter += 1
#                     print(line)
                routeProbe_ID_LINE = line
                routeProbe_ID = re.search('<routeProbe id="(.*)" e',routeProbe_ID_LINE, re.IGNORECASE).group(1)
                termLIST.append(re.search('<routeProbe id="(.*)" e',routeProbe_ID_LINE, re.IGNORECASE).group(1))
                logger_TEMPDF.loc['routeProbe_ID',counter-1] = routeProbe_ID
#                     routeProbe_ID = termLIST[0]
                # print("\nSUMO_outPUT_PREFIX = ",SUMO_outPUT_PREFIX,"\n")
                termcounter +=1
            elif '<calibrator id=' in line:
                calibrator_ID_LINE = line
                calibrator_ID = re.search('<calibrator id="(.*)" edge="(.*)" p',calibrator_ID_LINE, re.IGNORECASE).group(1)
                termLIST.append(re.search('<calibrator id="(.*)" edge="(.*)" p',calibrator_ID_LINE, re.IGNORECASE).group(1))
                calibrator_ID_edge = re.search('<calibrator id="(.*)" edge="(.*)" p',calibrator_ID_LINE, re.IGNORECASE).group(2)
                termLIST.append(re.search('<calibrator id="(.*)" edge="(.*)" p',calibrator_ID_LINE, re.IGNORECASE).group(2))
                logger_TEMPDF.loc['calibrator_ID',counter-1] = calibrator_ID
                logger_TEMPDF.loc['SUMO_edge_ID',counter-1] = calibrator_ID_edge
#                 elif '<flow begin="1"' in line:
# #                     print(line)
# #                     print(re.search('<flow begin="1" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', line, re.IGNORECASE).group(3))
#                     flow_vph_1_ID_LINE = line
#                     flow_vph_1_ID = re.search('<flow begin="1" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_1_ID_LINE, re.IGNORECASE).group(3)
#                     termLIST.append(re.search('<flow begin="1" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_1_ID_LINE, re.IGNORECASE).group(3))
#                     logger_TEMPDF.loc['vph_start_1',counter-1] = flow_vph_1_ID
            elif '<flow begin="1"' in line:
                flow_vph_1_ID_LINE = line
                flow_vph_1_ID = re.search('<flow begin="1" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_1_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="1" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_1_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_1', counter-1] = flow_vph_1_ID
            elif '<flow begin="901"' in line:
                flow_vph_901_ID_LINE = line
                flow_vph_901_ID = re.search('<flow begin="901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_901', counter-1] = flow_vph_901_ID
            elif '<flow begin="1801"' in line:
                flow_vph_1801_ID_LINE = line
                flow_vph_1801_ID = re.search('<flow begin="1801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_1801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="1801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_1801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_1801', counter-1] = flow_vph_1801_ID
            elif '<flow begin="2701"' in line:
                flow_vph_2701_ID_LINE = line
                flow_vph_2701_ID = re.search('<flow begin="2701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_2701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="2701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_2701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_2701', counter-1] = flow_vph_2701_ID
            elif '<flow begin="3601"' in line:
                flow_vph_3601_ID_LINE = line
                flow_vph_3601_ID = re.search('<flow begin="3601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_3601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="3601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_3601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_3601', counter-1] = flow_vph_3601_ID
            elif '<flow begin="4501"' in line:
                flow_vph_4501_ID_LINE = line
                flow_vph_4501_ID = re.search('<flow begin="4501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_4501_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="4501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_4501_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_4501', counter-1] = flow_vph_4501_ID
            elif '<flow begin="5401"' in line:
                flow_vph_5401_ID_LINE = line
                flow_vph_5401_ID = re.search('<flow begin="5401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_5401_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="5401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_5401_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_5401', counter-1] = flow_vph_5401_ID
            elif '<flow begin="6301"' in line:
                flow_vph_6301_ID_LINE = line
                flow_vph_6301_ID = re.search('<flow begin="6301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_6301_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="6301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_6301_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_6301', counter-1] = flow_vph_6301_ID
            elif '<flow begin="7201"' in line:
                flow_vph_7201_ID_LINE = line
                flow_vph_7201_ID = re.search('<flow begin="7201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_7201_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="7201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_7201_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_7201', counter-1] = flow_vph_7201_ID
            elif '<flow begin="8101"' in line:
                flow_vph_8101_ID_LINE = line
                flow_vph_8101_ID = re.search('<flow begin="8101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_8101_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="8101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_8101_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_8101', counter-1] = flow_vph_8101_ID
            elif '<flow begin="9001"' in line:
                flow_vph_9001_ID_LINE = line
                flow_vph_9001_ID = re.search('<flow begin="9001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_9001_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="9001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_9001_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_9001', counter-1] = flow_vph_9001_ID
            elif '<flow begin="9901"' in line:
                flow_vph_9901_ID_LINE = line
                flow_vph_9901_ID = re.search('<flow begin="9901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_9901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="9901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_9901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_9901', counter-1] = flow_vph_9901_ID
            elif '<flow begin="10801"' in line:
                flow_vph_10801_ID_LINE = line
                flow_vph_10801_ID = re.search('<flow begin="10801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_10801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="10801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_10801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_10801', counter-1] = flow_vph_10801_ID
            elif '<flow begin="11701"' in line:
                flow_vph_11701_ID_LINE = line
                flow_vph_11701_ID = re.search('<flow begin="11701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_11701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="11701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_11701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_11701', counter-1] = flow_vph_11701_ID
            elif '<flow begin="12601"' in line:
                flow_vph_12601_ID_LINE = line
                flow_vph_12601_ID = re.search('<flow begin="12601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_12601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="12601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_12601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_12601', counter-1] = flow_vph_12601_ID
            elif '<flow begin="13501"' in line:
                flow_vph_13501_ID_LINE = line
                flow_vph_13501_ID = re.search('<flow begin="13501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_13501_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="13501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_13501_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_13501', counter-1] = flow_vph_13501_ID
            elif '<flow begin="14401"' in line:
                flow_vph_14401_ID_LINE = line
                flow_vph_14401_ID = re.search('<flow begin="14401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_14401_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="14401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_14401_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_14401', counter-1] = flow_vph_14401_ID
            elif '<flow begin="15301"' in line:
                flow_vph_15301_ID_LINE = line
                flow_vph_15301_ID = re.search('<flow begin="15301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_15301_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="15301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_15301_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_15301', counter-1] = flow_vph_15301_ID
            elif '<flow begin="16201"' in line:
                flow_vph_16201_ID_LINE = line
                flow_vph_16201_ID = re.search('<flow begin="16201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_16201_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="16201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_16201_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_16201', counter-1] = flow_vph_16201_ID
            elif '<flow begin="17101"' in line:
                flow_vph_17101_ID_LINE = line
                flow_vph_17101_ID = re.search('<flow begin="17101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_17101_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="17101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_17101_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_17101', counter-1] = flow_vph_17101_ID
            elif '<flow begin="18001"' in line:
                flow_vph_18001_ID_LINE = line
                flow_vph_18001_ID = re.search('<flow begin="18001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_18001_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="18001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_18001_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_18001', counter-1] = flow_vph_18001_ID
            elif '<flow begin="18901"' in line:
                flow_vph_18901_ID_LINE = line
                flow_vph_18901_ID = re.search('<flow begin="18901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_18901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="18901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_18901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_18901', counter-1] = flow_vph_18901_ID
            elif '<flow begin="19801"' in line:
                flow_vph_19801_ID_LINE = line
                flow_vph_19801_ID = re.search('<flow begin="19801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_19801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="19801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_19801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_19801', counter-1] = flow_vph_19801_ID
            elif '<flow begin="20701"' in line:
                flow_vph_20701_ID_LINE = line
                flow_vph_20701_ID = re.search('<flow begin="20701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_20701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="20701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_20701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_20701', counter-1] = flow_vph_20701_ID
            elif '<flow begin="21601"' in line:
                flow_vph_21601_ID_LINE = line
                flow_vph_21601_ID = re.search('<flow begin="21601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_21601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="21601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_21601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_21601', counter-1] = flow_vph_21601_ID
            elif '<flow begin="22501"' in line:
                flow_vph_22501_ID_LINE = line
                flow_vph_22501_ID = re.search('<flow begin="22501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_22501_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="22501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_22501_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_22501', counter-1] = flow_vph_22501_ID
            elif '<flow begin="23401"' in line:
                flow_vph_23401_ID_LINE = line
                flow_vph_23401_ID = re.search('<flow begin="23401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_23401_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="23401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_23401_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_23401', counter-1] = flow_vph_23401_ID
            elif '<flow begin="24301"' in line:
                flow_vph_24301_ID_LINE = line
                flow_vph_24301_ID = re.search('<flow begin="24301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_24301_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="24301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_24301_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_24301', counter-1] = flow_vph_24301_ID
            elif '<flow begin="25201"' in line:
                flow_vph_25201_ID_LINE = line
                flow_vph_25201_ID = re.search('<flow begin="25201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_25201_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="25201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_25201_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_25201', counter-1] = flow_vph_25201_ID
            elif '<flow begin="26101"' in line:
                flow_vph_26101_ID_LINE = line
                flow_vph_26101_ID = re.search('<flow begin="26101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_26101_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="26101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_26101_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_26101', counter-1] = flow_vph_26101_ID
            elif '<flow begin="27001"' in line:
                flow_vph_27001_ID_LINE = line
                flow_vph_27001_ID = re.search('<flow begin="27001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_27001_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="27001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_27001_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_27001', counter-1] = flow_vph_27001_ID
            elif '<flow begin="27901"' in line:
                flow_vph_27901_ID_LINE = line
                flow_vph_27901_ID = re.search('<flow begin="27901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_27901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="27901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_27901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_27901', counter-1] = flow_vph_27901_ID
            elif '<flow begin="28801"' in line:
                flow_vph_28801_ID_LINE = line
                flow_vph_28801_ID = re.search('<flow begin="28801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_28801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="28801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_28801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_28801', counter-1] = flow_vph_28801_ID
            elif '<flow begin="29701"' in line:
                flow_vph_29701_ID_LINE = line
                flow_vph_29701_ID = re.search('<flow begin="29701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_29701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="29701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_29701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_29701', counter-1] = flow_vph_29701_ID
            elif '<flow begin="30601"' in line:
                flow_vph_30601_ID_LINE = line
                flow_vph_30601_ID = re.search('<flow begin="30601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_30601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="30601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_30601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_30601', counter-1] = flow_vph_30601_ID
            elif '<flow begin="31501"' in line:
                flow_vph_31501_ID_LINE = line
                flow_vph_31501_ID = re.search('<flow begin="31501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_31501_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="31501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_31501_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_31501', counter-1] = flow_vph_31501_ID
            elif '<flow begin="32401"' in line:
                flow_vph_32401_ID_LINE = line
                flow_vph_32401_ID = re.search('<flow begin="32401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_32401_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="32401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_32401_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_32401', counter-1] = flow_vph_32401_ID
            elif '<flow begin="33301"' in line:
                flow_vph_33301_ID_LINE = line
                flow_vph_33301_ID = re.search('<flow begin="33301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_33301_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="33301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_33301_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_33301', counter-1] = flow_vph_33301_ID
            elif '<flow begin="34201"' in line:
                flow_vph_34201_ID_LINE = line
                flow_vph_34201_ID = re.search('<flow begin="34201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_34201_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="34201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_34201_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_34201', counter-1] = flow_vph_34201_ID
            elif '<flow begin="35101"' in line:
                flow_vph_35101_ID_LINE = line
                flow_vph_35101_ID = re.search('<flow begin="35101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_35101_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="35101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_35101_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_35101', counter-1] = flow_vph_35101_ID
            elif '<flow begin="36001"' in line:
                flow_vph_36001_ID_LINE = line
                flow_vph_36001_ID = re.search('<flow begin="36001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_36001_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="36001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_36001_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_36001', counter-1] = flow_vph_36001_ID
            elif '<flow begin="36901"' in line:
                flow_vph_36901_ID_LINE = line
                flow_vph_36901_ID = re.search('<flow begin="36901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_36901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="36901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_36901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_36901', counter-1] = flow_vph_36901_ID
            elif '<flow begin="37801"' in line:
                flow_vph_37801_ID_LINE = line
                flow_vph_37801_ID = re.search('<flow begin="37801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_37801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="37801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_37801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_37801', counter-1] = flow_vph_37801_ID
            elif '<flow begin="38701"' in line:
                flow_vph_38701_ID_LINE = line
                flow_vph_38701_ID = re.search('<flow begin="38701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_38701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="38701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_38701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_38701', counter-1] = flow_vph_38701_ID
            elif '<flow begin="39601"' in line:
                flow_vph_39601_ID_LINE = line
                flow_vph_39601_ID = re.search('<flow begin="39601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_39601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="39601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_39601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_39601', counter-1] = flow_vph_39601_ID
            elif '<flow begin="40501"' in line:
                flow_vph_40501_ID_LINE = line
                flow_vph_40501_ID = re.search('<flow begin="40501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_40501_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="40501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_40501_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_40501', counter-1] = flow_vph_40501_ID
            elif '<flow begin="41401"' in line:
                flow_vph_41401_ID_LINE = line
                flow_vph_41401_ID = re.search('<flow begin="41401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_41401_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="41401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_41401_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_41401', counter-1] = flow_vph_41401_ID
            elif '<flow begin="42301"' in line:
                flow_vph_42301_ID_LINE = line
                flow_vph_42301_ID = re.search('<flow begin="42301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_42301_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="42301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_42301_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_42301', counter-1] = flow_vph_42301_ID
            elif '<flow begin="43201"' in line:
                flow_vph_43201_ID_LINE = line
                flow_vph_43201_ID = re.search('<flow begin="43201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_43201_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="43201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_43201_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_43201', counter-1] = flow_vph_43201_ID
            elif '<flow begin="44101"' in line:
                flow_vph_44101_ID_LINE = line
                flow_vph_44101_ID = re.search('<flow begin="44101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_44101_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="44101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_44101_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_44101', counter-1] = flow_vph_44101_ID
            elif '<flow begin="45001"' in line:
                flow_vph_45001_ID_LINE = line
                flow_vph_45001_ID = re.search('<flow begin="45001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_45001_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="45001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_45001_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_45001', counter-1] = flow_vph_45001_ID
            elif '<flow begin="45901"' in line:
                flow_vph_45901_ID_LINE = line
                flow_vph_45901_ID = re.search('<flow begin="45901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_45901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="45901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_45901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_45901', counter-1] = flow_vph_45901_ID
            elif '<flow begin="46801"' in line:
                flow_vph_46801_ID_LINE = line
                flow_vph_46801_ID = re.search('<flow begin="46801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_46801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="46801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_46801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_46801', counter-1] = flow_vph_46801_ID
            elif '<flow begin="47701"' in line:
                flow_vph_47701_ID_LINE = line
                flow_vph_47701_ID = re.search('<flow begin="47701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_47701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="47701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_47701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_47701', counter-1] = flow_vph_47701_ID
            elif '<flow begin="48601"' in line:
                flow_vph_48601_ID_LINE = line
                flow_vph_48601_ID = re.search('<flow begin="48601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_48601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="48601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_48601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_48601', counter-1] = flow_vph_48601_ID
            elif '<flow begin="49501"' in line:
                flow_vph_49501_ID_LINE = line
                flow_vph_49501_ID = re.search('<flow begin="49501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_49501_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="49501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_49501_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_49501', counter-1] = flow_vph_49501_ID
            elif '<flow begin="50401"' in line:
                flow_vph_50401_ID_LINE = line
                flow_vph_50401_ID = re.search('<flow begin="50401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_50401_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="50401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_50401_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_50401', counter-1] = flow_vph_50401_ID
            elif '<flow begin="51301"' in line:
                flow_vph_51301_ID_LINE = line
                flow_vph_51301_ID = re.search('<flow begin="51301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_51301_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="51301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_51301_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_51301', counter-1] = flow_vph_51301_ID
            elif '<flow begin="52201"' in line:
                flow_vph_52201_ID_LINE = line
                flow_vph_52201_ID = re.search('<flow begin="52201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_52201_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="52201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_52201_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_52201', counter-1] = flow_vph_52201_ID
            elif '<flow begin="53101"' in line:
                flow_vph_53101_ID_LINE = line
                flow_vph_53101_ID = re.search('<flow begin="53101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_53101_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="53101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_53101_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_53101', counter-1] = flow_vph_53101_ID
            elif '<flow begin="54001"' in line:
                flow_vph_54001_ID_LINE = line
                flow_vph_54001_ID = re.search('<flow begin="54001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_54001_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="54001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_54001_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_54001', counter-1] = flow_vph_54001_ID
            elif '<flow begin="54901"' in line:
                flow_vph_54901_ID_LINE = line
                flow_vph_54901_ID = re.search('<flow begin="54901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_54901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="54901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_54901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_54901', counter-1] = flow_vph_54901_ID
            elif '<flow begin="55801"' in line:
                flow_vph_55801_ID_LINE = line
                flow_vph_55801_ID = re.search('<flow begin="55801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_55801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="55801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_55801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_55801', counter-1] = flow_vph_55801_ID
            elif '<flow begin="56701"' in line:
                flow_vph_56701_ID_LINE = line
                flow_vph_56701_ID = re.search('<flow begin="56701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_56701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="56701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_56701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_56701', counter-1] = flow_vph_56701_ID
            elif '<flow begin="57601"' in line:
                flow_vph_57601_ID_LINE = line
                flow_vph_57601_ID = re.search('<flow begin="57601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_57601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="57601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_57601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_57601', counter-1] = flow_vph_57601_ID
            elif '<flow begin="58501"' in line:
                flow_vph_58501_ID_LINE = line
                flow_vph_58501_ID = re.search('<flow begin="58501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_58501_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="58501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_58501_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_58501', counter-1] = flow_vph_58501_ID
            elif '<flow begin="59401"' in line:
                flow_vph_59401_ID_LINE = line
                flow_vph_59401_ID = re.search('<flow begin="59401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_59401_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="59401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_59401_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_59401', counter-1] = flow_vph_59401_ID
            elif '<flow begin="60301"' in line:
                flow_vph_60301_ID_LINE = line
                flow_vph_60301_ID = re.search('<flow begin="60301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_60301_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="60301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_60301_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_60301', counter-1] = flow_vph_60301_ID
            elif '<flow begin="61201"' in line:
                flow_vph_61201_ID_LINE = line
                flow_vph_61201_ID = re.search('<flow begin="61201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_61201_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="61201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_61201_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_61201', counter-1] = flow_vph_61201_ID
            elif '<flow begin="62101"' in line:
                flow_vph_62101_ID_LINE = line
                flow_vph_62101_ID = re.search('<flow begin="62101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_62101_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="62101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_62101_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_62101', counter-1] = flow_vph_62101_ID
            elif '<flow begin="63001"' in line:
                flow_vph_63001_ID_LINE = line
                flow_vph_63001_ID = re.search('<flow begin="63001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_63001_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="63001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_63001_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_63001', counter-1] = flow_vph_63001_ID
            elif '<flow begin="63901"' in line:
                flow_vph_63901_ID_LINE = line
                flow_vph_63901_ID = re.search('<flow begin="63901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_63901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="63901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_63901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_63901', counter-1] = flow_vph_63901_ID
            elif '<flow begin="64801"' in line:
                flow_vph_64801_ID_LINE = line
                flow_vph_64801_ID = re.search('<flow begin="64801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_64801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="64801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_64801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_64801', counter-1] = flow_vph_64801_ID
            elif '<flow begin="65701"' in line:
                flow_vph_65701_ID_LINE = line
                flow_vph_65701_ID = re.search('<flow begin="65701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_65701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="65701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_65701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_65701', counter-1] = flow_vph_65701_ID
            elif '<flow begin="66601"' in line:
                flow_vph_66601_ID_LINE = line
                flow_vph_66601_ID = re.search('<flow begin="66601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_66601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="66601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_66601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_66601', counter-1] = flow_vph_66601_ID
            elif '<flow begin="67501"' in line:
                flow_vph_67501_ID_LINE = line
                flow_vph_67501_ID = re.search('<flow begin="67501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_67501_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="67501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_67501_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_67501', counter-1] = flow_vph_67501_ID
            elif '<flow begin="68401"' in line:
                flow_vph_68401_ID_LINE = line
                flow_vph_68401_ID = re.search('<flow begin="68401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_68401_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="68401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_68401_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_68401', counter-1] = flow_vph_68401_ID
            elif '<flow begin="69301"' in line:
                flow_vph_69301_ID_LINE = line
                flow_vph_69301_ID = re.search('<flow begin="69301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_69301_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="69301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_69301_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_69301', counter-1] = flow_vph_69301_ID
            elif '<flow begin="70201"' in line:
                flow_vph_70201_ID_LINE = line
                flow_vph_70201_ID = re.search('<flow begin="70201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_70201_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="70201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_70201_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_70201', counter-1] = flow_vph_70201_ID
            elif '<flow begin="71101"' in line:
                flow_vph_71101_ID_LINE = line
                flow_vph_71101_ID = re.search('<flow begin="71101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_71101_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="71101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_71101_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_71101', counter-1] = flow_vph_71101_ID
            elif '<flow begin="72001"' in line:
                flow_vph_72001_ID_LINE = line
                flow_vph_72001_ID = re.search('<flow begin="72001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_72001_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="72001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_72001_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_72001', counter-1] = flow_vph_72001_ID
            elif '<flow begin="72901"' in line:
                flow_vph_72901_ID_LINE = line
                flow_vph_72901_ID = re.search('<flow begin="72901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_72901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="72901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_72901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_72901', counter-1] = flow_vph_72901_ID
            elif '<flow begin="73801"' in line:
                flow_vph_73801_ID_LINE = line
                flow_vph_73801_ID = re.search('<flow begin="73801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_73801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="73801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_73801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_73801', counter-1] = flow_vph_73801_ID
            elif '<flow begin="74701"' in line:
                flow_vph_74701_ID_LINE = line
                flow_vph_74701_ID = re.search('<flow begin="74701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_74701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="74701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_74701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_74701', counter-1] = flow_vph_74701_ID
            elif '<flow begin="75601"' in line:
                flow_vph_75601_ID_LINE = line
                flow_vph_75601_ID = re.search('<flow begin="75601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_75601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="75601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_75601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_75601', counter-1] = flow_vph_75601_ID
            elif '<flow begin="76501"' in line:
                flow_vph_76501_ID_LINE = line
                flow_vph_76501_ID = re.search('<flow begin="76501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_76501_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="76501" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_76501_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_76501', counter-1] = flow_vph_76501_ID
            elif '<flow begin="77401"' in line:
                flow_vph_77401_ID_LINE = line
                flow_vph_77401_ID = re.search('<flow begin="77401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_77401_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="77401" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_77401_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_77401', counter-1] = flow_vph_77401_ID
            elif '<flow begin="78301"' in line:
                flow_vph_78301_ID_LINE = line
                flow_vph_78301_ID = re.search('<flow begin="78301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_78301_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="78301" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_78301_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_78301', counter-1] = flow_vph_78301_ID
            elif '<flow begin="79201"' in line:
                flow_vph_79201_ID_LINE = line
                flow_vph_79201_ID = re.search('<flow begin="79201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_79201_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="79201" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_79201_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_79201', counter-1] = flow_vph_79201_ID
            elif '<flow begin="80101"' in line:
                flow_vph_80101_ID_LINE = line
                flow_vph_80101_ID = re.search('<flow begin="80101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_80101_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="80101" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_80101_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_80101', counter-1] = flow_vph_80101_ID
            elif '<flow begin="81001"' in line:
                flow_vph_81001_ID_LINE = line
                flow_vph_81001_ID = re.search('<flow begin="81001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_81001_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="81001" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_81001_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_81001', counter-1] = flow_vph_81001_ID
            elif '<flow begin="81901"' in line:
                flow_vph_81901_ID_LINE = line
                flow_vph_81901_ID = re.search('<flow begin="81901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_81901_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="81901" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_81901_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_81901', counter-1] = flow_vph_81901_ID
            elif '<flow begin="82801"' in line:
                flow_vph_82801_ID_LINE = line
                flow_vph_82801_ID = re.search('<flow begin="82801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_82801_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="82801" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_82801_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_82801', counter-1] = flow_vph_82801_ID
            elif '<flow begin="83701"' in line:
                flow_vph_83701_ID_LINE = line
                flow_vph_83701_ID = re.search('<flow begin="83701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_83701_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="83701" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_83701_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_83701', counter-1] = flow_vph_83701_ID
            elif '<flow begin="84601"' in line:
                flow_vph_84601_ID_LINE = line
                flow_vph_84601_ID = re.search('<flow begin="84601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t',flow_vph_84601_ID_LINE, re.IGNORECASE).group(3)
                termLIST.append(re.search('<flow begin="84601" end="(.*)" route="(.*)" vehsPerHour="(.*)" t', flow_vph_84601_ID_LINE, re.IGNORECASE).group(3))
                logger_TEMPDF.loc['vph_start_84601', counter-1] = flow_vph_84601_ID
    pd.DataFrame.to_excel(logger_TEMPDF,'/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/BMAOI_Dbox-DataFrames/Calibrator_files_v1.xlsx')
#                     print(routeProbe_ID, calibrator_ID, calibrator_ID_edge, "vph =",flow_vph_1_ID)

    return logger_TEMPDF #routeProbe_ID, calibrator_ID,calibrator_ID_edge#, print("\nSUMO_outPUT_PREFIX = ", SUMO_outPUT_PREFIX,"\nSUMO_Traci_PORT = ", SUMO_Traci_PORT)


# In[ ]:

read_n_save_Cali_runFILE()


#         PATH_cali_MASTER_TEMPLATExlsx = '/Dropbox/Phd_R_Ms/Asset_Use_N_Management_Complete_Model/DropBox_ToolBox__MASTER__refresh_with_GIT/Calibrator_Master_TEMPLATE.xlsx'
#         PATH_to_Save_to = "/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/BMAOI_Dbox-DataFrames/Network_" + SUMO_outPUT_PREFIX + "_PeriodBook.xlsx"
#         wb =  OPENxlsx.load_workbook(filename = PATH_to_Save_to)
