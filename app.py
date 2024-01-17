import pickle


import pandas as pd
import streamlit as st
from streamlit.components.v1 import iframe


def recommend(skill):
    job_index = jobs[jobs['skills'] == skill].index[0]
    distances = similarity[job_index]
    job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    job_output = []
    for i in job_list:
        job_output.append(jobs.iloc[i[0]].jobtitle)
        print(jobs.iloc[i[0]].jobtitle)
    return job_output

st.title('Job recommendation system')

job_dict = pickle.load(open('job_recommend.pkl', 'rb'))
jobs = pd.DataFrame(job_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

Selected_skill = st.selectbox(
    'Enter or  Select Your Fav Movie',
    jobs['skills'].values)
st.write('You selected skill :', Selected_skill)


if st.button('Ask?', type="primary"):
    container = st.container(border=True)
    container.write('And below are the closest Job Options you can pursue : ')
    recomendations = recommend(Selected_skill)
    for i in recomendations:
        container.write(i)


