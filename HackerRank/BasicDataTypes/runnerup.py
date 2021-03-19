#!/usr/bin/python
# Find the runner up

def runnerup(arr):
    arr.sort()

    if (len(arr) == 1):
        return arr[0]
    else:
        top = arr[len(arr)-1]
        for i in range(len(arr)-1,-1, -1):            
            if arr[i] < top:
                return arr[i]
        return top


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
print(runnerup(arr))
