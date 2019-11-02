def calc_average(num_list):  # 计算平均数
    average = 0
    k = len(num_list)
    tmp = 0
    for num in num_list:
        tmp = tmp + num
    average = tmp / k
    return average

def calc_median(num_list):  # 计算中位数
    median = 0
    num_list.sort(key=None, reverse=False)
    k = len(num_list)
    if k % 2 == 0:
        print(k)
        median = (num_list[int(k / 2) - 1] + num_list[int(k / 2)]) / 2
    else:
        median = num_list[int(k / 2)]
    return median

def calc_mode(num_list): # 计算众数
    mode = 0
    temp = 0
    dic = dict((num, num_list.count(num)) for num in num_list)
    for key,value in dic.items():
        if temp < value:
            temp = value
            mode = key
    return mode

def calc_variance(num_list): # 计算方差
    variance = 0
    temp_list = []
    average = calc_average(num_list)
    for num in num_list:
        i = 0
        temp_list[i] = (average - num) ** 2
        i += 1
    variance = calc_average(temp_list)
    return variance

list = [73, 65, 84, 65, -1, -1, -1]

# print(calc_average(list))
# print(calc_median(list))
# print(calc_mode(list))
print(calc_variance(list))
