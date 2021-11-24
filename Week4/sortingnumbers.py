nums = [3, 4, 5, 7, 33, 6, 11, 89, 10, 2]
print("The list of unsorted numbers in the list:",nums)
nums.sort()
print("Print the list in a sorted fashion: ", nums)
print("Print number of items in list:", len(nums)) 
print("Highest number in list:", max(nums))
print("Smallest number is list:", min(nums))
print("Sum of all numbers in list:", sum(nums))
print("Average of all nums:", sum(nums)/len(nums))