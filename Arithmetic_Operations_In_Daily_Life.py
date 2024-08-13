# Task 1: Groucery Store Math
# Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the 
# cost of bread, peanut butter, and jelly be? Prices don't need to be realistic!

cost_of_bread = 10
cost_of_peanut_butter = 5
cost_of_jelly = 3
total_cost = (cost_of_bread + cost_of_peanut_butter + cost_of_jelly)
print(total_cost)

# Task 2: Bank Interest
# If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account 
# after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the 
# expected outcome would be $10,700.
# a = r * t * p 
# p = 10000 t = 1 year r = 7%

savings_account = 10000
interest_rate = .07
years = 1
total_interest = (savings_account * interest_rate * years)
savings_account += total_interest
print(savings_account)