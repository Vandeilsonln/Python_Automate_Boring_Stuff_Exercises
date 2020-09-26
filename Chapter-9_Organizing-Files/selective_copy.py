#! python3
# selective_copy.py - Once given a folder path, the program will walk through the folder tree
# and will copy a specific type of file (e.g. .txt or .pdf). They will be copied to a new folder.

import os, shutil


def copy_files(folderPath, destinyPath, extension):
    """
    Cope files from 'folderPath' to 'destinyPath' according to 'extension'.

    folderPath (str) - absolute path of the origin folder.
    destinyPath (str) - absolute path of the destination folder
    extension (str) - extension that will work as a filter. Only files with this extension will be copied.    
    """
    try:

        for currentFolder, subfolders, filenames in os.walk(folderPath):
            print(f'Looking for {extension} files in {currentFolder}')
            for file in filenames:
                if file.endswith(extension):
                    print(f'\tFound file: {os.path.basename(file)}.')
                    newFilePath = os.path.join(destinyPath, file) + extension
                    shutil.copy(os.path.join(currentFolder, file), newFilePath)
    except:
        print('Something went wrong. Please, verify the function arguments and try again.')    
    print('Done.')
    return None

copy_files('C:\\delicious', 'C:\\Python_Projetos', '.zip')