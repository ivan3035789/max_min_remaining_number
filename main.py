num1 = int(input())
num2 = int(input())
num3 = int(input())
max_num = 0
min_num = 0
average = 0
if num1 >= num2 >= num3:
    max_num = num1
    min_num = num3
    average = num2
    print(max_num, '\n', min_num, '\n', average)
elif num1 <= num2 <= num3:
    max_num = num3
    min_num = num1
    average = num2
    print(max_num, '\n', min_num, '\n', average)
elif num2 >= num1 >= num3:
    max_num = num2
    min_num = num3
    average = num1
    print(max_num, '\n', min_num, '\n', average)
elif num2 <= num1 <= num3:
    max_num = num3
    min_num = num2
    average = num1
    print(max_num, '\n', min_num, '\n', average)
elif num2 >= num3 >= num1:
    max_num = num2
    min_num = num1 
    print(max_num, '\n', min_num, '\n', average)
elif num2 <= num3 <= num1:
    max_num = num1
    min_num = num2
    average = num3
    print(max_num, '\n', min_num, '\n', average)
