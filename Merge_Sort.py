#import libraries
import random

#define merge sort first method
def mergeSort(unsortedList):
    #if length of unsortedList is 1, then the list is sorted, so return
    if (len(unsortedList) == 1):
        print("unsorted list:")
        print(unsortedList)
        return unsortedList
    
    #define list1 and list2 to 
    list1 = []
    list2 = []
    
    #loop through first half of unsorted list, adding elements to list1
    for i in range(0, int((len(unsortedList)) / 2)):
        list1.append(unsortedList[i])
    #loop through second half of unsorted list, adding elements to list2
    for i in range(int((len(unsortedList)) / 2), len(unsortedList)):
        list2.append(unsortedList[i])
    
    #recursive call to further split lists
    list1 = mergeSort(list1)
    list2 = mergeSort(list2)
    
    #once lists are reduced to length 1 each, plug them into this to re-merge them
    return merge(list1, list2)

def merge(list1, list2):
    #TEST PRINT list1 and list2
    print("now merging:")
    print(list1)
    print(list2)
    #declare sorted list to be returned
    sortedList = []
    
    #loop through both lists to find smaller first element and append to new list
    i = 0
    j = 0
    while(i < len(list1) and j < len(list2)):
        if(list1[i] < list2[j]):
            sortedList.append(list1[i])
            i += 1
        else:
            sortedList.append(list2[j])
            j += 1
            
    #loop through remnants of either list1 or list2 and append all remaining elements
    while(i < len(list1)):
        sortedList.append(list1[i])
        i += 1
        
    while(j < len(list2)):
        sortedList.append(list2[j])
        j += 1
        
    print("sorted list:")
    print(sortedList)
    return sortedList
#declare list
unsortedList = []

#populate list
for i in range(0,11):
    item = random.randint(1,10)
    unsortedList.append(item)

print(unsortedList)

print(mergeSort(unsortedList))

