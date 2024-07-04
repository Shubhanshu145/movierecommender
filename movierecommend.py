import streamlit as st
import pickle
import pandas as pd
import requests


# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ec54fc083da16332738dd3c8fa68b6e6&language=en-US'.format(movie_id))
#     data = response.json
#     poster_path = data[poster_path]
#     return " https://image.tmdb.org/t/p/w500/" + poster_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0 ]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended=[]
    recommended_movies_poster = []
    for i in distances[1:6]:
        #movie_id = movies.iloc[i[0]].id
        #fetch poster from the API
        #recommended_movies_poster.append(fetch_poster(movie_id))
        recommended.append(movies.iloc[i[0]].title)
        
    return recommended

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name  = st.selectbox(
    'Type or select a movie from drop-down.',
     (movies['title'].values)
)
if st.button("recommend"):
    names = recommend(selected_movie_name)
    for i in names:
        st.write(i)
    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])

    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
