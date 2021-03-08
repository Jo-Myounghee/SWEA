def bin_search(arr, target, start, end):
    if start > end:
        return False

    mid = (start + end) // 2
    if arr[mid] == target:
        return True
    
    elif arr[mid] > target:
        return bin_search(arr, target, start, mid - 1)
    else:
        return bin_search(arr, target, mid + 1, end)

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
inputs = list(map(int, input().split()))

lst.sort()

for i in range(len(inputs)):
    if bin_search(lst, inputs[i], 0, len(lst)-1):
        print(1)
    else:
        print(0)
