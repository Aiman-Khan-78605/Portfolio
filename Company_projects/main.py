import streamlit as st
import pandas

st.title("The Best Company")

st.write("A company is a legal entity formed by a group of individuals to engage in and operate a business—commercial or industrial—enterprise. A company may be organized in various ways for tax and financial liability purposes depending on the corporate law of its jurisdiction.")

col1,col2,col3=st.columns(3)

df=pandas.read_csv("data (1).csv",sep=",")

with col1:
        for index, row in df[:4].iterrows():
            st.header(f"{row['first name'].title()} {row['last name'].title()}")
            st.write(row["role"])
            st.image("/Users/aimankhan/Desktop/Python_Projects/Company_projects/images (2)/"+ row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("/Users/aimankhan/Desktop/Python_Projects/Company_projects/images (2)/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("/Users/aimankhan/Desktop/Python_Projects/Company_projects/images (2)/" + row["image"])
