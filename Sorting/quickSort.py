
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1

    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1


def quickSort(arr,low,high):
    if low<high:
        pIndex = partition(arr,low,high)
        quickSort(arr,low,pIndex-1)
        quickSort(arr,pIndex+1,high)

arr = [ 8,7,5,4,3]
low = 0
high = len(arr)-1
quickSort(arr,low,high)
print("sorted array: ",arr)












