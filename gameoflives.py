import sys
import numpy as np
import random
 
life_matrix = []
print("please enter the dim you want thats bigger than 3!")
value = int(input())

for i in range(0,value):
    field = []
    for j in range(0,value):
        x = random.randint(0, 1)
        field.append(x)
    life_matrix.append(field)

print("Next matrix is the init one:")
for index in life_matrix:
    print(index)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for k in range (0 , value):
    for i in range (0 ,value):
        for j in range (0 , value):
            temp = life_matrix[i][j]

            if j == 0 and i == 0:
                if temp == 0:
                    continue
                    
                elif temp == 1 :
                    one = life_matrix[i][j+1]
                    two = life_matrix[i+1][j]
                    sum = one + two 
                    if sum < 2:
                        life_matrix[i][j] = 0
                    else:
                        continue
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif j < value-1 and i < value-1:
                if temp == 0:
                    one = life_matrix[i-1][j]
                    two = life_matrix[i+1][j]
                    three = life_matrix[i][j+1]
                    four = life_matrix[i][j-1]
                    sum = one + two + three + four
                    if sum == 3:
                        life_matrix[i][j] = 1
                    else:
                        continue
                    
                elif temp == 1 :
                    one = life_matrix[i-1][j]
                    two = life_matrix[i+1][j]
                    three = life_matrix[i][j+1]
                    four = life_matrix[i][j-1]
                    sum = one + two + three + four
                    if sum < 2:
                        life_matrix[i][j] = 0
                    elif sum > 3 :
                        life_matrix[i][j] = 0
                    else:
                        continue


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif j == value-1 and i == 0:
                if temp == 0:
                    continue
  
                elif temp == 1 :
                    one = life_matrix[i+1][j]
                    two = life_matrix[i][j-1]
                    sum = one + two
                    if sum < 2:
                        life_matrix[i][j] = 0
                    else:
                        continue

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif j == 0 and i == value-1:
                if temp == 0:
                    continue
  
                elif temp == 1 :
                    one = life_matrix[i][j+1]
                    two = life_matrix[i-1][j]
                    sum = one + two 
                    if sum < 2:
                        life_matrix[i][j] = 0
                    else:
                        continue


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif j == value-1 and i == value-1 :
                if temp == 0:
                    continue
                    
                elif temp == 1 :
                    one = life_matrix[i][j-1]
                    two = life_matrix[i-1][j]
                    sum = one + two 
                    if sum < 2:
                        life_matrix[i][j] = 0
                    else:
                        continue
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif j != 0  and i == 0:
                if temp == 0:
                    one = life_matrix[i][j-1]
                    two = life_matrix[i][j+1]
                    three = life_matrix[i+1][j]
                    sum = one + two + three
                    if sum == 3 :
                        life_matrix[i][j] = 1
                    else:
                        continue
  
                elif temp == 1 :
                    one = life_matrix[i][j-1]
                    two = life_matrix[i][j+1]
                    three = life_matrix[i+1][j]
                    sum = one + two + three
                    if sum < 2:
                        life_matrix[i][j] = 0
                    else :
                        continue
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif j == 0 and i != 0 :
                if temp == 0:
                    one = life_matrix[i-1][j]
                    two = life_matrix[i+1][j]
                    three = life_matrix[i][j+1]
                    sum = one + two + three
                    if sum == 3 :
                        life_matrix[i][j] = 1
                    else:
                        continue
     
                elif temp == 1 :
                    one = life_matrix[i-1][j]
                    two = life_matrix[i+1][j]
                    three = life_matrix[i][j+1]
                    sum = one + two + three
                    if sum < 2:
                        life_matrix[i][j] = 0
                    else:
                        continue






    print("/////////////////////////////////////////")
    for index in life_matrix:
        print(index)
             


            

    




 

