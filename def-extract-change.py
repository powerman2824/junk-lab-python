def exact_change(input_val):
    num = input_val

    dollars = num / 100
    dollars = int(dollars)

    change = num % 100

    quaters = change / 25
    quaters = int(quaters)

    change = change % 25

    dimes = change / 10
    dimes = int(dimes)

    change = change % 10

    nickels = change / 5
    nickels = int(nickels)

    change = change % 5

    pennies = change / 1
    pennies = int(pennies)

    change = change % 1

    if dollars > 0:
        if dollars == 1:
            print(f'{dollars} dollar')
        else:
            print(f'{dollars} dollars')
    if quaters > 0:
        if quaters == 1:
            print(f'{quaters} quarter')
        else:
            print(f'{quaters} quarters')
    if dimes > 0:
        if dimes == 1:
            print(f'{dimes} dime')
        else:
            print(f'{dimes} dimes')
    if nickels > 0:
        if nickels == 1:
            print(f'{nickels} nickel')
        else:
            print(f'{nickels} nickels')
    if pennies > 0:
        if pennies == 1:
            print(f'{pennies} penny')
        else:
            print(f'{pennies} pennies')
    if num == 0:
        print('no change')
    return dollars, quaters, dimes, nickels, pennies

if __name__ == '__main__': 
    input_val = int(input())    
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
