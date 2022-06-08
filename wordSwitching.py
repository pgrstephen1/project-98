def switchAB():
	fileA = input("what is the first file you want to switch: ")
	fileB = input ("what is the second file you want to switch: ")
	with open(fileA, 'r') as a:
		data_a = a.read()
	with open(fileB, 'r') as b:
		data_b = b.read()
	with open(fileA, 'w') as a:
		a.write(data_b)
	with open(fileB, 'w') as b:
		b.write(data_a)
switchAB()