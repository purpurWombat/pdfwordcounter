import PyPDF2
import re
from tkinter import *
from tkinter import filedialog as fd

def main():
    root  = Tk()
    file = fd.askopenfilename(parent=root, title='Choose PDF')
    pdfReader = PyPDF2.PdfFileReader(file)
    pageNumber = pdfReader.getNumPages()
    wordcount = 0 
    for i in range(pageNumber):
        page = pdfReader.getPage(i)
        content = page.extractText()
        test = re.sub(r'[^a-zA-Z0-9 ]+', '', content)
        words = test.split()
        wordcount = wordcount + len(words)
    print(wordcount)

main()