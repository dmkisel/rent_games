import streamlit as st
import requests

API_URL = 'http://localhost:8000'

def login(email, password):
    url = f"{API_URL}/auth/jwt/login"
    payload = {
        'username': email,
        'password': password
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.cookies.get('token')




st.header("Авторизация")

if 'token' not in st.session_state:
    username = st.text_input("Email:")
    password = st.text_input("Пароль:", type="password")

    auth, reg = st.columns(2)

    with auth:
        if st.button("Войти"):
            if username and password:
                response = login(username, password)
                if response:
                    st.success("Login successful!")
                    st.write(f"Token: {response}")
                    st.session_state.token = response
                    st.switch_page("all_games.py")
                else:
                    st.error("Login failed. Please check your credentials.")
            else:
                st.error("Заполните все поля")

    with reg:
        if st.button("Регистрация"):
            st.switch_page("register.py")


elif st.button("Выйти"):
    st.session_state["token"] = None
    st.switch_page("auth.py")

