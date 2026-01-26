import streamlit as st 
from forms.allforms import contactform

@st.dialog("Contact Form")
def ContactForm():
    contactform()
    

col1,col2=st.columns(2)
col1.image("assets/profile.jpeg",width=260)
with col2:
    st.title("Shivam Yadav",anchor=False)
    st.write("A Civil Engineering Student learning Python to automate repititive tasks on construction company and to save time and efforts.")
    if st.button("Contact Me",on_click=ContactForm):
        pass 

st.subheader("Skills and Qualifications",anchor=False)
st.write("""
- Diploma in Civil Engineering (Central Engineering Campus)
- Python , SymPy , NumPy , SciPy , Pandas and Streamlit
- PostgreSQL                                   
""")


st.subheader("Future Plans ",anchor=False)
st.write("""
- Bachelors In Civil Engineering (Water Resources and Hydropower )
- FastAPI and React 
- AI/ML 
- Maybe Masters (After 2-4 yrs of Experience on Site)                           
""")

