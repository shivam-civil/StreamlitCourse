
import streamlit as st 
import time 

if "name" not in st.session_state:
    st.session_state["name"]=None
if "user_id" not in st.session_state:
    st.session_state.user_id=None 



def home():
    st.set_page_config(page_title="Home Page ",page_icon="🏡")
    st.title("Home Page")
    st.write("This is home page of our webapp , use sidebar to navigate to other page")
    st.session_state["name"]=st.text_input("Your Name ")
    st.session_state["user_id"]=st.text_input("User ID ")
    if st.button("Submit"):
        st.success(f"Thanks {st.session_state.name}! Successfully Submitted!")


@st.cache_data
def about():
    st.set_page_config(page_title="About Section",page_icon="👤")
    st.title("This is about session.")
    st.write(f"And This is Shivam Yadav")

        
@st.cache_data
def dashboard():
    st.set_page_config("Dashboard",page_icon="📝")
    st.title("Dashboard")
    st.write("This is dashboard section.")
    time.sleep(3)
    st.write("Perfect.")

@st.cache_data
def developer():
    st.set_page_config(page_title="Developer Information",page_icon="🧑‍💻") 
    st.write("I'm Shivam Yadav, a civil engineering student aim to automate things in firm to reduce efforts and save time.")
    st.write("Email : ryuzaki.till@gmail.com")

# Dictionary to map page's names to their function
pages={
    "Home Page":home,
    "About Section":about,
    "Dashboard":dashboard,
    "Developer Info's":developer
}  

# Sidebar for page navigation
st.session_state.selected_page=st.sidebar.selectbox(label="Choose Page",options=pages.keys())

# RUn the page associated with selected page
pages[st.session_state.selected_page]()


