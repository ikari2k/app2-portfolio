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

content2 = """
            Ipsum tempor occaecat id ex est eiusmod sunt irure in et. Proident laborum magna laborum ea laboris ex adipisicing consectetur ut reprehenderit. Dolor commodo ea dolor veniam. Consectetur eu nulla ex occaecat laborum irure officia ut esse exercitation dolor nostrud commodo irure. Labore sint aute enim laborum aliquip sunt deserunt incididunt ullamco non deserunt. Reprehenderit culpa amet et deserunt magna ea aliquip commodo elit minim minim. Deserunt nulla proident ea officia laboris ullamco est veniam cillum in.

            Eiusmod fugiat est aliquip commodo irure ea dolore fugiat veniam labore officia. Consectetur et ut minim cillum deserunt non laboris eu minim mollit. Culpa ullamco Lorem duis culpa. Ex aliqua cillum dolor Lorem ex. Do ullamco aliquip dolore amet in. Proident consequat ipsum sunt eiusmod exercitation exercitation.

            Duis irure in et veniam consectetur consectetur ea sunt anim aliquip amet voluptate magna qui. Officia esse Lorem nisi sunt. Exercitation esse officia quis est consectetur ad eiusmod tempor aliquip incididunt laborum.
            """
st.write(content2)