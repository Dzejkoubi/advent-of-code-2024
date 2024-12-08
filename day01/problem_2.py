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
            
    result = 0
    
    for i in range(len(first_list)):
        multiplication = 0
        for j in range(len(second_list)):
            if first_list[i] == second_list[j]:
                multiplication+=1
        result+=multiplication * first_list[i]
        
        
    print(result)
        
                
                
    
                
