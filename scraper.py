import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("<h1 style = 'text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Enter your keyword")
    search = st.form_submit_button("Search")
placeholder = st.empty()
if search:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, "lxml")
    rows = soup.find_all("div", class_="ripi6")
    col1,col2 = placeholder.columns(2)
    for index, row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img", class_ = "tB6UZ")
            list = (img["srcset"].split("?"))
            anchor = figures[i].find("a", class_="rEAWd")
            print(anchor["href"])
            if i == 1:
                col1.image(list[0])
                btn = col1.button("Download",key = str(index)+str(i))
                if btn:
                    print("Download Successfully")
            else:
                col2.image(list[0])
                btn = col2.button("Download",key = str(index)+str(i))
                if btn:
                    print("Download Successfully")
