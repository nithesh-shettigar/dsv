
import requests
from bs4 import BeautifulSoup
import pandas as pd 
 
url = 'https://en.wikipedia.org/wiki/Karnataka'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
df = pd.DataFrame(columns = ['Total url ']) 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))
    dm=link.get('href')
    df = df.append({'herf':dm}, ignore_index=True)


df.to_csv(r'E:\my_href2.csv', index=False)  
