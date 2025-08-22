import streamlit as st
import sqlite3 as sql

# Connection and Cursor
connection = sql.connect("pizza_database.db")
cursor = connection.cursor()

# Creating Table and Commit
cursor.execute("CREATE TABLE IF NOT EXISTS pizzas (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,small_price REAL,medium_price REAL,large_price REAL,ingredients TEXT,image TEXT)")
connection.commit()

st.header("Add Pizza")

with st.form("add_pizza",clear_on_submit=True):
    name = st.text_input("Pizza Name")
    small_price = st.number_input("Price for Small Pizza")
    medium_price = st.number_input("Price for Medium Pizza")
    large_price = st.number_input("Price for Large Pizza")
    ingredients = st.multiselect("İngredients",["Mushroom","Ham","Sausage","Onion","Mozzarella","Bacon","Spicy Chicken","Tuna","Pineapple","Basil","Salami","Celery"])

    image = st.file_uploader("Img of the pizza")

    add = st.form_submit_button("Add Pizza")

    if add:
        ingredients = str(ingredients)
        ingredients = ingredients.replace("[","")
        ingredients = ingredients.replace("]","")
        ingredients = ingredients.replace("'","")

        img_url = "img/"+image.name
        st.write(img_url)

        open(img_url,"wb").write(image.read())

        cursor.execute("INSERT INTO pizzas (name, small_price, medium_price, large_price, ingredients, image) VALUES(?,?,?,?,?,?)",(name,small_price,medium_price,large_price,ingredients,img_url))
        connection.commit()

        st.success("Pizza Added Successfully!")
