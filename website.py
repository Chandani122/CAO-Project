import streamlit as st
import pandas as pd
from src import Operations as op
from PIL import Image

header_style = """
    <style>
        .bold-header {
            font-size: 2.75em;
            text-align: center;
        }
        .italic-text {
            font-style: italic;
            font-size: 1.5em;
        }
        .italic-new{
            font-style: italic;
            font-size: 1.75em;
            text-align: center;
        }
        .bold-2 {
            font-weight: bold;
            font-size: 2.0em;
        }
        .font-1 {
            font-size: 1.5em;
        }
    </style>
"""
st.markdown(header_style, unsafe_allow_html=True)  
st.markdown("<h1 class='bold-header'>SMART IRRIGATION</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='italic-new'>Optimal water use for sustainable agriculture</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>🌱🌊🌟</h1>", unsafe_allow_html=True)

st.text("")
st.text("")

st.markdown("""<h3 class='bold-2'>OBJECTIVE:</h3>""", unsafe_allow_html=True)
st.text("")
st.markdown("""<p class='italic-text'>The primary objective of our project is to conduct a comprehensive analysis of water efficient crop irrigation practices in two distinct regions. The irrigation duration for any crop can be found out which helps us to efficiently grow crops in suitable places.</p>""", unsafe_allow_html=True)

st.text("")
st.text("")

st.markdown("""<h3 class='bold-2'>FORMULA USED:</h3>""", unsafe_allow_html=True)
st.text("")
st.markdown("""<p class='italic-text'>[(Crop ET x Crop coefficient) + (Rainfall - Evaporation)] / (Soil water holding capacity / Field Area)</p>""",unsafe_allow_html=True) 

st.text("")
st.text("")

st.markdown("""<h3 class='bold-2'>ALGORITHMS:</h3>""", unsafe_allow_html=True)
st.text("")

booth = "src/boothmultiplication.png"
res = "src/restoringdivision.png"
nonr = "src/nonrestoringdivision.png"

img1 = Image.open(booth)
img2 = Image.open(res)
img3 = Image.open(nonr)

st.markdown("""<p class='italic-text'>Booth Multiplication:</p>""",unsafe_allow_html=True) 
st.image(img1)
st.text("")
st.markdown("""<p class='italic-text'>Restoring Division:</p>""",unsafe_allow_html=True) 
st.image(img2)
st.text("")
st.markdown("""<p class='italic-text'>Non-restoring Division:</p>""",unsafe_allow_html=True) 
st.image(img3)

st.text("")
st.text("")

st.markdown("""<h3 class='bold-2'>CALCULATION:</h3>""", unsafe_allow_html=True)
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
    
    col3.success(f"Irrigation duration of Region A: {result1:.2f}")
    col4.success(f"Irrigation duration of Region B: {result2:.2f}")
    
    if (nonres1<nonres2):
        st.markdown("""<p class='italic-text>Region A is more water efficient than Region B.</p>""", unsafe_allow_html=True)
    elif(nonres1==nonres2):
        st.write("""<p class='italic-text>Region A and B are equally water efficient.</p>""", unsafe_allow_html=True)
    else:
        st.write("""<p class='italic-text'>Region B is more water efficient than Region A.</p>""", unsafe_allow_html=True)

    st.markdown("""<h3 class='bold-2'>CONCLUSION:</h3>""",unsafe_allow_html=True) 
    st.text("")
    st.markdown("""<p class='italic-text'>The project highlights regional disparities in water-efficient crop irrigation. This underscores the importance of optimizing irrigation practices for sustainability and encourages policymakers to promote water-saving techniques in agriculture for a more secure and environmentally responsible future.</p>""", unsafe_allow_html=True)
    st.text("")
