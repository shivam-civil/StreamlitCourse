import streamlit as st 
# rerun certain portion of the code 

st.title("My Awesome App")

@st.fragment()
def toggle_and_text():   # cant return data , use st.session_state 
    cols=st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter Text")

@st.fragment()
def filter_and_file():
    new_cols=st.columns(3)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload Image")
    new_cols[2].selectbox("Choose Option",["Option 1","Option 2","Option 3","Option 4"])


toggle_and_text()
cols=st.columns(2)
cols[0].selectbox("Select",[1,2,3],None)
cols[1].button("Update")
filter_and_file()

