from copyreg import pickle
from time import time
from turtle import speed
from click import option
from nbformat import write
import streamlit as st
import pandas as pd
import pickle
from streamlit_lottie import st_lottie
import requests 

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets6.lottiefiles.com/private_files/lf30_1TcivY.json"
lottie_json = load_lottieurl(lottie_url)

lottie_url2 = "https://assets8.lottiefiles.com/packages/lf20_vixkj2dq.json"
lottie_json2 = load_lottieurl(lottie_url2)

def recommend(songs2):
    song_index=songs[songs['Song_name']==songs2].index[0]
    distances=similarity[song_index]
    songs_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]

    recommended_songs=[]
    
    for i in songs_list:
        recommended_songs.append(songs.iloc[i[0]].Song_name)
    return recommended_songs

    

song_dict=pickle.load(open('songs_dict.pkl','rb'))
songs=pd.DataFrame(song_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Music Recommender System')
st_lottie(lottie_json,height=200,width=300)


option=st.selectbox('Select the song',songs['Song_name'].values)

if st.button('Recommend'):
    Recommendations=recommend(option)
    for i in Recommendations:
        st.write(i)

st_lottie(lottie_json2,height=150,width=700)