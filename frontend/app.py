import streamlit as st
import requests
from datetime import datetime

# API URL
API_URL = "http://localhost:8000"


# Страница авторизации
def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(f"{API_URL}/token", data={"username": username, "password": password})
        if response.status_code == 200:
            st.success("Logged in successfully!")
            token = response.json().get("access_token")
            st.session_state["token"] = token
            st.session_state["username"] = username
        else:
            st.error("Failed to login")


# Страница регистрации
def register():
    st.title("Register")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        response = requests.post(f"{API_URL}/users/", json={"username": username, "email": email, "password": password})
        if response.status_code == 200:
            st.success("Registered successfully!")
        else:
            st.error("Failed to register")


# Страница каталога игр
def game_catalog():
    st.title("Game Catalog")

    headers = {"Authorization": f"Bearer {st.session_state['token']}"}
    response = requests.get(f"{API_URL}/games/", headers=headers)

    if response.status_code == 200:
        games = response.json()
        for game in games:
            st.subheader(game["title"])
            st.text(game["description"])
            st.text(f"Price: {game['price']}")
            st.text(f"Available: {game['available']}")
            if st.button(f"Book {game['title']}"):
                st.session_state["selected_game"] = game
                st.experimental_rerun()
    else:
        st.error("Failed to fetch games")


# Страница бронирования игры
def book_game():
    st.title("Book Game")

    game = st.session_state["selected_game"]
    st.subheader(game["title"])
    st.text(game["description"])
    st.text(f"Price: {game['price']}")
    st.text(f"Available: {game['available']}")

    date = st.date_input("Date", min_value=datetime.now().date())
    time = st.time_input("Time", value=datetime.now().time())

    if st.button("Book Now"):
        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        data = {
            "user_id": st.session_state["user_id"],
            "game_id": game["id"],
            "date": date.isoformat(),
            "time": time.isoformat()
        }
        response = requests.post(f"{API_URL}/bookings/", json=data, headers=headers)
        if response.status_code == 200:
            st.success("Game booked successfully!")
        else:
            st.error("Failed to book game")


# Страница корзины и покупки игр
def shopping_cart():
    st.title("Shopping Cart")

    cart = st.session_state.get("cart", [])
    if not cart:
        st.info("Your cart is empty.")
        return

    for game in cart:
        st.subheader(game["title"])
        st.text(game["description"])
        st.text(f"Price: {game['price']}")
        if st.button(f"Remove {game['title']}"):
            st.session_state["cart"].remove(game)
            st.experimental_rerun()

    if st.button("Checkout"):
        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        order_data = [{"user_id": st.session_state["user_id"], "game_id": game["id"]} for game in cart]
        response = requests.post(f"{API_URL}/orders/", json=order_data, headers=headers)
        if response.status_code == 200:
            st.success("Order placed successfully!")
            st.session_state["cart"] = []
        else:
            st.error("Failed to place order")


# Основная функция для отображения интерфейса
def main():
    st.sidebar.title("Navigation")
    options = ["Login", "Register", "Game Catalog", "Shopping Cart"]
    choice = st.sidebar.radio("Go to", options)

    if choice == "Login":
        login()
    elif choice == "Register":
        register()
    elif choice == "Game Catalog":
        game_catalog()
    elif choice == "Shopping Cart":
        shopping_cart()

    if "selected_game" in st.session_state:
        book_game()


if __name__ == "__main__":
    main()
