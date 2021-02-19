import sortedcontainers

# {1: 'a', 2: 'b'}
'''
range(n) [0;n)
range(a, b) [a;b)
range(a, b, step)
'''

'''
2
3 3 6 2 4
15 2 1 2
20 3 1 2 3
17 2 1 3
14 1 1
17 2 0
17 3 0
21 1 0
21 2 1
21 3 0

2 1 4 3 4
25 2 1 2
14 2 0
20 2 0
18 2 1
28 1 0
'''

def getDateZeroPatient():
	for d in tests:
		for man in tests[d]:
			if tests[d][man] == 1:
				return [d, man]

T = int(input())
f = open('res.txt', 'w')
for i in range(T):
	n, m, k, a, b = list(map(int, input().split()))
	parties = sortedcontainers.SortedDict()
	tests = sortedcontainers.SortedDict()

	for j in range(m):
		temp = list(map(int, input().split()))
		ind = temp[0]
		temp = temp[2:]
		temp.sort()
		parties[ind] = temp
	for j in range(k):
		temp = list(map(int, input().split()))
		if not temp[0] in tests.keys():
			tests[temp[0]] = sortedcontainers.SortedDict()
		tests[temp[0]][temp[1]] = temp[2]
	# print(parties)
	# print(tests)
	print(getDateZeroPatient())
	
	input()
	f.close()