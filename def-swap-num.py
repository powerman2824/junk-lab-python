def swap_values(user_val1, user_val2):
    return user_val2, user_val1

if __name__ == '__main__': 
    user_val1 = int(input())
    user_val2 = int(input())
    print(f'{swap_values(user_val1, user_val2)[0]} {swap_values(user_val1, user_val2)[1]}')
