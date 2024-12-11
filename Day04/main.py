
from Utils import readline_clean

import numpy as np

def horizontal(arr, row, col):
	slice = arr[row:row+4, col]
	slice_str = ''.join(slice.tolist())

	count = 0
	if slice_str == "XMAS":
		count += 1

	if slice_str[::-1] == "XMAS":
		count += 1

	return count

def vertical(arr, row, col):
	slice = arr[row, col:col+4]
	slice_str = ''.join(slice.tolist())

	count = 0
	if slice_str == "XMAS":
		count += 1

	if slice_str[::-1] == "XMAS":
		count += 1

	return count

def diagonal(arr, row, col):
	slice = arr[row:row+4, col:col+4]
	slice_diag = slice.diagonal()

	slice_str = ''.join(slice_diag.tolist())

	count = 0
	if slice_str == "XMAS":
		count += 1

	if slice_str[::-1] == "XMAS":
		count += 1

	flip_slice = np.flip(slice, axis=0)
	flip_slice_diag = flip_slice.diagonal()

	slice_str = ''.join(flip_slice_diag.tolist())

	if slice_str == "XMAS":
		count += 1

	if slice_str[::-1] == "XMAS":
		count += 1

	return count

def xmas(arr, row, col):
	slice = arr[row:row+3, col:col+3]
	
	fall_slice_diag = slice.diagonal()
	rise_slice_diag = np.flipud(slice).diagonal()

	fall_slice_diag_str = ''.join(fall_slice_diag.tolist())
	rise_slice_diag_str = ''.join(rise_slice_diag.tolist())

	count = 0
	if fall_slice_diag_str == "MAS" and rise_slice_diag_str == "MAS":
		count += 1
	
	return count

def prob1(lst):

	lst = list(map(list, lst))
	lst = np.array(lst)

	rows, cols = lst.shape

	result = 0
	for r in range(rows):
		for c in range(cols):
			result += horizontal(lst, r, c)
			result += vertical(lst, r, c)
			result += diagonal(lst, r, c)

	return result

def prob2(lst):
	lst = list(map(list, lst))
	lst = np.array(lst)

	rows, cols = lst.shape

	result = 0

	for r in range(rows):
		for c in range(cols):
			result += xmas(lst, r, c)
			result += xmas(np.rot90(lst), r, c)
			result += xmas(np.rot90(np.rot90(lst)), r, c)
			result += xmas(np.rot90(np.rot90(np.rot90(lst))), r, c)

	return result

if __name__ == "__main__":

	from pprint import pprint

	input_txt = "Day04/input.txt"

	lines = readline_clean(input_txt)

# 	lines = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""

# 	lines = lines.split("\n")

	# day1 = prob1(lines)
	day2 = prob2(lines)

	pprint(day2)