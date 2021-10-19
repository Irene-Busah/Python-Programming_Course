#web scraping program: print a url to the profile picture of a user on github

import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input GitHub username: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)

