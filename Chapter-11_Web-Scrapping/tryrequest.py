#! python3

import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))

print(res.status_code == requests.codes.ok)

print(len(res.text))
print(res.text[:200])

res2 = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res2.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

print('-' * 50)

import bs4


res = requests.get('https://nostarch.com/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchSoup))


exampleFile = open(r'C:\Users\aline\Desktop\Vandeilson_UNICSUL\git_repositorio\python_automate_boring_stuff_exercises\Chapter-11_Web-Scrapping\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)

print(type(exampleSoup))