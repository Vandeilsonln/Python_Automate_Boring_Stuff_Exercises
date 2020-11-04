#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading
os.chdir(r'.\Chapter-15_scheduling_tasks')
os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page
        if urlNumber == 404:
            continue
        print(f'Downloading page http://xkcd.com/{urlNumber}')

        res = requests.get(f'https://xkcd.com/{urlNumber}')

        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find the url of the comic image.

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print(f'Downloading image {comicUrl}')
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

            # Save image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the Thread objects.
downloadThreads = []
for i in range(1, 1400, 100):
    
    downloadThread =threading.Thread(target=downloadXkcd, args=(i, i+98))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for i in downloadThreads:
    i.join()
print('Done.')