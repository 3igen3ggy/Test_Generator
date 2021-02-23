import os
import shutil
os.chdir('F:\\PYTON\\EXERCISE')

for folderName, subfolders, filenames in os.walk('F:'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')