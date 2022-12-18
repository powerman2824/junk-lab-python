def cost_per_mile(miles_per_gallon, dollars_per_gallon):
    cost_per_mile = dollars_per_gallon / miles_per_gallon
    miles_10 = cost_per_mile * 10
    miles_50 = cost_per_mile * 50
    miles_400 = cost_per_mile * 400
    return [miles_10, miles_50, miles_400]
def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    cost_per_mile = dollars_per_gallon / miles_per_gallon
    cost_of_drive = cost_per_mile * driven_miles
    return cost_of_drive
if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    print('\n'.join(str('{:.2f}'.format(x)).upper() for x in cost_per_mile(miles_per_gallon, dollars_per_gallon)))
if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    driven_miles = float(input())
    print('\n'.join(str('{:.2f}'.format(x)).upper() for x in cost_per_mile(miles_per_gallon, dollars_per_gallon)))
    print('{:.2f}'.format(driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon)))
