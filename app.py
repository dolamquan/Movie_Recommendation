import streamlit as st
import pickle
import requests

new_data = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

#Fetch poster function
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=[your_api_key]&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/"+poster_path

#Recommendation function
def recommend(movie):
    index = new_data[new_data['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True, key=lambda vector:vector[1])
    recommended_movies = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = new_data.iloc[i[0]].id
        recommend_poster.append(fetch_poster(movies_id))
        recommended_movies.append(new_data['title'].iloc[i[0]])
        print(new_data['title'].iloc[i[0]])
    return recommended_movies, recommend_poster


st.header("Movie Recommendation System")
value = st.selectbox("Select a movie from dropdown",new_data['title'])

if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
