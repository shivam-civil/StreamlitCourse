import streamlit as st 
from datetime import datetime
form_values={
    "name":None,
    "address":None,
    "gender":None,
    "dob":None
}
max_date=datetime.now()
min_date=datetime(1999,1,1)
with st.form(key="form_1"):
    st.header("Application Form")
    form_values["name"]=st.text_input("Your Name ")
    form_values["address"]=st.text_input("Your Address ")
    form_values["gender"]=st.selectbox("Gender",["Male","Female","Other"])
    form_values["dob"]=st.date_input(label="Date Of Birth",min_value=min_date,max_value=max_date)
    clicked=st.form_submit_button(label="Submit Now")
    if clicked : 
        if not all(form_values.values()): 
            st.warning("Please fill up all datas")
        else :
            st.balloons()
            st.write("### Info")
            for (key,value) in form_values.items():
                st.write(f"{key}: {value}")
