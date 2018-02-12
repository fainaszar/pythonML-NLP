#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk

from urllib import urlopen
import sys
reload(sys)
sys.setdefaultencoding('utf8')


url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()

print(html[:60])

raw = nltk.clean_html(html)
tokens = 