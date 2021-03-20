#!/usr/bin/python
# Find the runner up

# runner up with sort
def runnerup(arr):
    arr.sort()

    if (len(arr) == 1):
        return arr[0]
    else:
        return arr[len(arr)-2]

# runnerup without sort
def runnerup2(arr):
    if (len(arr) == 2):
        if (arr[0] < arr[1]):
            return arr[0]
        else:
            return arr[1]
    else:
        mx = arr[0]
        my = arr[0]        
        for i in range(0, len(arr)):
            if ( arr[i] > mx):
                mx= arr[i]
            if (arr[i] > my and arr[i] < mx):
                my = arr[i]
                        
    return my

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
print(runnerup2(arr))
