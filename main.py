import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)

# f = open("google.html",'w')
# f.write(res.text)
data = []
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all('div', attrs={'class': 'sh_text'})
for item in items:
    title = item.find('a', attrs={'class': 'sh_text_headline nclicks(cls_eco.clsart)'}).text
    link = item.find('a', attrs={'class': 'sh_text_headline nclicks(cls_eco.clsart)'})['href']
    content = item.find('div', attrs={'class': 'sh_text_lede'}).text
    publisher = item.find('div', attrs={'class': 'sh_text_info'}).find('div', attrs={'class': 'sh_text_press'}).text
    data.append([title, content, link, publisher])

df = pd.DataFrame(data, columns=['제목', '내용', '링크', '출판사'])
df.to_csv('naver news.csv', encoding='utf-8-sig')