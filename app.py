import os
import streamlit as st
import pickle
import pandas as pd
import numpy as np

psl = pickle.load(open('model\psl.pkl', 'rb'))

teams = ['Quetta Gladiators', 'Peshawar Zalmi', 'Karachi Kings', 'Islamabad United', 'Lahore Qalandars', 
        'Multan Sultans']


cities = ['Dubai', 'Sharjah', 'Karachi', 'Lahore', 'Rawalpindi']


st.title('PSL Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))

with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')

with col4:
    overs_completed = st.number_input('Overs completed (Works for over > 5)')

with col5:
    wickets = st.number_input('Wickets out')

last_five_overs = st.number_input('Runs scored in last 5 overs')

if st.button('Predict'):
    wickets_left = 10-wickets
    crr = current_score/overs_completed

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 'current_score': [current_score], 
     'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five_overs]})
    
    #st.table(input_df)
    result = psl.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))


