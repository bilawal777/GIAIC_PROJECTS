import streamlit as st


st.set_page_config(page_title= "growth mindset project")
st.title("Growth Mindset Challenge: Web App with Streamlit ")

st.header("Welcome to Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a gorwth mindset with reflection, challenges, and achievements!")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal ; it is the courage to continue that counts. Winston Churchill")

st. header("What's your Challlenge you're facing:")
user_input = st.text_input("Discribe a challenge you're facing: ")


#condition 
if user_input:
    st.success(f"you're facing:{user_input}. Keep pushing forward towords your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflection on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great Insight! your reflection: {reflection}")
else:
    st.info("Reflection on past experience help you grow! shre your difficulties")


#acheivements
st.header("Celebrate your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")


if acheivment:
    st.success(f"Amazing! you achieved:{acheivment}")
else:
    st.info("Big or small, every acheivment counts! share one now ")


#footer
st.write("- - -")
st.write("Keep bilieving in yourself. Growth is a journey, not a destination")
st.write("*Create by bilawal*")
