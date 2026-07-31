def search(arr,l,r,key):

    if l>r:
        return -1

    mid=(l+r)//2

    if arr[mid]==key:
        return mid

    if key<arr[mid]:
        return search(arr,l,mid-1,key)

    return search(arr,mid+1,r,key)

arr=[2,4,6,8,10]

print(search(arr,0,len(arr)-1,8))