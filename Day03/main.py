from Utils import readline_clean

def prob1(lst):

	linestr = ""
	for line in lst:
		linestr += line

	accum = []

	for i in range(len(linestr)):

		mul = linestr[i:i+4]

		if mul != "mul(":
			continue

		comm = mul

		counter = 0
		nxt = linestr[i+4]
		while True:
			if (nxt == "m"):
				comm += ")"
				break
			comm += nxt
			if (nxt == ")"):
				break
			counter += 1
			nxt = linestr[i+4+counter]

		accum.append(comm)

	addup = 0

	for comm in accum:
		comm_stripped = comm[4:-1]
		comm_split = comm_stripped.split(",")

		try:
			valid_ints = [int(i) for i in comm_split]
		except Exception as e:
			valid_ints = [0, 0]

		addup += valid_ints[0] * valid_ints[1]

	result = addup

	return result

def prob2(lst):

	linestr = ""
	for line in lst:
		linestr += line

	accum = []

	for i in range(len(linestr)):

		dont = linestr[i:i+7]
		if dont == "don't()":
			accum.append(dont)
			continue

		do = linestr[i:i+4]
		if do == "do()":
			accum.append(do)
			continue

		mul = linestr[i:i+4]

		if mul != "mul(":
			continue

		comm = mul

		counter = 0
		nxt = linestr[i+4]
		while True:
			if (nxt == "m"):
				comm += ")"
				break
			comm += nxt
			if (nxt == ")"):
				break
			counter += 1
			nxt = linestr[i+4+counter]

		accum.append(comm)

	addup = 0

	enable = True

	for comm in accum:
		if comm == "do()":
			enable = True
		elif comm == "don't()":
			enable = False
		else:
			if enable:
				comm_stripped = comm[4:-1]
				comm_split = comm_stripped.split(",")

				try:
					valid_ints = [int(i) for i in comm_split]
				except Exception as e:
					valid_ints = [0, 0]

				addup += valid_ints[0] * valid_ints[1]

	result = addup

	return result

if __name__ == "__main__":
	
	from pprint import pprint

	input_txt = "Day03/input.txt"

	lines = readline_clean(input_txt)

	day1 = prob1(lines)
	# day2 = prob2(lines)
    
	pprint(day1)