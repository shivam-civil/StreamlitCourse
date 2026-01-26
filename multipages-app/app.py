import streamlit as st 

# Setup all the pages (objects)

Dashboard=st.Page(
    page="contents/dashboard.py",
    title="Dashboard",
    icon="📈",
    default=True
)

AboutMe=st.Page(
    page="contents/aboutme.py",
    title="About Me",
    icon="🧞‍♂️"
)

DeveloperContact=st.Page(
    page="contents/developercontact.py",
    title="Developer Contact",
    icon="🧑‍💻"
)

# Set navigation with sections 
nav=st.navigation(
    {
        "Tools":[Dashboard],
        "Info's":[AboutMe,DeveloperContact]
    }
)

# run the navigation 
nav.run()

# Shared contents on all pages 
st.sidebar.write("Made with 💌 by Shivam")
