import streamlit as st 

# SET PAGE CONFIGURATION 

st.set_page_config(
    page_title="Form Dashboard",
    page_icon="📒"
)
with st.form(key="mykey") :
    st.markdown("## 📒 Form Dashboard ")
    name=st.text_input("Your Name ")
    address=st.text_input("Your Address ")
    coln1,coln2 = st.columns(2)
    with coln1:
        age=st.slider("Age ",0,150,18)
    with coln2:
        gender=st.selectbox("Gender",["Male","Female","Other"])  
    role=st.selectbox("Role ",["Site Enginner","Managing Director","Civil Enginner","Electircal Enginner","Contractor","Client","Company Owner"])  
    photo=st.file_uploader("Your Photo ",["jpg","jpeg","png"]) 
    submitted=st.form_submit_button("Submit")


    if submitted : 
     st.success(f"Hey {name}, Your profile is sent for **verification**. \nIt might take 24 hours for verification.\nThanks for **signing up** with **Apex Developers** Construction ")
