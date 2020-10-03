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