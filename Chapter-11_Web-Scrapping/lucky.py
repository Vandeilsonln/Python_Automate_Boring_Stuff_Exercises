#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4, pyperclip


print('Googling...')    # display text while downloading the Google page.


# It will get arguments either from sys.argv or clipboard

if len(sys.argv) > 1:   # get from command line (sys.argv)
    res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))

else:   # get from the clipboard
    res = requests.get('https://google.com/search?=' + '+'.join(pyperclip.paste().split()))
    print('clipboard', pyperclip.paste())   # checking
# Retrieve top search result links.

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Open a browser tab for each result.
linkElems = soup.select('a', {'class': 'ra'})
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
