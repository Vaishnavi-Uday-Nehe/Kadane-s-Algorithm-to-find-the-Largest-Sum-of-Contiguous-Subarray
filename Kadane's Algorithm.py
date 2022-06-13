def MaxSumArray(arr,size):
    curr_sum = 0
    max_sum = 0

    for i in range (0,size):
        curr_sum = curr_sum + arr[i]
        if curr_sum > max_sum :
            max_sum = curr_sum
        if curr_sum <0:
            curr_sum = 0
    return max_sum

arr = [1,-1,2,-3,4,5,-6,-1]
size = len(arr)
print("THE Largest Sum of a Contiguous Subarray is : ", MaxSumArray(arr,size))

#CodeByVaishnaviUdayNehe