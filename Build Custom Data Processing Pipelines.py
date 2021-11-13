balance = 100.0
rate = 0.03

print(0, round(balance,2))
for n in range(1,11):
    balance = round(balance * (1 + rate), 2)
    print(n, round(balance,2))

def compound(balance, rate, num_periods):
    print(0, round(balance,2))
    for n in range(1,num_periods+1):
        balance = round( balance * (1 + rate), 2)
        print(n, balance)
    return balance

# Do NOT write code above this line
# -----------------------

# Create the function compound_by_period here
def compound_by_period(balance, rate, num_periods):
    output = []
    output.append(round(balance,2))
    print(0, round(balance,2))
    for n in range(num_periods):
        balance = round( balance * (1 + rate), 2)
        output.append(round(balance,2))
    return output 
print(compound_by_period(100, 0.03, 10))

wheat = compound_by_period(1,1,63)
total_wheat = sum(wheat)

   
# Do NOT change the function below 
# -----------------------
def change_per_period(balances):
    for i in range(0,len(balances)-1):
         balances.append(balances[i+1] - balances[i])
    return balances
