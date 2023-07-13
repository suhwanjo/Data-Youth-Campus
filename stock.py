import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for page in range(1,43):
    url = f'https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http%3A%2F%2Ffinance.naver.com%2Fsise%2Fsise_market_sum.naver%3F%26page%3D{page}&fieldIds=quant&fieldIds=market_sum&fieldIds=per&fieldIds=roe&fieldIds=frgn_rate&fieldIds=listed_stock_cnt'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all('tr', attrs={'onmouseover': 'mouseOver(this)'})

    for item in items:
        cols = item.find_all('td')[1:-1]
        data.append([col.text.strip() for col in cols])

df = pd.DataFrame(data, columns=['종목명', '현재가', '전일비', '등락률', '액면가', '거래량', '상장주식수', '시가총액', '외국인비율', 'PER', 'ROE'])
df.to_csv('naver stock.csv', encoding='utf-8-sig')