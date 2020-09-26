#! python3
# bck_foldertozip.py - Copies an entire folder and its contents
# into a ZIP file whose name increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of 'folder' into a ZIP file.
    
    folder = os.path.abspath(folder)    # Make sure folder is absolute
    os.chdir(folder)
    # Figure out the filename this code should use based on what files already exist.

    number = 1

    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break   # You found it!
        number += 1
    
    # Create the ZIP file
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Walk the entire folder tree and compress the files in each folder.

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}')
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    # Don't backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\delicious')
