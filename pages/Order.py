import streamlit as st
import sqlite3 as sql

st.header("Orders")

# Connection and Cursor
connection = sql.connect("pizza_database.db")
cursor = connection.cursor()

#Creating Orders Table
cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,address TEXT,pizza TEXT,size TEXT,beverage TEXT,price REAL)")
connection.commit()

cursor.execute("SELECT name FROM pizzas")
names = cursor.fetchall()

pizza_list = []
for i in names:
    pizza_list.append(i[0])


with st.form("Order",clear_on_submit=True):
    name = st.text_input("Name/Surname")
    address = st.text_area("Address")
    pizza = st.selectbox("Select Your Fav Pizza",pizza_list)
    size = st.selectbox("Select Your Pizza's Size",["Small","Medium","Large"])
    beverage = st.selectbox("Select Your Best Drink",[
    "Coca Cola (330ml)",
    "Coca Cola Zero (330ml)",
    "Fanta (330ml)",
    "Sprite (330ml)",
    "Ice Tea Lemon (330ml)",
    "Ice Tea Peach (330ml)",
    "Ayran (300ml)",
    "Sparkling Water (250ml)",
    "Still Water (500ml)",
    "Energy Drink (250ml)"
])

    place_order_button = st.form_submit_button("Place Order")

    if place_order_button:
        if size == "Small":
            cursor.execute("SELECT small_price FROM pizzas where name = ? ",(pizza,))
            pay = cursor.fetchone()
        elif size == "Medium":
            cursor.execute("SELECT medium_price FROM pizzas where name = ? ", (pizza,))
            pay = cursor.fetchone()
        else:
            cursor.execute("SELECT large_price FROM pizzas where name = ? ", (pizza,))
            pay = cursor.fetchone()



        beverages = {
            "Coca Cola (330ml)": 50.5,
            "Coca Cola Zero (330ml)": 32.5,
            "Fanta (330ml)": 32.4,
            "Sprite (330ml)": 22.4,
            "Ice Tea Lemon (330ml)": 32.6,
            "Ice Tea Peach (330ml)": 32.6,
            "Ayran (300ml)": 21.5,
            "Sparkling Water (250ml)": 11.2,
            "Still Water (500ml)": 10.8,
            "Energy Drink (250ml)": 33.5
        }

        beverage_price = beverages[beverage]

        total_price = pay[0] + beverage_price

        cursor.execute("INSERT INTO orders (name,address,pizza,size,beverage,price) VALUES(?,?,?,?,?,?)",(name,address,pizza,size,beverage,total_price))
        connection.commit()

        st.success(f"Your order has been received successfully.Total Price:{total_price} ₺")
