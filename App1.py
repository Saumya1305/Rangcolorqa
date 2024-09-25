import random


MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 5,
    "B" : 6,
    "C" : 4,
    "D" : 8
}

def get_slot_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():                         #function deposit bet game
    while True:                             #this one will keep on going until the number entered is correct or not
        amount = input("Enter the valid amount $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():                #these are the number of lines
    while True:                             #this one will keep on going until the number entered is correct or not
        lines = input("Enter the lines to bet on (1-" + str(MAX_LINES) + ")?")      #for concatenation as input only takes string as a valid thing to concatenate so we convert it into string first and then we use it
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines")
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True:  # this one will keep on going until the number entered is correct or not
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number")

    return amount

def main():
     balance = deposit()
     lines = get_number_of_lines()
     while True:
         bet = get_bet()
         total_bet = bet * lines

         if total_bet > balance:
             print(f"You don't have enough money to bet on dumbo, See your freaking balance ${balance} ")
         else:
             break

     print(f"You are betting ${bet} on {lines} lines. Total bet is equals to ${total_bet}")

slots = get_slot_spin(ROWS, COLS, symbol_count)


main()



