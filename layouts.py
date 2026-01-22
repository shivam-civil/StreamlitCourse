import streamlit as st 

# Sidebar layout 
st.sidebar.title("This is Sidebar")
st.sidebar.write("You can place elements like sliders,buttons and text here.")
sidebar_input=st.sidebar.text_input("Write Something in sidebar ")


# Tabs layout 
tab1,tab2,tab3=st.tabs(["Tab 1","Tab 2","Tab 3"])
with tab1:
    st.write("You are in Tab 1")
with tab2:
    st.write("You are in Tab 2")
with tab3:
    st.write("You are in Tab 3 ")

# Columns layout 
col1,col2=st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for col1")

with col2:
    st.header("Column 2")
    st.write("Content for column2 ")

# Container example
with st.container(border=True):
    st.write("This is inside a container.")
    st.write("You can think of containers as a grouping of elements.")
    st.write("Containers help manage sections of the page")
 
# Empty placeholder 
placeholder=st.empty()
placeholder.write("This is an empty placeholder,useful for dynamic content")

if st.button("Update Placeholder "):
    placeholder.write("The content of placeholder has bemm updated.")

# Expander 
with st.expander("Expand for more details"):
    st.write("This is additional information that is hidden by default.")    
    st.write("You can use expanders to keep your interface cleaner.")

# Pop Over (Tooltip)
st.write("Hover over this button for a tooltip ")
st.button("Button With Tooltip",help="This is tooltip or popover on hover.")   


# Sidebar input handling 
if sidebar_input:
    st.write(f"You entered in side bar : {sidebar_input}")

