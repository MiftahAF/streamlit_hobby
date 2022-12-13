import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('Hobby_kids.sav','rb'))
st.title('Prediksi Hobi Anak')

Olympiad_Participation = st.number_input('Partisipasi Olimpiade')

col1, col2, col3, col4 = st.columns (4)

with col1: 
    Scholarship = st.number_input('Beasiswa')
with col2:
    School = st.number_input('Sekolah')
with col3:
    Fav_sub = st.number_input('Pelajaran Favorit')
with col4:
    Projects = st.number_input('Projek yang sudah dikerjakan')
with col1:
    Grasp_pow = st.number_input('Kekuatan Menggenggam')
with col2:
    Time_sprt = st.number_input('Waktu yang dihabiskan untuk berolahraga')
with col3:    
    Medals = st.number_input('Medali yang sudah di dapatkan dalam olahraga')
with col4:    
    Career_sprt = st.number_input('Cita-cita dalam bidang olahraga')
with col1:
    Act_sprt = st.number_input('Sering olahraga atau tidak')
with col2:    
    Fant_arts = st.number_input('Suka membuat lukisan fantasi')
with col3:
    Won_arts = st.number_input('Apakah sudah pernah juara dalam kompetisi seni')
with col4:
    Time_art = st.number_input('Waktu yang dihabiskan untuk seni')

result = ''

if st.button ('Prediksi Hobby Anak'):
    prediction = model.predict([[Olympiad_Participation,Scholarship,School,Fav_sub,Projects,Grasp_pow,Time_sprt,Medals,Career_sprt,Act_sprt,Fant_arts,Won_arts,Time_art]])

    if(prediction[0] == 1):
        result = 'Hobby masa depan anak adalah akademik'

    elif (prediction[0]== 2):
        result = 'Hobby masa depan anak adalah Seni'

    else : 
        result = 'Hobby masa depan anak adalah olahraga'

st.success(result)
st.write('191351164 MiftahAF')


