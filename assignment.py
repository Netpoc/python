#Sum of even numbers from 1 - 30 using for loop
sum = 0
for i in range(30):
    sum += i
    if sum % 2 == 0:
        print(sum)


#Sum of odd numbers from 1 - 30 using while loop
num = 0
while (num <= 30):
    num += 1
    if(num % 2 == 0):
        
        print(num)