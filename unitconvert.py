# units converter

import streamlit as st

st.title("Unit_Converter")
st.markdown("### Convert Length, Weight, and Time Instantaly")
st.write("*Welcome! Select a category, and enter a value, and get the converted result in real-time*" "(*Make by Bilawal*)")

category = st.selectbox("Select Category", ["Length", "Weight", "Time"])

def convert_units(category,value,units):
    if category == "Length":
        if units == 'kilometers to miles':
            return value * 0.60934
        elif units == "miles to kilometers":
            return value / 1.6034
    
    elif category == "Weight":
        if units == "kilograms to pounds":
            return value * 2.20468
        elif units == "pounds to kilograms":
            return value / 2.20468

    elif category == "Time":
        if units == "minutes to hours":
            return value / 60
        elif units == "hours to minutes":
            return value * 60
        elif units == "seconds to minutes":
            return value / 60
        elif units == "minutes to seconds":
            return value * 60
        elif units == "hours to days":
            return value / 24
        elif units == "days to hours":
            return value * 24
    return 0

if category == "Length":
    units = st.selectbox("Select units",["kilometers to miles", "miles to kilometers"])
elif category == "Weight":
    units = st.selectbox("Select units",["kilograms to pounds", "pounds to kilograms"])
elif category == "Time":
    units = st.selectbox("select units",["minutes to hours", "hours to minutes", "seconds to minutes", "minutes to seconds", "hours to days", "days to hours"])

value = st.number_input("Enter Value")

if st.button("Convert"):
    result = convert_units(category, value, units)
    st.success(f"The result is {result:2f}")