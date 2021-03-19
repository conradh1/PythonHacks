import PyPDF2
pdf_file = open('sample.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page_content = read_pdf.getPage(1).extractText()
print (page_content.encode('utf-8','strict'))