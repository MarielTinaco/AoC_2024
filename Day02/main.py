
from functools import reduce
from Utils import readline_clean
from copy import copy

def case1(seq):
	return seq == sorted(seq) or seq == sorted(seq, reverse=True)

def case2(seq):
	for i in range(len(seq)-1):
		diff = seq[i] - seq[i+1]
		absdiff = abs(diff)

		if ((absdiff < 1) or (absdiff > 3)):
			return False

	return True

def dampener(seq):
	combiner = lambda x: case1(x) and case2(x)

	for i in range(len(seq)):
		newseq = copy(seq)
		del newseq[i]

		if combiner(newseq):
			return True
	
	return False


def prob1(lst):
	result = map(lambda st: st.split(" "), lst)
	result = map(lambda lst: [int(i) for i in lst], result)
	result = map(lambda x: case1(x) and case2(x), result)
	result = map(int, result)
	result = sum(result)

	return result
	
def prob2(lst):
	result = map(lambda st: st.split(" "), lst)
	result = map(lambda lst: [int(i) for i in lst], result)
	result = map(dampener, result)
	result = map(int, result)
	result = sum(result)

	return result

if __name__ == "__main__":
    
	input_txt = "Day02/input.txt"

	lines = readline_clean(input_txt)
    
	day1 = prob1(lines)
	day2 = prob2(lines)

	# day2 = prob2(lines)

	# print(day1)
	print(day2)
    
