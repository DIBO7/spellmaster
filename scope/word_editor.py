unwanted_characters = ["?", "!", '"', "(", ")", ",", ".", "/", "\r", "\t", ":", ";", "-", "_", "'",] 
#"." is problematic because file may contain .net or .com or .somethingelse..."'" is also problematic beacuse of "isn't"
#may use reges to fix that...BUT GOD, WE MUST AVOID REGEX for as long as we can...
#or parhaps "." and ":" may be replaced with spaces (" ") instead of ""


def strip_unwanted_txt_character(sentence):
	#removes unwanted characters that may be attched to the word and render it incorrect
	for char in unwanted_characters:
		if char in sentence:
			sentence = sentence.replace(char, " ")
			#replace with a space instaed, so words "facebook.com" can be spell checked as "facebook" and "com" and NOT "facebookcom"
		else:
			pass

	return sentence


def remove_one_letter_words(list_of_words):
	for words in list_of_words:
		if len(words) < 2:
			list_of_words.remove(words)
	return list_of_words