import streamlit as st
import pandas as pd
from src import Operations as op

header_style = """
    <style>
        .bold-header {
            font-weight: bold;
            font-size: 2.75em;
        }
        .italic-text {
            font-style: italic;
            font-size: 1.5em;
        }
        .sidebar-radio label {
            font-size: 1.5em !important;
        }
        italic-new{
            font-style: italic;
            font-size: 3.0em;
        }
        .bold-2 {
            font-weight: bold;
            font-size: 2.0em;
        }
        .bold-1 {
            font-weight: bold;
            font-size: 1.0em;
        }
    </style>
"""
st.markdown(header_style, unsafe_allow_html=True)  
st.markdown("<h1 style='text-align: center;'>Smart Irrigation</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Optimal Water Use for Sustainable Agriculture</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>🌱🌊🌟</h1>", unsafe_allow_html=True)
st.text("")
st.text("")
st.markdown("""<p class='italic-text'>
Welcome to our groundbreaking project! 
Our mission is to revolutionize irrigation practices in agriculture by introducing a cutting-edge approach that harnesses the power of binary operations. 🌾💡</p>""",unsafe_allow_html=True)
st.text("")
st.markdown("""<p class='italic-text'>Our primary objective is to enhance the efficiency and sustainability of irrigation systems. 🔄 By seamlessly blending binary calculations with a sophisticated mathematical equation tailored for irrigation.🌏💧</p>""",unsafe_allow_html=True) 
st.text("")
st.text("")
st.markdown("""<p class='italic-text'>The irrigation duration for any crop can be found out which helps us to efficiently grow crops in suitable places.</p>""",unsafe_allow_html=True) 
st.text("")
st.text("")
col1, col2 = st.columns(2)

col1.markdown("""<p class='italic-text'>Data from region A:</p>""",unsafe_allow_html=True) 
col2.markdown("""<p class='italic-text'>Data from region B:</p>""",unsafe_allow_html=True) 

crop_et1 = col1.number_input("Crop ET of Region A: ")
kc1 = col1.number_input("Crop Coefficient of Region A: ")
rainfall1 = col1.number_input("Rainfall of Region A: ")
evaporation1 = col1.number_input("Evaporation of Region A: ")
swhc1 = col1.number_input("Soil Water Holding Capacity of Region A: ")
field_area1 = col1.number_input("Field Area of Region A: ")

crop_et2 = col2.number_input("Crop ET of Region B: ")
kc2 = col2.number_input("Crop Coefficient of Region B: ")
rainfall2 = col2.number_input("Rainfall of Region B: ")
evaporation2 = col2.number_input("Evaporation of Region B: ")
swhc2 = col2.number_input("Soil Water Holding Capacity of Region B: ")
field_area2 = col2.number_input("Field Area of Region B: ")
st.text("")
st.text("")
col3, col4 = st.columns(2)

if st.button(" Calculate "):
    with col3:
        prod1 = op.boothmultiplication(crop_et1, kc1)
        sub1 = op.binarysubtraction(rainfall1, evaporation1)
        add1 = op.binaryaddition(prod1, sub1)
        res1 = op.restoringdivision(swhc1, field_area1)
        nonres1 = op.nonrestoringdivision(add1, res1[1])
        result1 = (float(add1) / float(res1[1]))
    with col4:
        prod2 = op.boothmultiplication(crop_et2, kc2)
        sub2 = op.binarysubtraction(rainfall2, evaporation2)
        add2 = op.binaryaddition(prod2, sub2)
        res2 = op.restoringdivision(swhc2, field_area2)
        nonres2 = op.nonrestoringdivision(add2, res2[1])
        result2 = (float(add2) / float(res2[1]))
        
    col3.write(f"Irrigation duration of Region A: {result1:.2f}")
    col4.write(f"Irrigation duration of Region B: {result2:.2f}")
    
    st.markdown("""<p class='bold-2'>Conclusion:</p>""",unsafe_allow_html=True) 
    if (nonres1<nonres2):
        st.write("Region A is more water efficient than Region B")
    elif(nonres1==nonres2):
        st.write("Region A and B are equally water efficient")
    else:
        st.write("Region B is more water efficient than Region A")