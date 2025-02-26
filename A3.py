import array
num_array = array.array('i', [0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 3, 3])
print('Number of Times 3 Appears in this Array:', num_array.count(3))
num_array.reverse()
print('The Array Reversed:', num_array)