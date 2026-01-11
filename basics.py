
# IMPORT STREAMLIT MODULE 
import streamlit as st 
from datetime import date

# SET WEB PAGE CONFIGURATION 

st.set_page_config(
    page_title="My WebApp",
    page_icon="😁"  # OR file.png
   #layout="wide"   -
)

# TITLE OF WEBPAGE 
st.title("Title")

# HEADER OF WEBPAGE 
st.header("Header")

# SUBHEADER OF WEBPAGE 
st.subheader("Subheader")

# NORMAL WRITE 
st.write("This is **write**")
st.text("This is **text**")

# INPUT FROM USER 
name=st.text_input("Your Name ")
age=st.number_input("Your Age ",min_value=0)

# SELECT BOX 
method = st.selectbox("Select Method ",["HI METHOD","RISE FALL METHOD "])
if st.button("Done"):
    st.write(f"You selected {method}")
    st.text(f"You selected {method}")
    st.success(f"You selected {method}")
    st.warning(f"You selected {method}")

# radio in streamlit 
gender=st.radio("Gender",["Male","Female"])
st.success(f"Wow you are {gender}")


# COLUMNS IN STREAMLIT 

coln1,coln2=st.columns(2)

with coln1:
    drink=st.radio("Favourite drink",["Water","Always Water"])
with coln2:
    food=st.radio("Favourite Food",["Clean Diet","Always Clean Diet"])  

if st.button("OK"):
    st.success("Wow You are a healthy guy.")  

# CHECK BOX 
exist=st.checkbox("Alive ")
if st.button("DOne "):
    if exist==True:
        st.success("Wow how are you doing on Earth.")
    elif exist==False:
        st.success("Wow brother, Are you running my scripts in hell ? ")  

# SLIDER IN STREAMLIT 
age=st.slider("Your Age ",0,150,18)     
if st.button("Send"):
    st.success(f'Wow your age is {age}')     


# DATE INPUT 

dob=st.date_input(
    "Select Date",
    min_value=date(1999,1,1),
    max_value=date.today()
)
st.write(f"Well you born on {dob}")


# IMAGE IN STREAMLIT    - IMAGE SHOULD BE IN CWD 

st.image(
    "image.png",
    width=400,
    caption="Leveling Automation"
)
st.image(
    "https://images.pexels.com/photos/8486976/pexels-photo-8486976.jpeg",
    width=400,
    caption="Surveying"
)

# UPLOAD FILE 
uploaded=st.file_uploader("Upload Site Image",["png","jpg","jpeg"])

if uploaded:
    st.image(uploaded,caption="Uploaded Image")


# SIDEBAR 
company_logo=st.file_uploader("Company Photo ",["png","jpeg","jpg"])
if st.button("SET PROFILE"):
    st.sidebar.image(company_logo,caption="Apex Construction")
yourname=st.sidebar.text_input("Your Name ")
st.sidebar.write(f"Well {yourname.strip().split(" ")[0]}")


# EXPANDER 
with st.expander("View Tutorial"):
    st.write(""" 
    1. Clean your mindset 
    2. Fix your dopamine
    3. Fix your distractions.
    4. Just do what you commited 
    5. Build it as your habit.
    """)
    st.image("image.png",width=400,caption="Tutorial With Image")

# MARKDOWN 
st.markdown("## Code to install Streamlit")  # for headings,main section, subsections
st.markdown("> pip install streamlit")       # for blockquote
st.markdown("I am *italic*")
st.markdown("I am **bold**")
st.markdown("Use `pip install  streamlit` to install streamlit ")

# SUPPORTS LaTex FOR VISULAIZATION OF FORMULA 
st.markdown(r"""  
### BENDING MOMENT FORMULA
$$
M = \frac{wl^2}{8}
$$
$$
L=\frac{M}{L}
$$
""")

# INLINE MATH
st.markdown(r" Formula for inner cover : $d=D-cover$")