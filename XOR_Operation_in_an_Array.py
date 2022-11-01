def xorOperation(n,start):
	out = 0
	nums = [start + 2 * i for i in range(n)]
	for x in nums:
		out = out ^ x
	return out

n = 5
start = 0
print(xorOperation(n,start))