import streamlit as st
import re


st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐 Password Strength Checker")
st.markdown("""
# welcome to the ultimate password strength checker! 👋🏻
use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            we will give you helpful tips to create a **Strong Password** 🔒""")


password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 9:
        score += 1
    else:
        feedback.append("❌Password should be at least 9 characters long.")
    
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("❌Password should have at least one lowercase and one uppercase letter.")

    if re.search("[0-9]", password):
        score += 1
    else:
         feedback.append("❌Password should have at least one number.")
    if re.search("[!@#$%^&*_,./]", password):
        score += 1
    else:
         feedback.append("❌Password should have at least one special character (!@#$%^&*_,./).")
    if score == 4:
        st.success("✅Your password is strong!")
    elif score == 3:
            st.warning("❌Your password is medium. Try to add a special character.")
    else:
          st.error("❌Your password is weak. Please make it stronger.")

    if feedback:
        st.markdown("## Improvement Suggestions:")
        for tip in feedback:
            st.write(tip)

else:
    st.write("Please enter a password to check its strength.")

