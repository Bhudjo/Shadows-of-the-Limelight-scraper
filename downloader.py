from bs4 import BeautifulSoup
import requests
import urllib.parse

url = 'https://alexanderwales.com/shadows/'
header = {"User-Agent": "Mozilla - stocazzo"}
html = requests.get(url, headers=header).text
soup = BeautifulSoup(html, 'html.parser')
content = soup.find("div", class_='entry-content')
for child in content.descendants:
    if child.name == 'a':
      href = child.attrs['href']
      title = child.contents[0]
      encoded_title = urllib.parse.quote_plus(title)
      with open(f"{encoded_title}.html",'w') as target:
        html = requests.get(href, headers=header).text
        ch_soup = BeautifulSoup(html, 'html.parser')
        body = ch_soup.find("div", class_='entry-content').get_text()
        target.writelines(body)

