import streamlit as st
import random

word = random.choice('bcdfghjklmnprstvwyz')+random.choice('aeiou')+random.choice('bcdfgklmnpstvwz')

st.title('BAB')
st.button('NEXT WORD')
st.write('<center><h1><font size="7"><big><big>'+word+'</big></big></font></h1></center>', unsafe_allow_html=True)