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
	
	data = lines[0]

	temp_array = []
	id = 0

	if part == 1:
		for index, block in enumerate(data):
			if index & 1 == 0:		# Check if even
				entries = int(block) * [id]
				id += 1
			else:
				entries = int(block) * [None]
			temp_array.extend(entries)

		for i in tqdm(range(len(temp_array))):
			if temp_array[i] is not None:
				continue

			for j in reversed(range(i, len(temp_array))):
				if temp_array[j] is not None:
					temp_array[i] = temp_array[j]
					temp_array[j] = None
					break
	else:

		Pointer = namedtuple("Pointer", ["position", "value", "length"])

		pointer_stack = []
		index_tracker = 0

		for index, block in enumerate(data):
			if index & 1 == 0:
				entries = int(block) * [id]
				pointer = Pointer(position=index_tracker, value=id, length=int(block))
				id += 1
				pointer_stack.append(pointer)
			else:
				entries = int(block) * [None]
			temp_array.extend(entries)
			index_tracker += int(block)


		for pointer in tqdm(pointer_stack[::-1]):

			for i in range(len(temp_array)):

				if pointer.position < i:
					continue

				if temp_array[i:i+pointer.length] == [None]*pointer.length:
					temp_array[i:i+pointer.length] = [pointer.value]*pointer.length
					temp_array[pointer.position : pointer.position+pointer.length] = [None]*pointer.length
					break

	sum = 0
	for index, item in enumerate(temp_array):
		if item is None:
			continue
		sum += index * item

	return sum


if __name__ == "__main__":	

	import argparse

	parser = argparse.ArgumentParser(description='Solution to Advent of Code 2024 Day 06')
	parser.add_argument('-i', '--input', type=str, default='input', help='The input file')
	parser.add_argument('-p', '--part', type=int, default=1, help='The part of the challenge to solve')

	args = parser.parse_args()

	result = main(args.input, args.part)

	print(result)