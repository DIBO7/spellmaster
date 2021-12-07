from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser




def convert_pdf_to_string(document):
	output_string = StringIO()

	with document.open("rb") as doc:
		parser = PDFParser(doc)
		the_doc = PDFDocument(parser)
		rsrcmgr = PDFResourceManager()
		device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		for page in PDFPage.create_pages(the_doc):
			interpreter.process_page(page)
	
	return (output_string.getvalue()) #in brackets