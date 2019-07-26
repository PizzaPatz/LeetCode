def quicksort(a):
	if len(a) <= 1:
		return a # If the length of the array is 1, then return back the original array
	tmpLeftArray = []
	tmpRightArray = []
	mid = len(a) // 2 # Integer operation, no remainder. E.g. 10 // 3 => 3
	pivot = a[mid] # Get a pivot between recursive step
	a = a[:mid] + a[mid+1:] # Declare a as a new array with no pivot in it
							# E.g. if a = [1,2,3,4,5] then new a = [1,2,4,5]
							# because middle pivot "3" has been excluded
	for i in a:
		if i <= pivot:
			tmpLeftArray.append(i) # Insert value less than pivot to the left arr
		else:
			tmpRightArray.append(i) # Insert value more than pivot to the right arr
	return (quicksort(tmpLeftArray) + [pivot] + quicksort(tmpRightArray))



random_arr = [6,3,5,7,10,1,4,8]

print(quicksort(random_arr))
