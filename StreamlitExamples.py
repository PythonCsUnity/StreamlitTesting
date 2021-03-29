import streamlit as st
import pandas as pd
import numpy as np
# streamlit run StreamlitExamples.py in terminal

st.text("Yes")
st.write("Hello *world*")
st.markdown("OMG **YESS**")
st.latex('''a + ar + a r^2''')
st.title("Title")
st.header("header")
st.subheader("subheader")
age = st.slider('How old are you?', 0, 150, 25)
st.write("I'm ", age, 'years old')
chart_data = pd.DataFrame({
    'x': [1, 2, 3],
    'y': [1, 2, 1]
})
chart_data = chart_data.set_index('x')
st.line_chart(chart_data)
df = pd.DataFrame({
  'date': ['10/1/2019','10/2/2019', '10/3/2019', '10/4/2019'],
  'second column': [10, 20, 30, 40]
})
df = df.rename(columns={'date':'index'}).set_index('index')
st.line_chart(df)
st.text_area("Hello")
st.text_input("YEs please", "hi")
if st.button("Hello"):
    st.button("Hello There !")
if st.checkbox("I agree"):
    st.write("Great")
number = st.radio("wut is fav number?", [1, 2, 3, 4, 5, 6, 7, 8, 9, "Not here"])
if number == 1:
    st.write("SAME!")
else:
    st.write("Cool")
option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)
options = st.multiselect('What are your favorite colors',['Green', 'Yellow', 'Red', 'Blue'],['Yellow', 'Red'])
st.write('You selected:', options)