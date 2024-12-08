with open('input.txt', 'r') as file:
    data = []
    for line in file:
        numbers = list(map(int, line.strip().split()))
        data.append(numbers)
    result = 0
    for i in range(len(data)):
        sum = 0
        absolute = 0
        
        for j in range(len(data[i]) - 1):
            if -3 <= (data[i][j] - data[i][j+1]) <= 3 and (data[i][j] - data[i][j+1]) != 0:
                sum += abs(data[i][j] - data[i][j+1])
                absolute += data[i][j] - data[i][j+1]
            else:
                print('No: ' + str(data[i]) + ' ' + str(sum) + ' ' + str(absolute_final))
                break
        else:
            absolute_final = abs(absolute)
            if sum == absolute_final:
                print('Yes: ' + str(data[i]) + ' ' + str(sum) + ' ' + str(absolute_final))
                result += 1
            else:
                print('No: ' + str(data[i]) + ' ' + str(sum) + ' ' + str(absolute_final))
                
    print(result)
        # for j in range(2):
        #     
        #         print[data[i][j], data[i][j+1]]
        #         print('Yes')
        #     else:
        #         print('No' + str(data[i]))
            # else:
            #     print('--Nope' + str(data[i]))
            #     break
        # if absolute == sum:
        #     # print('Yes:' + data[i])
        # # else:
        # #     # print('No:' + str(data[i]))