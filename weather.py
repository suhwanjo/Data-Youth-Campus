import requests
from bs4 import BeautifulSoup
from fastapi import fastAPI
import uvicorn
url = 'https://weather.naver.com/today/09110115'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# 다음에 하겠습니다..

