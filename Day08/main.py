from typing import List
import itertools
import numpy as np
from pathlib import Path

from Utils import readline_clean

DAY = Path(__file__).resolve(strict=True).parent
VALID_ANTENNA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def main(inp='input', part=1):
	text = inp + ".txt"
	lines = readline_clean(f"{DAY}/{text}")
	lst = list(map(list, lines))
	lst = np.array(lst)

	rows, cols = lst.shape

	antinode = np.zeros((rows, cols), dtype=bool)

	for (r, c) in itertools.product(range(rows), range(cols)):
		if lst[r, c] not in VALID_ANTENNA:
			continue

		for (i, j) in itertools.product(range(rows), range(cols)):
			if i == r and j == c:
				continue

			if lst[i, j] != lst[r, c]:
				continue

			# Part 1
			if part == 1:
				diff_row = r - i
				diff_col = c - j

				row = i - diff_row
				col = j - diff_col

				if row < 0 or row >= rows or col < 0 or col >= cols:
					continue

				antinode[row, col] = 1

			# Part 2
			else:
				diff_row = r - i
				diff_col = c - j

				row = i
				col = j

				while not (row < 0 or row >= rows or col < 0 or col >= cols):

					antinode[row, col] = 1

					row -= diff_row
					col -= diff_col


	return antinode.sum()


if __name__ == "__main__":	

	import argparse

	parser = argparse.ArgumentParser(description='Solution to Advent of Code 2024 Day 06')
	parser.add_argument('-i', '--input', type=str, default='input', help='The input file')
	parser.add_argument('-p', '--part', type=int, default=1, help='The part of the challenge to solve')

	args = parser.parse_args()

	result = main(args.input, args.part)

	print(result)