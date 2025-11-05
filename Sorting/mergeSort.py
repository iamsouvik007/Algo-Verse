

def merge(arr,low,mid,high):
    merged=[]
    l=low
    r=mid+1

    while l<=mid and r<=high:
        if arr[l]<=arr[r]:
            merged.append(arr[l])
            l+=1
        elif arr[r]<arr[l]:
            merged.append(arr[r])
            r+=1
        else:

            merged.append(arr[l])
            merged.append(arr[r])
            l+=1
            r+=1

    while l<=mid:
        merged.append(arr[l])
        l+=1
    while r<=high:
        merged.append(arr[r])
        r+=1

    for i in range(len(merged)):
        arr[low+i] = merged[i]




def mergeSort(arr,low,high):
    if low>=high:
        return arr
    
    mid = (low + high) // 2
    left = mergeSort(arr,low,mid)
    right = mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)
    # return arr


arr = [ 8,7,5,4,3]
low = 0
high = len(arr)-1

# print(mergeSort(arr,low,high))   --> It will return None because we are not returning anything from mergeSort function
# If mergeSort returns arr then it will work properly.

mergeSort(arr,low,high)
print("sorted array: ",arr)



