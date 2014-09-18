import urllib2
import re
import os

def download_RNAseq(url, filename):
    dir_path = os.path.join(os.getcwd(), 'RNASeq')  # path name with the new folder name
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)                             # create directory [current_path]/FolderName
    response_rnaseq = urllib2.urlopen(url)     # File like object, catches the response
    file_rnaseq = open(os.path.join(dir_path, filename), 'wb')
    file_rnaseq.write(response_rnaseq.read())   # Extracts the response and write to a file
    file_rnaseq.close()


