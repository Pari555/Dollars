# Coins: amount of Cents that we outputted into least amount of coins.
# Dollars: amount of dollars that we output into least amount of bills.
# Hundred, Fifty, Twenty ,Ten, Five, One

# Ask the user for an amount of dollars
total = int(input("Enter a Number of Dollars: "))

hundred = 0
fifty = 0
twenty = 0
ten = 0
five = 0
one = 0

# total == 326
if(total >= 100):
  hundred = total / 100
  # 326 - 3 * 100 = 326 -300 = 26
  total = total % 100

if(total >= 50):
  fifty = total / 50
  total = total % 50

if(total >= 20):
  twenty = total / 20
  total = total % 20

if(total >= 10):
  ten = total / 10
  total = total % 10

if(total >= 5):
  five = total / 5
  total = total % 5

if(total >= 1):
  one = total / 1
  total = total % 1
  
print("hundreds: " + str(hundred))
print("fifties: " + str(fifty))
print("twenties: " + str(twenty))
print("tens: " + str(ten))
print("fives: " + str(five))
print("ones: " + str(one))