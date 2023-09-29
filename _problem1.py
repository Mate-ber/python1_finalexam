def num_to_dig(num):
    digs = []
    while num>0:
        digs.append(num%10)
        num = num//10
    return digs

def payload(card_num):
    mult = 2
    arr_mult = num_to_dig(int(card_num))
    sum_digits = 0
    for i in range(len(arr_mult)):
        each_num_mult = arr_mult[i]*mult
        arr_mult_nums = num_to_dig(each_num_mult)
        sum_for_test = 0
        for nums in arr_mult_nums:
            sum_for_test += nums
        sum_digits += sum_for_test
        if(mult==2):
            mult=1
        else:
            mult=2
    if sum_digits%10==0:
        return 0
    return 10-sum_digits%10

card_num = int( input("Input card number:") )
print(f"Checker is: {payload(card_num)}")
#7992739871