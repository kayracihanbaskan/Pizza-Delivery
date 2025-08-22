import streamlit as st
import sqlite3 as sql

st.header("Catalog")

# Connection and Cursor
connection = sql.connect("pizza_database.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM pizzas")
pizzas = cursor.fetchall()

for pizza in pizzas:
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image(pizza[6])
    with col2:
        st.subheader(pizza[1])
        st.write(pizza[5])
    with col3:
        st.write("Small",pizza[2],"₺")
        st.write("Medium",pizza[3],"₺")
        st.write("Large",pizza[4],"₺")

