# pages_content.py
import streamlit as st

def page_one():
    st.title("📈 Main Engine Data 1")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader("Engine Control")
        for k in ["MCR_Power(KW)", "Shaft_Power(KW)", "Shaft_rpm", "Engine_Load", "Throttle_Pos", "Rev_counter", "ME_Rhrs", "ME_Rhrs_Total"]:
            st.number_input(k.replace("_", " "), key=k, step=0.01)

    with col2:
        st.subheader("Exhaust Temp")
        for i in range(1, 7):
            st.number_input(f"Exh Temp {i} (°C)", key=f"exh_{i}", step=0.01)

    with col3:
        st.subheader("JCW Out Temp")
        for i in range(1, 7):
            st.number_input(f"JCW Temp {i} (°C)", key=f"jw_{i}", step=0.01)

    with col4:
        st.subheader("PCO Temp")
        for i in range(1, 7):
            st.number_input(f"PCO Temp {i} (°C)", key=f"pco_{i}", step=0.01)

    with col5:
        st.subheader("Torque")
        st.number_input("Torque Meter (kNm)", key="Torque_meter", step=0.01)
        st.number_input("Shaft Torque (kNm)", key="Shaft_Torque", step=0.01)
        st.number_input("Shaft Torque Energy (kWh)", key="Shaft_Torque_Energy", step=0.01)
       

def page_two():
    st.title("📈 Main Engine Data 2")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Air Side")
        st.number_input("Turbocharger RPM", key="TC_rpm", step=0.01)
        st.number_input("Scavenge Press (bar)", key="Scavenge_pr", step=0.01)
        st.number_input("Scavenge Temp (°C)", key="Scavenge_temp", step=0.01)
        st.number_input("TC Airfilter DP (bar)", key="TC_airfilter_DP", step=0.01)
        st.number_input("Aircooler DP (bar)", key="Aircooler_DP", step=0.01)
        st.number_input("Aircooler Air In Temp (°C)", key="Aircooler_airin_temp", step=0.01)
        st.number_input("Aircooler Air Out Temp (°C)", key="Aircooler_airout_temp", step=0.01)
        st.number_input("Aircooler CW In Temp (°C)", key="Aircooler_CWin_temp", step=0.01)
        st.number_input("Aircooler CW Out Temp (°C)", key="Aircooler_CWout_temp", step=0.01)

    with col2:
        st.subheader("Lub. Oil")
        st.number_input("LO In Temp (°C)", key="LO_in_t", step=0.01)
        st.number_input("LO Out Temp (°C)", key="LO_out_t", step=0.01)
        st.number_input("LO Pressure (bar)", key="LO_pr", step=0.01)
        st.number_input("LO Level (mm)", key="LO_lvl", step=0.01)
        st.number_input("TC Exhaust Gas In Temp (°C)", key="TC_exhgasin_temp", step=0.01)
        st.number_input("TC Exhaust Gas Out Temp (°C)", key="TC_exhgasout_temp", step=0.01)
        st.number_input("Turboblower LO Temp (°C)", key="Turboblower_LO_temp", step=0.01)
        st.number_input("Turbine LO Temp (°C)", key="Turbine_LO_temp", step=0.01)
        st.number_input("Water Content (%)", key="Water_Content", step=0.01)

    with col3:
        st.subheader("LT/HT System")
        st.number_input("HT In Temp (°C)", key="HT_in_t", step=0.01)
        st.number_input("HT Out Temp (°C)", key="HT_out_t", step=0.01)
        st.number_input("LT In Temp (°C)", key="LT_in_temp", step=0.01)
        st.number_input("LT Out Temp (°C)", key="LT_out_temp", step=0.01)
        st.number_input("HT In Press (bar)", key="HT_in_press", step=0.01)
        st.number_input("HT Out Press (bar)", key="HT_out_press", step=0.01)
        st.number_input("LT In Press (bar)", key="LT_in_press", step=0.01)
        st.number_input("LT Out Press (bar)", key="LT_out_press", step=0.01)

def page_three():
    st.title("📈 Main Engine Data 3")
    col1, col2, col3 = st.columns(3)    

    with col1:
        st.subheader("Cooling & Fuel")
        st.number_input("JCW In Temp (°C)", key="JCW_in_temp", step=0.01)
        st.number_input("PCO In Temp (°C)", key="PCO_in_temp", step=0.01)
        st.number_input("LO In Temp (°C)", key="LO_in_temp", step=0.01)
        st.number_input("Thrust Bearing Out Temp (°C)", key="Thustbrg_out_temp", step=0.01)
        st.number_input("F.O In Temp (°C)", key="F.O_in_temp", step=0.01)
        st.number_input("ME F.O Flowmeter (kg/h)", key="ME_F.O.Flowmeter", step=0.01)       
        st.number_input("ME Fuel Viscosity (cSt)", key="ME_fuel_viscosity", step=0.01)
        st.number_input("F.O LCV (kJ/kg)", key="F.O_LCV", step=0.01)
        st.number_input("Axial Vibration (mm)", key="Axial_vib", step=0.01)

    with col2:
        st.subheader("Coolers & pumps")
        st.number_input("LOcool LO In Temp (°C)", key="LOcool_LOin_temp", step=0.01)
        st.number_input("LOcool LO Out Temp (°C)", key="LOcool_LOout_temp", step=0.01)
        st.number_input("LOcool CW In Temp (°C)", key="LOcool_CWin_temp", step=0.01)
        st.number_input("LOcool CW Out Temp (°C)", key="LOcool_CWout_temp", step=0.01)
        st.number_input("LOpp In Press (bar)", key="LOpp_in_press", step=0.01)
        st.number_input("LOpp Out Press (bar)", key="LOpp_out_press", step=0.01)
        st.number_input("HTpp In Press (bar)", key="HTpp_in_press", step=0.01)
        st.number_input("HTpp Out Press (bar)", key="HTpp_out_press", step=0.01)
        st.number_input("LTpp In Press (bar)", key="LTpp_in_press", step=0.01)
        st.number_input("LTpp Out Press (bar)", key="LTpp_out_press", step=0.01)

    with col3:
        st.subheader("Backwash Counters")
        st.number_input("LO Filter Backwash Counter", key="LOfilter_backwash_ctr", step=1)
        st.number_input("ME FO Filter Backwash Counter", key="MEFOfilter_backwash_ctr", step=1) 
        st.number_input("AE FO Filter Backwash Counter", key="AEFOfilter_backwash_ctr", step=1)       

def page_four():
    st.title("📈 Main Engine Data (ME-B)")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("Hydraulic System")
        st.number_input("Hyd Oil Set Press (bar)", key="Hyd_oil_setpressB", step=0.01)
        st.number_input("Hyd Oil Press (bar)", key="Hyd_oil_pressB", step=0.01)
        st.number_input("Oil In Press (bar)", key="Oil_In_pressB", step=0.01)        
        st.number_input("Hyd Filter DP (bar)", key="Hyd_filter_DP_B", step=0.01)
        st.number_input("Hyd Oil Backwash Filter Counter", key="Hydoil_backwashfilter_ctrB", step=1)

    with col2:
        st.subheader("Hydraulic Pumps")
        st.number_input("Hyd Pump Press 1 (bar)", key="Hyd_pump_press1B", step=0.01)
        st.number_input("Hyd Pump Press 2 (bar)", key="Hyd_pump_press2B", step=0.01)
        st.number_input("Hyd Pump Load 1 (%)", key="Hyd_pump_load1B", step=0.01)
        st.number_input("Hyd Pump Load 2 (%)", key="Hyd_pump_load2B", step=0.01)        

    with col3:
        st.subheader("Controls")
        st.number_input("Scavair Press Receiver (bar)", key="Scavair_press_receiverB", step=0.01)
        st.number_input("Fuel Index Limiter (%)", key="Fuel_index_limiterB", step=0.01)
        st.number_input("Fuel Index Actual (%)", key="Fuel_index_actualB", step=0.01)
        st.number_input("RPM Setpoint", key="RPM_SPB", step=0.01)
        st.number_input("RPM Actual", key="RPM_actualB", step=0.01)
        st.number_input("Start Air Press (bar)", key="Start_air_pressB", step=0.01)
        st.number_input("Control Air Press (bar)", key="Cont_air_pressB", step=0.01)
        st.number_input("Pitch (%)-only if CPP", key="PitchB", step=0.01)

    with col4:
        st.subheader("Performance")
        st.number_input("Pmax (bar)", key="PmaxB", step=0.01)
        st.number_input("Pcomp (bar)", key="PcompB", step=0.01)
        st.number_input("Exhaust Valve Timing (°ATDC)", key="Exhvv_timingB", step=0.01)
        st.number_input("Estimated Engine Load (%)", key="Est_Engine_LoadB", step=0.01)
        st.number_input("Speed Setpoint (rpm)", key="Speedsetpoint_rpmB", step=0.01)
        st.number_input("Speed Actual (rpm)", key="Speedactual_rpmB", step=0.01)
        st.number_input("Fuel Index Setpoint (%)", key="Fuelindex_setpointB", step=0.01)     
        st.number_input("Scav Air Actual Press (bar)", key="Pscav_actualB", step=0.01)   
        st.number_input("ECS Insulation (Ohms)", key="ECS_insulation", step=0.01)

def page_five():
    st.title("📈 Main Engine Data (ME-C)")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Hydraulic System")
        st.number_input("Hyd Oil Set Press (bar)", key="Hyd_oil_setpressC", step=0.01)
        st.number_input("Hyd Oil Press bar)", key="Hyd_oil_pressC", step=0.01)
        st.number_input("Oil In Press (bar)", key="Oil_In_pressC", step=0.01)       
        st.number_input("Hyd Filter DP (bar)", key="Hyd_filter_DP_C", step=0.01)
        st.number_input("Hyd Oil Backwash Filter Counter", key="Hydoil_backwashfilter_ctrC", step=1)
        st.number_input("Swashplate Position 1 (%)", key="Swashplate_pos1", step=0.01)
        st.number_input("Swashplate Position 2 (%)", key="Swashplate_pos2", step=0.01)
        st.number_input("Swashplate Position 3 (%)", key="Swashplate_pos3", step=0.01)
        st.number_input("Controller Swashplate Pump", key="Controller", min_value=1, max_value=3,step=1)
        st.number_input("Follower Swashplate Pump1", key="Follower1", min_value=1, max_value=3,step=1)
        st.number_input("Follower Swashplate Pump2", key="Follower2", min_value=1, max_value=3,step=1)

    with col2:
        st.subheader("Controls")
        st.number_input("Scavair Press Receiver (bar)", key="Scavair_press_receiverC", step=0.01)
        st.number_input("Fuel Index Limiter (%)", key="Fuel_index_limiterC", step=0.01)
        st.number_input("Fuel Index Actual (%)", key="Fuel_index_actualC", step=0.01)
        st.number_input("RPM Setpoint", key="RPM_SPC", step=0.01)
        st.number_input("RPM Actual", key="RPM_actualC", step=0.01)
        st.number_input("Start Air Press (bar)", key="Start_air_pressC", step=0.01)  
        st.number_input("Control Air Press (bar)", key="Cont_air_pressC", step=0.01)  
        st.number_input("Pitch (%)-only if CPP", key="PitchC", step=0.01) 

    with col3:
        st.subheader("Performance")
        st.number_input("Pmax (bar)", key="PmaxC", step=0.01)
        st.number_input("Pcomp (bar)", key="PcompC", step=0.01)
        st.number_input("Exhaust Valve Timing (°ATDC)", key="Exhvv_timingC", step=0.01)
        st.number_input("Estimated Engine Load (%)", key="Est_Engine_LoadC", step=0.01)
        st.number_input("Speed Setpoint (rpm)", key="Speedsetpoint_rpmC", step=0.01)
        st.number_input("Speed Actual (rpm)", key="Speedactual_rpmC", step=0.01)
        st.number_input("Fuel Index Setpoint (%)", key="Fuelindex_setpointC", step=0.01)     
        st.number_input("Scav Air Actual Press (bar)", key="Pscav_actualC", step=0.01)
        st.number_input("ECS Insulation (Ohms)", key="ECS_insulationC", step=0.01)

def page_six():
    st.title("📈 LNG Parameters")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Dual fuel-LNG")
        st.number_input("BOG Rate (kg/h)", key="BOG_rate", step=0.01)
        st.number_input("LNG TK1 Level (m)", key="LNG_TK1_level", step=0.01)
        st.number_input("LNG TK2 Level (m)", key="LNG_TK2_level", step=0.01)
        st.number_input("LNG TK1 Press (bar)", key="LNG_TK1_press", step=0.01)
        st.number_input("LNG TK2 Press (bar)", key="LNG_TK2_press", step=0.01)
        st.number_input("LNG TK1 Liq Temp (°C)", key="LNG_TK1_liqtemp", step=0.01)
        st.number_input("LNG TK2 Liq Temp (°C)", key="LNG_TK2_liqtemp", step=0.01)
        st.number_input("LNG TK1 Vap Temp (°C)", key="LNG_TK1_vaptemp", step=0.01)
        st.number_input("LNG TK2 Vap Temp (°C)", key="LNG_TK2_vaptemp", step=0.01)

    with col2:
        st.subheader("Consumption & Composition")
        st.number_input("BDN (MT)", key="BDN", step=0.01)
        st.number_input("Density (kg/m³)", key="Density", step=0.0001, format="%.4f")
        st.number_input("ME Cons (MT)", key="ME_cons", step=0.01)
        st.number_input("AE Cons (MT)", key="AE_cons", step=0.01)
        st.number_input("Boiler Cons (MT)", key="Boiler_cons", step=0.01)
        st.number_input("CH4 (%)", key="CH4", step=0.01)
        st.number_input("C2H6 (%)", key="C2H6", step=0.01)
        st.number_input("C3H8 (%)", key="C3H8", step=0.01)
        st.number_input("iC4H10 (%)", key="iC4H10", step=0.01)
        st.number_input("nC4H10 (%)", key="nC4H10", step=0.01)
        st.number_input("iC5H12 (%)", key="iC5H12", step=0.01)
        st.number_input("nC5H12 (%)", key="nC5H12", step=0.01)
        st.number_input("nC6H14+ (%)", key="nC6H14plus", step=0.01)
        st.number_input("N2 (%)", key="N2", step=0.01)


def page_seven():
    st.title("📈 Auxiliary Engine Data 1")
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    with col1:
        st.subheader("AE1 Exh Temp")
        for i in range(1, 7):
            st.number_input(f"AE1 Exh Temp {i} (°C)", key=f"AE1_exh_{i}", step=0.01)
        st.number_input("AE1 RHRS (h)", key="AE1_RHRS", step=0.01)

    with col2:
        st.subheader("AE1 JW Temp")
        for i in range(1, 7):
            st.number_input(f"AE1 JCW Temp {i} (°C)", key=f"AE1_jw_{i}", step=0.01)

    with col3:
        st.subheader("AE2 Exh Temp")
        for i in range(1, 7):
            st.number_input(f"AE2 Exh Temp {i} (°C)", key=f"AE2_exh_{i}", step=0.01) 
        st.number_input("AE2 RHRS (h)", key="AE2_RHRS", step=0.01)

    with col4:
        st.subheader("AE2 JW Temp")
        for i in range(1, 7):
            st.number_input(f"AE2 JCW Temp {i} (°C)", key=f"AE2_jw_{i}", step=0.01)

    with col5:
        st.subheader("AE3 Exh Temp")
        for i in range(1, 7):
            st.number_input(f"AE3 Exh Temp {i} (°C)", key=f"AE3_exh_{i}", step=0.01)
        st.number_input("AE3 RHRS (h)", key="AE3_RHRS", step=0.01)

    with col6:
        st.subheader("AE3 JW Temp")
        for i in range(1, 7):
            st.number_input(f"AE3 JCW Temp {i} (°C)", key=f"AE3_jw_{i}", step=0.01)

    with col7:
        st.subheader("AE4 Exh Temp")
        for i in range(1, 7):
            st.number_input(f"AE4 Exh Temp {i} (°C)", key=f"AE4_exh_{i}", step=0.01)
        st.number_input("AE4 RHRS (h)", key="AE4_RHRS", step=0.01)

    with col8:
        st.subheader("AE4 JW Temp")        
        for i in range(1, 7):
            st.number_input(f"AE4 JCW Temp {i} (°C)", key=f"AE4_jw_{i}", step=0.01)


def page_eight():
    st.title("📈 Auxiliary Engine Data 2")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("AE1 parameters")
        st.number_input("AE1 TC In Exh Temp (°C)", key="AE1_TCin_Exhtemp", step=0.01)
        st.number_input("AE1 TC Out Exh Temp (°C)", key="AE1_TCout_Exhtemp", step=0.01)
        st.number_input("AE1 AC In Air Temp (°C)", key="AE1_ACin_Airtemp", step=0.01)
        st.number_input("AE1 AC Out Air Temp (°C)", key="AE1_ACout_Airtemp", step=0.01)
        st.number_input("AE1 TC RPM", key="AE1_TCRPM", step=0.01)
        st.number_input("AE1 KW", key="AE1_KW", step=0.01)
        st.number_input("AE1 Current (A)", key="AE1_CURR", step=0.01)
        st.number_input("AE1 Power Factor", key="AE1_PF", step=0.01)
        st.number_input("AE1 Voltage (V)", key="AE1_Volt", step=0.01)                
        st.number_input("AE1 F.O Temp (°C)", key="AE1_FO_TEMP", step=0.01)
        st.number_input("AE1 LO In Temp (°C)", key="AE1_LO_in_temp", step=0.01)
        st.number_input("AE1 LO Out Temp (°C)", key="AE1_LO_out_temp", step=0.01)
        st.number_input("AE1 LO Press (bar)", key="AE1_LO_press", step=0.01)
        st.number_input("AE1 LO Level (mm)", key="AE1_LO_lvl", step=0.01)
        st.number_input("AE1 Winding R Temp (°C)", key="AE1_WindingR_temp", step=0.01)
        st.number_input("AE1 Winding S Temp (°C)", key="AE1_WindingS_temp", step=0.01)
        st.number_input("AE1 Winding T Temp (°C)", key="AE1_WindingT_temp", step=0.01)

    with col2:
        st.subheader("AE2 parameters")
        st.number_input("AE2 TC In Exh Temp (°C)", key="AE2_TCin_Exhtemp", step=0.01)
        st.number_input("AE2 TC Out Exh Temp (°C)", key="AE2_TCout_Exhtemp", step=0.01)
        st.number_input("AE2 AC In Air Temp (°C)", key="AE2_ACin_Airtemp", step=0.01)
        st.number_input("AE2 AC Out Air Temp (°C)", key="AE2_ACout_Airtemp", step=0.01)
        st.number_input("AE2 TC RPM", key="AE2_TCRPM", step=0.01)
        st.number_input("AE2 KW", key="AE2_KW", step=0.01)
        st.number_input("AE2 Current (A)", key="AE2_CURR", step=0.01)
        st.number_input("AE2 Power Factor", key="AE2_PF", step=0.01)
        st.number_input("AE2 Voltage (V)", key="AE2_Volt", step=0.01)                
        st.number_input("AE2 F.O Temp (°C)", key="AE2_FO_TEMP", step=0.01)
        st.number_input("AE2 LO In Temp (°C)", key="AE2_LO_in_temp", step=0.01)
        st.number_input("AE2 LO Out Temp (°C)", key="AE2_LO_out_temp", step=0.01)
        st.number_input("AE2 LO Press (bar)", key="AE2_LO_press", step=0.01)
        st.number_input("AE2 LO Level (mm)", key="AE2_LO_lvl", step=0.01)
        st.number_input("AE2 Winding R Temp (°C)", key="AE2_WindingR_temp", step=0.01)
        st.number_input("AE2 Winding S Temp (°C)", key="AE2_WindingS_temp", step=0.01)
        st.number_input("AE2 Winding T Temp (°C)", key="AE2_WindingT_temp", step=0.01)

    with col3:
        st.subheader("AE3 parameters")
        st.number_input("AE3 TC In Exh Temp (°C)", key="AE3_TCin_Exhtemp", step=0.01)
        st.number_input("AE3 TC Out Exh Temp (°C)", key="AE3_TCout_Exhtemp", step=0.01)
        st.number_input("AE3 AC In Air Temp (°C)", key="AE3_ACin_Airtemp", step=0.01)
        st.number_input("AE3 AC Out Air Temp (°C)", key="AE3_ACout_Airtemp", step=0.01)
        st.number_input("AE3 TC RPM", key="AE3_TCRPM", step=0.01)
        st.number_input("AE3 KW", key="AE3_KW", step=0.01)
        st.number_input("AE3 Current (A)", key="AE3_CURR", step=0.01)
        st.number_input("AE3 Power Factor", key="AE3_PF", step=0.01)
        st.number_input("AE3 Voltage (V)", key="AE3_Volt", step=0.01)                
        st.number_input("AE3 F.O Temp (°C)", key="AE3_FO_TEMP", step=0.01)
        st.number_input("AE3 LO In Temp (°C)", key="AE3_LO_in_temp", step=0.01)
        st.number_input("AE3 LO Out Temp (°C)", key="AE3_LO_out_temp", step=0.01)
        st.number_input("AE3 LO Press (bar)", key="AE3_LO_press", step=0.01)
        st.number_input("AE3 LO Level (mm)", key="AE3_LO_lvl", step=0.01)
        st.number_input("AE3 Winding R Temp (°C)", key="AE3_WindingR_temp", step=0.01)
        st.number_input("AE3 Winding S Temp (°C)", key="AE3_WindingS_temp", step=0.01)
        st.number_input("AE3 Winding T Temp (°C)", key="AE3_WindingT_temp", step=0.01)

    with col4:
        st.subheader("AE4 parameters")
        st.number_input("AE4 TC In Exh Temp (°C)", key="AE4_TCin_Exhtemp", step=0.01)
        st.number_input("AE4 TC Out Exh Temp (°C)", key="AE4_TCout_Exhtemp", step=0.01)
        st.number_input("AE4 AC In Air Temp (°C)", key="AE4_ACin_Airtemp", step=0.01)
        st.number_input("AE4 AC Out Air Temp (°C)", key="AE4_ACout_Airtemp", step=0.01)
        st.number_input("AE4 TC RPM", key="AE4_TCRPM", step=0.01)
        st.number_input("AE4 KW", key="AE4_KW", step=0.01)
        st.number_input("AE4 Current (A)", key="AE4_CURR", step=0.01)
        st.number_input("AE4 Power Factor", key="AE4_PF", step=0.01)
        st.number_input("AE4 Voltage (V)", key="AE4_Volt", step=0.01)                
        st.number_input("AE4 F.O Temp (°C)", key="AE4_FO_TEMP", step=0.01)
        st.number_input("AE4 LO In Temp (°C)", key="AE4_LO_in_temp", step=0.01)
        st.number_input("AE4 LO Out Temp (°C)", key="AE4_LO_out_temp", step=0.01)
        st.number_input("AE4 LO Press (bar)", key="AE4_LO_press", step=0.01)
        st.number_input("AE4 LO Level (mm)", key="AE4_LO_lvl", step=0.01)
        st.number_input("AE4 Winding R Temp (°C)", key="AE4_WindingR_temp", step=0.01)
        st.number_input("AE4 Winding S Temp (°C)", key="AE4_WindingS_temp", step=0.01)
        st.number_input("AE4 Winding T Temp (°C)", key="AE4_WindingT_temp", step=0.01)  

def page_nine():
    st.title("📈 Ambient & Consumptions")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Summary 1")
        st.number_input("SW Temp (°C)", key="SW_TEMP", step=0.01)
        st.number_input("SW Press (bar)", key="SW_PRESS", step=0.01)
        st.number_input("ER Temp (°C)", key="ER_TEMP", step=0.01)
        st.number_input("SWpp In Press (bar)", key="SWpp_in_press", step=0.01)
        st.number_input("SWpp Out Press (bar)", key="SWpp_out_press", step=0.01)

    with col2:
        st.subheader("Summary 2")
        st.number_input("ME CLO FMR (lt/hr)", key="ME_CLO_FMR", step=0.01, format="%.2f")
        st.number_input("CLO Basic Feedrate (g/KWh)", key="CLO_Basic_Feedrate", step=0.01, format="%.2f")       
        st.number_input("ME F.O Cons (MT)", key="ME_FO_CONS", step=0.01)
        st.number_input("AE F.O Cons (MT)", key="AE_FO_CONS", step=0.01)
        st.number_input("Boiler F.O Cons (MT)", key="BOILER_FO_CONS", step=0.01)
        st.number_input("ME FMR (kg/hr)", key="ME_FMR", step=0.01, format="%.2f")
        st.number_input("AE FMR (kg/hr)", key="AE_FMR", step=0.01, format="%.2f")
        st.number_input("Boiler FMR (kg/hr)", key="BOILER_FMR", step=0.01, format="%.2f")            

def page_ten():
    st.title("📈 EGB & Boiler Parameters")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("EGB")
        st.number_input("EGB In Exh Temp (°C)", key="EGBIN_EXH_TEMP", step=0.01)
        st.number_input("EGB Out Exh Temp (°C)", key="EGBOUT_EXH_TEMP", step=0.01)
        st.number_input("EGB Water level (mm)", key="EGB_water_lvl", step=0.01)
        st.number_input("EGB Circwater Press (bar)", key="EGB_Circwater_press", step=0.01)
        st.number_input("Hot well Temp (°C)", key="Hotwell_temp", step=0.01)
        st.number_input("Hot well level (mm)", key="Hotwell_lvl", step=0.01)

    with col2:
        st.subheader("Boiler")
        st.number_input("Boiler Run hrs(°C)", key="BLR_RHR", step=0.01)
        st.number_input("Boiler Load (%)", key="BLR_LOAD", step=0.01)
        st.number_input("Boiler Water level (mm)", key="BLR_water_lvl", step=0.01)
        st.number_input("Main Steam Press (bar)", key="Main_Steam_press", step=0.01)
        st.number_input("Feed Water Press (bar)", key="Feed_water_press", step=0.01)
        st.number_input("Fuel oil Temp (°C)", key="BLR_FO_TEMP", step=0.01)
        st.number_input("Fuel oil Press (bar)", key="BLR_FO_PRESS", step=0.01)

def page_eleven():       
    st.title("📈 Navigation Parameters")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("Summary 1")
        st.number_input("Draft_fwd", key="Draft_fwd", step=0.01)
        st.number_input("Draft_aft", key="Draft_aft", step=0.01)
        st.number_input("Draft_mid_port", key="Draft_mid_port", step=0.01)
        st.number_input("Draft_mid_stbd", key="Draft_mid_stbd", step=0.01)
        st.number_input("Displacement", key="Displacement", step=0.01)
        st.number_input("Seastate", key="Seastate", step=0.01)
        st.number_input("Rudder_angle (°)", key="Rudder_angle", step=0.01)
        st.number_input("Rate_of_turn (°/min) ", key="Rate_of_turn", step=0.01)
        st.number_input("Depth_below_keel (m)", key="Depth_below_keel", step=0.01)      

    with col2:
        st.subheader("Summary 2")
        st.number_input("Apparent Wind Speed (m/s)", key="App_Wind_speed", step=0.01)
        st.number_input("Apparent Wind Direction (°)", key="App_Wind_dir", step=0.01)
        st.number_input("Air Temperature (°C)", key="Air_temp", step=0.01)
        st.number_input("Air Pressure (mmHg)", key="Air_press", step=0.01)
        st.number_input("Relative Humidity (%)", key="Rel_Humidity", step=0.01)
        st.number_input("Speed over Ground (knots)", key="SOG", step=0.01)
        st.number_input("Speed through Water (knots)", key="STW", step=0.01)
        st.number_input("Course (°)", key="Course", step=0.01)
        st.number_input("Heading (°)", key="Heading", step=0.01)

    with col3:
        st.subheader("Summary 3")
        st.number_input("Latitude", key="Latitude", step=0.000001, format="%.6f")
        st.number_input("Longitude", key="Longitude", step=0.000001, format="%.6f")
        st.number_input("Distance to Go (nm)", key="DTG", step=0.01)      
        st.number_input("Wave Height (m)", key="Wave_height", step=0.01)
        st.number_input("Wave Direction (°)", key="Wave_dir", step=0.01)
        st.number_input("Swell Height (m)", key="Swell_height", step=0.01)
        st.number_input("Swell Direction (°)", key="Swell_dir", step=0.01)
        st.number_input("Current Speed (knots)", key="Current_speed", step=0.01)
        st.number_input("Current Direction (°)", key="Current_dir", step=0.01)

    # --- 1. GLOBAL INITIALIZATION (At the top of your file) ---
    if "ETA" not in st.session_state:        
        st.session_state["ETA"] = "12:00"

    # --- 2. LAYOUT ---
    # If this is inside a function or a specific page, 
    # make sure this function is called immediately on run.
    with col4:
        st.subheader("Summary 4")

        st.number_input("Engine Miles (nm)", key="Eng_miles", step=0.01)
        st.number_input("Observed Miles (nm)", key="Obs_miles", step=0.01)
        st.number_input("Slip (%)", key="Slip", step=0.01)
        
        # This will now show up immediately because it's not hidden 
        # behind a 'if button_clicked:' check.
        st.text_input(
            label="ETA (hh:mm)", 
            max_chars=5, 
            key="ETA",
            help="Enter time in 24-hour format (e.g., 14:30)"
        )

def page_twelve():
    st.title("📈 CPP Common Parameters")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Summary 1")
        st.number_input("Ambient Temperature (°C)", key="Ambient_temp", step=0.01)
        st.number_input("Service Oil Temperature (°C)", key="Servooil_temp", step=0.01)
        st.number_input("Cooling Water Inlet Temperature (°C)", key="CWtemp_in", step=0.01)
        st.number_input("Cooling Water Outlet Temperature (°C)", key="CWtemp_out", step=0.01)
        st.number_input("Cooler Oil Inlet Temperature (°C)", key="Cooler_OilIn_temp", step=0.01)
        st.number_input("Cooler Oil Outlet Temperature (°C)", key="Cooler_OilOut_temp", step=0.01)

    with col2:
        st.subheader("Summary 2")
        st.number_input("Service Oil Pressure Ahead (bar)", key="Servooilpress_ahead", step=0.01)
        st.number_input("Service Oil Pressure Aft (bar)", key="Servooilpress_astern", step=0.01)
        st.number_input("CPP Pitch (%)", key="CPP_Pitch", step=0.01)
        st.number_input("Running Pump Number", key="Running_Pump_no", step=1)
        st.number_input("Running Pump Load (amps)", key="Running_pump_load", step=0.01)
        st.number_input("Sump Tank Level (mm)", key="Sumptk_level", step=0.01)

def page_thirteen():
    st.title("📈 Wartsila CPP Parameters")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Summary 1")
        st.number_input("CPP OD-ring_A1temp (°C)", key="ODring_A1temp", step=0.01)
        st.number_input("CPP OD-ring_A2temp (°C)", key="ODring_A2temp", step=0.01)
        st.number_input("CPP OD-ring_B1temp (°C)", key="ODring_B1temp", step=0.01)
        st.number_input("CPP OD-ring_B2temp (°C)", key="ODring_B2temp", step=0.01)
        st.number_input("CW Press (bar)", key="CW_press", step=0.01)
        st.number_input("Oil Main Supply Press (bar)", key="Oilmain_supplypress", step=0.01)
        st.number_input("Oil Main Return Press (bar)", key="Oilmain_returnpress", step=0.01)        

    with col2:
        st.subheader("Summary 2")
        st.number_input("Engine Load (%)", key="Engine_load", step=0.01)
        st.number_input("LO Filter Clog Indicator", key="LOfilterclog_ind", step=1)
        st.number_input("Remote Servo Pressure (bar)", key="Rem_servopress", step=0.01)       
