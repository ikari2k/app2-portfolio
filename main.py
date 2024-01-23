import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content= """
            In tempor cillum fugiat incididunt. Aliquip do sint ut ipsum incididunt nostrud nulla ullamco esse. 
            Ullamco et nisi voluptate cupidatat. Commodo ad minim sunt eiusmod eiusmod fugiat. 
            Occaecat duis enim nisi fugiat do occaecat exercitation.
            """
    st.info(content)