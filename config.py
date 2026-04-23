# config.py
PAGE_1_KEYS = [
    "MCR_Power", "Shaft_Power", "Shaft_rpm", "Engine_Load", "Throttle_Pos", "Rev_counter", "ME_Rhrs", "ME_Rhrs_Total",
    "Torque_meter", "Shaft_Torque", "Shaft_Torque_Energy", 
    "exh_1", "exh_2", "exh_3", "exh_4", "exh_5", "exh_6",
    "jw_1", "jw_2", "jw_3", "jw_4", "jw_5", "jw_6",
    "pco_1", "pco_2", "pco_3", "pco_4", "pco_5", "pco_6"
]

PAGE_2_KEYS = [
    "TC_rpm", "Scavenge_pr", "Scavenge_temp", "LT_in_temp", "LT_out_temp",
    "LO_in_t", "LO_out_t", "LO_pr", "LO_lvl", "HT_in_t", "HT_out_t", "Water_Content"
    "TC_airfilter_DP", "Aircooler_DP", "Aircooler_airin_temp", "Aircooler_airout_temp",
    "TC_exhgasin_temp", "TC_exhgasout_temp", "Turboblower_LO_temp", "Turbine_LO_temp",
    "HT_in_press", "HT_out_press", "LT_in_press", "LT_out_press",
    "Aircooler_CWin_temp", "Aircooler_CWout_temp"
]

PAGE_3_KEYS = [
    "JCW_in_temp", "PCO_in_temp", "LO_in_temp", "Thustbrg_out_temp", "Axial_vib",
    "FO_in_temp", "ME_FO_Flowmeter", "ME_fuel_viscosity", "FO_LCV",
    "LOcool_LOin_temp", "LOcool_LOout_temp", "LOcool_CWin_temp", "LOcool_CWout_temp", 
    "LOpp_in_press", "LOpp_out_press", "HTpp_in_press", "HTpp_out_press", "LTpp_in_press", "LTpp_out_press",
    "LOfilter_backwash_ctr", "MEFOfilter_backwash_ctr", "AEFOfilter_backwash_ctr"
]

PAGE_4_KEYS = [
    "Hyd_oil_setpressB", "Hyd_oil_pressB", "Cont_oil_pressB", "Hyd_filter_DP_B", "Hydoil_backwashfilter_ctrB", "ECS_insulationB",
    "Hyd_pump_press1B", "Hyd_pump_press2B", "Hyd_pump_load1B", "Hyd_pump_load2B", "Scavair_press_receiverB", "PitchB",
    "Fuel_index_limiterB", "Fuel_index_actualB", "RPM_SPB", "RPM_actualB", "Start_air_pressB", "Cont_air_pressB",
    "PmaxB", "PcompB", "Exhvv_timingB", "Est_Engine_LoadB", "Speedsetpoint_rpmB", "Speedactual_rpmB", "Fuelindex_setpointB", "Pscav_actualB"
]

PAGE_5_KEYS = [
    "Hyd_oil_setpressC", "Hyd_oil_pressC", "Cont_oil_pressC", "Hyd_filter_DP_C", "Hydoil_backwashfilter_ctrC",
    "Scavair_press_receiverC", "PitchC", "Fuel_index_limiterC", "Fuel_index_actualC", "ECS_insulationC",
    "RPM_SPC", "RPM_actualC", "Start_air_pressC", "Cont_air_pressC",
    "PmaxC", "PcompC", "Exhvv_timingC", "Est_Engine_LoadC", "Speedsetpoint_rpmC", "Speedactual_rpmC", "Fuelindex_setpointC", "Pscav_actualC",
    "Swashplate_pos1", "Swashplate_pos2", "Swashplate_pos3", "Controller", "Follower1", "Follower2"
]

PAGE_6_KEYS = [
    "BOG_rate", "LNG_TK1_level", "LNG_TK2_level", "LNG_TK1_press", "LNG_TK2_press",
    "LNG_TK1_liqtemp", "LNG_TK2_liqtemp", "LNG_TK1_vaptemp", "LNG_TK2_vaptemp", 
    "BDN", "Density", "ME_cons", "AE_cons", "Boiler_cons",
    "CH4", "C2H6", "C3H8", "iC4H10", "nC4H10", "iC5H12", "nC5H12", "nC6H14plus", "N2"
]

PAGE_7_KEYS = [
    "AE1_exh_1", "AE1_exh_2", "AE1_exh_3", "AE1_exh_4", "AE1_exh_5", "AE1_exh_6",
    "AE1_jw_1", "AE1_jw_2", "AE1_jw_3", "AE1_jw_4", "AE1_jw_5", "AE1_jw_6",
    "AE2_exh_1", "AE2_exh_2", "AE2_exh_3", "AE2_exh_4", "AE2_exh_5", "AE2_exh_6",
    "AE2_jw_1", "AE2_jw_2", "AE2_jw_3", "AE2_jw_4", "AE2_jw_5", "AE2_jw_6",
    "AE3_exh_1", "AE3_exh_2", "AE3_exh_3", "AE3_exh_4", "AE3_exh_5", "AE3_exh_6",
    "AE3_jw_1", "AE3_jw_2", "AE3_jw_3", "AE3_jw_4", "AE3_jw_5", "AE3_jw_6",
    "AE4_exh_1", "AE4_exh_2", "AE4_exh_3", "AE4_exh_4", "AE4_exh_5", "AE4_exh_6",
    "AE4_jw_1", "AE4_jw_2", "AE4_jw_3", "AE4_jw_4", "AE4_jw_5", "AE4_jw_6",
    "AE1_RHRS", "AE2_RHRS", "AE3_RHRS", "AE4_RHRS"
]

PAGE_8_KEYS = [
    "AE1_TCin_Exhtemp", "AE1_TCout_Exhtemp", "AE1_ACin_Airtemp", "AE1_ACout_Airtemp",
    "AE2_TCin_Exhtemp", "AE2_TCout_Exhtemp", "AE2_ACin_Airtemp", "AE2_ACout_Airtemp",
    "AE3_TCin_Exhtemp", "AE3_TCout_Exhtemp", "AE3_ACin_Airtemp", "AE3_ACout_Airtemp",
    "AE4_TCin_Exhtemp", "AE4_TCout_Exhtemp", "AE4_ACin_Airtemp", "AE4_ACout_Airtemp",
    "AE1_TCRPM", "AE2_TCRPM", "AE3_TCRPM", "AE4_TCRPM",
    "AE1_KW", "AE2_KW", "AE3_KW", "AE4_KW",
    "AE1_CURR", "AE2_CURR", "AE3_CURR", "AE4_CURR",
    "AE1_PF", "AE2_PF", "AE3_PF", "AE4_PF",
    "AE1_Volt", "AE2_Volt", "AE3_Volt", "AE4_Volt",
    "AE1_FO_TEMP", "AE2_FO_TEMP", "AE3_FO_TEMP", "AE4_FO_TEMP",
    "AE1_LO_in_temp", "AE2_LO_in_temp", "AE3_LO_in_temp", "AE4_LO_in_temp",
    "AE1_LO_out_temp", "AE2_LO_out_temp", "AE3_LO_out_temp", "AE4_LO_out_temp",
    "AE1_LO_press", "AE2_LO_press", "AE3_LO_press", "AE4_LO_press",
    "AE1_LO_lvl", "AE2_LO_lvl", "AE3_LO_lvl", "AE4_LO_lvl",
    "AE1_WindingR_temp", "AE2_WindingR_temp", "AE3_WindingR_temp", "AE4_WindingR_temp",
    "AE1_WindingS_temp", "AE2_WindingS_temp", "AE3_WindingS_temp", "AE4_WindingS_temp",
    "AE1_WindingT_temp", "AE2_WindingT_temp", "AE3_WindingT_temp", "AE4_WindingT_temp"
]

PAGE_9_KEYS = [
    "SW_TEMP", "SW_PRESS", "ER_TEMP", "SWpp_in_press", "SWpp_out_press",
    "ME_CLO_FMR", "CLO_Basic_Feedrate", "ME_FO_CONS", "AE_FO_CONS", "BOILER_FO_CONS", 
    "ME_FMR", "AE_FMR", "BOILER_FMR"
]

PAGE_10_KEYS = [
    "EGBIN_EXH_TEMP", "EGBOUT_EXH_TEMP", "BLR_RHR", "BLR_FO_TEMP", "BLR_FO_PRESS",
    "BLR_LOAD", "EGB_water_lvl", "BLR_water_lvl", "Main_Steam_press", "Feed_water_press",
    "EGB_Circwater_press", "Hotwell_temp", "Hotwell_lvl"
]

PAGE_11_KEYS = [
    "Draft_fwd", "Draft_aft", "Draft_mid_port", "Draft_mid_stbd", "Displacement", "Seastate",
    "App_Wind_speed", "App_Wind_dir", "Air_temp", "Air_press", "Rel_Humidity", "Wave_height", "Wave_dir",
    "Swell_height", "Swell_dir", "Current_speed", "Current_dir", "SOG", "STW",
    "Course", "Heading", "Rudder_angle", "Rate_of_turn", "Depth_below_keel",
    "Latitude", "Longitude", "DTG", "Eng_miles","Obs_miles", "Slip", "ETA"
]

PAGE_12_KEYS =[
    "Ambient_temp", "Servooil_temp", "CWtemp_in", "CWtemp_out", "Cooler_OilIn_temp", "Cooler_OilOut_temp",
    "Servooilpress_ahead", "Servooilpress_astern", "CPP_Pitch", "Running_Pump_no", "Running_pump_load","Sumptk_level"
] 

PAGE_13_KEYS = [
    "ODring_A1temp", "ODring_A2temp", "ODring_B1temp", "ODring_B2temp", "CW_press", "Oilmain_supplypress", "Oilmain_returnpress",
    "Engine_load", "LOfilterclog_ind", "Rem_servopress"
]

ALL_KEYS = (
    PAGE_1_KEYS + PAGE_2_KEYS + PAGE_3_KEYS + PAGE_4_KEYS + PAGE_5_KEYS + PAGE_6_KEYS 
    + PAGE_7_KEYS+ PAGE_8_KEYS + PAGE_9_KEYS + PAGE_10_KEYS + PAGE_11_KEYS + PAGE_12_KEYS + PAGE_13_KEYS
)

DB_NAME = "engine_data.db"