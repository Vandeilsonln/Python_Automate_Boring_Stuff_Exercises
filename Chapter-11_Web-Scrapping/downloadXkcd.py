#! pytoon3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'    # starting url

os.chdir(r'.\Chapter-11_Web-Scrapping')
os.makedirs(r'xkcd', exist_ok=True)  # store comics here

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # TODO: Find the URL of the comic image.

    # TODO: Download ther image.

    # TODO: Save the image to the folder.

    # TODO: Get the Prev button's url.

    pass
print('Done.')