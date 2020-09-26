#! python3
# selective_copy.py - Once given a folder path, the program will walk through the folder tree
# and will copy a specific type of file (e.g. .txt or .pdf). They will be copied to a new folder.

import os, shutil


def originPath(folderpath, destinyPath, extension):
    for currentFolder, subfolders, filenames in os.walk(folderpath):
        print(f'Looking for {extension} files in {currentFolder}')
        for file in filenames:
            if file.endswith(extension):
                print(f'\tFound file: {os.path.basename(file)}.')
                newFilePath = os.path.join(destinyPath, file) + extension
                # print(os.path.join(folderpath, file), newFilePath)
                shutil.copy(os.path.join(currentFolder, file), newFilePath)
    print('Done.')

originPath('C:\\delicious', 'C:\\Python_Projetos', '.zip')