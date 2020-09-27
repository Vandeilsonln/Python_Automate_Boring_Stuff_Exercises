#! python3

import os, shutil
from PIL import Image


os.chdir(r'C:\Users\aline\Pictures\Viagens')
root = os.getcwd()
picsPath = os.listdir(root)
ext = ['.jpg', '.mp4']

for i in range(len(ext)):
    for folderName, subfolders, filenames in os.walk(root):
        print(f'Looking for {ext[i]} files in {folderName}')
        for file in filenames:
            oldName = os.path.abspath(folderName) + '\\' + file
            myFile, myExt = os.path.splitext(oldName)
            print(myExt.lower())
            
            if not file.endswith(myExt.lower()):
                print('rejected')
                with open('.\\rejected.txt', 'a') as rejected:
                    rejected.write(file)
                    rejected.write('\n')
                continue
            try:
                with Image.open(oldName) as photo:
                    info = photo._getexif()
                    newFileName = root + '\\' + (info[36867].replace(':', '_')) + ext[i]
                # shutil.move(os.path.abspath(file), newFileName)
                # print(file)
                # print(oldName)
                # print(newFileName)
                # print('-'*50)
            except:
                print('an error ocurred.')
