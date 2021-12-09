from urllib.request import urlopen
from json import loads
import datetime

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))
revisions = data['query']['pages']['192203']['revisions']
max = 0

for date, count in groupby(revisions, lambda date: datetime.datetime.strptime(date['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()):
    if len(list(count)) > max:
        maxDate = date
        max = len(list(count))
print(maxDate)