#import base64
#print(base64.a85decode(chunk).decode('utf-8')) #chuck is the chunk of file to be read!
import PyPDF2
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def Read_Pdf_File(document):

	output_string = StringIO()

	with document.open("rb") as doc:
		parser = PDFParser(doc)
		the_doc = PDFDocument(parser)
		rsrcmgr = PDFResourceManager()
		device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		for page in PDFPage.create_pages(the_doc):
			interpreter.process_page(page)
	
	print(output_string)
	#print(output_string.getvalue())

	return [["This is a pdf file so I would read this differently"]]

'''
pdf_reader = PyPDF2.PdfFileReader(doc)
		reader_on_page = 0 #to start the reader from page 1
		while reader_on_page < pdf_reader.numPages:
			print("--------------------------------------")
			print(pdf_reader.getPage(reader_on_page).extractText())
			reader_on_page += 1
'''