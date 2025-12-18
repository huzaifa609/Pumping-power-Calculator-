import streamlit as st

st.title("Pumping Power Calculator")

st.write("This app calculates pumping power for a fluid system")

# Inputs
Q = st.number_input("Flow rate Q (m³/s)", min_value=0.0, step=0.01)
H = st.number_input("Pump head H (m)", min_value=0.0, step=0.1)
rho = st.number_input("Fluid density ρ (kg/m³)", value=1000.0)
eff = st.number_input("Pump efficiency (0 to 1)", min_value=0.01, max_value=1.0, value=0.7)

g = 9.81

if st.button("Calculate"):
    power = (rho * g * Q * H) / eff
    st.success(f"Pumping Power = {power:.2f} W")
    st.success(f"Pumping Power = {power/1000:.2f} kW")
