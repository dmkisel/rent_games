import time

import streamlit as st
import requests


API_URL = 'http://localhost:8000'


st.header("Регистрация")
email = st.text_input("Email")
username = st.text_input("Имя пользователя")
password = st.text_input("Пароль", type="password")
telegram = st.text_input("Telegram")

if st.button("Зарегистрироваться"):
    if username and password:
        response = requests.post(f"{API_URL}/auth/register", json={"email": email,
                                                                      "password": password,
                                                                      "is_active": True,
                                                                      "is_superuser": False,
                                                                      "is_verified": False,
                                                                      "telegram": telegram,
                                                                      "username": username})
        if response.status_code == 201:
            st.success("Регистрация успешна! Направляем на страницу авторизации.")
            st.switch_page("auth.py")
        else:
            st.error(response.json().get("detail"))
    else:
        st.error("Заполните все поля")