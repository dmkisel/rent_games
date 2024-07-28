import streamlit as st
import requests

from app import User

API_URL = 'http://localhost:8000'

game_id = st.session_state["game_id"]


# def get_info(token):
#     url = f'{API_URL}/games/{game_id}'
#     headers = {
#         'Authorization': f'Bearer {token}'
#     }
#     response = requests.get(url, headers=headers)
#     return response.json()

def post_info(token):
    url = f'{API_URL}/carts/{game_id}/'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.post(url, headers=headers)
    return response


response = requests.get(f"{API_URL}/games/{game_id}/")

game = response.json()

st.header(f"{game['title']}")

st.image(game['image_url'], width=300)

st.write(f"{game['description']}")

if game['price_type'] == 1:
    st.write(f"Цена: {game['price']} руб.")
if game['price_type'] == 2:
    st.write(f"Суточная аренда: {game['price']} руб.")


if st.button(label="Buy", key=f"game_by_{game['id']}"):
    if 'token' in st.session_state:
        game = post_info(User.token)
    else:
        st.warning("You not authorized")
    if game.status_code == 200:
        st.success('game add to you cart', icon="✅")
        st.switch_page("cart.py")

