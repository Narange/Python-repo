import random

#build a new sorted list by finding the min and removing it
def brute_sort(input_list):
	temp_list = input_list
	result_list = []

	while len(temp_list) > 0:
		smallest = min(temp_list)
		result_list.append(smallest)
		temp_list.remove(smallest)

	return result_list

#return a list of size length - each elem is random int in range given
def random_list(span, length):
	the_list = []
	for i in range(length):
		random_num = random.randint(span[0], span[1])
		the_list.append(random_num)
	return the_list



my_list = random_list((1,5000),5)

print("Input list:\n" + str(my_list))
print("Sorted list:\n" + str(brute_sort(my_list)))
