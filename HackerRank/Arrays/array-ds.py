
def array_ds(arr):    
    rev = []
    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    return rev

if __name__ == '__main__':

    arr = map(int, raw_input().rstrip().split())

    print array_ds(arr)
