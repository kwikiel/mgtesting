from models import Market
import datetime

from lxml import html
import requests

raw = requests.get("https://loanbase.com/stats")
tree = html.fromstring(raw.text)

active_loans =  float(tree.xpath('//div[@class="statistic"]/p//text()')[2].split(" ")[1])


