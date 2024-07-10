#Author: Adwiteeya
#Date: 02/23/2024
#Purpose: quicksort p2



#function to compare integers
def compare_ints(a, b):
    return a <= b

#function to compare strings
def compare_strings(a, b):
    return a.lower() <= b.lower()

#partition function:
def partition (the_list, p, r, compare_func):

    pivot = the_list[r]
    i = p- 1

    for j in range(p, r): #goes over indices of the_list
        if compare_func(the_list[j],the_list[r]):
            i = i + 1

            #switching the elements
            switch = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = switch

    #switching the pivot
    switch_pivot = the_list[i+ 1]
    the_list[i+ 1] = pivot
    the_list[r] = switch_pivot

    return i + 1

#quicksort function
def quicksort(the_list,p,r,compare_func):

    if p < r:
        q = partition(the_list,p,r,compare_func)
        quicksort(the_list,p, q-1, compare_func)
        quicksort(the_list,q+1,r,compare_func)

#sort function
def sort(the_list, compare_func):
    p = 0
    r = len(the_list) - 1
    quicksort(the_list,p,r,compare_func)
    return the_list















