#Assignment: Selection Sort
# Selection sort works by iterating through the list, finding the 
# minimum value, and moving it to the beginning of the list. Then,
# ignoring the first position, which is now sorted, iterate through the 
# list again to find the next minimum value and move it to index 1. This continues until all values are sorted

L = [8,1,5,3,2,0,9,10,5,7,8,321,5]
for i in range(len(L)):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)):
        # Update the min_index if the element at j is lower than it
                if L[j] < L[min_index]:
                        min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]
print(L)

