import os
import shutil
import zipfile

searchWorkerPath = 'pkg/SearchWorker.zip'
searchApiPath = 'pkg/SearchApi.zip'

if os.path.exists(searchWorkerPath):
    os.remove(searchWorkerPath)

if os.path.exists(searchApiPath):
    os.remove(searchApiPath)    

# create zip archives
shutil.make_archive('pkg/SearchWorker', 'zip', '../../virtualenvs/postcore-searchapi/lib/python3.6/site-packages')
shutil.make_archive('pkg/SearchApi', 'zip', '../../virtualenvs/postcore-searchapi/lib/python3.6/site-packages')

# add src files
os.system('zip -ur -j pkg/SearchWorker.zip src/SearchWorker.py')
os.system('zip -ur -j pkg/SearchApi.zip src/SearchApi.py')

