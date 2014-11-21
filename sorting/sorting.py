'''
	This file contains the following sorting algorithms:
	1) Bubble Sort
	2) Selection Sort
	3) Insertion Sort
	4) Merge Sort
	5) Quick Sort

	Author: Pranav Angara
'''

'''
	The bubble sort algorithm takes O(n^2) time to sort items
	Makes n-1 passes and for each pass it ends up placing an item
	in its correct position
	@param data, a list of data items
'''
def bubble_sort(data):
	needs_sorting = True
	passes = len(data)-1

	while passes > 0 and needs_sorting:
		needs_sorting = False

		for index in xrange(passes):
			if data[index] > data[index+1]:
				needs_sorting = True
				data[index], data[index+1] = data[index+1], data[index]

		passes -= 1


'''
	The selection sort algorithm takes O(n^2) time to sort items
	For each pass, it finds the max element and swaps it with an element
	at that respective position
	@param data, a list of data items
'''
def selection_sort(data):
	for pass_num in xrange(len(data)-1, 0, -1):
		max_index = 0

		for index in xrange(1, pass_num+1):
			max_index = index if data[index] > data[max_index] else max_index

		if max_index != pass_num:
			data[max_index], data[pass_num] = data[pass_num], data[max_index]


'''
	The insertion sort algorithm begins by treating the 1st element as part of a
	sorted sub-list. It then iteratively, "inserts" additional elements into their
	correct positions
'''
def insertion_sort(data):
	for index in xrange(1, len(data)):
		current_position = index
		needs_sorting = True

		while needs_sorting and current_position > 0:
			if data[current_position] >= data[current_position-1]:
				needs_sorting = False
			else:
				data[current_position], data[current_position-1] = data[current_position-1], data[current_position]

			current_position -= 1


'''
	The merge sort algorithm fares way better. On average, it takes O(n lg n) to sort elements
	It uses the divide & conquer approach. Divides the data in half until an array consists of
	only 1 element. It then begins merging partitions.
'''
def merge_sort(data):
	# Base case = array of 1 or 0 elements
	if len(data) > 1:
		mid = len(data)/2
		left = data[:mid]
		right = data[mid:]

		merge_sort(left)
		merge_sort(right)

		merge(data, left, right)


'''
	Given 2 lists, this function merges 2 lists and returns a sorted merged list
'''
def merge(data, left, right):

	left_ctr = right_ctr = tot_ctr = 0

	while left_ctr < len(left) and right_ctr < len(right):
		if left[left_ctr] < right[right_ctr]:
			data[tot_ctr] = left[left_ctr]
			left_ctr += 1
		else:
			data[tot_ctr] = right[right_ctr]
			right_ctr += 1
		tot_ctr += 1

	while left_ctr < len(left):
		data[tot_ctr] = left[left_ctr]
		left_ctr+=1
		tot_ctr+=1

	while right_ctr < len(right):
		data[tot_ctr] = right[right_ctr]
		right_ctr += 1
		tot_ctr += 1
