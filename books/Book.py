import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv('data/customerReviews.csv')
df_top100_books = pd.read_csv('data/Top100TrendingBooks.csv')

price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()

price = st.sidebar.slider('Price Range', price_min, price_max, price_max)

df_books = df_top100_books[df_top100_books['book price'] <= price]
df_books

fig_year_publication = px.bar(df_books['year of publication'].value_counts())
fig_book_price = px.histogram(df_books['book price'])

col1, col2 = st.columns(2)

col1.plotly_chart(fig_year_publication)
col2.plotly_chart(fig_book_price)