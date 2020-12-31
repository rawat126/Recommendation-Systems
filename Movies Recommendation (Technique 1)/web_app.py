# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 00:33:11 2020

@author: Ragvender Rawat
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir(r'/content/drive/My Drive/Projects')

count_data = pd.read_csv(r'count_data.csv')
data = np.load(r'pivot_table.npz')
correlation_table = pd.DataFrame(data['arr_1'])
correlation_table.columns = data['arr_2']
correlation_table.index = data['arr_3']

all_movies = correlation_table.columns()

movie_name = st.selectbox('Select The Last Movie : ', all_movies)

corr_movies = correlation_table.corrwith(correlation_table[movie_name])
corr_movies.reset_index(inplace = True)
corr_movies.columns = ['Title','Correlation']

movies = pd.merge(count_data,corr_movies,on = 'title')
selected_movies = movies[movies['Counts']>80].sort_values(by = 'Correlation',ascending = False)
selected_movies = selected_movies.head(20).values

