FROM ubuntu:latest
LABEL authors="HUAWEI"
ENTRYPOINT ["top", "-b"]
COPY ../ /opt/app
WORKDIR /opt/app


CMD ["streamlit", "run", "app.py"]