import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import concurrent.futures
import pandas as pd

links = [f'https://www.metacritic.com/browse/games/score/userscore/all/pc/filtered?sort=desc&page={i}' for i in range(45)]

urls = []

def get_urls(link):
	r = requests.get(link, headers = {'User-Agent' : UserAgent().chrome})
	s = BeautifulSoup(r.text, 'html.parser')

	for l in s.find_all('a', {'class' : 'title'}):
		urls.append(l.get('href'))


with concurrent.futures.ThreadPoolExecutor() as exec:
    exec.map(get_urls, links)

print(len(urls))
print(urls[:5])


links = [f'https://www.metacritic.com{i}' for i in urls]

data = []

def scrape_game_data(link):
	r = requests.get(link, headers = {'User-Agent' : UserAgent().chrome})
	s = BeautifulSoup(r.text, 'html.parser')

	t = []

	# Game Title

	for l in s.find_all('h1'):
		t.append(l.text)

	# MetaScore

	for l in s.find_all('div', {'class' : 'metascore_w xlarge game positive'}):
		x = re.findall(r'<span>(.*)</span>', str(l))[0]
		t.append(x)

	for l in s.find_all('div', {'class' : 'metascore_w xlarge game mixed'}):
		x = re.findall(r'<span>(.*)</span>', str(l))[0]
		t.append(x)

	for l in s.find_all('div', {'class' : 'metascore_w xlarge game negative'}):
		x = re.findall(r'<span>(.*)</span>', str(l))[0]
		t.append(x)

	# UserScore

	for l in s.find_all('div', {'class' : 'metascore_w user large game positive'}):
		x = re.findall(r'>(.*)</div>', str(l))[0]
		t.append(x)
		break

	for l in s.find_all('div', {'class' : 'metascore_w user large game mixed'}):
		x = re.findall(r'>(.*)</div>', str(l))[0]
		t.append(x)
		break

	for l in s.find_all('div', {'class' : 'metascore_w user large game negative'}):
		x = re.findall(r'>(.*)</div>', str(l))[0]
		t.append(x)
		break

	t = tuple(t)

	data.append(t)

	print('')
	print(f"[{t[0]}] successfully scraped")


with concurrent.futures.ThreadPoolExecutor() as exec:
    exec.map(scrape_game_data, links[:10])


df = pd.DataFrame(data, columns = ['Title', 'MetaScore', 'UserScore'])

df.set_index(df['Title'], inplace = True)
del df['Title']

df.to_csv('Data.csv')

print("Successfully Scraped All Game Data!")