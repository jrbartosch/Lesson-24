import array
num_array1 = array.array('i',[0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 3, 3])
print ('Number of Times 3 Appears in this Array:', num_array1.count(3))
num_array2 = num_array1.reverse()
print ('The Array Reversed:', str(num_array2))