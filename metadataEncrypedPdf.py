

import os
import PyPDF2
from PyPDF2 import PdfFileReader

fp = open("file.pdf")
pdfFile = PdfFileReader(fp)
if pdfFile.isEncrypted:
    try:
        pdfFile.decrypt('')
        info = pdfFile.getDocumentInfo()
        #print(info.title)
        #print(info.creator)
        #print(info.producer)
    except:
        command = ("cp "+ filename +
            " temp.pdf; qpdf --password='' --decrypt temp.pdf " + filename
            + "; rm temp.pdf")
        os.system(command)
        fp = open(filename)
        pdfFile = PdfFileReader(fp)

        info = pdfFile.getDocumentInfo()
        print(info.author)
else:
    print('File Not Encrypted')