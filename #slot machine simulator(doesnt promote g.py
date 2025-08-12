#slot machine simulator(doesnt promote gambling)

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 100
def deposit():
    while True:
        amount = input("what would you like to deposit:  $")
        if amount.isdigit():
            amount =int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount 

def get_number_of_lines():
    while True:
        line = input("enter the number of lines to bet on (1-" + str(MAX_LINES) + ")")
        if line.isdigit():
            line =int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
                print("Enter a valid no. of lines")
        else:
            print("Please enter a number")
    return line

def get_bet():
     while True:
        amount = input("what would you like to bet on each line:  $")
        if amount.isdigit():
            amount =int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
     return amount




def main():
    balance =deposit()
    line = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * line
    print(f"you are betting ${bet} on {line}lines. Total bet is equal to: {total_bet} ")
    if total_bet > balance:
        debt = total_bet - balance
        print(f"you are in debt of {debt}")

main()