import streamlit as st
import requests

from app import User

API_URL = 'http://localhost:8000'

def post_info(token, game_id):
    url = f'{API_URL}/carts/{game_id}/'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.post(url, headers=headers)
    return response

st.set_page_config(page_title="All Games", page_icon="🕹")

st.header("Доступные игры")
st.write(User.token)
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
                action = post_info(User.token, game['id'])
                if action.status_code == 200:
                    st.success('Game add to you cart', icon="✅")

