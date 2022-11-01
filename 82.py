def deleteDuplicates(head):
	remove = []
	for i in range(len(head)):
		for j in range(len(head)):
			if i == j:
				pass
			else:
				if head[i] == head[j]:
					remove.append(head[i])
	remove = list(set(remove))
	for i in remove:
		head = list(filter(lambda a:a!=i,head))
	print(head)
	pass

head = [1,2,3,3,4,4,5]
deleteDuplicates(head)