import streamlit as st
import requests

API_URL = 'http://localhost:8000'

st.set_page_config(page_title="All Games", page_icon="🕹")

st.header("Доступные игры")

response = requests.get(f"{API_URL}/games/")

game_list = response.json()


for game in game_list:

    container = st.container(border=True)
    row1, row2 = container.columns(2)
    with row1:
        if game['image_url']:
            row1.image(f"{game['image_url']}",width=250)
    with row2:
        row2.write(f"{game['title']}")
        row2.write(f"{game['description']}")
        row2.write(f"{game['price']} руб")

        detail, buy = row2.columns(2)
        with detail:
            if detail.button(label="Detail", key=f"game_detail_{game['id']}"):
                st.session_state['game_id'] = game['id']
                st.switch_page("detail_game.py")
        with buy:
            if buy.button(label="Buy", key=f"game_by_{game['id']}"):
                response = requests.post(f"{API_URL}/carts/{game['id']}")
                if response.status_code == 200:
                    st.success('Game add to you cart', icon="✅")

