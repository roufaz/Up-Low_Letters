import streamlit as st
st.header('Upper and Lower Letters')
label=st.text_input('Enter a string')
btn=st.button('Click')

if btn:
    st.subheader(label.upper())
    st.subheader(label.lower())
    
st.image('hhh.jpg') 



