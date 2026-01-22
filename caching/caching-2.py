import streamlit as st 

path="example.txt"

@st.cache_resource
def make_file():
    # opening the file in append mode which creates the file if not exist 
    file=open(path,"a+")
    return file 

# Use the cached file handler 
file_handler=make_file()

# write to the file using the cached handler 
if st.button("Write to file"):
    file_handler.write("New line of text\n")
    file_handler.flush() # Ensures the content is written immediately 
    st.success("Wrote a new line to the file!")

# Read and display the file contents 
if st.button("Read File "):
    file_handler.seek(0)  # Move to the beginning og the file 
    content=file_handler.read()
    st.text(content)

# Always make sure to close the file when done (useful for resource cleanup)
st.button("Close File",on_click=file_handler.close)
