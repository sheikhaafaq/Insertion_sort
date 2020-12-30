#Insertion Sorting in Data Structures
arr = [5, 4, 10, 1, 6, 2]
length = len(arr)

for i in range(1,length):
	#store the value of a[i] in temp variable
	temp = arr[i]
	j = i - 1
	while (j >= 0 and arr[j] > temp):
		#shift the of element by one position right
		arr[j+1] = arr[j]
		j -= 1
	#if while conditions donot met
	arr[j+1] = temp 
	print("\ncycle: {}\n{}".format(i,arr))
print("\nSorted array")
print(arr)

print("""\nTime complexty\n Worst case: O(n^2)\n Best case: O(n)""")

