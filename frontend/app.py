import streamlit as st

API_URL = 'http://localhost:8000'

auth = st.Page("auth.py", title="Auth", icon="🖥")
register = st.Page("register.py", title=" ")
all_games = st.Page("all_games.py", title="All games", icon="🕹")
detail = st.Page("detail_game.py", title=" ")
order = st.Page("order.py", title="Order", icon="💸")
history = st.Page("history.py", title="History", icon="📖")
cart = st.Page("cart.py", title="Cart", icon="🛒")



page = {"Accounts": [auth, cart, order, history, register],
            "Games": [all_games, detail]}


pg = st.navigation(page)

pg.run()
