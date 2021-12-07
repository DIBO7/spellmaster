#import base64
#print(base64.a85decode(chunk).decode('utf-8')) #chuck is the chunk of file to be read!
import PyPDF2


def Read_Pdf_File(document):
	with document.open("r") as doc:
		pdf_reader = PyPDF2.PdfFileReader(doc)
		reader_on_page = 0 #to start the reader from page 1
		while reader_on_page < pdf_reader.numPages:
			print("--------------------------------------")
			print(pdf_reader.getPage(reader_on_page).extractText())
			reader_on_page += 1
		

	return [["This is a pdf file so I would read this differently"]]