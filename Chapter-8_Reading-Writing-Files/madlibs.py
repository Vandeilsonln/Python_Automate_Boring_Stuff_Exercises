#! python3
# madlibs.py - This program will read a .txt file and find some words based on the
# re.compile() method. It will then prompt the user to
# replace them. In the end, it will print the new text and save it
# to the file (overwriting it).

# -----------------------------------------------------------------------

# Here's a small example of what the .txt file might look like:
"""
The ADJECTIVE panda VERB to the NOUN and then VERB. A nearby NOUN was
unaffected by these ADJECTIVE events.
A few ADJECTIVE hunters VERB to the NOUN and then VERB. The NOUN was
unaffected by these ADJECTIVE events.
"""

import re


# Open the file and get the text. Give the absolute path of the .txt file
madLibText = open('.\\replacingtext.txt', 'r').read()

print("--------------- ORIGINAL TEXT --------------")
print(madLibText, '\n----- END OF FILE -----')
print("\nNow it's your time to replace the words. Be creative!\n")

# Create the regex and identify the words in the text.
madLibRegex = re.compile(r'ADJECTIVE|NOUN|VERB')
madLibMo = madLibRegex.findall(madLibText)

# Replace the new words
newText = re.sub(madLibRegex, lambda x: input('Write a ' + x.group(0) + ': '), madLibText)
print("\n----- OK, THAT'S HOW YOUR TEXT LOOKS LIKE: -----\n")
print(newText)

# Save the new text to the file (overwriting it).
with open('C:\\Users\\aline\\PythonCourse\\readingwritingfiles\\madlibs\\replacingtext.txt', 'w') as newFile:
    newFile.write(newText)

print('-------------------- Done --------------------')