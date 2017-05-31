import bs4
import requests

res = requests.get('http://oper.ru/')
res.raise_for_status()
no_start_soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = no_start_soup.select('#middle dt a')
for elem in elems:
    print(elem)
