import streamlit as st 

def contactform():
    name=st.text_input("Your Name ")
    email=st.text_input("Your Email")
    with st.expander(label="Add Optional Details"):
        extra_info=st.text_area("Your Optional Information")
    message=st.text_area("Your Message")
    if st.button("Submit"):
        st.success("🚀Message Sent Successfully✅!")    
