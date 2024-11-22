cols = ['SiteInfo', 'TimeStamp', 'RECORD', 'Lvl_ft', 'Temp_F', 'Cond', 'Ct', 'Temp_F_2', 'OSE_flow_eq_cfs', 'NMSU_flow_cfs', 'BattV_Min', 'BattV_Max', 'BattV_Avg', 'Lvl_ft_Avg', 'Temp_F_Avg', 'Cond_Avg', 'Ct_Avg', 'Temp_F_2_Avg', 'OSE_flow_eq_cfs_Avg', 'NMSU_flow_cfs_Avg', 'VWC_Avg', 'EC_Avg', 'T_Avg', 'P_Avg', 'PA_Avg', 'VR_Avg', 'VWC_2_Avg', 'EC_2_Avg', 'T_2_Avg', 'P_2_Avg', 'PA_2_Avg', 'VR_2_Avg', 'VWC_3_Avg', 'EC_3_Avg', 'T_3_Avg', 'P_3_Avg', 'PA_3_Avg', 'VR_3_Avg', 'Temp_C_Avg', 'VWC_Max', 'VWC_Min', 'VWC_2_Max', 'VWC_2_Min', 'VWC_3_Max', 'VWC_3_Min', 'Cond_Max', 'Cond_Min', 'CV_Med_Turb_Max', 'CV_Med_Turb_Min', 'CV_Mean_Turb_Avg', 'CV_SD_Turb_Avg', 'CV_Min_Turb_Avg', 'CV_Max_Turb_Avg', 'CV_Mean_Temp_Avg', 'CV_Err_Code', 'CV_Mean_Turb_Max', 'CV_Mean_Turb_Min', 'SlrFD_W_Avg', 'Rain_mm_Tot', 'Strikes_Tot', 'Dist_km_Avg', 'WS_ms_Avg', 'WindDir_D1_WVT', 'WindDir', 'MaxWS_ms_Avg', 'AirT_C_Avg', 'VP_mbar_Avg', 'BP_mbar_Avg', 'RH_Max', 'RH_TMx', 'RHT_C_Avg', 'TiltNS_deg_Avg', 'TiltWE_deg_Avg', 'SlrTF_MJ_Tot', 'CVMeta', 'Temp_C_2_Avg', 'CV_Med_Turb_Avg', 'WS_ms_S_WVT', 'WindDir_SD1_WVT', 'ETos', 'Rso']

values = [('nmwrri_36.538778_-105.64564_Atalaya_CR800_Daily', 'datetime.datetime(2024, 11, 1, 0, 0)', 936.0, None, None, None, None, None, None, None, 12.85, 14.94, 13.5, 0.208, 43.52, 0.282, 0.1775354, 43.69, 0.936, 0.45, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None), ('nmwrri_36.538778_-105.64564_Atalaya_CR800_Daily', 'datetime.datetime(2024, 11, 2, 0, 0)', 937.0, None, None, None, None, None, None, None, 12.86, 14.87, 13.45, 0.19, 42.4, 0.284, 0.1750157, 42.47, 0.802, 0.375, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)]

values2 = ('nmwrri_36.538778_-105.64564_Atalaya_CR800_Daily', 'datetime.datetime(2024, 11, 1, 0, 0)', 936.0, None, None, None, None, None, None, None, 12.85, 14.94, 13.5, 0.208, 43.52, 0.282, 0.1775354, 43.69, 0.936, 0.45, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

vallist = zip(cols, values2)

# for val in vallist:
#     if val[1] is not None:
#         print(val)
newlist = []
for row in values:  # Iterate through each tuple in the values list
    for col, val in zip(cols, row):  # Zip the columns with the current row
        if val is not None:  # Check if the value is not None
            newlist.append((col, val))  # Print the column and its corresponding value

for tup in newlist:
    print(tup)

my_dict = {}

for tup in newlist:
    key, value = tup
    # print(key)
    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(value)

print(my_dict)
# for key,value in newlist:
#     my_dict[key] = value
# print(my_dict)

# for tup in newlist:
#         for col in cols:
#             if tup[0] == col:
#                 print(col)

# for val in vallist2:
#     if val[1] is not None:
#         print(val)
# for val in vallist2:
#     print(col, val)

# for val in values2, col in cols:
#     if val is not None:
#         print(col, val)
    



# newlist = []

# for index, value in enumerate(values):
#     newlist.append(values[index])

# for x in newlist:
#     for y in x:
#         print(type(y))
#     print()