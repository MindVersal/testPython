import bs4
import requests

url_name = 'https://www.youtube.com'
res = requests.get(url_name)
res.raise_for_status()
no_start_soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = no_start_soup.select('.yt-ui-ellipsis a')
print('Популярные видео на сайте youtube.com\n')
for elem in elems:
    print(elem.getText() + ":\n" + url_name + str(elem["href"]))
print('\n\nTHE END.')
