with open('input.txt', 'r') as file:
    data = []
    for line in file:
        numbers = map(int, line.split())
        data.extend(numbers)
    first_list = []
    second_list = []
    for i in range(len(data)):
        if i % 2 == 0:
            first_list.append(data[i])
        else:
            second_list.append(data[i])
    
    sorted_first_list = first_list.sort()
    sorted_second_list = second_list.sort()
    
    result = 0
    
    for i in range(len(first_list)):
        if first_list[i] > second_list[i]:
            result += first_list[i] - second_list[i]
        else :
            result += second_list[i] - first_list[i]
            
    print(result)