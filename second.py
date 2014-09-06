from itertools import chain, combinations
from first import mk

def to_output(lst):
	return ' '.join(str(x) for x in lst)

# https://docs.python.org/3.4/library/itertools.html#itertools-recipes
def powerset(iterable):
	"powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

lst = mk(input('Enter a sequence of integers (2 3 4 5 6): '))
chunks = 2

result = [[] for i in range(chunks)]
sums = {i:0 for i in range(chunks)}
x = 0

lst.sort()
lst.reverse()

for l in lst:
	for s in sums:

		if x == sums[s] or sums[s] + l == sum(lst)//chunks:
			result[s].append(l)
			sums[s] += l
			break
	
	x = min(sums.values())

print(to_output(result[0]), '-', to_output(result[1]))
#print([x for x in powerset(lst) if sum(x) == 100])
print('yes' if [x for x in powerset(lst) if sum(x) == 100] else 'no')