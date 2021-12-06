from .spelling_tools import unwanted_characters


def strip_unwanted_txt_character(sentence):
	#removes unwanted characters that may be attched to the word and render it incorrect
	for char in unwanted_characters:
		if char in sentence:
			sentence = sentence.replace(char, " ")
			#replace with a space instaed, so words "facebook.com" can be spell checked as "facebook" and "com" and NOT "facebookcom"
		else:
			pass

	return sentence