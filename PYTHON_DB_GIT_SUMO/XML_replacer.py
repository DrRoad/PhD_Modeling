
# coding: utf-8

# # Last worked on 3/2/2018
# # Goal reload cali_vphph_FILE with new numbers see end
# 
# ## re.sub(pattern, repl, string, max=0)
# # https://www.tutorialspoint.com/python3/python_reg_expressions.htm

# In[1]:

import numpy as np
import re
import pandas as pd
# import sumoPython_git_A as SP
import openpyxl as OPENxlsx
pd.set_option('display.max_columns', 99,'display.max_rows', 99)


# In[208]:

# cali_TEMP = pd.read_excel("C:\Dropbox\Phd_R_Ms\PhD_Modeling_DB_GIT\BMAOI_Dbox-DataFrames\Calibrator_Master_TEMPLATE_312018.xlsx")
# recNUM_LIST_OLD = ['33083', '33084', '33087', '37100', '37101', '37671', '37672', '47340', '47341', '47475', '53494', '53497', '53496', '53723', '53723', '67303', '67304', '78089', '87722', '87723', '110747', '110748', '110749', '110750', '118680', '127934', '127937', '135472', '135471', '135477', '135473', '135473', '118680']
recNUM_LIST = ['33083', '33084', '33087', '37100', '37101', '37671', '37672', '47340', '47341', '47475', '53494', '53497', '53496', '53723a', '53723', '67303', '67304', '78089', '87722', '87723', '110747', '110748', '110749', '110750', '118680a', '127934', '127937', '135472', '135471', '135477', '33087a','33087b','135473a', '135473b', '118680']
cali_raw_TXTPATH = '/Dropbox/Phd_R_Ms/SUMO_DB_root/Belmont_Ave-Run/DVRPC-Traffic_Count_Data-Belmount-AOI/Selected_Small_Belmount_AOI_ALL-class-turn-volume_MOD.txt'
PennDOT_AADT_day_month_TG3_DF = pd.read_excel("C:\Dropbox\Phd_R_Ms\Asset_Use_N_Management_Complete_Model\DropBox_ToolBox__MASTER__refresh_with_GIT\PennDOT AADT factors by day of week and month.xlsx")
PennDOT_Daily_Variance_TG3_DF = pd.read_excel("C:\Dropbox\Phd_R_Ms\Asset_Use_N_Management_Complete_Model\DropBox_ToolBox__MASTER__refresh_with_GIT\PennDOT vphph factors_TG3.xlsx")


# In[224]:

cali_M_DF = pd.read_excel("C:\Dropbox\Phd_R_Ms\PhD_Modeling_DB_GIT\BMAOI_Dbox-DataFrames\Calibrator_Master_TEMPLATE_312018.xlsx")
readfromPATH = '/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/Belmont_AOI_git/Belmont_AOI_toolBOX_Not_Master/Belmount_AOI-caliborators-DB-V6-SUMO31-15min_RAW.xml'
caliXMLTESTPATH = '/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/Belmont_AOI_git/Belmont_AOI_toolBOX_Not_Master/cali_test.xml'
# print(cali_M_DF.shape,cali_M_DF.columns, cali_M_DF.index)
cali_XML_output = '/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/Belmont_AOI_git/Belmont_AOI_toolBOX_Not_Master/cali_test_OutP_'#.xml'


# In[ ]:




# In[4]:

#create a dictionary of calibrator names and location in XML_file


# In[170]:

XML_cali = open(caliXMLTESTPATH,'r') #open(caliXMLTESTPATH,'r')
XMLdataRL = XML_cali.readlines()
XML_cali.close()


# In[171]:

cali_counter = 0
XML_cali_iloc_DICT = dict()
XML_cali_ID_LIST = list()
for line in range(len(XMLdataRL)):
    if '<calibrator id=' in XMLdataRL[line]:
        cali_counter += 1
        calibrator_ID_LINE = XMLdataRL[line]
        calibrator_ID = re.search('<calibrator id="(.*)" edge="(.*)" p',calibrator_ID_LINE, re.IGNORECASE).group(1)
#         print(XMLdataRL[line])
        XML_cali_ID_LIST.append(calibrator_ID)
        XML_cali_iloc_DICT.update({calibrator_ID:cali_counter})
print(XML_cali_ID_LIST,"\n",XML_cali_iloc_DICT) 


# In[266]:

# len(XML_cali_iloc_DICT)
cali_M_row_2_ID_DF_DICT = dict()
cali_M_ID_2_row_DF_DICT = dict()
for columns in cali_M_DF:
    if cali_M_DF.loc['calibrator_ID',columns] in XML_cali_ID_LIST:
#         cali_DF_DICT.update({str(cali_TEMP.loc['calibrator_ID',columns]):str(columns)})
        cali_M_row_2_ID_DF_DICT.update({str(columns) : str(cali_TEMP.loc['calibrator_ID',columns])})
        cali_M_ID_2_row_DF_DICT.update({str(cali_TEMP.loc['calibrator_ID',columns]) : str(columns)})
print(cali_M_row_2_ID_DF_DICT,"\n\n\n",cali_M_ID_2_row_DF_DICT)


# In[268]:

write_new_Cali_XML(caliXMLTESTPATH,cali_XML_output,'March','Monday')


# day_t = 'Monday'
# month_t = 'March'
# XML_outmod = str(cali_XML_output) +"_"+month_t+"_"+day_t+".xml"

# print(PennDOT_AADT_day_month_TG3_DF.index,"\n", PennDOT_AADT_day_month_TG3_DF.columns,"\n\n",PennDOT_Daily_Variance_TG3_DF.index,"\n",PennDOT_Daily_Variance_TG3_DF.columns)
# day_t = 'Monday'
# month_t = 'March'
# PennDOT_AADT_day_month_TG3_DF.loc[day_t,month_t]
# PennDOT_Daily_Variance_TG3_DF.iloc[2,3]

# In[267]:

def update_vphph_i(cali_counter, flow_ID, DF_row, month_t, day_t):
    print("cali_counter = ", cali_counter)
    print(XML_cali_ID_LIST[cali_counter], XML_cali_ID_LIST[cali_counter] == caliLISTa[cali_counter].calibrator_ID,end=" ")
    cali_M_DF.iloc[DF_row, col_DF]
    Month_Day_Factor = PennDOT_AADT_day_month_TG3_DF.loc[day_t,month_t]
#     Hour_Factor = PennDOT_Daily_Variance_TG3_DF
    flow_X_i = caliLISTa[cali_counter].vph_DF[DF_row]*Month_Day_Factor
    print("DF_row = ",caliLISTa[cali_counter].vph_DF[DF_row], "Month_Day_Factor = ", Month_Day_Factor, "flow_X_i = ",flow_X_i)
    return flow_X_i

    
def write_new_Cali_XML(XML_in,XML_out,month_t,day_t):
    XML_cali = open(XML_in,'r') #open(caliXMLTESTPATH,'r')
    XMLdataRL = XML_cali.readlines()
    XML_cali.close()
#     capture = 0
    cali_counter = 0
    period_start_LIST = list()
    XML_outmod = str(XML_out) +"_"+month_t+"_"+day_t+".xml"
    newfile = open(XML_outmod,'w') #open(cali_XML_output,'w')
    newfile.write("<!-- File created for "+str(month_t)+" "+str(day_t)+"-->\n")
    newfile.close()
    for line in range(len(XMLdataRL)):
        if '<calibrator id=' in XMLdataRL[line]:
            col_DF = cali_M_row_2_ID_DF_DICT[str(cali_counter)]
            cali_counter += 1
            calibrator_ID_LINE = XMLdataRL[line]
            calibrator_ID = re.search('<calibrator id="(.*)" edge="(.*)" p',calibrator_ID_LINE, re.IGNORECASE).group(1)
        elif '<flow begin="' in XMLdataRL[line]:
            LINE_i = XMLdataRL[line]
#             print(LINE_i)
            flow_ID = re.search('<flow begin="(.*)" e',LINE_i, re.IGNORECASE).group(1)
            if flow_ID == "1":
                DF_row = 3
            else:
                DF_row += 1
            period_start_LIST.append(flow_ID)
            vph_pattern = re.search('vehsPerHour="(.*)" t',LINE_i, re.IGNORECASE).group(1)
            repl_i = str(update_vphph_i(cali_counter, flow_ID,DF_row,month_t,day_t))#, day))
            print("repl_i = ",repl_i," should not equal vph_pattern",vph_pattern)
            XMLdataRL[line] = re.sub(vph_pattern, repl_i, LINE_i)
            print(LINE_i)
        newfile = open(XML_outmod,'a')
        newfile.write(XMLdataRL[line])
        newfile.close()
    newfile.close()
    return XMLdataRL


# In[ ]:

# def make_new_XML_vphph_all_calis():
counter =0
vph_index_LIST = list()
for n in range(len(cali_M_DF.index)):
    if 'vph' in cali_M_DF.index[n]:
        vph_index_LIST.append(cali_M_DF.index[n])
vph_index_LIST


# In[184]:

class Cali():
    cali_M_DF = pd.read_excel("C:\Dropbox\Phd_R_Ms\PhD_Modeling_DB_GIT\BMAOI_Dbox-DataFrames\Calibrator_Master_TEMPLATE_312018.xlsx")
    cali_XML_output = '/Dropbox/Phd_R_Ms/PhD_Modeling_DB_GIT/Belmont_AOI_git/Belmont_AOI_toolBOX_Not_Master/cali_test_OutP_1.xml'
    
    def __init__(self):
        self.calibrator_ID = 0
        self.cali_M_DF_col = 0
        self.routeProbe_ID = 0
        self.SUMO_edge_ID = 0
        
        #Big long self list if wanted
        self.RECORDNUM = 0
        self.AXLE_CORR_FACTOR = 0
        self.AADT = 0
        self.AM_Peak_prct = 0
        self.Hour_Beginning_AM = 0
        self.SEASONAL_FACTOR = 0
        self.PM_Peak_prct = 0
        self.Hour_Beginning_PM = 0
        
        self.vph_index_LIST = list()
        self.vph_DF = pd.DataFrame(np.zeros((95,1)))
        
    def set_prarams(self,calibrator_ID,cali_M_DF):#,vph_index_LIST):
        self.calibrator_ID = calibrator_ID
        self.vph_DF = pd.DataFrame(np.zeros((95,1)),index = vph_index_LIST)
        for col in range(cali_M_DF.shape[1]):
            if cali_M_DF.loc['calibrator_ID',col] == self.calibrator_ID:
                self.cali_M_DF_col = col
                self.routeProbe_ID = cali_M_DF.loc['routeProbe_ID',col]
                self.SUMO_edge_ID = cali_M_DF.loc['SUMO_edge_ID',col]
                self.RECORDNUM = cali_M_DF.loc['RECORDNUM',col]
                self.AXLE_CORR_FACTOR = cali_M_DF.loc['AXLE_CORR_FACTOR',col]
                self.AADT = cali_M_DF.loc['AADT',col]
                self.AM_Peak_prct = cali_M_DF.loc['AM_Peak_prct',col]
                self.Hour_Beginning_AM = cali_M_DF.loc['Hour_Beginning_AM',col]
                self.SEASONAL_FACTOR = cali_M_DF.loc['SEASONAL_FACTOR',col]
                self.PM_Peak_prct = cali_M_DF.loc['PM_Peak_prct',col]
                self.Hour_Beginning_PM = cali_M_DF.loc['Hour_Beginning_PM',col]
                self.vph_DF = cali_M_DF.iloc[3:98,col]
    

    @classmethod # means class instead of self (Edge.create_Edge_Instances() becomes create_Edge_Instances(Edge))
    def create_cali_Instances(cls):
        # @staticmethod # means no self
        # def create_Edge_Instances():
        tabber = "<>"
        print("\n\t\t\t\t<><>Please wait creating Cali Instances<><>\n")
        caliLISTa = list()
        counter = 0
        for cali_i in XML_cali_ID_LIST[:]: #### HERE TO INCLUDE ALL INSTANCES
            caliNAME = cali_i#"cali_"+str(counter)
            #cali_i#"edge_"+str(counter) #str(SP.Belmont_AVEDic[counter])
            caliLISTa.append(caliNAME)
            # print(edgeLISTa[counter])
            caliLISTa[counter]= cls()
            caliLISTa[counter].set_prarams(cali_i,cali_M_DF)
   
            print("cali_i = ", cali_i,tabber,end='\r',flush=True)#, edgeLISTa[counter].__dict__)
            counter = counter + 1
            # tabber = str(tabber+"<>")#\t")
#             if (counter/47).is_integer() == True:
#                 tabber = "\n<>"
#             else:
            tabber = str(tabber+"<>")#\t")
        print("\n\t\t\t\t<<<caliLISTa Instances loaded on edgeLISTa>>>\n")
        print("Testing caliLISTa[1].__dict__ ...\n",caliLISTa[1].__dict__,"\n")
        return caliLISTa


# In[185]:

caliLISTa = Cali.create_cali_Instances()
vph_index_LIST[0],caliLISTa[0].vph_DF[vph_index_LIST[0]]


# In[125]:

cali_M_DF.index


# In[127]:

pp = Cali('ConcrseDR-Belmont-MemHll-WB-02-33084')
pp.set_prarams(cali_M_DF)


# In[139]:

pp.vph_DF[vph_index_LIST[2]]


# In[27]:

# for line in XMLdataR:
#     print(line)
cali_counter = 0
XML_cali_iloc_DICT = dict()
XML_cali_ID_LIST = list()
for line in range(len(XMLdataRL)):
    if '<calibrator id=' in XMLdataRL[line]:
        cali_counter += 1
        calibrator_ID_LINE = XMLdataRL[line]
        calibrator_ID = re.search('<calibrator id="(.*)" edge="(.*)" p',calibrator_ID_LINE, re.IGNORECASE).group(1)
        print(XMLdataRL[line])
        XML_cali_ID_LIST.append(calibrator_ID)
        XML_cali_iloc_DICT.update({calibrator_ID:cali_counter})
print(XML_cali_ID_LIST,"\n",XML_cali_iloc_DICT) 


# In[40]:




# In[221]:

XMLdataRL


# In[61]:

cali_TEMP.iloc[3,0]


# ##TESTING
# cali_counter = 0
# for line in range(len(XMLdataRL)):
#     if '<calibrator id=' in XMLdataRL[line]:
#         cali_counter += 1
#         calibrator_ID_LINE = XMLdataRL[line]
#         calibrator_ID = re.search('<calibrator id="(.*)" edge="(.*)" p',calibrator_ID_LINE, re.IGNORECASE).group(1)
#         pattern_CID = '<calibrator id="'+calibrator_ID+'" e'
#         repl_CID = '<calibrator id="' + "Poo_" + str(cali_counter) + '" e'
#         XMLdataRL[line] = re.sub(pattern_CID, repl_CID, calibrator_ID_LINE)
#         print(XMLdataRL[line])#,"\nreplacement line = ",repline)

# In[52]:

XMLdataRL


# 
#         self.vph_start_1 = 0
#         self.vph_start_901 = 0
#         self.vph_start_1801 = 0
#         self.vph_start_2701 = 0
#         self.vph_start_3601 = 0
#         self.vph_start_4501 = 0
#         self.vph_start_5401 = 0
#         self.vph_start_6301 = 0
#         self.vph_start_7201 = 0
#         self.vph_start_8101 = 0
#         self.vph_start_9001 = 0
#         self.vph_start_9901 = 0
#         self.vph_start_10801 = 0
#         self.vph_start_11701 = 0
#         self.vph_start_12601 = 0
#         self.vph_start_13501 = 0
#         self.vph_start_14401 = 0
#         self.vph_start_15301 = 0
#         self.vph_start_16201 = 0
#         self.vph_start_17101 = 0
#         self.vph_start_18001 = 0
#         self.vph_start_18901 = 0
#         self.vph_start_19801 = 0
#         self.vph_start_20701 = 0
#         self.vph_start_21601 = 0
#         self.vph_start_22501 = 0
#         self.vph_start_23401 = 0
#         self.vph_start_24301 = 0
#         self.vph_start_25201 = 0
#         self.vph_start_26101 = 0
#         self.vph_start_27001 = 0
#         self.vph_start_27901 = 0
#         self.vph_start_28801 = 0
#         self.vph_start_29701 = 0
#         self.vph_start_30601 = 0
#         self.vph_start_31501 = 0
#         self.vph_start_32401 = 0
#         self.vph_start_33301 = 0
#         self.vph_start_34201 = 0
#         self.vph_start_35101 = 0
#         self.vph_start_36001 = 0
#         self.vph_start_36901 = 0
#         self.vph_start_37801 = 0
#         self.vph_start_38701 = 0
#         self.vph_start_39601 = 0
#         self.vph_start_40501 = 0
#         self.vph_start_41401 = 0
#         self.vph_start_42301 = 0
#         self.vph_start_43201 = 0
#         self.vph_start_44101 = 0
#         self.vph_start_45001 = 0
#         self.vph_start_45901 = 0
#         self.vph_start_46801 = 0
#         self.vph_start_47701 = 0
#         self.vph_start_48601 = 0
#         self.vph_start_49501 = 0
#         self.vph_start_50401 = 0
#         self.vph_start_51301 = 0
#         self.vph_start_52201 = 0
#         self.vph_start_53101 = 0
#         self.vph_start_54001 = 0
#         self.vph_start_54901 = 0
#         self.vph_start_55801 = 0
#         self.vph_start_56701 = 0
#         self.vph_start_57601 = 0
#         self.vph_start_58501 = 0
#         self.vph_start_59401 = 0
#         self.vph_start_60301 = 0
#         self.vph_start_61201 = 0
#         self.vph_start_62101 = 0
#         self.vph_start_63001 = 0
#         self.vph_start_63901 = 0
#         self.vph_start_64801 = 0
#         self.vph_start_65701 = 0
#         self.vph_start_66601 = 0
#         self.vph_start_67501 = 0
#         self.vph_start_68401 = 0
#         self.vph_start_69301 = 0
#         self.vph_start_70201 = 0
#         self.vph_start_71101 = 0
#         self.vph_start_72001 = 0
#         self.vph_start_72901 = 0
#         self.vph_start_73801 = 0
#         self.vph_start_74701 = 0
#         self.vph_start_75601 = 0
#         self.vph_start_76501 = 0
#         self.vph_start_77401 = 0
#         self.vph_start_78301 = 0
#         self.vph_start_79201 = 0
#         self.vph_start_80101 = 0
#         self.vph_start_81001 = 0
#         self.vph_start_81901 = 0
#         self.vph_start_82801 = 0
#         self.vph_start_83701 = 0
#         self.vph_start_84601 = 0
