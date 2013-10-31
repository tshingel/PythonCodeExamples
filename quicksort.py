# function implements quicksort algorithm and 
# computes the total number of comparisons used 
# to sort the given input file by QuickSort. 
# The number of comparisons depends on the choice of 
# pivot element. There are three different ways to choose 
# a pivot element provided in function Pivot

import numpy as np

# small array for testing purposes 
A = np.array([3, 2, 5, 1, 6])

# perform swaps for pivot to be the first element of array 
def Pivot(A, lindx, rbound):
    #uncomment to swap pivot from last to first
    #A[rbound - 1], A[lindx] = A[lindx], A[rbound - 1] 
    #uncomment for three-median pivot construction
    a = A[lindx] 
    b = A[(lindx + rbound - 1)/2]
    c = A[rbound - 1] 
    if b > min(a, c) and b < max(a, c):
        A[(lindx + rbound - 1)/2], A[lindx] = A[lindx], A[(lindx + rbound - 1)/2]
    elif c > min(a, b) and c < max(a, b):   
        A[rbound - 1], A[lindx] = A[lindx], A[rbound - 1]    
    return(A)

# partitioning of array in place around a pivot element    
def Partition(A, lindx, rbound):
    A = Pivot(A, lindx, rbound)
    pivot = A[lindx] #pivot is the first element
    i = lindx + 1
    for j in range(lindx + 1, rbound): 
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j] #  swaps two elements, A[j] and A[i]
            i += 1
    A[lindx], A[i-1] = A[i-1], A[lindx] # placing pivot in the right position 
    return(i-1) # return the index of the pivot in the partitioned array 

# quicksort routine 
def QuickSort1(A, left, right): 
    if right - left <= 1:
        return(A) 
    piv_idx = Partition(A, left, right)
    lindx1 = left
    rindx1 = piv_idx
    QuickSort1(A, lindx1, rindx1)   
    lindx2 = piv_idx + 1
    rindx2 = right
    QuickSort1(A, lindx2, rindx2)
    return(A)

# number of comparisons in QuickSort1
def QuickSort1Comp(A, left, right): 
    if right - left <= 1:
        return 0
    comp = right - left - 1   # number of comparisons in the recursive call  
    piv_idx = Partition(A, left, right)
    lindx1 = left
    rbound1 = piv_idx
    comp += QuickSort1Comp(A, lindx1, rbound1)   
    lindx2 = piv_idx + 1
    rbound2 = right
    comp += QuickSort1Comp(A, lindx2, rbound2)
    return(comp)

def main():
    # data = np.loadtxt(open('QuickSort.txt', 'r'), dtype='f8')
    data = np.loadtxt(open('100.txt', 'r'), dtype='f8')
    n = data.size
    print('Initial Array')
    # WARNING: DON'T PRINT OUT QuickSort.txt file, it's huge 
    print(data)
    print('After implementing QuickSort')
    print QuickSort1(data, 0, n)
    #comp = QuickSort1Comp(A, 0, A.size) 
    comp = QuickSort1Comp(data, 0, n)
    print "Number of comparisons: ", comp 
    #B = QuickSort1(A, 0, A.size)
    #print(B)
if __name__ == '__main__':
    main()                     
       
