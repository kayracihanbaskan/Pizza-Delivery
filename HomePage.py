import streamlit as st
import sqlite3 as sql
import pandas as pd

st.header("Home Page")

# Connection and Cursor
connection = sql.connect("pizza_database.db")
cursor = connection.cursor()

cursor.execute("SELECT name,address,pizza,size,beverage,price FROM orders")
orders = cursor.fetchall()

df = pd.DataFrame(orders)

df.columns = ["Name","Address","Pizza","Size","Beverage","Total Price"]

st.table(df)