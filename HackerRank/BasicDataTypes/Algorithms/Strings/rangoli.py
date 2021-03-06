import sys
def print_rangoli(size):
    # your code goes here
    # assign characters in array
    arr = list(map(chr, range(97, 97+size)))
    arr.reverse()
    line = '' #one dash for the first line
    end= len(arr)

    for i in range(0, end):
        line = '-'*(end-i-1)
        for j in range(0,i+1):
            line += arr[j]+'-'
        for k in range(i-1, -1,-1):
            line += arr[k]+'-'
        line += '-'*(end-i-1)
        print line


if __name__ == '__main__':
    size = int(raw_input().strip())
    print_rangoli(size)
