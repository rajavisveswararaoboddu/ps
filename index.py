#ap to check if the digits of each number in an list are in increasing order, returning true or false for each Increasing order or not


numbers = [253, 678, 258, 321]
for number in numbers:
    str_number = str(number)
    increasing = True
    for i in range(len(str_number) - 1):
        if str_number[i] >= str_number[i + 1]:  
            increasing = False
            break
    
    
    print(increasing)
    
    
#Wap to check if the digits of each number in an list are in decreasing order and return an array of true otherwise false.Decreasing order -true   

numbers = [111, 321, 300, 652, 789]
result = []  
for number in numbers:
    str_number = str(number)
    decreasing = True  
    for i in range(len(str_number) - 1):
        if str_number[i] <= str_number[i + 1]:   
            decreasing = False
            break  
    result.append(decreasing)
print(result)




#  Finding the frequency of elements in an array.

arr = [10, 30, 10, 20, 10, 20, 30, 10]
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1   
    else:
        frequency[num] = 1  
for key, value in frequency.items():
    print(f"{key} => {value}")