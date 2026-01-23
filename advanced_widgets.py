import streamlit as st 

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False 

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox
st.checkbox("Show Input Field ",on_change=toggle_input,value=st.session_state.checkbox)        

if st.session_state.checkbox :
    user_input=st.text_input("Write Something",value=st.session_state.get("user_input",""))
    st.session_state.user_input=user_input
else : 
    user_input=st.session_state.get("user_input","")

st.write(f"User Input : {user_input}")
