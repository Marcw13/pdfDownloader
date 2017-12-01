import os
import urllib
import csv

DOWNLOADS_DIR = os.path.dirname(os.path.realpath(__file__))

with open('links.txt', 'r') as f:
    reader=csv.reader(f, delimiter='\t')
    for link, name in reader:
        name = name
        filename = os.path.join(DOWNLOADS_DIR, name)
        urllib.urlretrieve(link, filename)
