
def recsum(nums):
    if len(nums)==0:
        return 0
    else:
        return nums[0] + recsum(nums[1:])
arr_sz = int(input("How many numbers you want: "))
num_arr = []
for i in range(arr_sz):
    num = int(input(f"Num no:{i+1}: "))
    num_arr.append(num)
print (recsum(num_arr))
