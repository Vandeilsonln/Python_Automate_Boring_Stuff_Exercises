#! python3
# renamepictures.py - The code will go through a directory tree and will rename all the pictures
# based on it's creation date.

# For now the code will just identify '.jpg' files. Any other formats will remain unchanged, although
# their filenames will be written in the 'rejected.txt' file. By doing this, you are aware of any
# other formats you have to deal with.

import os, shutil
from PIL import Image


# TODO: Create a list of acceptable extension files and make the code working with all of them.
def rename_pictures_to_date(rootPath, ext='.jpg'):
    os.chdir(rootPath)
    root = os.getcwd()
    for folderName, subfolders, filenames in os.walk(root):
        for file in filenames:
            if not file.endswith(ext):
                with open('.\\rejected.txt', 'a') as rejected:
                    rejected.write(file)
                    rejected.write('\n')
                continue
            else:
                oldName = os.path.abspath(folderName) + '\\' + file

                with Image.open(oldName) as photo:
                    try:
                        info = photo._getexif()
                        newFileName = root + '\\' + (info[36867].replace(':', '_')) + ext
                        # shutil.move(oldName, newFileName)
                    except:
                        # TODO: Create a function write_to_reject(file) in this case AND for the files with other file extensions as well
                        pass
    return 'Done.'

print(rename_pictures_to_date(r'C:\Users\aline\Pictures\Viagens', '.jpg'))
