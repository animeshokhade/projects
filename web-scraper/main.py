import profile
import requests
from bs4 import BeautifulSoup as bs

github_user = input('Provide Github Username: ')
url = 'https://github.com/' + github_user

r = requests.get(url)
soup = bs(r.content, 'html.parser') 
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)