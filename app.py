import streamlit as st

st.title("$$Streamlit Demo$$")

st.write("Hi I am vivek")

x=st.text_input("type name")

st.write('name is : ',x.upper())
st.write('name is : ',x.title())


l1=['sholay','deewar','agneepath','hum']

f=st.radio("select one from the list : ",l1)
st.write("yes you selected : ",f)

a=st.selectbox("select one :",l1)

st.write(a)