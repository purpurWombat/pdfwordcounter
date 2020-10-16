import PyPDF2
import re

def main():
    file = "C:/Users/janni/Desktop/pdfwordcounter/pdfwordcounter/test.pdf"
    pdfReader = PyPDF2.PdfFileReader(file)
    pageNumber = pdfReader.getNumPages()
    wordcount = 0 
    for i in range(pageNumber):
        page = pdfReader.getPage(i)
        content = page.extractText()
        test = re.sub(r'[^a-zA-Z ]+', '', content)
        words = test.split()
        wordcount = wordcount + len(words)
    print(test)
    print(wordcount)

main()