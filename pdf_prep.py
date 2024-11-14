from PyPDF2 import PdfFileWriter, PdfFileReader
import os


# names all the output files (as strings)
original_pdf = input("Enter the path of the PDF you wish to reformat:")

original_pdf_stem = original_pdf.replace('.pdf', '')
split_page_pdf = original_pdf_stem + '_split_pages.pdf'
removed_images_pdf = original_pdf_stem + '_final.pdf'


# adds page markers between each page of original PDF
pdfIn = open(original_pdf, 'rb')
pdfFile = PdfFileReader(pdfIn)
NumPages = pdfFile.getNumPages()

page_marker = open('_page_marker.pdf' ,'rb')
page_marker = PdfFileReader(page_marker)

output = PdfFileWriter()

with open(split_page_pdf, "wb") as outputStream:

    pages = []

    for page in range(NumPages):

        pgObj = pdfFile.getPage(page)
        output.addPage(pgObj)
        pages.append(page + 1)
        output.addPage(page_marker.getPage(0))
        output.write(outputStream)
        print('WORKING ON IT')
        print('______________')

    output.write(outputStream)


# removes redacted "images"
with open(split_page_pdf, "rb") as inputStream:

    outputStream = open(removed_images_pdf, "wb")

    src = PdfFileReader(inputStream)
    output = PdfFileWriter()

    [output.addPage(src.getPage(i)) for i in range(src.getNumPages())]
    output.removeImages()

    output.write(outputStream)


# deletes excess files
os.remove((split_page_pdf))


# success message
print('Finished!')


