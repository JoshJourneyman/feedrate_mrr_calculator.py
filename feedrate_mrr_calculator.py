
import streamlit as st

st.title("CNC Feedrate & MRR Calculator")

rpm = st.number_input("Spindle Speed (RPM)", min_value=100, max_value=15000, step=10)
fpt = st.number_input("Feed per Tooth (in)", min_value=0.001, max_value=0.05, step=0.001, format="%.3f")
flutes = st.number_input("Number of Flutes", min_value=1, max_value=20, step=1)
width = st.number_input("Width of Cut (in)", min_value=0.01, max_value=10.0, step=0.01)
depth = st.number_input("Depth of Cut (in)", min_value=0.01, max_value=1.0, step=0.01)

if st.button("Calculate"):
    feedrate = rpm * fpt * flutes
    mrr = width * depth * feedrate

    st.subheader("Machining Summary")
    st.write(f"**Feedrate:** {feedrate:.2f} IPM")
    st.write(f"**Material Removal Rate:** {mrr:.2f} in³/min")
