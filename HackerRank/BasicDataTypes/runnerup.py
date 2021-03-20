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
    mx = arr[1]
    my = arr[0]        
    for i in range(0, len(arr)):
        if ( arr[i] > mx):
            my = mx
            mx= arr[i]
                        
    return my

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
print(runnerup2(arr))
