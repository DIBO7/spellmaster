import base64


def Read_Pdf_File(document):
	chunck_of_file = document.chunks()

	for chunk in chunck_of_file:
		
		print(base64.a85decode(chunk).decode('utf-8'))


	return [["This is a pdf file so I would read this differently"]]