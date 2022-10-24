#Even numbers from 1 - 30 using for loop
for i in range(30):
    if i % 2 == 0:
        print(f"Even Numbers Using For Loop: ", i)


#Odd numbers from 1 - 30 using while loop
num = 1
while num <= 30:
    if (num % 2 == 0):
        print(f"Even Numbers Using While Loop: ", num)
    num += 1