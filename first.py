from statistics import median

def mk(num_arr):
	#return [ int(x) for x in num_arr.split() ] # 100000 loops, best of 3: 7.42 µs per loop
	return list(map(int, num_arr.split())) # 100000 loops, best of 3: 5.84 µs per loop


if __name__ == '__main__':
	
	result = median(mk(input('Enter first sorted numeric array (1 2 3 4): ')) + mk(input('Enter second sorted numeric array (1 4 5 6): ')))

	print(result)