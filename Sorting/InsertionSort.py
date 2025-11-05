


def insertionsort(arr):

    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1

        while j>=0 and temp<arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = temp
            
    return arr

arr = [5,4,3,2,1]
print(insertionsort(arr))









