import streamlit as st

st.title("5GNET Control Panel")
st.write("Welcome to your first app!")

if st.button("Change Network Name"):
    st.write("Executing command...")

if st.button("Change Password"):
    st.write("Request sent to the modem!")

ip_input = st.text_input("Enter Modem IP:", "192.168.10.1")
