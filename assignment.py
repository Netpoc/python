#Even numbers from 1 - 30 using for loop
print("++++++++++++++ Even NUMBER's With For +++++++++++++")
for i in range(30):
    if i % 2 == 0:
        print(f"Even Numbers Using For Loop: ", i)

#Even numbers from 1 - 30 using while loop
print("++++++++++++++ Even NUMBER's With While +++++++++++++")
num = 1
while num <= 30:
    if (num % 2 == 0):
        print(f"Even Numbers Using While Loop: ", num)
    num += 1
   
#Odd numbers from 1 - 30 using for loop
print("++++++++++++++ ODD NUMBER's With For ++++++++++")
for i in range(30):
    if i % 3 == 0:
        print(f"Even Numbers Using For Loop: ", i)

#Odd numbers from 1 - 30 using while loop
print("+++++++++++++++++ ODD NUMBER's With While ++++++++++")
num = 1
while num <= 30:
    if (num % 3 == 0):
        print(f"Even Numbers Using While Loop: ", num)
    num += 1
print("+++++++++++++++++++++++++++++++++++++++++++++")

#Ahmed Financials on 50,000 Budget
print("++++++++++++++ AHMED's BUDGET +++++++++++++++")
Budget = 50000
print(f"Total Budget= ", Budget)
MarketingExp = 0.25 * Budget
print(f"Marketing Expenses = ", MarketingExp)
OpEX = 0.5 * Budget
print(f"Operational Expenses = ", OpEX)
CustomerAcq = 0.25 * Budget
print(f"Customer Acquisition Budget = ", CustomerAcq)
CostOfCustomer = 5
AcquiredCustomer = (0.25 * Budget)/5
print("---------------------------------------------")
print(f"Total Customers Acquired: ", AcquiredCustomer)
print("---------------------------------------------")