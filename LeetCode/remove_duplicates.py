# remove_duplicates.py
# See: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def removeDuplicates(nums):
    i = 0    
    while ( i < len(nums)-1):
        if (nums[i] == nums[i+1]):
            nums.pop(i)
        else: 
            i += 1        
    return len(nums)

if __name__ == '__main__':

    arr = map(int, raw_input().rstrip().split())

    print removeDuplicates(arr)
