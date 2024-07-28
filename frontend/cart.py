import streamlit as st
import requests

API_URL = 'http://localhost:8000'

st.set_page_config(page_title="Cart", page_icon="🕹")

st.header("Корзина")


response = requests.get(f"{API_URL}/cart/")

game_list = response.json()

for game in game_list:
    container = st.container(border=True)
    row1, row2, row3 = container.columns(3)
    with row1:
        row1.write(f"{game['title']}")
    with row2:
        row2.write(f"{game['price']} руб")
    with row3:
        if row3.button(label="Удалить", key=f"game_detail_{game['id']}"):
            st.session_state['game_id'] = game['id']
            st.switch_page("cart.py")


if st.button(label="Buy", key=f"by"):
    st.success('G', icon="✅")
