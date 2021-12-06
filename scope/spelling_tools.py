from spellchecker import SpellChecker


spellcheckmaster = SpellChecker(distance=2, language="en")
spellcheckmaster.word_frequency.load_words(["s", "http", "https", "html", "css", "javascript", "100%"]) 
#.load_text("a string"), .load_text_file("./path_to_file.txt"), .load_dictionary("./path_to_file.json") OR .add("a single word"), .remove("a word from the dic")
#list of words that should NOT be flagged as incorrect. List will grow larger

def run_spellcheck(list_of_lines_list):
	result = []
	#list_of_lines_list is a list containing a sammler list of lines. The smaller list of lines contain words as strings
	line_counter = 1
	for lines in list_of_lines_list:
		#lines is a list of each word (strings) in one line
		result += one_line_spellcheck(lines, line_counter)
		line_counter += 1
	return result

def one_line_spellcheck(one_line, line_number=1):
	result = []
	wrong_words = spellcheckmaster.unknown(one_line)#find the wrong words..and we will correct them
	for words in wrong_words:
		suggestion = spellcheckmaster.correction(words)

		if suggestion != words:
			result.append('"{}" in line {} is spelled incorrectly, parhaps you mean "{}"'.format(words, line_number, suggestion))
			#this is because the corrections are sometimes the same as the wrong words
		else:
			result.append('"{}" in line {} seems to be spelled incorrectly.'.format(words.upper(), line_number))
	return result


unwanted_characters = ["?", "!", '"', "(", ")", ",", ".", "/", "\r", "\t", ":", ";", "-", "_", "'"] 
#"." is problematic because file may contain .net or .com or .somethingelse..."'" is also problematic beacuse of "isn't"
#may use reges to fix that...BUT GOD, WE MUST AVOID REGEX for as long as we can...
#or parhaps "." and ":" may be replaced with spaces (" ") instead of ""
