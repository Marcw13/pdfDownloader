# pdfDownloader
Python CLI PDF Downloader

This simple CLI downloads all PDF files from a links.txt file (tab separated) where the first column corresponds to the file links and the second column specifies the name of the downloaded PDF. All files are saved in the same directory where the script is saved. 

## Example
links.txt file should look as follows (no headers):

Link | File Name
--- | --- 
www.test.com/test.pdf | test.pdf 

Execution:
```
python pythonPDFDownloader.py
```
