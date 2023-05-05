import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image("/Users/aimankhan/Desktop/Python_Projects/app2_portfolio/images /photo.png")

with col2:
    st.title("Aiman Khan")
    content="""Hello, I am Aiman Khan,I am a Python programmer. I study at IIT Roorkee . """
    st.info(content)

content2="""Below you can find some apps I have built in Python.Feel free to contact me !"""
st.write(content2)

col3,emplty_col,col4=st.columns([1.5,0.5,1.5])

df=pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images /"+row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images /"+row["image"])
        st.write(f"[Source Code]({row['url']})")

