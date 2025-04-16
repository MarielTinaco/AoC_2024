from typing import List
import itertools
import numpy as np
from pathlib import Path
from collections import deque, namedtuple
from Utils import readline_clean
from functools import lru_cache
import math
from tqdm import tqdm


DAY = Path(__file__).resolve(strict=True).parent

def main_unoptimized(inp='input', part=1):
	text = inp + ".txt"
	lines = readline_clean(f"{DAY}/{text}")

	data = lines[0].split(" ")

	STEPS = 25 if part == 1 else 75

	for _ in tqdm(list(range(STEPS))):
		temp = []
		for entry in data:
			if int(entry) == 0:
				temp.extend(["1"])
			elif len(entry) & 1 != 1:
				entry_len = len(entry)
				stones = [entry[:entry_len//2], entry[entry_len//2:]]
				temp.extend([str(int(stone)) for stone in stones])
			else:
				temp.extend([str(int(entry)*2024)])

		data = temp.copy()

	return len(data)

@lru_cache(maxsize=None)
def count(stone, depth):

	if depth == 0:
		return 1
	if stone == 0:
		return count(1, depth - 1)
	
	digits = math.floor(math.log10(stone)) + 1

	if digits % 2 == 0:
		midpoint = digits // 2
		tens = 10 ** midpoint
		left_stones = stone // tens
		right_stones = stone % tens

		return count(left_stones, depth - 1) + count(right_stones, depth -1)

	return count(stone*2024, depth-1)

def main(inp='input', part=1):
	text = inp + ".txt"
	lines = readline_clean(f"{DAY}/{text}")

	data = map(int, lines[0].split(" "))

	STEPS = 25 if part == 1 else 75

	return sum(count(stone, STEPS) for stone in data)


if __name__ == "__main__":	

	import argparse

	parser = argparse.ArgumentParser(description=f'Solution to Advent of Code 2024 {str(DAY)[:3]} {str(DAY)[3:]}')
	parser.add_argument('-i', '--input', type=str, default='input', help='The input file')
	parser.add_argument('-p', '--part', type=int, default=1, help='The part of the challenge to solve')

	args = parser.parse_args()

	result = main(args.input, args.part)

	print(result)