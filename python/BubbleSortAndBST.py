# Bubble sort and Binary search

def bubbleSort(inList: list) -> list:
    """
    This function receives a list and sorts it out
    using bubble sort algorithm, then returns the 
    sorted list
    """
    
    length = len(inList)

    for i in range(0, length):
        for j in range(0, length-i-1):
            if (inList[j] > inList[j+1]):
                inList[j], inList[j+1] = inList[j+1], inList[j]

    return inList

def binarySearch(inList: list[int], toSearch: int, start = 0, end = None) -> int:
    """
    This function received a sorted list and searches
    for the inputed number inside the list using 
    binary search algorithm. It finally returns the
    index of found number inside the list.
    """

    if end == None:
        end = len(inList) - 1
    
    if start > end:  # reccursion error!
        raise RuntimeError(f"Could not find the number in the list!")

    mid = (start + end) // 2

    if (inList[mid] == toSearch):
        return mid
    if (toSearch > inList[mid]):
        return binarySearch(inList, toSearch, mid+1, end)
    if (toSearch < inList[mid]):
        return binarySearch(inList, toSearch, start, mid-1)


tlist = [57,76,5,4534,4,6,56,57,5,8,8,56,6246,8]
print(f"Original list: {tlist}")
sorted_list = bubbleSort(tlist)
print(f"Original list: {sorted_list}")

numSearch = int(input("\nWhich number to search? "))
foundIndex = binarySearch(sorted_list, numSearch)
print(f"Found no.{numSearch} at index {foundIndex}")

