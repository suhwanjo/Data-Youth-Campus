import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://comic.naver.com/webtoon?tab=new'
data = []

driver = webdriver.Chrome()
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'item')))

items = driver.find_elements(By.CLASS_NAME, 'item')

for item in items:
    title = item.find_element(By.CLASS_NAME, 'ContentTitle__title--e3qXt').text
    author = item.find_element(By.CLASS_NAME, 'ContentAuthor__author--CTAAP').text
    rating = item.find_element(By.CLASS_NAME, 'Rating__star_area--dFzsb').text.replace('별점','').strip()
    link = item.find_element(By.CLASS_NAME, 'ContentTitle__title_area--x24vt').get_attribute('href')
    data.append([title, author, rating, link])

df = pd.DataFrame(data, columns=['제목', '작가', '평점', '링크'])
df.to_csv('naver webtoon.csv', encoding='utf-8-sig')