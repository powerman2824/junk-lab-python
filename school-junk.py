def miles_to_laps(user_miles): 
    user_laps = user_miles * 4
    return user_laps
    
user_miles = float(input())

print('{:.2f}'.format(miles_to_laps(user_miles)))