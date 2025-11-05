# Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False

        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
    
arr = [ 8,7,5,4,3]
print(bubbleSort(arr))





    






