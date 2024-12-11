

def readline_clean(textfile):
	
	lines_str = []

	with open(textfile, "r") as textfile:
		for line in textfile.readlines():
			textLn = line.strip("\n") \
						 .rstrip()	\
						 .lstrip()
			lines_str.append(textLn)

	return lines_str