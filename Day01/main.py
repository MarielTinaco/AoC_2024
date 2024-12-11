import numpy as np

from Utils import readline_clean

def prob1(lst):

	def split_3spaces(str):
		return str.split("   ")

	genr = map(split_3spaces, lst)
	genr = np.fromiter(genr, dtype='2i')
	genr = np.apply_along_axis(sorted, 0, genr)
	genr = genr[:,0] - genr[:,1]
	genr = np.abs(genr)
	genr = np.sum(genr)

	result = genr

	return result

def prob2(lst):

	def split_3spaces(str):
		return str.split("   ")

	genr = map(split_3spaces, lst)
	genr = np.fromiter(genr, dtype='2i')

	sim = 0
	for l in genr[:,0]:
		sim += l*len(list(filter(lambda x: x == l, genr[:,1])))
	
	return sim

if __name__ == "__main__":
    
	input_txt = "Day01/input.txt"

	lines = readline_clean(input_txt)
    
	day1 = prob1(lines)

	day2 = prob2(lines)

	# print(day1)
	print(day2)