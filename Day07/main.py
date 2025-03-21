from typing import List
import itertools

from Utils import readline_clean

def check_valid_ops(total, hends) -> bool:
	
	num_ops = len(hends) - 1

	ops = ["+", "*"]

	for roll in itertools.product(ops, repeat=num_ops):
		ptr = 0
		running = hends[ptr]
		for r in roll:
			ptr += 1
			expr = f"{running} {r} {hends[ptr]}"
			running = eval(expr)

		if running == int(total):
			return True

	return False

def check_valid_ops_with_concat(total, hends) -> bool:

	num_ops = len(hends) - 1

	ops = ["+", "*", "||"]

	for roll in itertools.product(ops, repeat=num_ops):
		ptr = 0
		running = hends[ptr]
		for r in roll:
			ptr += 1
			if r == "||":
				running = int(f"{running}{hends[ptr]}")
			elif r == "+":
				running += hends[ptr]
			elif r == "*":
				running *= hends[ptr]

		if running == int(total):
			return True

	return False

def main(inp='input', part=1):
	text = inp + ".txt"
	lines = readline_clean(f"Day07/{text}")

	accum = 0

	for line in lines:
		sto : List[str] = line.split(": ")
		store = [sto[0]]
		store = store + sto[1].split(" ")

		intvals = list(map(int, store))

		if part == 1:
			if check_valid_ops(intvals[0], intvals[1:]):
				accum += intvals[0]
		else:
			if check_valid_ops_with_concat(intvals[0], intvals[1:]):
				accum += intvals[0]

	print(accum)


if __name__ == "__main__":	

	import argparse

	parser = argparse.ArgumentParser(description='Solution to Advent of Code 2024 Day 06')
	parser.add_argument('-i', '--input', type=str, default='input', help='The input file')
	parser.add_argument('-p', '--part', type=int, default=1, help='The part of the challenge to solve')

	args = parser.parse_args()

	main(args.input, args.part)