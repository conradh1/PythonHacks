# remove_duplicates.py
# See: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def removeDuplicates(nums):

    dup = -1
    i = 0
    while ( i < len(nums)):
        if (nums[i] == dup ):
            del(nums[i])
        else:
            dup = nums[i]
            i += 1
    print nums
    return len(nums)

if __name__ == '__main__':

    arr = map(int, raw_input().rstrip().split())

    print removeDuplicates(arr)
