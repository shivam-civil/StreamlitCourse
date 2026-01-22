import streamlit as st 

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info={}

def gotostep2(name):
    st.session_state.info["name"]=name
    st.session_state.step=2
def gotostep1():
    st.session_state.step=1

if st.session_state.step==1:
    st.header("Part 1 : Info")
    name=st.text_input("Name",value=st.session_state.info.get("name",""))
    st.button("Next",on_click=gotostep2,args=(name,))
        
if st.session_state.step==2:
    st.header("Part 2 : Review")
    st.subheader("Please Review this.")
    st.write(f"Name : {st.session_state.info.get("name","")}")
    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info={}
    st.button("Back",on_click=gotostep1)    





     

