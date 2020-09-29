#! python3
# renamepictures.py - The code will go through a directory tree and will rename all the pictures
# based on it's creation date.

# For now the code will just identify '.jpg' files. Any other formats will remain unchanged, although
# their filenames will be written in the 'rejected.txt' file. By doing this, you are aware of any
# other formats you have to deal with.

import os, shutil
from PIL import Image


os.chdir(r'C:\Users\aline\Pictures\Viagens')
root = os.getcwd()

# TODO: Create a list of acceptable extension files and make the code working with all of them.
ext = '.jpg'

for folderName, subfolders, filenames in os.walk(root):     # we won't be using 'subfolders' here, but it is still needed to unpack the os.walk() function's correctly.
    print(f'Looking for {ext} files in {folderName}')
    for file in filenames:      # every actual file that is inside the current folder.
        print(file)
        if not file.endswith(ext):
            print("File's extension rejected")
            with open('.\\rejected.txt', 'a') as rejected:
                rejected.write(file)
                rejected.write('\n')
            continue
        else:
            oldName = os.path.abspath(folderName) + '\\' + file

            with Image.open(oldName) as photo:
                info = photo._getexif()
                newFileName = root + '\\' + (info[36867].replace(':', '_')) + ext
                # In some photos, the line above gives the error (TypeError: 'NoneType object is not subscriptable)
            # shutil.move(oldName, newFileName)
            print(oldName)
            print(newFileName)
            print('-' * 50)
                