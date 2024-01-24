import streamlit as st
import pandas
from st_pages import Page, show_pages

st.set_page_config(layout="wide")

show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Page("pages/contact_us.py", "Contact Us", "📧")
    ]
)

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Mateusz P.")
    content= """
            I am Mateusz, python developer wannabe! 
            """
    st.info(content)

content2 = """
            Below you can find some of the apps I have built in Python!
            """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[source Code]({row['url']})")
