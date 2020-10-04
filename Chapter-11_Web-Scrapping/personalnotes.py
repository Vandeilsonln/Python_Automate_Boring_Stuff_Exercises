#! python3

import bs4

exampleFile = open(r'C:\Users\aline\Desktop\Vandeilson_UNICSUL\git_repositorio\python_automate_boring_stuff_exercises\Chapter-11_Web-Scrapping\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())

elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

print('-' * 50)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

############################
print('-' * 50)
############################

spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)