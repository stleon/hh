from statistics import median

st = '{} {}'.format(input('Enter first sorted numeric array (1 2 3 4): '), input('Enter second sorted numeric array (1 4 5 6): '))

print(median(set(map(int, st.split()))))