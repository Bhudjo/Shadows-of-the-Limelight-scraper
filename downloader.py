from bs4 import BeautifulSoup
import requests
import urllib.parse

url = 'https://alexanderwales.com/shadows/'
header = {"User-Agent": "Mozilla - stocazzo"}
html = requests.get(url, headers=header).text
soup = BeautifulSoup(html, 'html.parser')
content = soup.find("div", class_='entry-content')
body = ""
with open(f"Shadows-of-the-Limelight.html",'w') as target:
    for child in content.descendants:
        if child.name == 'a':
            href = child.attrs['href']
            title = child.contents[0]
            html = requests.get(href, headers=header).text
            ch_soup = BeautifulSoup(html, 'html.parser')
            body += f"<h1>{title}</h1>"
            extracted = ch_soup.find("div", class_='entry-content').get_text()
            prev = "Previously …"
            next_ = "Next …"
            body += extracted.replace(prev,"").replace(next_,"")
            print(f"{title}: done")
    target.writelines(body)

