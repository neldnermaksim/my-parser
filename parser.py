import requests
from bs4 import BeautifulSoup

# Парсим заголовки новостей с сайта
url = 'https://news.ycombinator.com/'  # Это сайт Hacker News

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем все заголовки
titles = soup.find_all('a', class_='storylink')

for idx, title in enumerate(titles, 1):
    print(f"{idx}. {title.text}")
