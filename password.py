import streamlit as st
import re

#page styling
st.set_page_config(page_title = "Password Strength")
st.title("Password Strength Generator")
st.write("Enter your password below to check its security level. ")

#function to check password strength

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score  += 1 #incressed score by 1
    else:
        feedback.append("Password should be **atleast 8 character long**.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include ** both upper case (A-Z) and lower case (a-z) letters**.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("password should include ** at least one number (0-9)**.")
    
#special characters
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("Include **at least one special character (!@#$%^&*)**.")

#display password strength results
    if score == 4:
        st.success("**Strong Password** Your password is secure.")
    elif score == 3:
        st.info("**Moderate Password** - Your password is secure.")
    else:
        st.error("**Week Password**")

#feedback
    if feedback:
        with st.expander("**Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong ")

#Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("please enter a password first! ") #show warning if password empty

st.write("*Created by Bilawal*")