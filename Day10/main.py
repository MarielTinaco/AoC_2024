from typing import List
import itertools
import numpy as np
from pathlib import Path
from collections import deque, namedtuple
from Utils import readline_clean

from tqdm import tqdm


DAY = Path(__file__).resolve(strict=True).parent


def main(inp='input', part=1):
	text = inp + ".txt"
	lines = readline_clean(f"{DAY}/{text}")

	lst = list(map(list, lines))
	lst = np.array(lst, dtype=int)

	rows, cols = lst.shape

	total_count = 0

	for (r, c) in tqdm(list(itertools.product(range(rows), range(cols)))):
		if lst[r, c] != 0:
			continue

		frontier = deque()
		explored = set()

		frontier.append((r, c))
		count = 0

		while len(frontier) > 0:
			curr = frontier.pop()

			for x, y in zip([-1, 0, 0, 1], [0, -1, 1, 0]):
				newx = curr[0] + x
				newy = curr[1] + y

				if not (0 <= newx < rows):
					continue

				if not (0 <= newy < cols):
					continue

				if not (lst[newx, newy] == lst[curr[0], curr[1]] + 1):
					continue

				if (newx, newy) in explored:
					continue

				if lst[newx, newy] == 9:
					count += 1
				
				if part == 1:
					explored.add((newx, newy))

				frontier.append((newx, newy))



		total_count += count
	
	return total_count



if __name__ == "__main__":	

	import argparse

	parser = argparse.ArgumentParser(description='Solution to Advent of Code 2024 Day 06')
	parser.add_argument('-i', '--input', type=str, default='input', help='The input file')
	parser.add_argument('-p', '--part', type=int, default=1, help='The part of the challenge to solve')

	args = parser.parse_args()

	result = main(args.input, args.part)

	print(result)