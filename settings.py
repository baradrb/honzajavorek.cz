
from danube_delta.settings import *  # NOQA


AUTHOR = 'Honza Javorek'
SITENAME = 'Javorové lístky'


ABOUT_HEADING = AUTHOR
ABOUT = '''
[Honza](http://honzajavorek.cz) je programátor. Od roku 2011 buduje českou
komunitu kolem jazyka [Python](http://python.cz/). V současnosti pomáhá hlavně s
propagací aktivit, jako jsou [PyLadies](http://pyladies.cz/),
[Pyvo](http://pyvo.cz/), nebo [PyCon CZ](https://cz.pycon.org/). Přes den jej
najdete v [Apiary](https://apiary.io/), kde se stará o
[Dredd](https://github.com/apiaryio/dredd), framework na testování API. Občas
taky radí lidem jak mají API dělat a přednáší o tom na konferencích.
'''
ABOUT_IMAGE = 'images/honza.jpg'


if PRODUCTION:
    SITEURL = 'http://honzajavorek.cz'


# URL and save paths settings
URL_PREFIX = 'blog/'
ARTICLE_URL = URL_PREFIX + ARTICLE_URL
ARTICLE_SAVE_AS = URL_PREFIX + ARTICLE_SAVE_AS
ARTICLE_LANG_URL = URL_PREFIX + ARTICLE_LANG_URL
ARTICLE_LANG_SAVE_AS = URL_PREFIX + ARTICLE_LANG_SAVE_AS
INDEX_URL = SITEURL + '/' + URL_PREFIX
INDEX_SAVE_AS = URL_PREFIX + 'index.html'


# Theming
DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = 'UA-1316071-6'
