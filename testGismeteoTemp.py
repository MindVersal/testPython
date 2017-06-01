from grab import Grab

url_name = 'http://www.gismeteo.ru/weather-cherepovets-4285/now/'
g = Grab()
g.go(url_name)
print(g.doc.rex_text('<title>([^>]+)' + u'сейчас') + ':')
print(g.doc.rex_text('<span class=\"nowvalue__sign\">([^<]+)</span>') +
      g.doc.rex_text('<span class=\"nowvalue__sign\">[^<]*</span>([^<]+)<span') +
      g.doc.rex_text('<span class=\"nowvalue__text_m\">([^<]+)</span>'))
print('\n\nTHE END.')
